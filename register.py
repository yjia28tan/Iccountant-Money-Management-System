import math
import random  # to create otp
import smtplib  # to send email
import requests  # to verify email
import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont
import customtkinter
import os

# Create Database
connect = sqlite3.connect('Iccountant.db')
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS user (
    user_id    INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name       VARCHAR NOT NULL,
    username   VARCHAR NOT NULL,
    email      VARCHAR NOT NULL,
    password   VARCHAR NOT NULL);''')
connect.commit()


class RegisterPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1280x720')
        self.root.resizable(None, None)
        self.root.title("Iccountant Money Management System")
        self.root.config(bg='black')
        self.root.state('zoomed')

        # register pages
        self.pg1 = tk.Frame(self.root, bg='black')

        # page 1
        self.pg1_title = tk.Label(self.pg1, text='User Account Registration', fg='white', bg='black')
        self.pg1_title.config(font=tkFont.Font(family='Lato', size=20, weight="bold"))
        self.pg1_title.pack(anchor=NW, padx=80, pady=5)
        Canvas(self.pg1, width=1000, height=2.0, bg='white', highlightthickness=1).pack(pady=10)
        tk.Label(self.pg1, text='', bg='black').pack(pady=8)

        # full name
        self.fname_lb = tk.Label(self.pg1, text='Full name', fg='white', bg='black')
        self.fname_lb.config(font=tkFont.Font(family='Lato', size=15, weight="bold"))
        self.fname_lb.pack(pady=5)
        self.fname = StringVar()
        self.fname_entry = Entry(self.pg1, justify='center', width=30, highlightthickness=0, textvariable=self.fname,
                                 relief=FLAT, font=('Bold', 12), fg='white', bg='black', insertbackground='white')
        self.fname_entry.config(font=tkFont.Font(family='Lato', size=12))
        self.fname_entry.pack()
        self.fname_line = Canvas(self.pg1, width=300, height=2.0, bg='white', highlightthickness=0)
        self.fname_line.pack()
        tk.Label(self.pg1, text='', bg='black').pack(pady=3)

        # username
        self.username_lb = tk.Label(self.pg1, text='Username', fg='white', bg='black')
        self.username_lb.config(font=tkFont.Font(family='Lato', size=15, weight="bold"))
        self.username_lb.pack(pady=5)
        self.username = StringVar()
        self.username_lb_entry = Entry(self.pg1, justify='center', width=30, highlightthickness=0,
                                       textvariable=self.username, relief=FLAT, font=('Bold', 12), fg='white',
                                       bg='black', insertbackground='white')
        self.username_lb_entry.config(font=tkFont.Font(family='Lato', size=12))
        self.username_lb_entry.pack()
        self.username_lb_line = Canvas(self.pg1, width=300, height=2.0, bg='white', highlightthickness=0)
        self.username_lb_line.pack()
        tk.Label(self.pg1, text='', bg='black').pack(pady=3)

        # email
        # User Email Label and Text Entry Box
        self.email_lb = tk.Label(self.pg1, text='Email', fg='white', bg='black')
        self.email_lb.config(font=tkFont.Font(family='Lato', size=15, weight="bold"))
        self.email_lb.pack(pady=5)
        self.email = StringVar()
        self.email_entry = Entry(self.pg1, justify='center', width=30, highlightthickness=0, textvariable=self.email,
                                 relief=FLAT, font=('Bold', 12), fg='white', bg='black', insertbackground='white')
        self.email_entry.config(font=tkFont.Font(family='Lato', size=12))
        self.email_entry.pack()
        self.email_line = Canvas(self.pg1, width=300, height=2.0, bg='white', highlightthickness=0)
        self.email_line.pack()
        tk.Label(self.pg1, text='', bg='black').pack(pady=3)

        # password
        self.password_lb = tk.Label(self.pg1, text='Password', font=('Bold', 15), fg='white', bg='black')
        self.password_lb.config(font=tkFont.Font(family='Lato', size=15, weight="bold"))
        self.password_lb.pack(pady=5)
        self.password = StringVar()
        self.password_lb_entry = Entry(self.pg1, justify='center', width=30, highlightthickness=0,
                                       textvariable=self.password, relief=FLAT, font=('Bold', 12), show='*', fg='white',
                                       bg='black', insertbackground='white')
        self.password_lb_entry.config(font=tkFont.Font(family='Lato', size=12))
        self.password_lb_entry.pack()
        self.password_lb_line = Canvas(self.pg1, width=300, height=2.0, bg='white', highlightthickness=0)
        self.password_lb_line.pack()
        tk.Label(self.pg1, text='', bg='black').pack(pady=3)

        # confirm password
        self.conpassword_lb = tk.Label(self.pg1, text='Confirm Password', fg='white', bg='black')
        self.conpassword_lb.config(font=tkFont.Font(family='Lato', size=15, weight="bold"))
        self.conpassword_lb.pack(pady=5)
        self.conpassword = StringVar()
        self.conpassword_lb_entry = Entry(self.pg1, justify='center', width=30, highlightthickness=0,
                                          textvariable=self.conpassword, relief=FLAT, font=('Bold', 12), show='*',
                                          fg='white', bg='black', insertbackground='white')
        self.conpassword_lb_entry.config(font=tkFont.Font(family='Lato', size=12))
        self.conpassword_lb_entry.pack()
        self.conpassword_lb_line = Canvas(self.pg1, width=300, height=2.0, bg='white', highlightthickness=0)
        self.conpassword_lb_line.pack()
        self.btn_value = IntVar(value=0)
        self.check_btn = Checkbutton(self.pg1, text="Show password", variable=self.btn_value,
                                     command=self.show_password, fg='white', bg='black')
        self.check_btn.pack()
        self.pg1.pack(pady=40)

        # buttons
        # next button
        self.nextbtn = customtkinter.CTkButton(master=self.pg1, text="Next", width=140, height=40, fg_color="#464E63",
                                               hover_color="#667190", command=self.data_validation)
        self.nextbtn.pack(side=tk.RIGHT)

        # back button
        self.back = ImageTk.PhotoImage(Image.open('backicon.png').resize((40, 40), resample=Image.LANCZOS))
        self.backbtn1 = Button(self.pg1, image=self.back, bg='black', relief='flat', command=self.open_login)
        self.backbtn1.place(x=3, y=1)

    # page 2
    def page2(self):
        self.pg2 = Toplevel()
        self.pg2.geometry("1280x720")
        self.pg2.resizable(None, None)
        self.pg2.title("Iccountant")
        self.pg2.configure(bg='black')
        self.pg2_title = tk.Label(self.pg2, text='Email Verification', fg='white', bg='black')
        self.pg2_title.config(font=tkFont.Font(family='Lato', size=20, weight="bold"))
        self.pg2_title.place(x=225, y=45)
        Canvas(self.pg2, width=1000, height=2.0, bg='white', highlightthickness=1).place(x=640, y=100,
                                                                                         anchor=tk.CENTER)

        # otp
        self.otp_lb = tk.Label(self.pg2, text='4-digit OTP', fg='white', bg='black')
        self.otp_lb.config(font=tkFont.Font(family='Lato', size=15, weight="bold"))
        self.otp_lb.place(x=640, y=230, anchor=tk.CENTER)
        self.otp_ = StringVar()
        self.otp_lb_entry = Entry(self.pg2, justify='center', width=30, highlightthickness=0,
                                  textvariable=self.otp_, relief=FLAT, font=('Bold', 15), show='*', fg='white',
                                  bg='black', insertbackground='white')
        self.otp_lb_entry.config(font=tkFont.Font(family='Lato', size=12))
        self.otp_lb_entry.place(x=640, y=265, anchor=tk.CENTER)
        self.otp_lb_line = Canvas(self.pg2, width=300, height=2.0, bg='white', highlightthickness=0)
        self.otp_lb_line.place(x=640, y=280, anchor=tk.CENTER)

        # back button
        self.back2 = ImageTk.PhotoImage(Image.open('backicon.png').resize((40, 40), resample=Image.LANCZOS))
        self.backbtn2 = Button(self.pg2, image=self.back2, bg='black', relief='flat', command=lambda:
        self.pg2.destroy())
        self.backbtn2.place(x=140, y=40)

        # finish button
        self.nextbtn = customtkinter.CTkButton(master=self.pg2,
                                               text="Finish",
                                               width=140, height=40,
                                               fg_color="#464E63",
                                               hover_color="#667190",
                                               command=self.finish_session)
        self.nextbtn.pack(side=tk.RIGHT, padx=140, pady=320)

    def gobackpage1(self):
        self.pg2.quit()
        self.show_frame(self.pg1)

    def show_password(self):
        if self.btn_value.get() == 1:
            self.password_lb_entry.config(show='')
            self.conpassword_lb_entry.config(show='')
        else:
            self.password_lb_entry.config(show='*')
            self.conpassword_lb_entry.config(show='*')

    def data_validation(self):
        self.name = self.fname.get()
        self.uname = self.username.get()
        self.pwd = self.password.get()
        self.conpwd = self.conpassword.get()
        self.email_ = self.email.get()

        # email stuff
        self.s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        self.s.starttls()

        # authentication
        self.s.login("iccountant2022@gmail.com", "vgndqclbhalavixj")

        # create 4-digit OTP
        self.digits = "0123456789"
        self.OTP = ""
        for i in range(4):
            self.OTP += self.digits[math.floor(random.random() * 10)]

        # message to be sent
        self.subject = "Email verification code"
        self.text = "Hi user,\n\nYour OTP for the registration is:\n\n" + self.OTP + "\n\nThank you.\n\n\nIccountant"
        self.msg = 'Subject: {}\n\n{}'.format(self.subject, self.text)
        self.response = requests.get("https://isitarealemail.com/api/email/validate", params={'email': self.email_})
        self.status = self.response.json()['status']

        # input validation
        if not self.fname.get() or not self.name or not self.uname or not self.email_ or not self.pwd or not \
                self.conpwd:
            messagebox.showerror('Error!', "Please fill the form!")
        else:
            cursor.execute('SELECT * from user where username="%s"' % self.uname)
            if cursor.fetchone():
                messagebox.showerror('Error!', "Please enter a unique username!")
            else:
                cursor.execute('SELECT * from user where email="%s"' % self.email_)
                if cursor.fetchone():
                    messagebox.showerror('Error!', "Please enter a unique email!")
                elif len(self.pwd) < 8:
                    messagebox.showerror('Error!', "Please enter a password that is at least 8 characters!")
                elif self.pwd != self.conpwd:
                    messagebox.showerror('Error!', "Please match both password and confirm password!")
                elif self.status != "valid":
                    messagebox.showerror('Error!', "Please enter a valid/existing email!")
                else:
                    messagebox.showinfo('Success!', "All of the form is filled!")
                    self.s.sendmail("all2ctt@gmail.com", self.email_, self.msg)
                    self.page2()

    def insert_data(self):
        cursor.execute("INSERT INTO user (name,username,email,password) VALUES (:name, :username, :email, :password)",
                       {'name': self.name, 'username': self.uname, 'email': self.email_, 'password': self.pwd})
        connect.commit()
        messagebox.showinfo('Confirmation', 'Record Saved! Session is finished!')
        self.root.destroy()
        os.system('Login.py')

    def finish_session(self):
        if self.otp_.get() == self.OTP:
            messagebox.showinfo('Success!', "OTP verified!")

            # message to be sent: successfully registered
            self.subject2 = "Icccountant account has successfully registered!"
            self.text2 = "Hi user,\n\nYour account for Icccountant desktop app has successfully registered.\n" \
                         "Thank you.\n\n\nIccountant"
            self.msg2 = 'Subject: {}\n\n{}'.format(self.subject2, self.text2)
            self.s.sendmail("all2ctt@gmail.com", self.email_, self.msg2)

            # terminating the session
            self.s.quit()
            self.insert_data()
        else:
            messagebox.showerror('Error!', "incorrect OTP try again!")

    def show_frame(self, frame):
        frame.tkraise()

    def open_login(self):
        self.root.destroy()
        os.system('window.py')


def main():
    root = tk.Tk()
    RegisterPage(root)
    root.mainloop()


if __name__ == '__main__':
    main()
