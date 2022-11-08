import math
import random #to create otp
import smtplib #to send email
import requests #to verify email
import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import customtkinter

# Create Database
conn = sqlite3.connect('Iccountant')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS user (
    user_id    INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name       VARCHAR NOT NULL,
    username   VARCHAR NOT NULL,
    email      VARCHAR NOT NULL,
    password   VARCHAR NOT NULL);''')
conn.commit()

class RegisterPage:
    def __init__(self,root):
        self.root = root
        
        self.root.geometry('1280x720')
        self.root.resizable(0, 0)
        self.root.title("Iccountant Money Management System")
        self.root.config(bg='black')

        
        #register frame
        #self.reg_frame = tk.Frame(self.root, bg = 'white')
        #self.reg_frame.pack(fill = 'both', expand= 'yes')

        
        #2 regiser pages
        self.pg1 = tk.Frame(self.root, bg = 'black')#,width=1150, height=600
        #self.pg1.pack() #fill = 'both', expand= 'yes'
        self.pg2 = tk.Frame(self.root, bg = 'black')
    


        self.pages = [self.pg1, self.pg2]
        self.count = 0

        #page 1
        self.pg1_title = tk.Label(self.pg1, text = 'User Account Registration', font = ('Bold', 20, 'bold'),fg = 'white', bg='black')
        self.pg1_title.pack(pady = 20)

        #full name
        self.fname_lb = tk.Label(self.pg1, text='Full name', font=('Bold', 15), fg = 'white', bg='black')
        self.fname_lb.pack(pady=5)
        self.fname = StringVar()
        self.fname_entry = Entry(self.pg1, width = 30, highlightthickness = 0, textvariable=self.fname, relief = FLAT, font = ('Bold', 12),fg = 'white', bg = 'black', insertbackground = 'white')
        self.fname_entry.pack(pady=5)
        self.fname_line = Canvas(self.pg1, width=300, height = 2.0, bg = 'white', highlightthickness = 0)
        self.fname_line.pack()

        #user name
        self.username_lb = tk.Label(self.pg1, text='Username', font=('Bold', 15), fg = 'white', bg='black')
        self.username_lb.pack(pady=5)
        self.username = StringVar()
        self.username_lb_entry = Entry(self.pg1, width = 30,highlightthickness = 0, textvariable=self.username, relief = FLAT, font = ('Bold', 12),fg = 'white', bg = 'black', insertbackground = 'white')
        self.username_lb_entry.pack(pady=5)
        self.username_lb_line = Canvas(self.pg1, width=300, height = 2.0, bg = 'white', highlightthickness = 0)
        self.username_lb_line.pack()

        #email
        # User Email Label and Text Entry Box
        self.email_lb = tk.Label(self.pg1, text='Email', font=('Bold', 15),fg = 'white', bg='black')
        self.email_lb.pack(pady=5)
        self.email = StringVar()
        self.email_entry = Entry(self.pg1, width = 30,highlightthickness = 0, textvariable=self.email, relief = FLAT, font = ('Bold', 12),fg = 'white', bg = 'black', insertbackground = 'white')
        self.email_entry.pack(pady=5)
        self.email_line = Canvas(self.pg1, width=300, height = 2.0, bg = 'white', highlightthickness = 0)
        self.email_line.pack()



        #password
        self.password_lb = tk.Label(self.pg1, text='Password', font=('Bold', 15),fg = 'white', bg='black')
        self.password_lb.pack(pady=5)
        self.password = StringVar()
        self.password_lb_entry = Entry(self.pg1, width = 30,highlightthickness = 0, textvariable=self.password, relief = FLAT, font = ('Bold', 12),show='*',fg = 'white', bg = 'black', insertbackground = 'white')
        self.password_lb_entry.pack(pady=5)
        self.password_lb_line = Canvas(self.pg1, width=300, height = 2.0, bg = 'white', highlightthickness = 0)
        self.password_lb_line.pack()

        #confirm password
        self.conpassword_lb = tk.Label(self.pg1, text='Confirm Password', font=('Bold', 15), fg = 'white', bg='black')
        self.conpassword_lb.pack(pady=5)
        self.conpassword = StringVar()
        self.conpassword_lb_entry = Entry(self.pg1,width = 30, highlightthickness = 0, textvariable=self.conpassword, relief = FLAT, font = ('Bold', 12),show='*',fg = 'white', bg = 'black', insertbackground = 'white')
        self.conpassword_lb_entry.pack(pady=5)
        self.conpassword_lb_line = Canvas(self.pg1, width=300, height = 2.0, bg = 'white', highlightthickness = 0)
        self.conpassword_lb_line.pack()


        self.btn_value = IntVar(value=0)
        self.check_btn = Checkbutton(self.pg1, text="Show password", variable=self.btn_value, command=self.show_password, fg = 'white',bg='black')
        self.check_btn.pack(pady=5)

        self.pg1.pack(pady = 100)


        #pge 2
        
        self.pg2_title = tk.Label(self.pg2, text = 'Email Verification', font = ('Bold', 20, 'bold'),fg = 'white', bg='black')
        self.pg2_title.pack(pady = 20)

        tk.Label(self.pg2, text =  '', bg= 'black').pack(pady=30)
        
        #otp
        self.otp_lb = tk.Label(self.pg2, text='4-digit OTP', font=('Bold', 15), fg = 'white', bg='black')
        self.otp_lb.pack(pady=5)
        self.otp_ = StringVar()
        self.otp_lb_entry = Entry(self.pg2, width = 30, highlightthickness = 0, textvariable=self.otp_, relief = FLAT, font = ('Bold', 15),show='*',fg = 'white', bg = 'black', insertbackground = 'white')
        self.otp_lb_entry.pack()
        self.otp_lb_line = Canvas(self.pg2, width=300, height = 2.0, bg = 'white', highlightthickness = 0)
        self.otp_lb_line.pack()

        self.pg2.pack(pady = 100)


        #self.bottom_frame = tk.Frame(root)
        #buttons
        #next button
        self.nextbtn = customtkinter.CTkButton(master=self.pg1,
                                          text="Next",
                                          width=90, height=40,
                                          fg_color="#464E63",
                                          hover_color = "#667190",
                                          command = self.data_validation)
        self.nextbtn.pack(side=tk.RIGHT, padx=20)

        #back button
        self.backbtn = customtkinter.CTkButton(master=self.pg2,
                                          text="Back",
                                          width=90,
                                          height=40,
                                          fg_color="#464E63",
                                          hover_color = "#667190",
                                          command = self.move_back_page)
        self.backbtn.pack(side=tk.LEFT, padx=20, pady = 20)

        #finish button
        self.nextbtn = customtkinter.CTkButton(master=self.pg2,
                                          text="Finish",
                                          width=90, height=40,
                                          fg_color="#464E63",
                                          hover_color = "#667190",
                                          command = self.finish_session)
        self.nextbtn.pack(side=tk.RIGHT, padx=20)


        #self.bottom_frame.pack(side=tk.BOTTOM, pady=30)
        
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
        #email stuff
        # ?
        self.s = smtplib.SMTP('smtp.gmail.com', 587)
        self.s.starttls()#start TLS for security
        self.s.login("iccountant2022@gmail.com", "vgndqclbhalavixj")#authentication
        self.digits="0123456789"#create 4-digit OTP
        self.OTP=""
        for self.i in range(4):
            self.OTP+=self.digits[math.floor(random.random()*10)]

        #message to be sent   
        self.subject = "Email verification code"

        self.text = "Hi user,\n\nYour OTP for the registeration is:\n\n" + self.OTP + "\n\nThank you.\n\n\nIccountant"

        self.msg = 'Subject: {}\n\n{}'.format(self.subject, self.text)
        
        self.response = requests.get(
            "https://isitarealemail.com/api/email/validate",
            params = {'email': self.email_})
        self.status = self.response.json()['status']

        

        self.conn = sqlite3.connect('Iccountant')
        

        #input validation
        if not self.fname.get() or not self.name or not self.uname or not self.email_ or not self.pwd or not self.conpwd:
            messagebox.showerror('Error!', "Please fill the form!")
        else:
            #self.conn = sqlite3.connect('Iccountant')
            self.cursor= self.conn.execute('SELECT * from user where username="%s"'%(self.uname))
            if self.cursor.fetchone():
                messagebox.showerror('Error!', "Please enter a unique username!")
            else:
                self.cursor= self.conn.execute('SELECT * from user where email="%s"'%(self.email_))
                if self.cursor.fetchone():
                    messagebox.showerror('Error!', "Please enter a unique email!")
                elif len(self.pwd) < 8:
                    messagebox.showerror('Error!', "Please enter a password that is at least 8 characters!")

                elif self.pwd != self.conpwd:
                    messagebox.showerror('Error!', "Please match both password and confirm password!")
                elif self.status != "valid":
                    messagebox.showerror('Error!', "Please enter a valid/existing email!")
                else:
                    messagebox.showinfo('Success!', "All of the form is filled!")
                    self.s.sendmail("all2ctt@gmail.com",self.email_,self.msg)
                    
                    self.move_next_page()
                    
     
            
        
        
        
    def insert_data(self):
        
        self.conn = sqlite3.connect('Iccountant')
        self.cur = self.conn.cursor()
        #cur.execute("INSERT INTO user VALUES (:name, :username, :email, :password",{'name': fname.get(), 'username': username.get(),'email': email.get(), 'password': password.get()})
        self.cur.execute("INSERT INTO user (name,username,email,password) VALUES (:name, :username, :email, :password)",
                    {'name': self.name, 'username': self.uname, 'email': self.email_, 'password': self.pwd})
        self.conn.commit()
        messagebox.showinfo('Confirmation', 'Record Saved! Session is finished!')

    def finish_session(self):
        print(self.otp_.get())
        if self.otp_.get() == self.OTP:
            messagebox.showinfo('Success!', "OTP verified!")

            #message to be sent: succesfully registered
            self.subject2 = "Icccountant account has successfully registered!"
            self.text2 = "Hi user,\n\nYour account for Icccountant desktop app has successfully registered.\nThank you.\n\n\nIccountant"
            self.msg2 = 'Subject: {}\n\n{}'.format(self.subject2, self.text2)
            self.s.sendmail("all2ctt@gmail.com",self.email_,self.msg2)
            

            #terminating the session
            self.s.quit()
            self.insert_data()
            #self.move_next_page()
            print('all good!')

            
        else:
            messagebox.showerror('Error!', "incorrect OTP try again!")
    def move_next_page(self):
        global count

        if not self.count > len(self.pages) - 2:

            for self.p in self.pages:
                self.p.pack_forget()

            self.count += 1

            self.page = self.pages[self.count]
            self.page.pack(pady = 100)

    def move_back_page(self):
        global count

        if not self.count == 0:

            for self.p in self.pages:
                self.p.pack_forget()

            self.count -= 1

            self.page = self.pages[self.count]
            self.page.pack(pady = 100)



def main(): 
    root = tk.Tk()
    r = RegisterPage(root)
    root.mainloop()

if __name__ == '__main__':
    main()



