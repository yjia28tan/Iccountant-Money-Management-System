import tkinter as tk
from sqlite3 import Cursor
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
from tkinter import messagebox
import sqlite3

window = Tk()
window.title("ICCOUNTANT")
window.geometry("1280x720")
window.resizable(None, None)
window.state('zoomed')
window.resizable(True, True)
window.iconphoto(False, tk.PhotoImage(file="logo_refined.png"))
window.configure(bg='#1A1A1A')


def show_frame(self, cont):
    frame = self.frames[cont]
    # raises the current frame to the top
    frame.tkraise()

# userID = IntVar()
global userID

def connectDatabase():
    try:
        global conn
        global cur
        # connect to database
        conn = sqlite3.connect("Iccountant")
        cur = conn.cursor()
    except:
        messagebox.showerror('Error', 'Cannot connect to database!')


class Account:
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

        # ============= Heading Label =================
        self.heading_label = Label(master, text='ACCOUNTS', fg='white', bg='#1A1A1A')
        self.heading_label.config(font=tkFont.Font(family='Lato', size=20, weight="bold", slant="italic"))
        self.heading_label.place(x=200, y=15)

        # ====================================== Account table ===============================================
        # Frame for tree view
        self.treeFrame = Frame(master, bg='#1A1A1A', width=1500, height=400)
        self.treeFrame.place(x=200, y=100)

        self.Account = ttk.Treeview(self.treeFrame, selectmode="extended", show='headings',
                                    columns=('Account', 'Amount'), height=20)
        self.Account.place(relwidth=1, relheight=1)

        self.Account.heading('Account', text='Account', anchor=CENTER)
        self.Account.heading('Amount', text='Amount', anchor=CENTER)

        self.Account.column("Account", anchor=CENTER, width=600)
        self.Account.column("Amount", anchor=CENTER, width=600)

        self.Account.tag_configure('oddrow', background='#cccccc')
        self.Account.tag_configure('evenrow', background='#999999')
        
        self.treestyle = ttk.Style()
        self.treestyle.theme_use("default")
        self.treestyle.configure("Treeview", background="#666666", foreground="black", fieldbackground="#666666",
                             rowheight=25)
        self.treestyle.configure('.', borderwidth=1)
        self.treestyle.map('Treeview', background=[('selected', '#9fc5f8')])
        self.treestyle.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        self.Account.pack()

        # call function to display Account
        self.displayAccount()

        # ============= Buttons ===============
        self.style = ttk.Style()
        self.style.configure('TButton', font=tkFont.Font(family='calibri', size=20, weight="bold", slant="italic"),
                             borderwidth='4')

        self.add_button = Button(master, text='Add', fg='white', bg='#666666', relief='ridge',
                                 command=lambda: self.addAccountWindow(Toplevel))
        self.add_button.place(x=200, y=58)
        self.edit_button = Button(master, text='Edit', fg='white', bg='#666666', relief='ridge',
                                  command=lambda: self.editAccountWindow(Toplevel))
        self.edit_button.place(x=260, y=58)
        self.delete_button = Button(master, text='Delete', fg='white', bg='#666666', relief='ridge',
                                    command=lambda: self.deleteAccount())
        self.delete_button.place(x=320, y=58)

    # ================================================ Functions =======================================================
    # display accounts of users
    def displayAccount(self):
        connectDatabase()
        cur = conn.cursor()
        cur.execute("SELECT acc_name, acc_amount FROM account WHERE user_id = 1 ")  # change 1 to user_id = ?
        rows = cur.fetchall()
                global count
        count = 0
        for row in rows:  # loop to display account
            if count % 2 == 0:
                self.Account.insert("", END, values=row, tags='evenrow')
            else:
                self.Account.insert("", END, values=row, tags='oddrow')
            count += 1

    # update and display tree
    def updatetree(self):
        self.Account.delete(*self.Account.get_children())
        self.displayAccount()

    # ========== Add New Accounts ==========
    def addAccountWindow(self, Toplevel):
        self.addWindow = tk.Toplevel()
        self.addWindow.title("Add Account")
        self.addWindow.configure(bg='#1A1A1A')
        self.addWindow.iconphoto(False, tk.PhotoImage(file="logo_refined.png"))
        self.addWindow.geometry('450x300')

        # Labels
        self.AddAccountLabel = Label(self.addWindow, text='Add Account', fg='white', bg='#1A1A1A',
                                     font=tkFont.Font(family='calibri', size=20))
        self.AddAccountLabel.pack()

        self.AccountNameLabel = Label(self.addWindow, text='Account Name', fg='white', bg='#1A1A1A',
                                      font=tkFont.Font(family='calibri', size=15))
        self.AccountNameLabel.place(x=50, y=60)

        self.AmountLabel = Label(self.addWindow, text='Begin Amount', fg='white', bg='#1A1A1A',
                                 font=tkFont.Font(family='calibri', size=15))
        self.AmountLabel.place(x=50, y=130)

        # Entries
        self.AccNameEntry = Entry(self.addWindow, width=30, fg='white', bg='#1A1A1A', relief=FLAT)
        self.AccNameEntry.place(x=50, y=88)
        self.accname_line = Canvas(self.addWindow, width=200, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.accname_line.place(x=50, y=110)

        self.AmountEntry = Entry(self.addWindow, width=30, fg='white', bg='#1A1A1A', relief=FLAT)
        self.AmountEntry.place(x=50, y=158)
        self.amount_line = Canvas(self.addWindow, width=200, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.amount_line.place(x=50, y=180)

        # Buttons
        self.addConfirm = Button(self.addWindow, text='OK', fg='white', bg='#666666', relief='ridge',
                                 command=lambda: self.addAcc())
        self.addConfirm.place(x=55, y=200)

        self.cancel = Button(self.addWindow, text='Cancel', fg='white', bg='#666666', relief='ridge',
                             command=lambda: self.addWindow.destroy())
        self.cancel.place(x=150, y=200)

    #  add account
    def addAcc(self):
        self.AccNameEntry.get()
        self.AmountEntry.get()
        # validation
        if not self.AccNameEntry.get() or not self.AmountEntry.get():
            messagebox.showerror('Error', "Please fill in all the fields!")
        else:
            try:
                float(self.AmountEntry.get()) # validate amount is float
                try:
                    user = 1
                    connectDatabase()
                    cur.execute("""INSERT INTO account ('acc_name', 'acc_amount', 'user_id') VALUES(?,?,?)""",
                                (self.AccNameEntry.get(), self.AmountEntry.get(), user))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo('Record added', f"{self.AccNameEntry.get()} was successfully added")
                    self.clearall()
                    self.updatetree()
                except sqlite3.IntegrityError:
                    messagebox.showerror('Error', "Database failed to update")
            except ValueError:
                messagebox.showerror('Error', "Amount must be a number!")


    # clear entry box for add window
    def clearall(self):
        self.AccNameEntry.delete(0, END)
        self.AmountEntry.delete(0, END)

    # ========== Edit Account ===========
    def editAccountWindow(self, Toplevel):
        if not self.Account.selection():  # if not select any row
            tk.messagebox.showerror("Error", "Please select an account to edit")
        else:  # after selected a row
            selected = self.Account.focus()
            values = self.Account.item(selected)
            selection = values["values"]
            connectDatabase()
            user = 1
            cur.execute("SELECT a.acc_id FROM account a, user u WHERE a.user_id =  u.user_id AND a.acc_name = ? "
                             "AND a.acc_amount = ? AND a.user_id = ?",
                             (selection[0], selection[1], user, ))
            self.AccID = cur.fetchall()
            self.accID = self.AccID[0][0]
            self.acc_name = selection[0]
            self.acc_amount = selection[1]

            # window configure
            self.editWindow = tk.Toplevel()
            self.editWindow.title("Edit Account")
            self.editWindow.configure(bg='#1A1A1A')
            self.editWindow.iconphoto(False, tk.PhotoImage(file="logo_refined.png"))
            self.editWindow.geometry('450x300')

            # Labels
            self.EditAccountLabel = Label(self.editWindow, text='Edit Account', fg='white', bg='#1A1A1A',
                                         font=tkFont.Font(family='calibri', size=20))
            self.EditAccountLabel.pack()

            self.EditAccountNameLabel = Label(self.editWindow, text='Account Name', fg='white', bg='#1A1A1A',
                                          font=tkFont.Font(family='calibri', size=15))
            self.EditAccountNameLabel.place(x=50, y=60)

            self.EditAmountLabel = Label(self.editWindow, text='Begin Amount', fg='white', bg='#1A1A1A',
                                     font=tkFont.Font(family='calibri', size=15))
            self.EditAmountLabel.place(x=50, y=130)

            # Entries
            self.EditAccNameEntry = Entry(self.editWindow, width=30, fg='white', bg='#1A1A1A', relief=FLAT)
            self.EditAccNameEntry.place(x=50, y=88)
            self.Editaccname_line = Canvas(self.editWindow, width=200, height=2.0, bg="#bdb9b1", highlightthickness=0)
            self.Editaccname_line.place(x=50, y=110)

            self.EditAmountEntry = Entry(self.editWindow, width=30, fg='white', bg='#1A1A1A', relief=FLAT)
            self.EditAmountEntry.place(x=50, y=158)
            self.Editamount_line = Canvas(self.editWindow, width=200, height=2.0, bg="#bdb9b1", highlightthickness=0)
            self.Editamount_line.place(x=50, y=180)

            # Buttons
            self.editConfirm = Button(self.editWindow, text='OK', fg='white', bg='#666666', relief='ridge',
                                      command=lambda: self.editAccount())
            self.editConfirm.place(x=55, y=200)

            self.Editcancel = Button(self.editWindow, text='Cancel', fg='white', bg='#666666', relief='ridge',
                                 command=lambda: self.editWindow.destroy())
            self.Editcancel.place(x=150, y=200)

            # display record in Entry box
            for record in self.AccID:
                self.EditAccNameEntry.insert(0, selection[0])
                self.EditAmountEntry.insert(0, selection[1])

    # update new value of account
    def editAccount(self):
        connectDatabase()
        if not self.EditAccNameEntry.get() or not self.EditAmountEntry.get():
            messagebox.showerror('Error', "Please fill in all the fields!")
        else:
            try:
                float(self.EditAmountEntry.get()) # validate amount is float
                cur.execute("UPDATE account SET acc_name = ?, acc_amount = ? WHERE acc_id =?",
                            (self.EditAccNameEntry.get(), self.EditAmountEntry.get(), self.accID,))
                # edit values in database
                conn.commit()  # commit changes
                messagebox.showinfo('Update', f"{self.acc_name} account was successfully edited")
                self.updatetree()  # display updated value
                self.editWindow.destroy()  # close Edit window
            except ValueError:
                messagebox.showerror('Error', "Amount must be a number!")

    # ========== Delete Account ==========
    def deleteAccount(self):
        if not self.Account.selection():  # if not select any row
            tk.messagebox.showerror("Error", "Please select an account to delete")
        else:  # To confirm the user really want to delete?
            result = tk.messagebox.askquestion('Confirm', 'Are you sure you want to delete this account?',
                                               icon="warning")
            if result == 'yes':
                acc = self.Account.focus()
                contents = (self.Account.item(acc))
                selected = contents['values']
                self.Account.delete(acc)
                cursor = cur.execute("DELETE FROM account WHERE acc_name=?", (str(selected[0]),))
                conn.commit()  # delete data from database
                cursor.close()
                tk.messagebox.showinfo('Deleted', 'The account is successfully delete')
                self.Account.delete(*self.Account.get_children())  # clear all rows in tree table
                self.displayAccount()  # redisplay the data

a = Account(window)
window.mainloop()
