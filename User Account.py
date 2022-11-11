import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
from tkinter import messagebox
import customtkinter
import sqlite3
import os

window = Tk()
window.title("ICCOUNTANT")
window.geometry("1280x720")
window.state('zoomed')
window.resizable(False, False)
window.iconphoto(False, tk.PhotoImage(file="logo_refined.png"))
window.configure(bg='#1A1A1A')
customtkinter.set_appearance_mode("dark")

def connectDatabase():
    try:
        global connect
        global cursor
        # connect to database
        connect = sqlite3.connect("Iccountant")
        cursor = connect.cursor()
    except:
        messagebox.showerror('Error', 'Cannot connect to database!')


class UserAccount:
    def __init__(self, master, controller):
        self.controller = controller
        self.hide_button = None
        Frame.__init__(self, master)

        self.menuFrame = Frame(self, bg='#000000', width=180, height=master.winfo_height(),
                               highlightbackground='#1A1A1A')  # 000000
        self.menuFrame.pack(side=LEFT, fill=BOTH)

        self.sideFrame = Frame(self, bg='#1A1A1A', width=1280, height=720)
        self.sideFrame.place(x=180, y=0)

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

        # Defining the buttons for menu bar
        self.logo_l = Label(self.menuFrame, image=self.logo, bg='#000000')
        self.logo_l.grid(row=1)
        self.dashboard_b = Button(self.menuFrame, image=self.dashboard, bg='#000000', relief='flat',
                                  command=lambda: controller.show_frame(Dashboard))
        self.dashboard_b.grid(row=2)
        self.statistic_b = Button(self.menuFrame, image=self.statistic, bg='#000000', relief='flat')
        self.statistic_b.grid(row=3)
        self.transaction_b = Button(self.menuFrame, image=self.transaction, bg='#000000', relief='flat',
                                    command=lambda: self.controller.show_frame(Transaction))
        self.transaction_b.grid(row=4)
        self.category_b = Button(self.menuFrame, image=self.category, bg='#000000', relief='flat',
                                 command=lambda: controller.show_frame(Category))
        self.category_b.grid(row=5)
        self.account_b = Button(self.menuFrame, image=self.account, bg='#000000', relief='flat',
                                command=lambda: controller.show_frame(Account))
        self.account_b.grid(row=6)
        self.currency_b = Button(self.menuFrame, image=self.currency, bg='#000000', relief='flat', command=self.con)
        self.currency_b.grid(row=7)
        self.calculator_b = Button(self.menuFrame, image=self.calculator, bg='#000000', relief='flat', command=self.cal)
        self.calculator_b.grid(row=8)
        self.customer_b = Button(self.menuFrame, image=self.customer, bg='#000000', relief='flat')
        self.customer_b.grid(row=9)
        self.tips_b = Button(self.menuFrame, image=self.tips, bg='#000000', relief='flat')
        self.tips_b.grid(row=10)
        self.logout_b = Button(self.menuFrame, image=self.logout, bg='#000000', relief='flat',
                               command=self.logout_system)
        self.logout_b.place(x=1, y=570)
        self.user_b = Button(self.menuFrame, image=self.user, bg='#000000', relief='flat',
                             command=lambda: self.controller.show_frame(UserAccount))
        self.user_b.place(x=10, y=610)

        # So that it does not depend on the widgets inside the frame
        self.menuFrame.grid_propagate(False)

        # ============================== User Account Display Frame =========================================

        connectDatabase()
        cursor.execute("SELECT username FROM user WHERE user_id = 1")  # change  to user_id=?
        username = cursor.fetchone()
        username_get = username[0]

        cursor.execute("SELECT email FROM user WHERE user_id = 1")  # change to user_id=?
        email = cursor.fetchone()
        email_get = email[0]

        # Labels
        self.UsernameLabel = Label(self.sideFrame, text='USERNAME ', fg='white', bg='#1A1A1A',
                                     font=tkFont.Font(family='Lato', size=15))
        self.UsernameLabel.pack(padx=10, pady=5, anchor=W)

        self.username_l = Label(self.sideFrame, fg='white', bg='#333333', width=30,
                                     font=tkFont.Font(family='calibri', size=15, slant="italic"))
        self.username_l.config(text=str(username_get))
        self.username_l.pack(padx=10, pady=5, anchor=N)

        self.EmailLabel = Label(self.sideFrame, text='EMAIL ', fg='white', bg='#1A1A1A',
                                      font=tkFont.Font(family='Lato', size=15))
        self.EmailLabel.pack(padx=10, pady=10, anchor=W)

        self.email_l = Label(self.sideFrame, fg='white', bg='#333333', width=30,
                                     font=tkFont.Font(family='calibri', size=15, slant="italic"))
        self.email_l.config(text=str(email_get))
        self.email_l.pack(padx=10, pady=5, anchor=N)

        self.Label = Label(self.sideFrame, text='', bg='#1A1A1A')
        self.Label.pack(padx=100, pady=100)

        self.editUsername_button = customtkinter.CTkButton(self.sideFrame, text='Edit Username', width=50, height=30,
                                                           text_color='black', fg_color="#b4a7d6",
                                                           hover_color="#ffffff",
                                                           command=lambda: self.editUsername(Toplevel))
        self.editUsername_button.place(x=10, y=250)

        self.editPassword_button = customtkinter.CTkButton(self.sideFrame, text='Edit Password', width=50, height=30,
                                                           text_color='black',
                                                           fg_color="#b4a7d6",
                                                           hover_color="#ffffff",
                                                           command=lambda: self.editPassword(Toplevel))
        self.editPassword_button.place(x=210, y=250)


    def editUsername(self, Toplevel):
        self.editUsernameWindow = tk.Toplevel()
        self.editUsernameWindow.title("Edit Username")
        self.editUsernameWindow.configure(bg='#1A1A1A')
        self.editUsernameWindow.iconphoto(False, tk.PhotoImage(file="logo_refined.png"))
        self.editUsernameWindow.geometry('1000x600')

        # Buttons
        self.addConfirm = customtkinter.CTkButton(self.editUsernameWindow, text='OK', width=50, height=30, fg_color="#464E63",
                                                  hover_color="#667190", command=lambda: self.editusername())
        self.addConfirm.pack(pady=10)

        self.cancel = customtkinter.CTkButton(self.editUsernameWindow, text='Cancel', width=55, height=30, fg_color="#464E63",
                                              hover_color="#667190", command=lambda: self.editUsernameWindow.destroy())
        self.cancel.pack(pady=10)

    def editusername(self):
        pass

    def editPassword(self, Toplevel):
        self.editPasswordWindow = tk.Toplevel()
        self.editPasswordWindow.title("Edit Passwprd")
        self.editPasswordWindow.configure(bg='#1A1A1A')
        self.editPasswordWindow.iconphoto(False, tk.PhotoImage(file="logo_refined.png"))
        self.editPasswordWindow.geometry('1000x600')

        # Buttons
        self.addConfirm = customtkinter.CTkButton(self.editPasswordWindow, text='OK', width=50, height=30, fg_color="#464E63",
                                                  hover_color="#667190", command=lambda: self.editpassword())
        self.addConfirm.pack(pady=10)

        self.cancel = customtkinter.CTkButton(self.editPasswordWindow, text='Cancel', width=55, height=30, fg_color="#464E63",
                                              hover_color="#667190", command=lambda: self.editPasswordWindow.destroy())
        self.cancel.pack(pady=10)

    def editpassword(self):
        pass

    def con(self):
        os.system('CurrencyConverter.py')

    def cal(self):
        os.system('python calculator.py')

    def logout_system(self):
        answer = messagebox.askyesno(title='Confirmation', message='Are you sure that you want to logout?')
        if answer:
            messagebox.showinfo('Log Out', 'You have successfully Logged Out!')
            # self.controller.show_frame(LoginPage)


u = UserAccount(window)
window.mainloop()