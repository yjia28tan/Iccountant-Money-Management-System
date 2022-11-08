import math
import random #to create otp
import smtplib #to send email
import requests #to verify email
import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import customtkinter

class ForgotPassword:

    def __init__(self, root):
        self.root = root
        
        self.root.geometry('1280x720')
        self.root.resizable(0, 0)
        self.root.title("Iccountant Money Management System")
        self.root.config(bg= 'black')

        
        #forgot password frames/pages
        self.fgt_frame = tk.Frame(self.root, bg = 'black')
        #self.fgt_frame.pack(fill = 'both', expand= 'yes')
        self.fgt_frame2 = tk.Frame(self.root, bg = 'black')
        #self.fgt_frame2.pack(fill = 'both', expand= 'yes')

        self.pages =[self.fgt_frame,self.fgt_frame2]
        self.count = 0

        #page1
        self.fgt_title = tk.Label(self.fgt_frame, text = 'Reset Password', font = ('Bold', 20, 'bold'),fg = 'white', bg='black')
        self.fgt_title.pack()
        
        tk.Label(self.fgt_frame, text =  '', bg= 'black').pack(pady=30)

         #email
        # User Email Label and Text Entry Box
    
        self.regemail_lb = tk.Label(self.fgt_frame, text='Email', font=('Bold', 15),fg = 'white', bg='black')
        self.regemail_lb.pack(pady=5)
        self.regemail = StringVar()
        self.regemail_entry = Entry(self.fgt_frame, width = 30,highlightthickness = 0, textvariable=self.regemail, relief = FLAT, font = ('Bold', 12),fg = 'white', bg = 'black', insertbackground = 'white')
        self.regemail_entry.pack(pady=5)
        self.regemail_line = Canvas(self.fgt_frame, width=300, height = 2.0, bg = 'white', highlightthickness = 0)
        self.regemail_line.pack()



        #newpassword
        self.newpassword_lb = tk.Label(self.fgt_frame, text='New Password', font=('Bold', 15),fg = 'white', bg='black')
        self.newpassword_lb.pack(pady=5)
        self.newpassword = StringVar()
        self.newpassword_lb_entry = Entry(self.fgt_frame, width = 30,highlightthickness = 0, textvariable=self.newpassword, relief = FLAT, font = ('Bold', 12),show='*',fg = 'white', bg = 'black', insertbackground = 'white')
        self.newpassword_lb_entry.pack(pady=5)
        self.newpassword_lb_line = Canvas(self.fgt_frame, width=300, height = 2.0, bg = 'white', highlightthickness = 0)
        self.newpassword_lb_line.pack()
        
     
        #confirm password
        self.conpassword_lb = tk.Label(self.fgt_frame, text='Confirm New Password', font=('Bold', 15),fg = 'white', bg='black')
        self.conpassword_lb.pack(pady=5)
        self.conpassword = StringVar()
        self.conpassword_lb_entry = Entry(self.fgt_frame, width = 30,highlightthickness = 0, textvariable=self.conpassword, relief = FLAT, font = ('Bold', 12),show='*',fg = 'white', bg = 'black', insertbackground = 'white')
        self.conpassword_lb_entry.pack(pady=5)
        self.conpassword_lb_line = Canvas(self.fgt_frame, width=300, height = 2.0, bg = 'white', highlightthickness = 0)
        self.conpassword_lb_line.pack()

        
      


        self.btn_value = IntVar(value=0)
        self.check_btn = Checkbutton(self.fgt_frame, text="Show password", variable=self.btn_value, command=self.show_password, fg = 'white', bg='black')
        self.check_btn.pack(pady = 5)
    

        self.fgt_frame.pack(pady = 100)


        #page 2
        self.fgt_title2 = tk.Label(self.fgt_frame2, text = 'Email Verification', font = ('Bold', 20, 'bold'),fg = 'white', bg='black')
        self.fgt_title2.pack()

        tk.Label(self.fgt_frame2, text =  '', bg= 'black').pack(pady=30)
                             
        self.otp_lb = tk.Label(self.fgt_frame2, text='4-digit OTP', font=('Bold', 15),fg = 'white', bg='black')
        self.otp_lb.pack(pady=5)
        self.otp_ = StringVar()
        self.otp_lb_entry = Entry(self.fgt_frame2, width = 30,highlightthickness = 0, textvariable=self.otp_, relief = FLAT, font = ('Bold', 12),show='*',fg = 'white', bg='black', insertbackground = 'white')
        self.otp_lb_entry.pack()
        self.otp_lb_line = Canvas(self.fgt_frame2, width=300, height = 2.0, bg = 'white', highlightthickness = 0)
        self.otp_lb_line.pack()
                             
        self.fgt_frame2.pack(pady = 100)
                             
        #buttons
        #next button
        self.sendotpbtn = customtkinter.CTkButton(master=self.fgt_frame,
                                          text="Send/Resend OTP",
                                          width=90, height=40,
                                          fg_color="#464E63",
                                          hover_color = "#667190",
                                          command = self.data_validation)
        self.sendotpbtn.pack(pady = 20)

        #back button
        self.backbtn = customtkinter.CTkButton(master=self.fgt_frame2,
                                          text="Back",
                                          width=90,
                                          height=40,
                                          fg_color="#464E63",
                                          hover_color = "#667190",
                                          command = self.move_back_page)
        self.backbtn.pack(side=tk.LEFT, padx=20, pady=20)
        #finish session button
        self.finishbtn = customtkinter.CTkButton(master=self.fgt_frame2,
                                          text="Finish",
                                          width=90, height=40,
                                          fg_color="#464E63",
                                          hover_color = "#667190",
                                          command = self.otp_validation)
        self.finishbtn.pack(side = tk.RIGHT,padx = 20)

    def show_password(self):
        if self.btn_value.get() == 1:
            self.newpassword_lb_entry.config(show='')
            self.conpassword_lb_entry.config(show='')
            
        else:
            self.newpassword_lb_entry.config(show='*')
            self.conpassword_lb_entry.config(show='*')
            


    def data_validation(self):

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
        self.subject = "Reset password verification code"

        self.text = "Hi user,\n\nYour OTP for the reseting password is:\n\n" + self.OTP + "\n\nThank you.\n\n\nIccountant"

        self.msg = 'Subject: {}\n\n{}'.format(self.subject, self.text)
      


        #inputs
        self.r_email = self.regemail.get()
        self.npwd = self.newpassword.get()
        self.cpwd = self.conpassword.get()
        #applying validation
        if not self.r_email or not self.npwd or not self.cpwd:
            messagebox.showerror('Error!', "Please fill the form!")
        elif len(self.newpassword.get()) < 8:
            messagebox.showerror('Error!', "Please enter a password that is at least 8 characters!")
            
        elif self.newpassword.get() != self.conpassword.get():
            messagebox.showerror('Error!', "Please match both password and confirm password!")
        else:
            
            #open database
            self.conn = sqlite3.connect('Iccountant')
            
            self.cursor= self.conn.execute('SELECT email from user where email="%s"'%(self.r_email))#and email="%s"
            #fetch data 
            if self.cursor.fetchone():
                messagebox.showinfo('Success!', "All of the form is filled!")
                self.s.sendmail("all2ctt@gmail.com",self.r_email,self.msg)
                self.move_next_page()
            else:
                messagebox.showerror('Error!', "Please enter the email that is registered in the system!")
        
                
    def otp_validation(self):
        print(self.otp_.get())
        if self.otp_.get() == self.OTP:
            messagebox.showinfo('Success!', "OTP verified!")

            #message to be sent: succesfully registered
            self.subject2 = "Icccountant account has successfully updated the password!"
            self.text2 = "Hi user,\n\nYour account for Icccountant desktop app has successfully reset the acount password.\nThank you.\n\n\nIccountant"
            self.msg2 = 'Subject: {}\n\n{}'.format(self.subject2, self.text2)
            self.s.sendmail("all2ctt@gmail.com",self.regemail.get(),self.msg2)
            

            #terminating the session
            self.s.quit()
            self.update_data()
            #self.move_next_page()
            print('all good!')
            #self.new_window()
            
        else:
            messagebox.showerror('Error!', "incorrect OTP try again!")

    def update_data(self):
        #inputs
        self.r_email = self.regemail.get()
        self.npwd = self.newpassword.get()
        
        #open database
        self.conn = sqlite3.connect('Iccountant')
        self.cur = self.conn.cursor()
        #self.cur.execute("INSERT INTO user VALUES (:name, :username, :email, :password)",
                    #{'name': self.fname.get(), 'username': self.username.get(), 'email': self.email.get(), 'password': self.password.get()})
        #self.cur.execute('SELECT email from user where email="%s"'%(self.r_email))
        self.cur.execute("""UPDATE user SET password = ? WHERE email = ?""",(self.npwd,self.r_email))
        
        self.conn.commit()
        print('should be updated here')
        messagebox.showinfo('Confirmation', 'Record Updated! Session is finished!')

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
    r = ForgotPassword(root)
    root.mainloop()

if __name__ == '__main__':
    main()

