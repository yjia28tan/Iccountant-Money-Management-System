import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import sqlite3
from tkinter import messagebox
import pandas as pd
from datetime import datetime
from tkcalendar import DateEntry
import tkinter.font as tkFont
import customtkinter
import math
import random  # to create otp
import smtplib  # to send email
import requests  # to verify email

customtkinter.set_appearance_mode("dark")
connect = sqlite3.connect('Iccountant')
# connect = sqlite3.connect('Iccountant.db')
cursor = connect.cursor()


class windows(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.title("Iccountant Money Management System")
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.geometry('1280x720')
        self.config(bg='black')
        self.resizable(FALSE, FALSE)

        # Creating the sharing variables across classes
        self.shared_user_id = {'userID': IntVar()}

        # creating a frame and assigning it to container
        self.container = container = tk.Frame(self, height='720', width='1280', bg='black')
        # container = Frame(self, height='720', width='1280')
        # specifying the region where the frame is packed in root
        container.pack_configure(fill=BOTH, expand=TRUE)

        # configuring the location of the container using grid
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}

        # we'll create the frames themselves later but let's add the components to the dictionary.
        # for F in (LoginPage, RegisterPage, ForgotPassword, Dashboard, Account): # , Category, Transaction,
        #     frame = F(container, self)
        #
        #     # the windows class acts as the root window for the frames.
        #     self.frames[F] = frame
        #     frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(LoginPage)

    def show_frame(self, controller):
        if controller not in self.frames:
            self.frames[controller] = frame = controller(self.container, self)
            frame.grid(row=0, column=0, sticky="nsew")
            # frame.grid_size()
        frame = self.frames[controller]
        # raises the current frame to the top
        frame.tkraise()


class LoginPage(tk.Frame):
    def __init__(self, window, controller):
        self.controller = controller
        self.hide_button = None
        Frame.__init__(self, window)

        self.LoginFrame = tk.Frame.__init__(self, window, bg="black")

        self.logo_frame = Frame(self, bg='black')
        self.logo_frame.pack(side='left',  fill='both', expand=True)
        self.lgn_frame = Frame(self, bg='black')
        self.lgn_frame.pack(side='right',  fill='both', expand=True)

        tk.Label(self.logo_frame, text='', bg='black').pack(pady=50)
        # import picture
        self.logo = ImageTk.PhotoImage(Image.open("logo_refined.png").resize((500, 381), resample=Image.LANCZOS))
        self.logo1 = Label(self.logo_frame, image=self.logo, bg='black')
        self.logo1.pack(anchor=CENTER, pady=50)

        # title
        tk.Label(self.lgn_frame, text='', bg='black').pack(pady=50)
        self.lgn_title = tk.Label(self.lgn_frame, text='Log In', fg='white', bg='black')
        self.lgn_title.config(font=tkFont.Font(family='Lato', size=20, weight="bold"))
        self.lgn_title.pack(pady=20)
        tk.Label(self.lgn_frame, text='', bg='black').pack(pady=10)

        # email/username
        self.username_or_email_lb = tk.Label(self.lgn_frame, text='Email/username', fg='white', bg='black')
        self.username_or_email_lb.config(font=tkFont.Font(family='Lato', size=15, weight="bold"))
        self.username_or_email_lb.pack(pady=5)
        self.username_or_email = StringVar()
        self.username_or_email_entry = Entry(self.lgn_frame, justify='center', width=30, highlightthickness=0,
                                             textvariable=self.username_or_email, relief=FLAT, fg='white', bg='black',
                                             insertbackground='white')
        self.username_or_email_entry.config(font=tkFont.Font(family='Lato', size=12))
        self.username_or_email_entry.pack(pady=5)
        self.username_or_email_line = Canvas(self.lgn_frame, width=300, height=2.0, bg='white', highlightthickness=0)
        self.username_or_email_line.pack()

        # password
        self.password_lb = tk.Label(self.lgn_frame, text='Password', fg='white', bg='black')
        self.password_lb.config(font=tkFont.Font(family='Lato', size=15, weight="bold"))
        self.password_lb.pack(pady=5)
        self.password = StringVar()
        self.password_lb_entry = Entry(self.lgn_frame, justify='center', width=30, highlightthickness=0,
                                       textvariable=self.password, relief=FLAT, fg='white', bg='black',
                                       insertbackground='white', show='*')
        self.password_lb_entry.config(font=tkFont.Font(family='Lato', size=12))
        self.password_lb_entry.pack(pady=5)
        self.password_lb_line = Canvas(self.lgn_frame, width=300, height=2.0, bg='white', highlightthickness=0)
        self.password_lb_line.pack()
        self.btn_value = IntVar(value=0)
        self.check_btn = Checkbutton(self.lgn_frame, text='Show password', variable=self.btn_value,
                                     command=lambda : show_password(self), fg='white', bg='black')
        self.check_btn.pack(pady=5)

        # import button #master=self.lgn_frame
        self.lgnbtn = customtkinter.CTkButton(self.lgn_frame, text="Login", width=220, height=40,
                                              fg_color="#464E63", hover_color="#667190",
                                              command=lambda: data_validation(self))
        self.lgnbtn.pack(pady=5)

        # register
        self.regbtn = customtkinter.CTkButton(self.lgn_frame, text="Register", width=220, height=40,
                                              fg_color="#464E63", hover_color="#667190",
                                              command=lambda: controller.show_frame(RegisterPage))
        self.regbtn.pack(pady=5)

        # forgot password
        self.fgpbtn = customtkinter.CTkButton(master=self.lgn_frame, text="Forgot Password?", width=220, height=40,
                                              fg_color="#464E63", hover_color="#667190",
                                              command=lambda: controller.show_frame(ForgotPassword))
        self.fgpbtn.pack(pady=5)

        # self.user = Entry(self.lgn_frame, justify='center', bg='black', fg='red',
        #                   textvariable=self.controller.shared_user_id["userID"])
        # self.user.pack()

        def show_password(self):
            if self.btn_value.get() == 1:
                self.password_lb_entry.config(show='')

            else:
                self.password_lb_entry.config(show='*')

        def data_validation(self):
            self.uname_email = self.username_or_email.get()
            self.pwd = self.password.get()

            # applying empty validation
            if not self.uname_email or not self.pwd:
                messagebox.showerror('Error!', "Please fill the form!")
            else:
                # fetch with username
                cur = connect.execute('SELECT * from user where username="%s"  and password="%s"' % (self.uname_email,
                                                                                                     self.pwd))
                if cur.fetchone():
                    messagebox.showinfo('Success!', "Login Success!")
                    cur = connect.execute(
                        'SELECT user_id from user WHERE username ="%s" and password="%s"' % (self.uname_email, self.pwd))
                    USER_ID = cur.fetchone() # output: (1,)
                    userid = USER_ID[0] # output: 1
                    self.controller.shared_user_id['userID'].set(int(userid))
                    self.controller.shared_user_id['userID'].get()
                    controller.show_frame(Dashboard)
                else:
                    # fetch with email
                    cur = connect.execute('SELECT * from user where email="%s" and password="%s"' % (self.uname_email,
                                                                                                     self.pwd))
                    if cur.fetchone():
                        messagebox.showinfo('Success!', "Login Success!")
                        cur = connect.execute('SELECT user_id from user WHERE email="%s" and password="%s"' %
                                              (self.uname_email, self.pwd))
                        USER_ID = cur.fetchone()  # output: (1,)
                        userid = USER_ID[0]  # output: 1
                        self.controller.shared_user_id['userID'].set(int(userid))
                        self.controller.shared_user_id['userID'].get()
                        controller.show_frame(Dashboard)
                    else:
                        messagebox.showerror('Error!', "Incorrect email, username, or password!")


class RegisterPage(tk.Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        self.hide_button = None
        self.controller = controller

        self.pg1 = Frame(self, bg='black')
        self.pg1.pack(fill=BOTH)

        # page 1
        tk.Label(self.pg1, text='', bg='black').pack(anchor=CENTER, pady=5)
        self.pg1_title = tk.Label(self.pg1, text='User Account Registration', fg='white', bg='black')
        self.pg1_title.config(font=tkFont.Font(family='Lato', size=20, weight="bold"))
        self.pg1_title.pack(anchor=CENTER, padx=0, pady=5)
        Canvas(self.pg1, width=1000, height=2.0, bg='white', highlightthickness=1).pack(anchor=CENTER, padx=150, pady=2)
        tk.Label(self.pg1, text='', bg='black').pack(anchor=CENTER, pady=5)

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
                                     command=lambda: show_password(self), fg='white', bg='black')
        self.check_btn.pack()

        # buttons
        # next button
        self.nextbtn = customtkinter.CTkButton(master=self.pg1, text="Next", width=140, height=40, fg_color="#464E63",
                                               hover_color="#667190", command=lambda: data_validation(self))
        self.nextbtn.pack(side=tk.RIGHT, anchor=W, padx=170)

        # back button
        self.back = ImageTk.PhotoImage(Image.open('backicon.png').resize((40, 40), resample=Image.LANCZOS))
        self.backbtn1 = Button(self.pg1, image=self.back, bg='black', relief='flat',
                               command=lambda: controller.show_frame(LoginPage))
        self.backbtn1.place(x=142, y=30)
        tk.Label(self.pg1, text='', bg='black').pack(pady=30)
        tk.Label(self.pg1, text='', bg='black').pack(pady=30)

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
                                                  textvariable=self.otp_, relief=FLAT, font=('Bold', 15), show='*',
                                                  fg='white',
                                                  bg='black', insertbackground='white')
                        self.otp_lb_entry.config(font=tkFont.Font(family='Lato', size=12))
                        self.otp_lb_entry.place(x=640, y=265, anchor=tk.CENTER)
                        self.otp_lb_line = Canvas(self.pg2, width=300, height=2.0, bg='white', highlightthickness=0)
                        self.otp_lb_line.place(x=640, y=280, anchor=tk.CENTER)

                        # back button
                        self.back2 = ImageTk.PhotoImage(
                            Image.open('backicon.png').resize((40, 40), resample=Image.LANCZOS))
                        self.backbtn2 = Button(self.pg2, image=self.back2, bg='black', relief='flat',
                                               command=lambda: showpage1(self))
                        self.backbtn2.place(x=140, y=40)

                        # finish button
                        self.nextbtn = customtkinter.CTkButton(master=self.pg2,
                                                               text="Finish",
                                                               width=140, height=40,
                                                               fg_color="#464E63",
                                                               hover_color="#667190",
                                                               command=lambda: finish_session(self))
                        self.nextbtn.pack(side=tk.RIGHT, padx=140, pady=320)

        def showpage1(self):
            self.pg2.destroy()
            controller.show_frame(RegisterPage)

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

                # insert data to database
                cursor.execute(
                    "INSERT INTO user (name,username,email,password) VALUES (:name, :username, :email, :password)",
                    {'name': self.name, 'username': self.uname, 'email': self.email_, 'password': self.pwd})
                connect.commit()
                messagebox.showinfo('Confirmation', 'Record Saved! Session is finished!')
                self.pg2.destroy()
                controller.show_frame(LoginPage)
            else:
                messagebox.showerror('Error!', "incorrect OTP try again!")


class ForgotPassword(tk.Frame):
    def __init__(self, window, controller):
        Frame.__init__(self, window)
        self.controller = controller
        self.hide_button = None

        # forgot password frames/pages
        self.fgt_frame = Frame(self, bg='black')
        self.fgt_frame.pack(fill=BOTH)

        # page1
        tk.Label(self.fgt_frame, text='', bg='black').pack(anchor=CENTER, pady=30)
        self.pg1_title = tk.Label(self.fgt_frame, text='Reset Password', fg='white', bg='black')
        self.pg1_title.config(font=tkFont.Font(family='Lato', size=20, weight="bold"))
        self.pg1_title.pack(anchor=CENTER, padx=0, pady=5)
        Canvas(self.fgt_frame, width=1000, height=2.0, bg='white', highlightthickness=1).pack(anchor=CENTER, padx=150, pady=2)
        tk.Label(self.fgt_frame, text='', bg='black').pack(anchor=CENTER, pady=5)

        # email
        # User Email Label and Text Entry Box
        self.regemail_lb = tk.Label(self.fgt_frame, text='Email', fg='white', bg='black')
        self.regemail_lb.config(font=tkFont.Font(family='Lato', size=15, weight="bold"))
        self.regemail_lb.pack(pady=5)
        self.regemail = StringVar()
        self.regemail_entry = Entry(self.fgt_frame, justify='center', width=30, highlightthickness=0,
                                    textvariable=self.regemail, relief=FLAT, font=('Bold', 12), fg='white', bg='black',
                                    insertbackground='white')
        self.regemail_entry.config(font=tkFont.Font(family='Lato', size=12))
        self.regemail_entry.pack()
        self.regemail_line = Canvas(self.fgt_frame, width=300, height=2.0, bg='white', highlightthickness=0)
        self.regemail_line.pack()
        tk.Label(self.fgt_frame, text='', bg='black').pack(pady=3)

        # new password
        self.newpassword_lb = tk.Label(self.fgt_frame, text='Password', font=('Bold', 15), fg='white', bg='black')
        self.newpassword_lb.config(font=tkFont.Font(family='Lato', size=15, weight="bold"))
        self.newpassword_lb.pack(pady=5)
        self.newpassword = StringVar()
        self.newpassword_lb_entry = Entry(self.fgt_frame, justify='center', width=30, highlightthickness=0,
                                          textvariable=self.newpassword, relief=FLAT, font=('Bold', 12), show='*',
                                          fg='white', bg='black', insertbackground='white')
        self.newpassword_lb_entry.config(font=tkFont.Font(family='Lato', size=12))
        self.newpassword_lb_entry.pack()
        self.newpassword_lb_line = Canvas(self.fgt_frame, width=300, height=2.0, bg='white', highlightthickness=0)
        self.newpassword_lb_line.pack()
        tk.Label(self.fgt_frame, text='', bg='black').pack(pady=3)

        # confirm password
        self.conpassword_lb = tk.Label(self.fgt_frame, text='Confirm Password', fg='white', bg='black')
        self.conpassword_lb.config(font=tkFont.Font(family='Lato', size=15, weight="bold"))
        self.conpassword_lb.pack(pady=5)
        self.conpassword = StringVar()
        self.conpassword_lb_entry = Entry(self.fgt_frame, justify='center', width=30, highlightthickness=0,
                                          textvariable=self.conpassword, relief=FLAT, font=('Bold', 12), show='*',
                                          fg='white', bg='black', insertbackground='white')
        self.conpassword_lb_entry.config(font=tkFont.Font(family='Lato', size=12))
        self.conpassword_lb_entry.pack()
        self.conpassword_lb_line = Canvas(self.fgt_frame, width=300, height=2.0, bg='white', highlightthickness=0)
        self.conpassword_lb_line.pack()
        self.btn_value = IntVar(value=0)
        self.check_btn = Checkbutton(self.fgt_frame, text="Show password", variable=self.btn_value,
                                     command=self.show_password, fg='white', bg='black')
        self.check_btn.pack(pady=5)

        # buttons
        # next button
        self.sendotpbtn = customtkinter.CTkButton(master=self.fgt_frame, text="Send/Resend OTP", width=140, height=40,
                                                  fg_color="#464E63", hover_color="#667190",
                                                  command=lambda: self.data_validation())
        self.sendotpbtn.pack(side=tk.RIGHT, anchor=W, padx=170)

        # back button
        self.back = ImageTk.PhotoImage(Image.open('backicon.png').resize((40, 40), resample=Image.LANCZOS))
        self.backbtn1 = Button(self.fgt_frame, image=self.back, bg='black', relief='flat',
                               command=lambda: controller.show_frame(LoginPage))
        self.backbtn1.place(x=150, y=80)
        tk.Label(self.fgt_frame, text='', bg='black').pack(anchor=CENTER, pady=100)

    def show_password(self):
        if self.btn_value.get() == 1:
            self.newpassword_lb_entry.config(show='')
            self.conpassword_lb_entry.config(show='')

        else:
            self.newpassword_lb_entry.config(show='*')
            self.conpassword_lb_entry.config(show='*')

    def data_validation(self):
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
        self.subject = "Reset password verification code"

        self.text = "Hi user,\n\nYour OTP for the reseting password is:\n\n" + self.OTP + "\n\nThank you.\n\n\n" \
                                                                                          "Iccountant"
        self.msg = 'Subject: {}\n\n{}'.format(self.subject, self.text)

        # inputs
        self.r_email = self.regemail.get()
        self.npwd = self.newpassword.get()
        self.cpwd = self.conpassword.get()

        # applying validation
        if not self.r_email or not self.npwd or not self.cpwd:
            messagebox.showerror('Error!', "Please fill the form!")
        elif len(self.newpassword.get()) < 8:
            messagebox.showerror('Error!', "Please enter a password that is at least 8 characters!")
        elif self.newpassword.get() != self.conpassword.get():
            messagebox.showerror('Error!', "Please match both password and confirm password!")
        else:
            cursor.execute('SELECT email from user where email="%s"' % self.r_email)
            self.Email = cursor.fetchone() # fetch data
            self.email = self.Email[0]
            if self.r_email != self.email:
                messagebox.showerror('Error!', "Please enter the email that is registered in the system!")
            else:
                messagebox.showinfo('Success!', "All of the form is filled!")
                self.s.sendmail("all2ctt@gmail.com", self.r_email, self.msg)

                # =============== page 2 ================
                self.fgt_frame2 = Toplevel()
                self.fgt_frame2.geometry("1280x720")
                self.fgt_frame2.resizable(None, None)
                self.fgt_frame2.title("Iccountant")
                self.fgt_frame2.configure(bg='black')

                self.fgt_frame2_title = tk.Label(self.fgt_frame2, text='Email Verification', fg='white', bg='black')
                self.fgt_frame2_title.config(font=tkFont.Font(family='Lato', size=20, weight="bold"))
                self.fgt_frame2_title.place(x=250, y=45)
                Canvas(self.fgt_frame2, width=1000, height=2.0, bg='white', highlightthickness=1).place(x=640, y=100,
                                                                                                        anchor=tk.CENTER)
                # otp
                self.otp_lb = tk.Label(self.fgt_frame2, text='4-digit OTP', fg='white', bg='black')
                self.otp_lb.config(font=tkFont.Font(family='Lato', size=15, weight="bold"))
                self.otp_lb.place(x=640, y=230, anchor=tk.CENTER)
                self.otp_ = StringVar()
                self.otp_lb_entry = Entry(self.fgt_frame2, justify='center', width=30, highlightthickness=0,
                                          textvariable=self.otp_, relief=FLAT, font=('Bold', 15), show='*', fg='white',
                                          bg='black', insertbackground='white')
                self.otp_lb_entry.config(font=tkFont.Font(family='Lato', size=12))
                self.otp_lb_entry.place(x=640, y=265, anchor=tk.CENTER)
                self.otp_lb_line = Canvas(self.fgt_frame2, width=300, height=2.0, bg='white', highlightthickness=0)
                self.otp_lb_line.place(x=640, y=280, anchor=tk.CENTER)

                # back button
                self.back2 = ImageTk.PhotoImage(Image.open('backicon.png').resize((40, 40), resample=Image.LANCZOS))
                self.backbtn2 = Button(self.fgt_frame2, image=self.back2, bg='black', relief='flat', command=lambda:
                self.fgt_frame2.destroy())
                self.backbtn2.place(x=145, y=40)

                # finish session button
                self.finishbtn = customtkinter.CTkButton(master=self.fgt_frame2, text="Finish", width=140, height=40,
                                                         fg_color="#464E63", hover_color="#667190",
                                                         command=lambda: self.otp_validation())
                self.finishbtn.pack(side=tk.RIGHT, padx=140)


    def otp_validation(self):
        if self.otp_.get() == self.OTP:
            messagebox.showinfo('Success!', "OTP verified!")

            # message to be sent: successfully registered
            self.subject2 = "Icccountant account has successfully updated the password!"
            self.text2 = "Hi user,\n\nYour account for Icccountant desktop app has successfully reset the account " \
                         "password.\nThank you.\n\n\nIccountant"
            self.msg2 = 'Subject: {}\n\n{}'.format(self.subject2, self.text2)
            self.s.sendmail("all2ctt@gmail.com", self.regemail.get(), self.msg2)

            # terminating the session
            self.s.quit()

            # update data
            # inputs
            self.r_email = self.regemail.get()
            self.npwd = self.newpassword.get()
            cursor.execute("UPDATE user SET password = ? WHERE email = ?", (self.npwd, self.r_email))
            connect.commit()
            messagebox.showinfo('Confirmation', 'Record Updated! Session is finished!')
            self.fgt_frame2.destroy()
            self.controller.show_frame(LoginPage)
        else:
            messagebox.showerror('Error!', "incorrect OTP try again!")


class Dashboard(tk.Frame):
    def __init__(self, master, controller):
        self.controller = controller
        self.hide_button = None
        Frame.__init__(self, master)

        self.menuFrame = Frame(self, bg='#000000', width=180, height=master.winfo_height(),
                               highlightbackground='#1A1A1A')  # 000000
        self.menuFrame.pack(side=LEFT, fill=BOTH)

        self.db = Frame(self, bg='#1A1A1A', width=1280, height=720)
        self.db.place(x=180, y=0)

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

    def con(self):
        os.system('CurrencyConverter.py')

    def cal(self):
        os.system('calculator.py')

    def logout_system(self):
        answer = messagebox.askyesno(title='Confirmation', message='Are you sure that you want to logout?')
        if answer:
            messagebox.showinfo('Log Out', 'You have successfully Logged Out!')
            self.controller.show_frame(LoginPage)


class Account(tk.Frame):
    def __init__(self, master, controller):
        self.controller = controller
        self.hide_button = None
        Frame.__init__(self, master)

        self.menuFrame = Frame(self, bg='#000000', width=180, height=master.winfo_height(),
                               highlightbackground='#1A1A1A')  # 000000
        self.menuFrame.pack(side=LEFT, fill=BOTH)

        self.rightFrame = Frame(self, bg='#1A1A1A', width=1280, height=720)
        self.rightFrame.place(x=180, y=0)

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
                                 command=lambda: self.controller.show_frame(Category))
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

        # ============= Heading Label =================
        self.heading_label = Label(self.rightFrame, text='ACCOUNT BALANCES', fg='white', bg='#1A1A1A')
        self.heading_label.config(font=tkFont.Font(family='Lato', size=20, weight="bold", slant="italic"))
        self.heading_label.place(x=15, y=15)

        # ====================================== Account table ===============================================
        # Frame for tree view
        self.treeFrame = Frame(self.rightFrame, bg='#1A1A1A', width=1050, height=25)
        self.treeFrame.place(x=15, y=100)
        self.Account = ttk.Treeview(self.treeFrame, selectmode="extended", show='headings',
                                    columns=('Account', 'Amount'), height=18)
        self.Account.place(relwidth=1, relheight=1)
        self.Account.heading('Account', text='Account', anchor=CENTER)
        self.Account.heading('Amount', text='Amount', anchor=CENTER)
        self.Account.column("Account", anchor=CENTER, width=525)
        self.Account.column("Amount", anchor=CENTER, width=525)
        self.Account.tag_configure('oddrow', background='#cccccc')
        self.Account.tag_configure('evenrow', background='#999999')
        self.treestyle = ttk.Style()
        self.treestyle.theme_use("default")
        self.treestyle.configure("Treeview", background="#666666", foreground="black", fieldbackground="#666666",
                                 rowheight=30)
        self.treestyle.configure('.', borderwidth=1)
        self.treestyle.map('Treeview', background=[('selected', '#9fc5f8')])
        self.treestyle.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        self.Account.pack()

        # call function to display Account
        self.updatetree()

        # ============= Buttons ===============
        self.add_button = customtkinter.CTkButton(self.rightFrame, text='Add', width=50, height=30, text_color='black',
                                                  fg_color="#b4a7d6", hover_color="#ffffff",
                                                  command=lambda: self.addAccountWindow(Toplevel))
        self.add_button.place(x=15, y=58)
        self.edit_button = customtkinter.CTkButton(self.rightFrame, text='Edit', width=50, height=30, text_color='black',
                                                   fg_color="#b4a7d6", hover_color="#ffffff",
                                                   command=lambda: self.editAccountWindow(Toplevel))

        self.edit_button.place(x=75, y=58)
        self.delete_button = customtkinter.CTkButton(self.rightFrame, text='Delete', width=50, height=30, text_color='black',
                                                     fg_color="#b4a7d6", hover_color="#ffffff",
                                                     command=lambda: self.deleteAccount())
        self.delete_button.place(x=135, y=58)

    # ================================================ Functions =======================================================
    # display accounts of users
    def displayAccount(self):
        cursor.execute("SELECT acc_name, acc_amount FROM account WHERE user_id = ? ",
                       (self.controller.shared_user_id['userID'].get(), ))
        rows = cursor.fetchall()
        # print(rows)
        # column1 = [tple[1] for tple in rows]
        # print(column1)
        # introw01 = str(column1)
        # print(introw01)
        # list = [[(rows[0], round(introw01, 2)) for rows in lin] for lin in rows]
        # print(list)
        global count
        count = 0
        # loop to display account
        for row in rows:
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
        self.addConfirm = customtkinter.CTkButton(self.addWindow, text='OK', width=50, height=30, fg_color="#464E63",
                                                  hover_color="#667190", command=lambda: self.addAcc())
        self.addConfirm.place(x=55, y=200)
        self.cancel = customtkinter.CTkButton(self.addWindow, text='Cancel', width=50, height=30, fg_color="#464E63",
                                              hover_color="#667190", command=lambda: self.addWindow.destroy())
        self.cancel.place(x=180, y=200)

    #  add account
    def addAcc(self):
        self.AccNameEntry.get()
        self.AmountEntry.get()

        # validation
        if not self.AccNameEntry.get() or not self.AmountEntry.get():
            messagebox.showerror('Error', "Please fill in all the fields!")
        else:
            try:
                # validate amount is float
                float(self.AmountEntry.get())
                try:
                    cursor.execute("INSERT INTO account ('acc_name', 'acc_amount', 'user_id') VALUES(?,?,?)",
                                   (self.AccNameEntry.get(), self.AmountEntry.get(),
                                    self.controller.shared_user_id['userID'].get()))
                    connect.commit()
                    messagebox.showinfo('Record added', f"{self.AccNameEntry.get()} was successfully added")
                    self.addWindow.destroy()
                    self.updatetree()
                except sqlite3.IntegrityError:
                    messagebox.showerror('Error', "Database failed to update")
            except ValueError:
                messagebox.showerror('Error', "Amount must be a number!")

    # ========== Edit Account ===========
    def editAccountWindow(self, Toplevel):
        if not self.Account.selection():  # if not select any row
            tk.messagebox.showerror("Error", "Please select an account to edit")
        else:
            # after selected a row
            selected = self.Account.focus()
            values = self.Account.item(selected)
            selection = values["values"]
            cursor.execute("SELECT a.acc_id FROM account a, user u WHERE a.user_id =  u.user_id AND a.acc_name = ? "
                           "AND a.acc_amount = ? AND a.user_id = ?", (selection[0], selection[1],
                                                                      self.controller.shared_user_id['userID'].get(),))
            self.AccID = cursor.fetchall()
            self.accID = self.AccID[0][0]
            # print(self.accID)
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
            self.EditAmountLabel = Label(self.editWindow, text='Amount', fg='white', bg='#1A1A1A',
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
            self.editConfirm = customtkinter.CTkButton(self.editWindow, text='OK', width=50, height=30,
                                                       fg_color="#464E63", hover_color="#667190", command=lambda:
                self.editAccount())
            self.editConfirm.place(x=55, y=200)
            self.Editcancel = customtkinter.CTkButton(self.editWindow, text='Cancel', width=50, height=30,
                                                      fg_color="#464E63", hover_color="#667190", command=lambda:
                self.editWindow.destroy())
            self.Editcancel.place(x=180, y=200)

            # display record in Entry box
            for record in self.AccID:
                self.EditAccNameEntry.insert(0, selection[0])
                self.EditAmountEntry.insert(0, selection[1])

    # update new value of account
    def editAccount(self):
        if not self.EditAccNameEntry.get() or not self.EditAmountEntry.get():
            messagebox.showerror('Error', "Please fill in all the fields!")
        else:
            try:
                # validate amount is float
                float(self.EditAmountEntry.get())
                cursor.execute("UPDATE account SET acc_name = ?, acc_amount = ? WHERE acc_id =?",
                            (self.EditAccNameEntry.get(), self.EditAmountEntry.get(), self.accID,))

                # edit values in database
                # commit changes
                connect.commit()
                messagebox.showinfo('Update', f"{self.acc_name} account was successfully edited")

                # display updated value
                self.updatetree()

                # close Edit window
                self.editWindow.destroy()
            except ValueError:
                messagebox.showerror('Error', "Amount must be a number!")

    # ========== Delete Account ==========
    def deleteAccount(self):
        # if not select any row
        if not self.Account.selection():
            tk.messagebox.showerror("Error", "Please select an account to delete")
        else:
            # To confirm the user really want to delete?
            result = tk.messagebox.askquestion('Confirm', 'Are you sure you want to delete this account?',
                                               icon="warning")
            if result == 'yes':
                acc = self.Account.focus()
                contents = (self.Account.item(acc))
                selected = contents['values']
                self.Account.delete(acc)

                # delete data from database
                cursor.execute("DELETE FROM account WHERE acc_name=?", (str(selected[0]),))
                connect.commit()
                tk.messagebox.showinfo('Deleted', 'The account is successfully delete')

                # clear all rows in tree table
                self.Account.delete(*self.Account.get_children())

                # redisplay the data
                self.displayAccount()

    def con(self):
        os.system('CurrencyConverter.py')

    def cal(self):
        os.system('python calculator.py')

    def logout_system(self):
        answer = messagebox.askyesno(title='Confirmation', message='Are you sure that you want to logout?')
        if answer:
            messagebox.showinfo('Log Out', 'You have successfully Logged Out!')
            self.controller.show_frame(LoginPage)


class Category(tk.Frame):
    def __init__(self, master, controller):
        self.controller = controller
        self.hide_button = None
        Frame.__init__(self, master)

        self.menuFrame = Frame(self, bg='#000000', width=180, height=master.winfo_height(),
                               highlightbackground='#1A1A1A')  # 000000
        self.menuFrame.pack(side=LEFT, fill=BOTH)

        self.rightFrame = Frame(self, bg='#1A1A1A', width=1280, height=720)
        self.rightFrame.place(x=180, y=0)

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

        # Defining the buttons for menu bar
        self.logo_l = Label(self.menuFrame, image=self.logo, bg='#000000')
        self.logo_l.grid(row=1)
        self.dashboard_b = Button(self.menuFrame, image=self.dashboard, bg='#000000', relief='flat',
                                  command=lambda: self.controller.show_frame(Dashboard))
        self.dashboard_b.grid(row=2)
        self.statistic_b = Button(self.menuFrame, image=self.statistic, bg='#000000', relief='flat')
        self.statistic_b.grid(row=3)
        self.transaction_b = Button(self.menuFrame, image=self.transaction, bg='#000000', relief='flat',
                                    command=lambda: self.controller.show_frame(Transaction))
        self.transaction_b.grid(row=4)
        self.category_b = Button(self.menuFrame, image=self.category, bg='#000000', relief='flat',
                                 command=lambda: self.controller.show_frame(Category))
        self.category_b.grid(row=5)
        self.account_b = Button(self.menuFrame, image=self.account, bg='#000000', relief='flat',
                                command=lambda: self.controller.show_frame(Account))
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

        # ===== Heading Label =====
        self.heading_label = Label(self.rightFrame, text='Category', fg='white', bg='#1A1A1A')
        self.heading_label.config(font=tkFont.Font(family='Lato', size=20, weight="bold", slant="italic"))
        self.heading_label.place(x=15, y=15)

        # ================== Category table ===============================================
        # Frame for tree view
        self.treeFrame = Frame(self.rightFrame, bg='#1A1A1A', width=550, height=550)
        self.treeFrame.place(x=260, y=100)
        self.CategoryTree = ttk.Treeview(self.treeFrame, selectmode="extended", show='headings', columns='Category',
                                         height=18)
        self.CategoryTree.place(relwidth=1, relheight=1)
        self.CategoryTree.heading('Category', text='Category', anchor=CENTER)
        self.CategoryTree.column("Category", anchor=CENTER, width=60)
        self.CategoryTree.tag_configure('oddrow', background='#cccccc')
        self.CategoryTree.tag_configure('evenrow', background='#999999')
        self.treestyle = ttk.Style()
        self.treestyle.theme_use("default")
        self.treestyle.configure("Treeview", background="#666666", foreground="black", fieldbackground="#666666",
                                 rowheight=30)
        self.treestyle.configure('.', borderwidth=1)
        self.treestyle.map('Treeview', background=[('selected', '#9fc5f8')])
        self.treestyle.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        # call function to display the newest Category
        self.updatetree()

        # Buttons
        self.add_button = customtkinter.CTkButton(self.rightFrame, text='Add', width=50, height=30, text_color='black',
                                                  fg_color="#b4a7d6", hover_color="#ffffff", command=lambda:
            self.addCategoryWindow(Toplevel))
        self.add_button.place(x=15, y=58)
        self.edit_button = customtkinter.CTkButton(self.rightFrame, text='Edit', width=50, height=30, text_color='black'
                                                   , fg_color="#b4a7d6", hover_color="#ffffff",
                                                   command=lambda: self.editCategoryWindow(Toplevel))
        self.edit_button.place(x=75, y=58)
        self.delete_button = customtkinter.CTkButton(self.rightFrame, text='Delete', width=50, height=30,
                                                     text_color='black', fg_color="#b4a7d6", hover_color="#ffffff",
                                                     command=lambda: self.deleteCategory())
        self.delete_button.place(x=135, y=58)

    # ========================================= Functions =================================================
    # display category
    def displayCategory1(self):
        cursor.execute("SELECT cat_name FROM category WHERE user_id = ?",
                       (self.controller.shared_user_id['userID'].get(),))
        rows = cursor.fetchall()
        global count
        count = 0
        # loop to display all the invoice
        for row in rows:
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
        self.AddCategoryNameEntry.get()

        # validation
        if not self.AddCategoryNameEntry.get():
            messagebox.showerror('Error', "Please fill in all the fields!")
        else:
            try:
                cursor.execute("INSERT INTO category (cat_name, user_id) VALUES(?,?) ", 
                (self.AddCategoryNameEntry.get(), self.controller.shared_user_id['userID'].get()))
                connect.commit()
                messagebox.showinfo('Record added', f"{self.AddCategoryNameEntry.get()} was successfully added")
                self.updatetree()
                self.addWindow.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror('Error', "Database failed to update")
                self.addWindow.destroy()

    # close add window
    def closeAdd(self):
        self.addWindow.destroy()

    # ========== Edit Account ===========
    def editCategoryWindow(self, Toplevel):
        # if not select any row
        if not self.CategoryTree.selection():
            tk.messagebox.showerror("Error", "Please select a category to edit")
        else:
            # after selected a row
            selected = self.CategoryTree.focus()
            values = self.CategoryTree.item(selected)
            selection = values["values"]
            cursor.execute("SELECT c.cat_id FROM category c, user u WHERE c.user_id = u.user_id AND c.cat_name = ? "
                           "AND c.user_id = ?", (selection[0], self.controller.shared_user_id['userID'].get(),))
            self.CatID = cursor.fetchall()
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
            self.editConfirm = customtkinter.CTkButton(self.editWindow, text='OK', width=50, height=30,
                                                       fg_color="#464E63", hover_color="#667190", command=lambda:
                self.editCat())
            self.editConfirm.pack(pady=10)
            self.Editcancel = customtkinter.CTkButton(self.editWindow, text='Cancel', width=50, height=30,
                                                      fg_color="#464E63", hover_color="#667190", command=lambda:
                self.editWindow.destroy())
            self.Editcancel.pack(pady=10)

            # display record in Entry box
            self.EditCategoryNameEntry.insert(0, selection[0])

    # update new value of category
    def editCat(self):
        if not self.EditCategoryNameEntry.get():
            messagebox.showerror('Error', "Please fill in all the fields!")
        else:
            cursor.execute("UPDATE category SET cat_name = ? WHERE cat_id =?", (self.EditCategoryNameEntry.get(),
                                                                                self.catID,))

            # edit values in database
            # commit changes
            connect.commit()
            messagebox.showinfo('Update', f"{self.EditCategoryNameEntry.get()} was successfully edited.")
            # display updated value
            self.updatetree()
            # close Edit window
            self.editWindow.destroy()

    # ========== Delete Category ==========
    def deleteCategory(self):
        # if not select any row
        if not self.CategoryTree.selection():
            tk.messagebox.showerror("Error", "Please select a category to delete")
        else:
            # To confirm the user really want to delete?
            result = tk.messagebox.askquestion('Confirm', 'Are you sure you want to delete this category?',
                                               icon="warning")
            if result == 'yes':
                cat = self.CategoryTree.focus()
                contents = (self.CategoryTree.item(cat))
                selected = contents['values']
                self.CategoryTree.delete(cat)

                # delete data from database
                cursor.execute("DELETE FROM category WHERE cat_name=?", (str(selected[0]),))
                connect.commit()
                tk.messagebox.showinfo('Deleted', 'The category is successfully delete.')

                # clear all rows in tree table
                self.CategoryTree.delete(*self.CategoryTree.get_children())

                # redisplay the data
                self.displayCategory1()

    def con(self):
        os.system('CurrencyConverter.py')

    def cal(self):
        os.system('python calculator.py')

    def logout_system(self):
        answer = messagebox.askyesno(title='Confirmation', message='Are you sure that you want to logout?')
        if answer:
            messagebox.showinfo('Log Out', 'You have successfully Logged Out!')
            self.controller.show_frame(LoginPage)


class Transaction(tk.Frame):
    def __init__(self, master, controller):
        self.controller = controller
        self.hide_button = None
        Frame.__init__(self, master)

        self.menuFrame = Frame(self, bg='#000000', width=180, height=master.winfo_height(),
                               highlightbackground='#1A1A1A')  # 000000
        self.menuFrame.pack(side=LEFT, fill=BOTH)

        self.side_frame = Frame(self, bg='#1A1A1A', width=1280, height=720)
        self.side_frame.place(x=180, y=0)

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
                                  command=lambda: self.controller.show_frame(Dashboard))
        self.dashboard_b.grid(row=2)
        self.statistic_b = Button(self.menuFrame, image=self.statistic, bg='#000000', relief='flat')
        self.statistic_b.grid(row=3)
        self.transaction_b = Button(self.menuFrame, image=self.transaction, bg='#000000', relief='flat',
                                    command=lambda: self.controller.show_frame(Transaction))
        self.transaction_b.grid(row=4)
        self.category_b = Button(self.menuFrame, image=self.category, bg='#000000', relief='flat',
                                 command=lambda: self.controller.show_frame(Category))
        self.category_b.grid(row=5)
        self.account_b = Button(self.menuFrame, image=self.account, bg='#000000', relief='flat',
                                command=lambda: self.controller.show_frame(Account))
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

        transaction_l = Label(self.side_frame, font=('lato', 24), bg='#1A1A1A', text='Transaction', fg='white')
        transaction_l.place(x=20, y=20)

        # Define and resize the icons to be shown in Transaction
        self.transaction_add = ImageTk.PhotoImage(Image.open('trans_add.png')
                                                  .resize((45, 30), resample=Image.LANCZOS))
        self.transaction_edit = ImageTk.PhotoImage(Image.open('trans_edit.png')
                                                   .resize((50, 30), resample=Image.LANCZOS))
        self.transaction_delete = ImageTk.PhotoImage(Image.open('trans_delete.png')
                                                     .resize((55, 30), resample=Image.LANCZOS))
        self.transaction_filter = ImageTk.PhotoImage(Image.open('trans_filter.png')
                                                     .resize((85, 30), resample=Image.LANCZOS))
        # Buttons
        self.add_b = tk.Button(self.side_frame, image=self.transaction_add, bg='#1A1A1A', relief='flat', command=self.add)
        self.add_b.place(x=20, y=60)

        self.edit_b = tk.Button(self.side_frame, image=self.transaction_edit, bg='#1A1A1A', relief='flat', command=self.edit)
        self.edit_b.place(x=70, y=60)

        self.delete_b = tk.Button(self.side_frame, image=self.transaction_delete, bg='#1A1A1A', relief='flat',
                                  command=self.delete)
        self.delete_b.place(x=125, y=60)

        self.filter_b = tk.Button(self.side_frame, image=self.transaction_filter, bg='#1A1A1A', relief='flat',
                                  command=self.filter)
        self.filter_b.place(x=980, y=60)

        # total income label
        self.total_in_l = Label(self.side_frame, font=('lato', 12), bg='#1A1A1A', text='Total Income: ', fg='lightgreen')
        self.total_in_l.place(x=500, y=65)

        self.total_in_a = Label(self.side_frame, font=('lato', 12), bg='#1A1A1A', fg='lightgreen')
        self.total_in_a.place(x=600, y=65)

        self.total_ex = Label(self.side_frame, font=('lato', 12), bg='#1A1A1A', text='Total Expense: ', fg='red')
        self.total_ex.place(x=725, y=65)

        self.total_ex_a = Label(self.side_frame, font=('lato', 12), bg='#1A1A1A', fg='red')
        self.total_ex_a.place(x=835, y=65)

        # get total income from database
        cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id = u.user_id AND "
                       "t.type_id = ty.type_id AND t.type_id = 1 AND u.user_id = ? ",
                       (self.controller.shared_user_id['userID'].get(),))
        self.total_in_Amount = cursor.fetchall()
        if self.total_in_Amount == None:
            self.total_in_amount.set(0)
        else:
            self.total_in_amount = round(float(self.total_in_Amount[0][0]), 2)
            self.total_in_a.config(text=str(self.total_in_amount))

        # get total expense from database
        cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id = u.user_id AND "
                       "t.type_id = ty.type_id AND t.type_id = 2 AND u.user_id = ? ",
                       (self.controller.shared_user_id['userID'].get(),))
        self.total_ex_Amount = cursor.fetchall()
        if self.total_ex_Amount == None:
            self.total_ex_amount.set(0)
        else:
            self.total_ex_amount = round(float(self.total_ex_Amount[0][0]), 2)
            self.total_ex_a.config(text=str(self.total_ex_amount))

        # Transaction List (tree table)
        self.transaction_frame = Frame(self.side_frame, bg='#1A1A1A', height=25, width=1050)
        self.transaction_frame.grid(padx=20, pady=100, sticky='nw')
        self.transaction_frame.grid_rowconfigure(0, weight=1)
        self.transaction_frame.grid_columnconfigure(0, weight=1)

        self.transaction_list = ttk.Treeview(self.transaction_frame, selectmode="extended", show='headings', height=18,
                                             columns=('Date', 'Account', 'Category', 'Type', 'Amount', 'Remark'))
        self.transaction_list.grid(row=0, column=0, sticky='nsew', in_=self.transaction_frame)
        self.list_scroll = ttk.Scrollbar(self.transaction_frame, orient="vertical", command=self.transaction_list.yview)
        self.list_scroll.grid(row=0, column=1, sticky="ns", in_=self.transaction_frame)
        self.transaction_list.config(yscrollcommand=self.list_scroll.set)
        self.list_scroll.config(command=self.transaction_list.yview)

        self.transaction_list.heading('Date', text='Date', anchor=CENTER)
        self.transaction_list.heading('Account', text='Account', anchor=CENTER)
        self.transaction_list.heading('Category', text='Category', anchor=CENTER)
        self.transaction_list.heading('Type', text='Type', anchor=CENTER)
        self.transaction_list.heading('Amount', text='Amount', anchor=CENTER)
        self.transaction_list.heading('Remark', text='Remark', anchor=CENTER)

        self.transaction_list.column("Date", anchor=CENTER, width=100)
        self.transaction_list.column("Account", anchor=CENTER, width=200)
        self.transaction_list.column("Category", anchor=CENTER, width=200)
        self.transaction_list.column("Type", anchor=CENTER, width=100)
        self.transaction_list.column("Amount", anchor=CENTER, width=200)
        self.transaction_list.column("Remark", anchor=CENTER, width=250)

        #style for treeview
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Treeview", background="#666666", foreground="black", fieldbackground="#666666",
                             rowheight=30)
        self.style.configure('.', borderwidth=1)
        self.style.map('Treeview', background=[('selected', '#9fc5f8')])
        self.style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        self.transaction_list.tag_configure('oddrow', background='#cccccc')
        self.transaction_list.tag_configure('evenrow', background='#999999')

        # call function to display transaction list
        self.updateTree()

    def con(self):
        os.system('CurrencyConverter.py')

    def cal(self):
        os.system('calculator.py')

    def logout_system(self):
        answer = messagebox.askyesno(title='Confirmation', message='Are you sure that you want to logout?')
        if answer:
            messagebox.showinfo('Log Out', 'You have successfully Logged Out!')
            self.controller.show_frame(LoginPage)

    def display_all(self):
        cursor.execute("SELECT t.date, a.acc_name, c.cat_name, ty.type_name, t.amount, t.remark FROM transactions t, "
                       "account a, category c, type ty, user u WHERE t.acc_id = a.acc_id AND t.cat_id = c.cat_id AND "
                       "t.type_id = ty.type_id AND u.user_id = t.user_id AND t.user_id = ?",
                       (self.controller.shared_user_id['userID'].get(),))
        rows = cursor.fetchall()

        # loop to display all the transaction in treeview
        global count
        count = 0
        for row in rows:
            if count % 2 == 0:
                self.transaction_list.insert("", END, values=row, tags='evenrow')
            else:
                self.transaction_list.insert("", END, values=row, tags='oddrow')
            count += 1

    def updateTree(self):
        self.transaction_list.delete(*self.transaction_list.get_children())
        self.display_all()

    def insert_transaction(self):
        # validate input
        if self.account_cbox.get() == 'Select Account':
            messagebox.showerror('Error', 'Please select an account.')
            self.root.destroy()
        else:
            if self.category_cbox.get() == 'Select Category':
                messagebox.showerror('Error', 'Please select a category.')
                self.root.destroy()
            else:
                if self.type_cbox.get() == 'Select Type':
                    messagebox.showerror('Error', 'Please select a type.')
                    self.root.destroy()
                else:
                    if self.amount_entry.get() == '':
                        messagebox.showerror('Error', 'Please enter an amount.')
                        self.root.destroy()
                    else:
                        try:
                            self.amount = round(float(self.amount_entry.get()), 2)

                            # get the latest id from database
                            cursor.execute("SELECT max(trans_id) FROM transactions")
                            self.id = cursor.fetchall()

                            # create new id
                            self.ID = int(self.id[0][0]) + 1

                            # get current date
                            today = datetime.now()

                            # get type id that user input from database
                            cursor.execute("SELECT type_id FROM type WHERE type_name = ?", (self.type_cbox.get(),))
                            self.typeID = cursor.fetchall()
                            self.typeid = self.typeID[0][0]

                            # get account id that user input from database
                            cursor.execute("SELECT a.acc_id FROM account a, user u WHERE a.user_id = u.user_id AND "
                                           "a.user_id = ? AND a.acc_name = ?",
                                           (self.controller.shared_user_id['userID'].get(), self.account_cbox.get(),))
                            self.accountID = cursor.fetchall()
                            self.accountid = self.accountID[0][0]

                            # get category id that user input from database
                            cursor.execute("SELECT c.cat_id FROM category c, user u WHERE c.user_id = u.user_id AND"
                                           " c.user_id = ? AND c.cat_name = ?",
                                           (self.controller.shared_user_id['userID'].get(), self.category_cbox.get(),))
                            self.categoryID = cursor.fetchall()
                            self.categoryid = self.categoryID[0][0]

                            # insert the data that user input to database
                            cursor.execute("INSERT INTO transactions (trans_id, amount, date, remark, user_id, type_id,"
                                           " acc_id, cat_id) VALUES (?,?,?,?,?,?,?,?)",
                                           (self.ID, self.amount, today.strftime("%Y-%m-%d"),
                                            self.remark_entry.get(), self.controller.shared_user_id['userID'].get(),
                                            self.typeid, self.accountid, self.categoryid))
                            connect.commit()
                            messagebox.showinfo('Information', 'Record successfully added.')

                            # validate income or expense
                            # update the income amount to the selected account in the database
                            if self.typeid == 1:
                                cursor.execute("UPDATE account SET acc_amount = (acc_amount+?) WHERE acc_id = ?",
                                               (self.amount, self.accountid,))
                                connect.commit()

                            # update the expense amount to the selected account in the database
                            else:
                                cursor.execute("UPDATE account SET acc_amount = (acc_amount-?) WHERE acc_id = ?",
                                               (self.amount, self.accountid,))
                                connect.commit()
                            self.root.destroy()

                            # empty the treeview
                            self.transaction_list.delete(*self.transaction_list.get_children())
                            self.display_all()

                            # get total income from database
                            cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id ="
                                           " u.user_id AND t.type_id = ty.type_id AND t.type_id = 1 AND u.user_id = ? ",
                                           (self.controller.shared_user_id['userID'].get(),))
                            self.total_in_Amount = cursor.fetchall()
                            if self.total_in_Amount == None:
                                self.total_in_amount.set(0)
                            else:
                                self.total_in_amount = round(float(self.total_in_Amount[0][0]), 2)
                                self.total_in_a.config(text=str(self.total_in_amount))

                            # get total expense from database
                            cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id ="
                                           " u.user_id AND t.type_id = ty.type_id AND t.type_id = 2 AND u.user_id = ? ",
                                           (self.controller.shared_user_id['userID'].get(),))
                            self.total_ex_Amount = cursor.fetchall()
                            if self.total_ex_Amount == None:
                                self.total_ex_amount.set(0)
                            else:
                                self.total_ex_amount = round(float(self.total_ex_Amount[0][0]), 2)
                                self.total_ex_a.config(text=str(self.total_ex_amount))
                            self.root.destroy()
                        except ValueError:
                            messagebox.showerror('Error', 'Please reenter the amount in number.')


    def add(self):
        self.root = Toplevel()
        self.root.geometry("425x215")
        self.root.title("Iccountant - Add New Transaction")
        self.root.configure(bg='#1A1A1A')

        self.title_l = Label(self.root, font=('lato', 15), bg='#1A1A1A', text='New Transaction', fg='white')
        self.title_l.grid(row=0, column=0)

        self.account_l = Label(self.root, font=('lato', 12), bg='#1A1A1A', text='Account :', fg='white')
        self.account_l.grid(row=1, column=0)

        self.account_get = pd.read_sql_query("SELECT a.acc_name AS Account FROM account a, user u WHERE a.user_id = "
                                             "u.user_id AND a.user_id IN ('{}') GROUP BY a.acc_id".format
                                             (self.controller.shared_user_id['userID'].get()), connect)
        self.account_df = pd.DataFrame(self.account_get)
        self.account_list = self.account_df['Account'].values.tolist()
        self.account_cbox = ttk.Combobox(self.root, values=self.account_list, font=('lato', 12), state='readonly',
                                         justify='center')
        self.account_cbox.grid(row=1, column=1)
        self.account_cbox.set("Select Account")
        self.category_l = Label(self.root, font=('lato', 12), bg='#1A1A1A', text='Category :', fg='white')
        self.category_l.grid(row=2, column=0)
        self.category_get = pd.read_sql_query("SELECT c.cat_name AS Category FROM category c, user u "
                                              "WHERE c.user_id = u.user_id AND c.user_id IN ('{}') GROUP BY c.cat_id"
                                              .format(self.controller.shared_user_id['userID'].get()), connect)
        self.category_df = pd.DataFrame(self.category_get)
        self.category_list = self.category_df['Category'].values.tolist()
        self.category_cbox = ttk.Combobox(self.root, values=self.category_list, font=('lato', 12), state='readonly',
                                          justify='center')
        self.category_cbox.grid(row=2, column=1)
        self.category_cbox.set("Select Category")
        self.type_l = Label(self.root, font=('lato', 12), bg='#1A1A1A', text='Type :', fg='white')
        self.type_l.grid(row=3, column=0)
        self.type_get = pd.read_sql_query("SELECT type_name AS Type FROM type", connect)
        self.type_df = pd.DataFrame(self.type_get)
        self.type_list = self.type_df['Type'].values.tolist()
        self.type_cbox = ttk.Combobox(self.root, values=self.type_list, font=('lato', 12), state='readonly',
                                      justify='center')
        self.type_cbox.grid(row=3, column=1)
        self.type_cbox.set("Select Type")
        self.amount_l = Label(self.root, font=('lato', 12), bg='#1A1A1A', text='Amount :', fg='white')
        self.amount_l.grid(row=4, column=0)
        self.amount_entry = Entry(self.root, font=('lato', 12), justify='center')
        self.amount_entry.grid(row=4, column=1)
        self.remark_l = Label(self.root, font=('lato', 12), bg='#1A1A1A', text='Remark :', fg='white')
        self.remark_l.grid(row=5, column=0)
        self.remark_entry = Entry(self.root, font=('lato', 12), justify='center')
        self.remark_entry.grid(row=5, column=1)
        self.confirm_pic = ImageTk.PhotoImage(Image.open('confirm button.png')
                                              .resize((75, 35), resample=Image.LANCZOS))
        self.cancel_pic = ImageTk.PhotoImage(Image.open('cancel button.png')
                                             .resize((75, 35), resample=Image.LANCZOS))
        self.confirm_b = tk.Button(self.root, image=self.confirm_pic, bg='#1A1A1A', relief='flat',
                                   command=self.insert_transaction)
        self.confirm_b.grid(row=6, columnspan=3)
        self.cancel_b = tk.Button(self.root, image=self.cancel_pic, bg='#1A1A1A', relief='flat',
                                  command=self.root.destroy)
        self.cancel_b.grid(row=6, column=1)

    def update_transaction(self):
        if self.amount_entry.get() == '':
            messagebox.showerror('Error', 'Please enter an amount.')
        else:
            try:
                # verify input is number or not
                self.amount = round(float(self.amount_entry.get()), 2)

                # get the original account id from the database
                cursor.execute("SELECT acc_id FROM account WHERE acc_name = ?", (self.oriaccount,))
                self.oriAccount = cursor.fetchall()
                self.oriacc = self.oriAccount[0][0]

                # get the original type id from the database
                cursor.execute("SELECT type_id FROM type WHERE type_name = ?", (self.oritypeID,))
                self.oritypeId = cursor.fetchall()
                self.oritypeid = self.oritypeId[0][0]

                # get the type id that user input from the database
                cursor.execute("SELECT type_id FROM type WHERE type_name = ?", (self.type_cbox.get(),))
                self.typeID = cursor.fetchall()
                self.typeid = self.typeID[0][0]

                # get the account id that user input from the database
                cursor.execute("SELECT a.acc_id FROM account a, user u WHERE a.user_id = u.user_id AND "
                               "a.user_id = ? AND a.acc_name = ?", (self.controller.shared_user_id['userID'].get(),
                                                                    self.account_cbox.get(),))
                self.accountID = cursor.fetchall()
                self.accountid = self.accountID[0][0]

                # get the category id that user input from the database
                cursor.execute("SELECT c.cat_id FROM category c, user u WHERE c.user_id = u.user_id AND"
                               " c.user_id = ? AND c.cat_name = ?", (self.controller.shared_user_id['userID'].get(),
                                                                     self.category_cbox.get(),))
                self.categoryID = cursor.fetchall()
                self.categoryid = self.categoryID[0][0]

                # update transaction table in database
                cursor.execute("UPDATE transactions SET amount= ?, date = ?, remark = ?, user_id = ?, type_id = ?, "
                               "acc_id = ?, cat_id = ? WHERE trans_id = ?",
                               (self.amount_entry.get(), self.date_entry.get(), self.remark_entry.get(),
                                self.controller.shared_user_id['userID'].get(), self.typeid, self.accountid,
                                self.categoryid, self.transid,))
                connect.commit()
                messagebox.showinfo('Information', 'Record successfully updated.')

                # validate the condition to update the amount of the acoount in database
                # if the user did not change the account
                if self.oriacc == self.accountid:

                    # if the original type is income
                    if self.oritypeid == 1:

                        # if the user did not change the type
                        if self.typeid == 1:
                            cursor.execute("UPDATE account SET acc_amount = (acc_amount-?+?) WHERE acc_id = ?",
                                           (self.oriamount, self.amount_entry.get(), self.accountid,))

                        # if the user change the type to expense
                        else:
                            cursor.execute("UPDATE account SET acc_amount = (acc_amount-?-?) WHERE acc_id = ?",
                                           (self.oriamount, self.amount_entry.get(), self.accountid,))

                    # if the original type is expense
                    else:

                        # if the user change the type to income
                        if self.typeid == 1:
                            cursor.execute("UPDATE account SET acc_amount = (acc_amount+?+?) WHERE acc_id = ?",
                                           (self.oriamount, self.amount_entry.get(), self.accountid,))

                        # if the user did not change the type
                        else:
                            cursor.execute("UPDATE account SET acc_amount = (acc_amount+?-?) WHERE acc_id = ?",
                                           (self.oriamount, self.amount_entry.get(), self.accountid,))

                # if the user change the account
                else:

                    # if the original type is income
                    if self.oritypeid == 1:
                        cursor.execute("UPDATE account SET acc_amount = (acc_amount-?) WHERE acc_id = ?",
                                       (self.oriamount, self.oriacc,))

                        # if the user did not change the type
                        if self.typeid == 1:
                            cursor.execute("UPDATE account SET acc_amount = (acc_amount+?) WHERE acc_id = ?",
                                           (self.amount_entry.get(), self.accountid,))

                        # if the user change the type to expense
                        else:
                            cursor.execute("UPDATE account SET acc_amount = (acc_amount-?) WHERE acc_id = ?",
                                           (self.amount_entry.get(), self.accountid,))

                    # if the original type is expense
                    else:
                        cursor.execute("UPDATE account SET acc_amount = (acc_amount+?) WHERE acc_id = ?",
                                       (self.oriamount, self.oriacc,))

                        # if the user change the type to income
                        if self.typeid == 1:
                            cursor.execute("UPDATE account SET acc_amount = (acc_amount+?) WHERE acc_id = ?",
                                           (self.amount_entry.get(), self.accountid,))

                        # if the user did not change the type
                        else:
                            cursor.execute("UPDATE account SET acc_amount = (acc_amount-?) WHERE acc_id = ?",
                                           (self.amount_entry.get(), self.accountid,))
                connect.commit()
                self.root.destroy()

                # empty treeview
                self.transaction_list.delete(*self.transaction_list.get_children())
                self.display_all()

                # get total income from database
                cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id = u.user_id "
                               "AND t.type_id = ty.type_id AND t.type_id = 1 AND u.user_id = ? ",
                               (self.controller.shared_user_id['userID'].get(),))
                self.total_in_Amount = cursor.fetchall()
                if self.total_in_Amount == None:
                    self.total_in_amount.set(0)
                else:
                    self.total_in_amount = round(float(self.total_in_Amount[0][0]), 2)
                    self.total_in_a.config(text=str(self.total_in_amount))

                # get total expense from database
                cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id = u.user_id "
                               "AND t.type_id = ty.type_id AND t.type_id = 2 AND u.user_id = ? ",
                               (self.controller.shared_user_id['userID'].get(),))
                if self.total_ex_Amount == None:
                    self.total_ex_amount.set(0)
                else:
                    self.total_ex_amount = round(float(self.total_ex_Amount[0][0]), 2)
                    self.total_ex_a.config(text=str(self.total_ex_amount))

            except ValueError:
                messagebox.showerror('Error', 'Please reenter the amount in number.')

    def edit(self):
        # if the user did not select a row in the treeview
        if not self.transaction_list.selection():
            messagebox.showerror("Error", "Please select a row to edit.")
        else:
            # get the value of the selected row
            selected = self.transaction_list.focus()
            values = self.transaction_list.item(selected)
            selection = values["values"]
            cursor.execute("SELECT t.trans_id FROM transactions t, type ty, account a, category c WHERE ty.type_id = "
                           "t.type_id AND a.acc_id = t.acc_id AND c.cat_id = t.cat_id AND t.amount= ? AND t.date = ? "
                           "AND t.remark = ? AND t.user_id = ? AND ty.type_name = ? AND a.acc_name = ? AND c.cat_name ="
                           " ?", (selection[4], selection[0], selection[5],
                                  self.controller.shared_user_id['userID'].get(), selection[3], selection[1],
                                  selection[2],))
            self.transID = cursor.fetchall()
            self.transid = self.transID[0][0]
            self.oriaccount = selection[1]
            self.oritypeID = selection[3]
            self.oriamount = selection[4]

            self.root = Toplevel()
            self.root.geometry("425x215")
            self.root.title("Iccountant - Edit Transaction")
            self.root.configure(bg='#1A1A1A')

            self.title_l = Label(self.root, font=('lato', 15), bg='#1A1A1A', text='Edit Transaction', fg='white')
            self.title_l.grid(row=0, column=0)
            self.account_l = Label(self.root, font=('lato', 12), bg='#1A1A1A', text='Account :', fg='white')
            self.account_l.grid(row=1, column=0)
            self.account_get = pd.read_sql_query("SELECT a.acc_name AS Account FROM transactions t, account a, user u "
                                                 "WHERE a.acc_id = t.acc_id AND u.user_id = t.user_id AND t.user_id IN "
                                                 "('{}') GROUP BY t.acc_id".format
                                                 (self.controller.shared_user_id['userID'].get()), connect)
            self.account_df = pd.DataFrame(self.account_get)
            self.account_list = self.account_df['Account'].values.tolist()
            self.account_cbox = ttk.Combobox(self.root, values=self.account_list, font=('lato', 12), state='readonly',
                                             justify='center')
            self.account_cbox.grid(row=1, column=1)
            self.account_cbox.set(selection[1])
            self.category_l = Label(self.root, font=('lato', 12), bg='#1A1A1A', text='Category :', fg='white')
            self.category_l.grid(row=2, column=0)
            self.category_get = pd.read_sql_query("SELECT c.cat_name AS Category FROM category c, transactions t, user "
                                                  "u WHERE c.cat_id = t.cat_id AND t.user_id = u.user_id AND u.user_id "
                                                  "IN ('{}') GROUP BY t.cat_id".format
                                                  (self.controller.shared_user_id['userID'].get()), connect)
            self.category_df = pd.DataFrame(self.category_get)
            self.category_list = self.category_df['Category'].values.tolist()
            self.category_cbox = ttk.Combobox(self.root, values=self.category_list, font=('lato', 12), state='readonly',
                                              justify='center')
            self.category_cbox.grid(row=2, column=1)
            self.category_cbox.set(selection[2])
            self.type_l = Label(self.root, font=('lato', 12), bg='#1A1A1A', text='Type :', fg='white')
            self.type_l.grid(row=3, column=0)
            self.type_get = pd.read_sql_query("SELECT type_name AS Type FROM type", connect)
            self.type_df = pd.DataFrame(self.type_get)
            self.type_list = self.type_df['Type'].values.tolist()
            self.type_cbox = ttk.Combobox(self.root, values=self.type_list, font=('lato', 12), state='readonly',
                                          justify='center')
            self.type_cbox.grid(row=3, column=1)
            self.type_cbox.set(selection[3])
            self.amount_l = Label(self.root, font=('lato', 12), bg='#1A1A1A', text='Amount :', fg='white')
            self.amount_l.grid(row=4, column=0)
            self.amount_entry = Entry(self.root, font=('lato', 12), justify='center')
            self.amount_entry.grid(row=4, column=1)
            self.amount_entry.insert(0, selection[4])
            self.remark_l = Label(self.root, font=('lato', 12), bg='#1A1A1A', text='Remark :', fg='white')
            self.remark_l.grid(row=5, column=0)
            self.remark_entry = Entry(self.root, font=('lato', 12), justify='center')
            self.remark_entry.grid(row=5, column=1)
            self.remark_entry.insert(0, selection[5])
            self.date_l = Label(self.root, font=('lato', 12), bg='#1A1A1A', text='Date :', fg='white')
            self.date_l.grid(row=6, column=0)
            self.date_entry = DateEntry(self.root, selectmode='day', font=('lato', 12), date_pattern='YYYY-mm-dd',
                                        state='readonly')
            self.date_entry.grid(row=6, column=1)
            self.date_entry.set_date(selection[0])
            self.update_pic = ImageTk.PhotoImage(Image.open('update button.png').resize((75, 35),
                                                                                        resample=Image.LANCZOS))
            self.cancel_pic = ImageTk.PhotoImage(Image.open('cancel button.png').resize((75, 35),
                                                                                        resample=Image.LANCZOS))
            self.update_b = tk.Button(self.root, image=self.update_pic, bg='#1A1A1A', relief='flat',
                                      command=self.update_transaction)
            self.update_b.grid(row=7, columnspan=3)
            self.cancel_b = tk.Button(self.root, image=self.cancel_pic, bg='#1A1A1A', relief='flat',
                                      command=self.root.destroy)
            self.cancel_b.grid(row=7, column=1)

    def delete(self):
        # if the user did not select a row in the treeview
        if not self.transaction_list.selection():
            tk.messagebox.showerror("Error", "Please select a row to delete.")
        else:
            result = tk.messagebox.askquestion('Delete Confirmation', 'Are you sure you want to delete this record?',
                                               icon="warning")
            if result == 'yes':

                # get the value of the selected row
                selected = self.transaction_list.focus()
                values = self.transaction_list.item(selected)
                selection = values["values"]
                self.transaction_list.delete(selected)

                # get account amount that selected
                self.account_amount = selection[4]

                # get the transaction id of the selected row from the database
                cursor.execute("SELECT t.trans_id FROM transactions t, type ty, account a, category c WHERE ty.type_id "
                               "= t.type_id AND a.acc_id = t.acc_id AND c.cat_id = t.cat_id AND t.amount= ? AND t.date "
                               "= ? AND t.remark = ? AND t.user_id = ? AND ty.type_name = ? AND a.acc_name = ? AND "
                               "c.cat_name = ?", (selection[4], selection[0], selection[5],
                                                  self.controller.shared_user_id['userID'].get(), selection[3],
                                                  selection[1], selection[2],))
                self.transID = cursor.fetchall()
                self.transid = self.transID[0][0]

                # get the account id of the selected row from the database
                cursor.execute("SELECT acc_id from transactions WHERE trans_id = ?", (self.transid,))
                self.accountID = cursor.fetchall()
                self.accountid = self.accountID[0][0]

                # get the type id of the selected row from the database
                cursor.execute("SELECT type_id from transactions WHERE trans_id = ?", (self.transid,))
                self.typeID = cursor.fetchall()
                self.typeid = self.typeID[0][0]

                # verify conditions to update account table in database
                # if the type of the selected row is income
                if self.typeid == 1:
                    cursor.execute("UPDATE account SET acc_amount = acc_amount-? WHERE acc_id = ?",
                                   (self.account_amount, self.accountid,))

                # if the type of the selected row is expense
                else:
                    cursor.execute("UPDATE account SET acc_amount = acc_amount+? WHERE acc_id = ?",
                                   (self.account_amount, self.accountid,))
                connect.commit()

                # remove record in database
                cursor.execute("DELETE FROM transactions WHERE trans_id = ? ", (self.transid,))
                connect.commit()

                # empty treeview
                self.transaction_list.delete(*self.transaction_list.get_children())
                self.display_all()

                # get total income from database
                cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id = u.user_id "
                               "AND t.type_id = ty.type_id AND t.type_id = 1 AND u.user_id = ? ",
                               (self.controller.shared_user_id['userID'].get(),))
                self.total_in_Amount = cursor.fetchall()
                self.total_in_amount = round(float(self.total_in_Amount[0][0]), 2)
                self.total_in_a.config(text=str(self.total_in_amount))

                # get total expense from database
                cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id = u.user_id "
                               "AND t.type_id = ty.type_id AND t.type_id = 2 AND u.user_id = ? ",
                               (self.controller.shared_user_id['userID'].get(),))
                if self.total_ex_Amount == None:
                    self.total_ex_amount.set(0)
                else:
                    self.total_ex_amount = round(float(self.total_ex_Amount[0][0]), 2)
                    self.total_ex_a.config(text=str(self.total_ex_amount))

    def sort(self):
        # verify conditions to filter out data
        # query to display the transaction with condition in the treeview
        self.query = "SELECT t.date, a.acc_name, c.cat_name, ty.type_name, t.amount, t.remark FROM transactions t, " \
                     "account a, category c, type ty, user u WHERE t.acc_id = a.acc_id AND t.cat_id = c.cat_id AND " \
                     "t.type_id = ty.type_id AND t.user_id = u.user_id AND t.user_id = ? "

        # query to get the total income amount
        self.query1 = "SELECT sum(t.amount) FROM transactions t, account a, category c, type ty, user u WHERE " \
                      "t.acc_id = a.acc_id AND t.cat_id = c.cat_id AND t.type_id = ty.type_id AND t.user_id = " \
                      "u.user_id AND t.type_id = 1 AND t.user_id = ? "

        # query to get the total expense amount
        self.query2 = "SELECT sum(t.amount) FROM transactions t, account a, category c, type ty, user u WHERE " \
                      "t.acc_id = a.acc_id AND t.cat_id = c.cat_id AND t.type_id = ty.type_id AND t.user_id = " \
                      "u.user_id AND t.type_id = 2 AND t.user_id = ? "

        # a list to store the condition variable
        self.variable_list = [self.controller.shared_user_id['userID'].get()]

        # verify the condition
        if self.account_cbox.get() == 'None':
            pass
        else:
            # get the account id that user input
            cursor.execute("SELECT a.acc_id FROM account a, user u WHERE a.user_id = u.user_id AND a.user_id = ? AND "
                           "a.acc_name = ?", (self.controller.shared_user_id['userID'].get(), self.account_cbox.get(),))
            self.accountID = cursor.fetchall()
            self.accountid = self.accountID[0][0]
            self.query = self.query + "AND t.acc_id = ? "
            self.query1 = self.query1 + "AND t.acc_id = ? "
            self.query2 = self.query2 + "AND t.acc_id = ? "
            self.variable_list.append(self.accountid)
        if self.category_cbox.get() == 'None':
            pass
        else:
            # get the category id that the user input
            cursor.execute("SELECT c.cat_id FROM category c, user u WHERE c.user_id = u.user_id AND c.user_id = ? AND "
                           "c.cat_name = ?", (self.controller.shared_user_id['userID'].get(), self.category_cbox.get(),))
            self.categoryID = cursor.fetchall()
            self.categoryid = self.categoryID[0][0]
            self.query = self.query + "AND c.cat_id = ? "
            self.query1 = self.query1 + "AND c.cat_id = ? "
            self.query2 = self.query2 + "AND c.cat_id = ? "
            self.variable_list.append(self.categoryid)
        if self.type_cbox.get() == 'None':
            pass
        else:
            # get the type id that the user input
            cursor.execute("SELECT type_id FROM type WHERE type_name = ?", (self.type_cbox.get(),))
            self.typeID = cursor.fetchall()
            self.typeid = self.typeID[0][0]
            self.query = self.query + "AND ty.type_id = ? "
            self.variable_list.append(self.typeid)
        if self.month_cbox.get() == 'None':
            if self.year_cbox.get() == 'None':
                pass
            else:
                self.query = self.query + "AND strftime('%Y', t.date) = ? "
                self.query1 = self.query1 + "AND strftime('%Y', t.date) = ? "
                self.query2 = self.query2 + "AND strftime('%Y', t.date) = ? "
                self.variable_list.append(self.year_cbox.get())
        else:
            if self.year_cbox.get() == 'None':
                messagebox.showerror('Error', 'Please select the year of the month that you choose.')
            else:
                self.query = self.query + "AND strftime('%Y', t.date) = ? AND strftime('%m', t.date) = ? "
                self.query1 = self.query1 + "AND strftime('%Y', t.date) = ? AND strftime('%m', t.date) = ? "
                self.query2 = self.query2 + "AND strftime('%Y', t.date) = ? AND strftime('%m', t.date) = ? "
                self.variable_list.append(self.year_cbox.get())
                self.variable_list.append(self.month_cbox.get())

        # verify if the user did not filter data with any condition
        if self.account_cbox.get() == 'None' and self.category_cbox.get() == 'None' and self.type_cbox.get() == 'None' \
                and self.month_cbox.get() == 'None' and self.year_cbox.get() == 'None':
            messagebox.showerror('Information', 'You does not filter transaction with any conditions.')

            # empty the treeview
            self.transaction_list.delete(*self.transaction_list.get_children())
            self.display_all()

            # get total income from database
            cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id = u.user_id "
                           "AND t.type_id = ty.type_id AND t.type_id = 1 AND u.user_id = ? ",
                           (self.controller.shared_user_id['userID'].get(),))
            if self.total_in_Amount == None:
                self.total_in_amount.set(0)
            else:
                self.total_in_amount = round(float(self.total_in_Amount[0][0]), 2)
                self.total_in_a.config(text=str(self.total_in_amount))

            # get total expense from database
            cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id = u.user_id "
                           "AND t.type_id = ty.type_id AND t.type_id = 2 AND u.user_id = ? ",
                           (self.controller.shared_user_id['userID'].get(),))
            if self.total_ex_Amount == None:
                self.total_ex_amount.set(0)
            else:
                self.total_ex_amount = round(float(self.total_ex_Amount[0][0]), 2)
                self.total_ex_a.config(text=str(self.total_ex_amount))
        self.root.destroy()

        # assign new variable from the variable list
        for n, val in enumerate(self.variable_list):
            globals()["var%d" % n] = val

        # empty treeview
        self.transaction_list.delete(*self.transaction_list.get_children())
        try:
            cursor.execute(self.query, (var0,))
            self.rows = cursor.fetchall()

            # get total income from database
            cursor.execute(self.query1, (var0,))
            self.total_in_Amount = cursor.fetchall()
            if self.total_in_Amount == None:
                self.total_in_amount.set(0)
            else:
                self.total_in_amount = round(float(self.total_in_Amount[0][0]), 2)
                self.total_in_a.config(text=str(self.total_in_amount))

            # get total expense from database
            cursor.execute(self.query2, (var0,))
            self.total_ex_Amount = cursor.fetchall()
            if self.total_ex_Amount == None:
                self.total_ex_amount.set(0)
            else:
                self.total_ex_amount = round(float(self.total_ex_Amount[0][0]), 2)
                self.total_ex_a.config(text=str(self.total_ex_amount))
        except:
            try:
                cursor.execute(self.query, (var0, var1,))
                self.rows = cursor.fetchall()

                # get total income from database
                cursor.execute(self.query1, (var0, var1,))
                self.total_in_Amount = cursor.fetchall()
                if self.total_in_Amount == None:
                    self.total_in_amount.set(0)
                else:
                    self.total_in_amount = round(float(self.total_in_Amount[0][0]), 2)
                    self.total_in_a.config(text=str(self.total_in_amount))

                # get total expense from database
                cursor.execute(self.query2, (var0, var1,))
                self.total_ex_Amount = cursor.fetchall()
                if self.total_ex_Amount == None:
                    self.total_ex_amount.set(0)
                else:
                    self.total_ex_amount = round(float(self.total_ex_Amount[0][0]), 2)
                    self.total_ex_a.config(text=str(self.total_ex_amount))
            except:
                try:
                    cursor.execute(self.query, (var0, var1, var2,))
                    self.rows = cursor.fetchall()

                    # get total income from database
                    cursor.execute(self.query1, (var0, var1,))
                    self.total_in_Amount = cursor.fetchall()
                    if self.total_in_Amount == None:
                        self.total_in_amount.set(0)
                    else:
                        self.total_in_amount = round(float(self.total_in_Amount[0][0]), 2)
                        self.total_in_a.config(text=str(self.total_in_amount))

                    # get total expense from database
                    cursor.execute(self.query2, (var0, var1,))
                    self.total_ex_Amount = cursor.fetchall()
                    if self.total_ex_Amount == None:
                        self.total_ex_amount.set(0)
                    else:
                        self.total_ex_amount = round(float(self.total_ex_Amount[0][0]), 2)
                        self.total_ex_a.config(text=str(self.total_ex_amount))
                except:
                    try:
                        cursor.execute(self.query, (var0, var1, var3,))
                        self.rows = cursor.fetchall()

                        # get total income from database
                        cursor.execute(self.query1, (var0, var1, var3,))
                        self.total_in_Amount = cursor.fetchall()
                        if self.total_in_Amount == None:
                            self.total_in_amount.set(0)
                        else:
                            self.total_in_amount = round(float(self.total_in_Amount[0][0]), 2)
                            self.total_in_a.config(text=str(self.total_in_amount))

                        # get total expense from database
                        cursor.execute(self.query2, (var0, var1, var3,))
                        self.total_ex_Amount = cursor.fetchall()
                        if self.total_ex_Amount == None:
                            self.total_ex_amount.set(0)
                        else:
                            self.total_ex_amount = round(float(self.total_ex_Amount[0][0]), 2)
                            self.total_ex_a.config(text=str(self.total_ex_amount))
                    except:
                        try:
                            cursor.execute(self.query, (var0, var1, var3, var4,))
                            self.rows = cursor.fetchall()

                            # get total income from database
                            cursor.execute(self.query1, (var0, var1, var3, var4,))
                            self.total_in_Amount = cursor.fetchall()
                            if self.total_in_Amount == None:
                                self.total_in_amount.set(0)
                            else:
                                self.total_in_amount = round(float(self.total_in_Amount[0][0]), 2)
                                self.total_in_a.config(text=str(self.total_in_amount))

                            # get total expense from database
                            cursor.execute(self.query2, (var0, var1, var3, var4,))
                            self.total_ex_Amount = cursor.fetchall()
                            if self.total_ex_Amount == None:
                                self.total_ex_amount.set(0)
                            else:
                                self.total_ex_amount = round(float(self.total_ex_Amount[0][0]), 2)
                                self.total_ex_a.config(text=str(self.total_ex_amount))
                        except:
                            pass

        # if self.total_in_Amount == None:
        #     self.total_in_amount.set(0)
        # else:
        #     self.total_in_amount = round(float(self.total_in_Amount[0][0]), 2)
        #     self.total_in_a.config(text=str(self.total_in_amount))

        # if self.total_ex_Amount == None:
        #     self.total_ex_amount.set(0)
        # else:
        #     self.total_ex_amount = round(float(self.total_ex_Amount[0][0]), 2)
        #     self.total_ex_a.config(text=str(self.total_ex_amount))

        # loop to display all the transaction in treeview
        global count
        count = 0
        for row in self.rows:
            if count % 2 == 0:
                self.transaction_list.insert("", END, values=row, tags='evenrow')
            else:
                self.transaction_list.insert("", END, values=row, tags='oddrow')
            count += 1

    def filter(self):
        self.root = Toplevel()
        self.root.geometry("425x215")
        self.root.title("Iccountant - Filter Transaction")
        self.root.configure(bg='#1A1A1A')
        self.title_l = Label(self.root, font=('lato', 15), bg='#1A1A1A', text='Filter Transaction', fg='white')
        self.title_l.grid(row=0, column=0)
        self.account_l = Label(self.root, font=('lato', 12), bg='#1A1A1A', text='Account :', fg='white')
        self.account_l.grid(row=1, column=0)
        self.account_get = pd.read_sql_query("SELECT a.acc_name AS Account FROM transactions t, account a, user u "
                                             "WHERE a.acc_id = t.acc_id AND u.user_id = t.user_id AND t.user_id IN "
                                             "('{}') GROUP BY t.acc_id".format
                                             (self.controller.shared_user_id['userID'].get()), connect)
        self.account_df = pd.DataFrame(self.account_get)
        self.account_list = self.account_df['Account'].values.tolist()
        self.account_list.insert(0, 'None')
        self.account_cbox = ttk.Combobox(self.root, values=self.account_list, font=('lato', 12), state='readonly',
                                         justify='center')
        self.account_cbox.grid(row=1, column=1)
        self.account_cbox.set("None")
        self.category_l = Label(self.root, font=('lato', 12), bg='#1A1A1A', text='Category :', fg='white')
        self.category_l.grid(row=2, column=0)
        self.category_get = pd.read_sql_query("SELECT c.cat_name AS Category FROM category c, transactions t, user "
                                              "u WHERE c.cat_id = t.cat_id AND t.user_id = u.user_id AND u.user_id "
                                              "IN ('{}') GROUP BY t.cat_id".format
                                              (self.controller.shared_user_id['userID'].get()), connect)
        self.category_df = pd.DataFrame(self.category_get)
        self.category_list = self.category_df['Category'].values.tolist()
        self.category_list.insert(0, 'None')
        self.category_cbox = ttk.Combobox(self.root, values=self.category_list, font=('lato', 12), state='readonly',
                                          justify='center')
        self.category_cbox.grid(row=2, column=1)
        self.category_cbox.set("None")
        self.type_l = Label(self.root, font=('lato', 12), bg='#1A1A1A', text='Type :', fg='white')
        self.type_l.grid(row=3, column=0)
        self.type_get = pd.read_sql_query("SELECT type_name AS Type FROM type", connect)
        self.type_df = pd.DataFrame(self.type_get)
        self.type_list = self.type_df['Type'].values.tolist()
        self.type_list.insert(0, 'None')
        self.type_cbox = ttk.Combobox(self.root, values=self.type_list, font=('lato', 12), state='readonly',
                                      justify='center')
        self.type_cbox.grid(row=3, column=1)
        self.type_cbox.set("None")
        self.year_l = Label(self.root, font=('lato', 12), bg='#1A1A1A', text='Year :', fg='white')
        self.year_l.grid(row=4, column=0)
        self.year_get = pd.read_sql_query("SELECT strftime('%Y', t.date) AS Year FROM transactions t, user u WHERE "
                                          "u.user_id = t.user_id AND t.user_id IN ('{}') GROUP BY "
                                          "strftime('%Y', t.date)".format(self.controller.shared_user_id['userID'].get()), connect)
        self.year_df = pd.DataFrame(self.year_get)
        self.year_list = self.year_df['Year'].values.tolist()
        self.year_list.insert(0, 'None')
        self.year_cbox = ttk.Combobox(self.root, values=self.year_list, font=('lato', 12), state='readonly',
                                      justify='center')
        self.year_cbox.grid(row=4, column=1)
        self.year_cbox.set("None")
        self.month_l = Label(self.root, font=('lato', 12), bg='#1A1A1A', text='Month :', fg='white')
        self.month_l.grid(row=5, column=0)
        self.month_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        self.month_cbox = ttk.Combobox(self.root, values=self.month_list, font=('lato', 12), state='readonly',
                                       justify='center')
        self.month_cbox.grid(row=5, column=1)
        self.month_cbox.set("None")
        self.confirm_pic = ImageTk.PhotoImage(Image.open('confirm button.png')
                                              .resize((75, 35), resample=Image.LANCZOS))
        self.cancel_pic = ImageTk.PhotoImage(Image.open('cancel button.png')
                                             .resize((75, 35), resample=Image.LANCZOS))
        self.confirm_b = tk.Button(self.root, image=self.confirm_pic, bg='#1A1A1A', relief='flat', command=self.sort)
        self.confirm_b.grid(row=6, columnspan=3)
        self.cancel_b = tk.Button(self.root, image=self.cancel_pic, bg='#1A1A1A', relief='flat',
                                  command=self.root.destroy)
        self.cancel_b.grid(row=6, column=1)


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
        self.addConfirm = customtkinter.CTkButton(self.editUsernameWindow, text='OK', width=50, height=30,
                                                  fg_color="#464E63",
                                                  hover_color="#667190", command=lambda: self.editusername())
        self.addConfirm.pack(pady=10)

        self.cancel = customtkinter.CTkButton(self.editUsernameWindow, text='Cancel', width=55, height=30,
                                              fg_color="#464E63",
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
        self.addConfirm = customtkinter.CTkButton(self.editPasswordWindow, text='OK', width=50, height=30,
                                                  fg_color="#464E63",
                                                  hover_color="#667190", command=lambda: self.editpassword())
        self.addConfirm.pack(pady=10)

        self.cancel = customtkinter.CTkButton(self.editPasswordWindow, text='Cancel', width=55, height=30,
                                              fg_color="#464E63",
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


if __name__ == "__main__":
    app = windows()
    app.mainloop()
