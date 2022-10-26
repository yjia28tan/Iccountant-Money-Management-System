import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("ICCOUNTANT")
window.geometry("1920x2080")
window.resizable(0, 0)
window.state('zoomed')
window.resizable(True, True)
window.iconphoto(False, tk.PhotoImage(file="logo_refined.png"))
window.configure(bg='#1A1A1A')

# Define and resize the icons to be shown in Menu bar
logo = ImageTk.PhotoImage(Image.open('logo_small.png').resize((165, 58), resample=Image.LANCZOS))
dashboard = ImageTk.PhotoImage(Image.open('Dashboard.png').resize((160, 30), resample=Image.LANCZOS))
statistic = ImageTk.PhotoImage(Image.open('Chart.png').resize((160, 30), resample=Image.LANCZOS))
transaction = ImageTk.PhotoImage(Image.open('transaction.png').resize((160, 30), resample=Image.LANCZOS))
category = ImageTk.PhotoImage(Image.open('category.png').resize((160, 30), resample=Image.LANCZOS))
account = ImageTk.PhotoImage(Image.open('accounts.png').resize((160, 30), resample=Image.LANCZOS))
currency = ImageTk.PhotoImage(Image.open('currency.png').resize((160, 30), resample=Image.LANCZOS))
calculator = ImageTk.PhotoImage(Image.open('calculator.png').resize((160, 30), resample=Image.LANCZOS))
customer = ImageTk.PhotoImage(Image.open('QNA.png').resize((160, 30), resample=Image.LANCZOS))
tips = ImageTk.PhotoImage(Image.open('tips.png').resize((160, 30), resample=Image.LANCZOS))
user = ImageTk.PhotoImage(Image.open('user.png').resize((145, 45), resample=Image.LANCZOS))


menuFrame = Frame(window, bg='#000000', width=180, height=window.winfo_height(), highlightbackground='#1A1A1A')
menuFrame.place(x=0, y=0)

# Defining the buttons for menu bar in Home page
logo_l = Label(menuFrame, image=logo, bg='#000000').grid(row=1)
dashboard_b = Button(menuFrame, image=dashboard, bg='#000000', relief='flat').grid(row=2)
statistic_b = Button(menuFrame, image=statistic, bg='#000000', relief='flat').grid(row=3)
transaction_b = Button(menuFrame, image=transaction, bg='#000000', relief='flat').grid(row=4)
category_b = Button(menuFrame, image=category, bg='#000000', relief='flat').grid(row=5)
account_b = Button(menuFrame, image=account, bg='#000000', relief='flat').grid(row=6)
currency_b = Button(menuFrame, image=currency, bg='#000000', relief='flat').grid(row=7)
calculator_b = Button(menuFrame, image=calculator, bg='#000000', relief='flat').grid(row=8)
customer_b = Button(menuFrame, image=customer, bg='#000000', relief='flat').grid(row=9)
tips_b = Button(menuFrame, image=tips, bg='#000000', relief='flat').grid(row=10)
user_b = Button(menuFrame, image=user, bg='#000000', relief='flat').place(x=15, y=720)

# Bind to the frame, if centered or left
menuFrame.bind('<Enter>')
menuFrame.bind('<Leave>')

# So that it does not depend on the widgets inside the frame
menuFrame.grid_propagate(False)

window.mainloop()
