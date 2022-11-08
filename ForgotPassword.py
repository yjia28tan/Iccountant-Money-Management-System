import math
import random #to create otp
import smtplib #to send email
import requests #to verify email
import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
import customtkinter
import tkinter.font as tkFont

class ForgotPassword:

    def __init__(self, root):
        self.root = root
        
        self.root.geometry('1280x720')
        self.root.resizable(0, 0)
        self.root.title("Iccountant Money Management System")
        self.root.config(bg= 'black')

        
        #forgot password frames/pages
        self.fgt_frame = tk.Frame(self.root, bg = 'black')
       
        
        #page1

        self.fgt_title = tk.Label(self.fgt_frame, text = 'Reset Password', fg = 'white', bg='black')
        self.fgt_title.config(font=tkFont.Font(family='Lato', size=20, weight="bold"))
        self.fgt_title.pack(anchor = NW, padx=80, pady = 5)
        Canvas(self.fgt_frame, width=1000, height = 2.0, bg = 'white', highlightthickness = 1).pack(pady=10)

        tk.Label(self.fgt_frame, text =  '', bg= 'black').pack(pady=8)


        
         #email
        # User Email Label and Text Entry Box
    

        self.regemail_lb = tk.Label(self.fgt_frame, text='Email',fg = 'white', bg='black')
        self.regemail_lb.config(font=tkFont.Font(family='Lato', size=15, weight="bold"))
        self.regemail_lb.pack(pady=5)
        self.regemail = StringVar()
        self.regemail_entry = Entry(self.fgt_frame, justify = 'center',width = 30,highlightthickness = 0, textvariable=self.regemail, relief = FLAT, font = ('Bold', 12),fg = 'white', bg = 'black', insertbackground = 'white')
        self.regemail_entry.config(font=tkFont.Font(family='Lato', size=12))
        self.regemail_entry.pack()
        self.regemail_line = Canvas(self.fgt_frame, width=300, height = 2.0, bg = 'white', highlightthickness = 0)
        self.regemail_line.pack()
        tk.Label(self.fgt_frame, text =  '', bg= 'black').pack(pady=3)



        #newpassword

        self.newpassword_lb = tk.Label(self.fgt_frame, text='Password', font=('Bold', 15),fg = 'white', bg='black')
        self.newpassword_lb.config(font=tkFont.Font(family='Lato', size=15, weight="bold"))
        self.newpassword_lb.pack(pady=5)
        self.newpassword = StringVar()
        self.newpassword_lb_entry = Entry(self.fgt_frame, justify = 'center',width = 30,highlightthickness = 0, textvariable=self.newpassword, relief = FLAT, font = ('Bold', 12),show='*',fg = 'white', bg = 'black', insertbackground = 'white')
        self.newpassword_lb_entry.config(font=tkFont.Font(family='Lato', size=12))
        self.newpassword_lb_entry.pack()
        self.newpassword_lb_line = Canvas(self.fgt_frame, width=300, height = 2.0, bg = 'white', highlightthickness = 0)
        self.newpassword_lb_line.pack()
        tk.Label(self.fgt_frame, text =  '', bg= 'black').pack(pady=3)

        
     
        #confirm password
        self.conpassword_lb = tk.Label(self.fgt_frame, text='Confirm Password', fg = 'white', bg='black')
        self.conpassword_lb.config(font=tkFont.Font(family='Lato', size=15, weight="bold"))
        self.conpassword_lb.pack(pady=5)
        self.conpassword = StringVar()
        self.conpassword_lb_entry = Entry(self.fgt_frame,justify = 'center',width = 30, highlightthickness = 0, textvariable=self.conpassword, relief = FLAT, font = ('Bold', 12),show='*',fg = 'white', bg = 'black', insertbackground = 'white')
        self.conpassword_lb_entry.config(font=tkFont.Font(family='Lato', size=12))
        self.conpassword_lb_entry.pack()
        self.conpassword_lb_line = Canvas(self.fgt_frame, width=300, height = 2.0, bg = 'white', highlightthickness = 0)
        self.conpassword_lb_line.pack()

        
      


        self.btn_value = IntVar(value=0)
        self.check_btn = Checkbutton(self.fgt_frame, text="Show password", variable=self.btn_value, command=self.show_password, fg = 'white', bg='black')
        self.check_btn.pack(pady = 5)
    

        self.fgt_frame.pack(pady = 40)


        
                             
        #buttons
        #next button
        self.sendotpbtn = customtkinter.CTkButton(master=self.fgt_frame,
                                          text="Send/Resend OTP",
                                          width=140, height=40,
                                          fg_color="#464E63",
                                          hover_color = "#667190",
                                          command = self.data_validation)
        self.sendotpbtn.pack(pady = 20)


        #back button    
        self.back = ImageTk.PhotoImage(Image.open('backicon.png').resize((40, 40), resample=Image.LANCZOS))
        self.backbtn1 = Button(self.fgt_frame, image=self.back, bg='black', relief='flat', command=self.move_back_page).place(x=3, y=1)

        

    def page2(self):
        #pge 2
        self.fgt_frame2= Toplevel()
        self.fgt_frame2.geometry("1280x720")
        self.fgt_frame2.resizable(0, 0)
        self.fgt_frame2.title("Iccountant")
        self.fgt_frame2.configure(bg='black')

        

        
        self.fgt_frame2_title = tk.Label(self.fgt_frame2, text = 'Email Verification', fg = 'white', bg='black')
        self.fgt_frame2_title.config(font=tkFont.Font(family='Lato', size=20, weight="bold"))
        self.fgt_frame2_title.place( x=225,y = 45)
        Canvas(self.fgt_frame2, width=1000, height = 2.0, bg = 'white', highlightthickness = 1).place(x = 640, y=100, anchor =tk.CENTER)

       
        
        #otp
        self.otp_lb = tk.Label(self.fgt_frame2, text='4-digit OTP', fg = 'white', bg='black')
        self.otp_lb.config(font=tkFont.Font(family='Lato', size=15, weight="bold"))
        self.otp_lb.place(x = 640,y=230, anchor =tk.CENTER)
        self.otp_ = StringVar()
        self.otp_lb_entry = Entry(self.fgt_frame2, justify = 'center',width = 30, highlightthickness = 0, textvariable=self.otp_, relief = FLAT, font = ('Bold', 15),show='*',fg = 'white', bg = 'black', insertbackground = 'white')
        self.otp_lb_entry.config(font=tkFont.Font(family='Lato', size=12))
        self.otp_lb_entry.place(x=640,y=265, anchor =tk.CENTER)
        self.otp_lb_line = Canvas(self.fgt_frame2, width=300, height = 2.0, bg = 'white', highlightthickness = 0)
        self.otp_lb_line.place(x=640,y=280, anchor =tk.CENTER)

        #back button
        self.back2 = ImageTk.PhotoImage(Image.open('backicon.png').resize((40, 40), resample=Image.LANCZOS))
        self.backbtn2 = Button(self.fgt_frame2, image=self.back2, bg='black', relief='flat', command= lambda: self.fgt_frame2.destroy()).place(x=140, y=40)

        #finish session button
        self.finishbtn = customtkinter.CTkButton(master=self.fgt_frame2,
                                          text="Finish",
                                          width=140, height=40,
                                          fg_color="#464E63",
                                          hover_color = "#667190",
                                          command = self.otp_validation)
        self.finishbtn.pack(side = tk.RIGHT,padx = 140)

        
    def show_password(self):
        if self.btn_value.get() == 1:
            self.newpassword_lb_entry.config(show='')
            self.conpassword_lb_entry.config(show='')
            
        else:
            self.newpassword_lb_entry.config(show='*')
            self.conpassword_lb_entry.config(show='*')
            


    def data_validation(self):

        #email stuff
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
             
                self.page2()
            else:
                messagebox.showerror('Error!', "Please enter the email that is registered in the system!")
        
                
    def otp_validation(self):
        
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
            
            
        else:
            messagebox.showerror('Error!', "incorrect OTP try again!")

    def update_data(self):
        #inputs
        self.r_email = self.regemail.get()
        self.npwd = self.newpassword.get()
        
        #open database
        self.conn = sqlite3.connect('Iccountant')
        self.cur = self.conn.cursor()
        self.cur.execute("""UPDATE user SET password = ? WHERE email = ?""",(self.npwd,self.r_email))
        
        self.conn.commit()
        
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
