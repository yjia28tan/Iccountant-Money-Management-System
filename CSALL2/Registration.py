# Register
import sqlite3
import tkinter as tk
import re
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


# Connect Database
def connectDatabase():
    try:
        global conn
        global cursor
        # connect to database
        conn = sqlite3.connect('CSALL2')
        # define cursor
        cursor =conn.cursor()
    except:
        messagebox.showerror('Error', 'Cannot connect to database!')



"""
class MainWindow():
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.win_title("Test Application")

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=400, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (SignInPage, SignUpPage):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(MainPage)
"""


def SignIn():
    connectDatabase()  # connect to database
    # ==== Declaring variables =====
    userEmail = tk.StringVar()
    username = tk.StringVar()
    password = tk.StringVar()
    # get entries from user
    user_email = userEmail.get()
    pw = password.get()
    try:
        # select data from database
        cursor.execute('SELECT * FROM user WHERE AND email =? AND password LIKE ?', [userEmail, password])

        # retrieve data from database
        login = cursor.fetchall()

        # define column in database
        for row in login:
            user_id = row[0]
            user_name = row[1]
            email = row[2]
            password = row[4]

    except Exception as ep:
        # show error message if error
        messagebox.showerror("Error", ep)

        # validation for log in entry
    # validate if entry not filled
    if userEmail == '' or pw == '':
        messagebox.showerror('Login Error', 'Please fill in all the fields.')
    else:
        if login:
            # show log in status
            messagebox.showinfo('Login Status', 'Successfully Signed In')

            # reset log in entry to empty
            for i in [userEmail, password]:
                i.set('')

        else:
            messagebox.showerror('Login Status', 'Invalid email or password')


#class SignInPage():
signInWindow = Tk()
signInWindow.rowconfigure(0, weight=1)
signInWindow.columnconfigure(0, weight=1)
signInWindow.state('zoomed')  # window full screen
signInWindow.title('ICCOUNTANT')

user_email = Label(signInWindow, text='Email', font=('Arial', 30, 'bold'))
user_email.grid(column=2, row=2)
user_email_entry = Entry(signInWindow)
user_email_entry.grid(column=2, row=3)
pw = Label(signInWindow, text='Password', font=('Arial', 30, 'bold'))
pw.grid(column=2, row=5)
pw_entry = Entry(signInWindow)
pw_entry.grid(column=2, row=6)

signInButton = Button(signInWindow, text="Sign In", font=('Arial', 15, 'bold'), command=lambda: SignIn)



    # Data Validation
def insert_data():
    check_count = 0
    msg = ""
    valid_email = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if re.search(valid_email, user_email.get()):
        check_count += 1
    else:
        msg = "Invalid email"
    if len(password.get()) < 5:
        msg = "Password too short"
    else:
        check_count += 1
    if password.get() != con_password.get():
        msg = "Password and confirm password did not match"
    else:
        check_count += 1
    if user_email.get() == "" or user_id.get() == "" or user_name.get() == "" or role.get() == "" or \
            password.get() == "" or con_password.get() == "":
        msg = "Input box cannot be empty"
    else:
        check_count += 1
    if check_count == 4:
        try:
            conn = sqlite3.connect('Poh Cheong Tong DB')
            cur = conn.cursor()
            cur.execute("INSERT INTO user VALUES (:user_id, :user_name, :user_email, :role, :password)",
                            {'user_id': user_id.get(), 'user_name': user_name.get(), 'user_email': user_email.get(),
                             'role': role.get(), 'password': password.get()})
            conn.commit()
            messagebox.showinfo('confirmation', 'Record Saved')
        except Exception as ect:
            messagebox.showerror('', str(ect))
    else:
        messagebox.showinfo('message', msg)

    # Show password
def show_password():
    if btn_value.get() == 1:
        password_entry.config(show='')
        con_password_entry.config(show='')
    else:
        password_entry.config(show='*')
        con_password_entry.config(show='*')