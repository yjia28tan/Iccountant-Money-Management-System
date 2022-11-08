import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
from tkinter import messagebox
import sqlite3

window = Tk()
window.title("ICCOUNTANT")
window.geometry("1280x720")
window.state('zoomed')
window.resizable(True, True)
window.iconphoto(False, tk.PhotoImage(file="logo_refined.png"))
window.configure(bg='#1A1A1A')

def connectDatabase():
    try:
        global connect
        global cur
        # connect to database
        connect = sqlite3.connect("Iccountant")
        cur = connect.cursor()
    except:
        messagebox.showerror('Error', 'Cannot connect to database!')

class Category:
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        # ====================================== Menubar ====================================================
        # Define and resize the icons to be shown in Menu bar
        self.logo = ImageTk.PhotoImage(Image.open('logo_small.png').resize((165, 58), resample=Image.LANCZOS))
        self.dashboard = ImageTk.PhotoImage(Image.open('Dashboard.png').resize((160, 30), resample=Image.LANCZOS))
        self.statistic = ImageTk.PhotoImage(Image.open('Chart.png').resize((160, 30), resample=Image.LANCZOS))
        self.transaction = ImageTk.PhotoImage(Image.open('transaction.png').resize((160, 30), resample=Image.LANCZOS))
        self.category = ImageTk.PhotoImage(Image.open('category.png').resize((160, 30), resample=Image.LANCZOS))
        self.account = ImageTk.PhotoImage(Image.open('accounts.png').resize((160, 30), resample=Image.LANCZOS))
        self.currency = ImageTk.PhotoImage(Image.open('currency.png').resize((160, 30), resample=Image.LANCZOS))
        self.calculator = ImageTk.PhotoImage(Image.open('calculator.png').resize((160, 30), resample=Image.LANCZOS))
        self.customer = ImageTk.PhotoImage(Image.open('QNA.png').resize((160, 30), resample=Image.LANCZOS))
        self.tips = ImageTk.PhotoImage(Image.open('tips.png').resize((160, 30), resample=Image.LANCZOS))
        self.logout = ImageTk.PhotoImage(Image.open('logout.png').resize((160, 30), resample=Image.LANCZOS))
        self.user = ImageTk.PhotoImage(Image.open('user.png').resize((145, 45), resample=Image.LANCZOS))

        self.menuFrame = Frame(master, bg='#000000', width=180, height=master.winfo_height(),
                               highlightbackground='#1A1A1A')
        self.menuFrame.place(x=0, y=0)

        # Defining the buttons for menu bar in Home page
        self.logo_l = Label(self.menuFrame, image=self.logo, bg='#000000').grid(row=1)
        self.dashboard_b = Button(self.menuFrame, image=self.dashboard, bg='#000000', relief='flat').grid(row=2)
        self.statistic_b = Button(self.menuFrame, image=self.statistic, bg='#000000', relief='flat').grid(row=3)
        self.transaction_b = Button(self.menuFrame, image=self.transaction, bg='#000000', relief='flat').grid(row=4)
        self.category_b = Button(self.menuFrame, image=self.category, bg='#000000', relief='flat').grid(row=5)
        self.account_b = Button(self.menuFrame, image=self.account, bg='#000000', relief='flat').grid(row=6)
        self.currency_b = Button(self.menuFrame, image=self.currency, bg='#000000', relief='flat').grid(row=7)
        self.calculator_b = Button(self.menuFrame, image=self.calculator, bg='#000000', relief='flat').grid(row=8)
        self.customer_b = Button(self.menuFrame, image=self.customer, bg='#000000', relief='flat').grid(row=9)
        self.tips_b = Button(self.menuFrame, image=self.tips, bg='#000000', relief='flat').grid(row=10)
        self.logout_b = Button(self.menuFrame, image=self.logout, bg='#000000', relief='flat').place(x=1, y=680)
        self.user_b = Button(self.menuFrame, image=self.user, bg='#000000', relief='flat').place(x=8, y=720)

        # So that it does not depend on the widgets inside the frame
        self.menuFrame.grid_propagate(False)

        # ===== Heading Label =====
        self.heading_label = Label(master, text='Category', fg='white', bg='#1A1A1A')
        self.heading_label.config(font=tkFont.Font(family='Lato', size=20, weight="bold", slant="italic"))
        self.heading_label.place(x=200, y=15)

        # ================== Category table ===============================================
        # Frame for tree view
        self.treeFrame = Frame(master, bg='#1A1A1A',  width=1000, height=400)
        self.treeFrame.place(x=200, y=100)

        self.CategoryTree = ttk.Treeview(self.treeFrame, selectmode="extended", show='headings', columns='Category', height=20)
        self.CategoryTree.place(relwidth=1, relheight=1)

        self.CategoryTree.heading('Category', text='Income', anchor=CENTER)
        self.CategoryTree.column("Category", anchor=CENTER, width=60)

        self.CategoryTree.tag_configure('oddrow', background='#cccccc')
        self.CategoryTree.tag_configure('evenrow', background='#999999')

        self.treestyle = ttk.Style()
        self.treestyle.theme_use("default")
        self.treestyle.configure("Treeview", background="#666666", foreground="black", fieldbackground="#666666",
                                 rowheight=25)
        self.treestyle.configure('.', borderwidth=1)
        self.treestyle.map('Treeview', background=[('selected', '#9fc5f8')])
        self.treestyle.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        # call function to display Account
        self.displayCategory1()

        # call function to display Category
        self.updatetree()

        # Buttons
                self.add_button = customtkinter.CTkButton(master, text='Add', width=50, height=30, text_color='black',
                                                  fg_color="#b4a7d6",
                                                  hover_color="#ffffff",
                                                  command=lambda: self.addCategoryWindow(Toplevel))
        self.add_button.place(x=200, y=58)

        self.edit_button = customtkinter.CTkButton(master, text='Edit', width=50, height=30, text_color='black',
                                                   fg_color="#b4a7d6",
                                                   hover_color="#ffffff",
                                                   command=lambda: self.editCategoryWindow(Toplevel))

        self.edit_button.place(x=260, y=58)

        self.delete_button = customtkinter.CTkButton(master, text='Delete', width=50, height=30, text_color='black',
                                                     fg_color="#b4a7d6",
                                                     hover_color="#ffffff", command=lambda: self.deleteCategory())
        self.delete_button.place(x=320, y=58)

    # ========================================= Functions =================================================
    # display category
    def displayCategory1(self):
        connectDatabase()
        self.cur = connect.cursor()
        self.cur.execute("SELECT cat_name FROM category WHERE user_id = 1") # change user_id = ?
        rows = self.cur.fetchall()
        global count
        count = 0
        for row in rows:  # loop to display all the invoice
            if count % 2 == 0:
                self.CategoryTree.insert("", END, values=row, tags='evenrow')
            else:
                self.CategoryTree.insert("", END, values=row, tags='oddrow')
            count += 1

    # update and display tree
    def updatetree(self):
        self.CategoryTree.delete(*self.CategoryTree.get_children())
        self.displayCategory1()

    # ======= add new category ======
    def addCategoryWindow(self, Toplevel):
        self.addWindow = tk.Toplevel()
        self.addWindow.title("Add Category")
        self.addWindow.configure(bg='#1A1A1A')
        self.addWindow.iconphoto(False, tk.PhotoImage(file="logo_refined.png"))
        self.addWindow.geometry('450x300')

        # Labels
        self.AddCategoryLabel = Label(self.addWindow, text='Add Category', fg='white', bg='#1A1A1A',
                                     font=tkFont.Font(family='calibri', size=20))
        self.AddCategoryLabel.pack(pady=10)

        self.CategoryNameLabel = Label(self.addWindow, text='Category Name', fg='white', bg='#1A1A1A',
                                      font=tkFont.Font(family='calibri', size=15))
        self.CategoryNameLabel.pack(pady=10)

        # Entries
        self.AddCategoryNameEntry = Entry(self.addWindow, width=30, fg='white', bg='#1A1A1A', relief=FLAT)
        self.AddCategoryNameEntry.pack(pady=5)
        self.accname_line = Canvas(self.addWindow, width=200, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.accname_line.pack()

        # Buttons
        self.addConfirm = customtkinter.CTkButton(self.addWindow, text='OK', width=50, height=30, fg_color="#464E63",
                                                  hover_color="#667190", command=lambda: self.addCategory())
        self.addConfirm.pack(pady=10)

        self.cancel = customtkinter.CTkButton(self.addWindow, text='Cancel', width=55, height=30, fg_color="#464E63",
                                              hover_color="#667190", command=lambda: self.closeAdd())
        self.cancel.pack(pady=10)

    # add category
    def addCategory(self):
        connectDatabase()
        self.AddCategoryNameEntry.get()

        # validation
        if not self.AddCategoryNameEntry.get():
            messagebox.showerror('Error', "Please fill in all the fields!")
        else:
            try:
                user = 1
                cur.execute("""INSERT INTO category (cat_name, user_id) VALUES(?,?) """,
                            (self.AddCategoryNameEntry.get(), user))
                connect.commit()
                messagebox.showinfo('Record added', f"{self.AddCategoryNameEntry.get()} was successfully added")
                self.clearall()
                self.updatetree()
            except sqlite3.IntegrityError:
                messagebox.showerror('Error', "Database failed to update")

    # clear entry
    def clearall(self):
        self.AddCategoryNameEntry.delete(0, END)

    # close add window
    def closeAdd(self):
        self.addWindow.destroy()

    # ========== Edit Account ===========
    def editCategoryWindow(self, Toplevel):
        if not self.CategoryTree.selection():  # if not select any row
            tk.messagebox.showerror("Error", "Please select a category to edit")
        else:  # after selected a row
            selected = self.CategoryTree.focus()
            values = self.CategoryTree.item(selected)
            selection = values["values"]
            connectDatabase()
            user = 1
            cur.execute("SELECT c.cat_id FROM category c, user u WHERE c.user_id = u.user_id AND c.cat_name = ? "
                        "AND c.user_id = ?", (selection[0], user,))
            self.CatID = cur.fetchall()
            self.catID = self.CatID[0][0]
            self.cat_name = selection[0]

            # window configure
            self.editWindow = tk.Toplevel()
            self.editWindow.title("Edit Account")
            self.editWindow.configure(bg='#1A1A1A')
            self.editWindow.iconphoto(False, tk.PhotoImage(file="logo_refined.png"))
            self.editWindow.geometry('450x300')

            # Labels
            self.EditCategoryLabel = Label(self.editWindow, text='Edit Category', fg='white', bg='#1A1A1A',
                                              font=tkFont.Font(family='calibri', size=20))
            self.EditCategoryLabel.pack(pady=10)

            self.EditCategoryNameLabel = Label(self.editWindow, text='Category Name', fg='white', bg='#1A1A1A',
                                                  font=tkFont.Font(family='calibri', size=15))
            self.EditCategoryNameLabel.pack(pady=10)

            # Entries
            self.EditCategoryNameEntry = Entry(self.editWindow, width=30, fg='white', bg='#1A1A1A', justify=CENTER,
                                               relief=FLAT)
            self.EditCategoryNameEntry.pack(pady=5)
            self.EditCatName_line = Canvas(self.editWindow, width=200, height=2.0, bg="#bdb9b1", highlightthickness=0)
            self.EditCatName_line.pack()

            # Buttons
            self.editConfirm = customtkinter.CTkButton(self.editWindow, text='OK', width=50, height=30, fg_color="#464E63",
                                                      hover_color="#667190", command=lambda: self.editCat())
            self.editConfirm.pack(pady=10)

            self.Editcancel = customtkinter.CTkButton(self.editWindow, text='Cancel', width=50, height=30, fg_color="#464E63",
                                                      hover_color="#667190", command=lambda: self.editWindow.destroy())
            self.Editcancel.pack(pady=10)
            
            # display record in Entry box
            self.EditCategoryNameEntry.insert(0, selection[0])

    # update new value of category
    def editCat(self):
        connectDatabase()
        if not self.EditCategoryNameEntry.get():
            messagebox.showerror('Error', "Please fill in all the fields!")
        else:
            cur.execute("UPDATE category SET cat_name = ? WHERE cat_id =?",
                        (self.EditCategoryNameEntry.get(), self.catID,))
            # edit values in database
            connect.commit()  # commit changes
            messagebox.showinfo('Update', f"{self.EditCategoryNameEntry.get()} was successfully edited.")
            self.updatetree()  # display updated value
            self.editWindow.destroy()  # close Edit window

    # ========== Delete Category ==========
    def deleteCategory(self):
        if not self.CategoryTree.selection():  # if not select any row
            tk.messagebox.showerror("Error", "Please select a category to delete")
        else:  # To confirm the user really want to delete?
            result = tk.messagebox.askquestion('Confirm', 'Are you sure you want to delete this category?', icon="warning")
            if result == 'yes':
                cat = self.CategoryTree.focus()
                contents = (self.CategoryTree.item(cat))
                selected = contents['values']
                self.CategoryTree.delete(cat)
                cursor = cur.execute("DELETE FROM category WHERE cat_name=?", (str(selected[0]),))
                connect.commit()  # delete data from database
                cursor.close()
                tk.messagebox.showinfo('Deleted', 'The category is successfully delete.')
                self.CategoryTree.delete(*self.CategoryTree.get_children())  # clear all rows in tree table
                self.displayCategory1()  # redisplay the data

c = Category(window)
window.mainloop()
