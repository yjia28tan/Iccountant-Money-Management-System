import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import sqlite3
connect = sqlite3.connect('Iccountant.db')
cursor = connect.cursor()
from tkinter import messagebox
import pandas as pd
from datetime import datetime
from tkcalendar import DateEntry

window = Tk()
window.title("ICCOUNTANT")
window.geometry("1280x780")
window.resizable(None, None)
window.state('zoomed')
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
logout = ImageTk.PhotoImage(Image.open('logout.png').resize((160, 30), resample=Image.LANCZOS))
user = ImageTk.PhotoImage(Image.open('user.png').resize((145, 45), resample=Image.LANCZOS))

menuFrame = Frame(window, bg='#000000', width=180, height=window.winfo_height(), highlightbackground='#1A1A1A')
menuFrame.place(x=0, y=0)


def con():
    os.system('CurrencyConverter.py')


def cal():
    os.system('python calculator.py')


def trans():
    Transaction(window)


class Transaction:
    def __init__(self, master):
        # Assign instance to master
        self.master = master
        side_frame = tk.Frame(master, bg='#1A1A1A', width=1100, height=window.winfo_height())
        side_frame.place(x=180, y=0)
        transaction_l = Label(side_frame, font=('lato', 24), bg='#1A1A1A', text='Transaction', fg='white')
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
        self.add_b = tk.Button(side_frame, image=self.transaction_add, bg='#1A1A1A', relief='flat', command=self.add)
        self.add_b.place(x=20, y=60)
        self.edit_b = tk.Button(side_frame, image=self.transaction_edit, bg='#1A1A1A', relief='flat', command=self.edit)
        self.edit_b.place(x=70, y=60)
        self.delete_b = tk.Button(side_frame, image=self.transaction_delete, bg='#1A1A1A', relief='flat',
                                  command=self.delete)
        self.delete_b.place(x=125, y=60)
        self.filter_b = tk.Button(side_frame, image=self.transaction_filter, bg='#1A1A1A', relief='flat',
                                  command=self.filter)
        self.filter_b.place(x=980, y=60)
        self.total_in_l = Label(side_frame, font=('lato', 12), bg='#1A1A1A', text='Total Income: ', fg='lightgreen')
        self.total_in_l.place(x=500, y=65)

        # get total income from database
        cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id = u.user_id AND "
                       "t.type_id = ty.type_id AND t.type_id = 1 AND u.user_id = 1")
        self.total_in_Amount = cursor.fetchall()
        self.total_in_amount = round(float(self.total_in_Amount[0][0]), 2)
        self.total_in_a = Label(side_frame, font=('lato', 12), bg='#1A1A1A', text=str(self.total_in_amount),
                                fg='lightgreen')
        self.total_in_a.place(x=600, y=65)
        self.total_ex = Label(side_frame, font=('lato', 12), bg='#1A1A1A', text='Total Expense: ', fg='red')
        self.total_ex.place(x=725, y=65)

        # get total expense from database
        cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id = u.user_id AND "
                       "t.type_id = ty.type_id AND t.type_id = 2 AND u.user_id = 1")
        self.total_ex_Amount = cursor.fetchall()
        self.total_ex_amount = round(float(self.total_ex_Amount[0][0]), 2)
        self.total_ex_a = Label(side_frame, font=('lato', 12), bg='#1A1A1A', text=str(self.total_ex_amount), fg='red')
        self.total_ex_a.place(x=835, y=65)

        # Transaction List
        self.transaction_frame = Frame(side_frame, bg='#1A1A1A', height=25, width=1050)
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
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Treeview", background="#666666", foreground="black", fieldbackground="#666666",
                             rowheight=30)
        self.style.configure('.', borderwidth=1)
        self.style.map('Treeview', background=[('selected', '#9fc5f8')])
        self.style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        self.transaction_list.tag_configure('oddrow', background='#cccccc')
        self.transaction_list.tag_configure('evenrow', background='#999999')
        self.display_all()


    def display_all(self):
        cursor.execute("SELECT t.date, a.acc_name, c.cat_name, ty.type_name, t.amount, t.remark FROM transactions t, "
                       "account a, category c, type ty, user u WHERE t.acc_id = a.acc_id AND t.cat_id = c.cat_id AND "
                       "t.type_id = ty.type_id AND u.user_id = t.user_id AND t.user_id = 1")
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
                            user = 1

                            # get current date
                            today = datetime.now()

                            # get type id that user input from database
                            cursor.execute("SELECT type_id FROM type WHERE type_name = ?", (self.type_cbox.get(),))
                            self.typeID = cursor.fetchall()
                            self.typeid = self.typeID[0][0]

                            # get account id that user input from database
                            cursor.execute("SELECT a.acc_id FROM account a, user u WHERE a.user_id = u.user_id AND "
                                           "a.user_id = 1 AND a.acc_name = ?", (self.account_cbox.get(),))
                            self.accountID = cursor.fetchall()
                            self.accountid = self.accountID[0][0]

                            # get category id that user input from database
                            cursor.execute("SELECT c.cat_id FROM category c, user u WHERE c.user_id = u.user_id AND"
                                           " c.user_id = 1 AND c.cat_name = ?", (self.category_cbox.get(),))
                            self.categoryID = cursor.fetchall()
                            self.categoryid = self.categoryID[0][0]

                            # insert the data that user input to database
                            cursor.execute("INSERT INTO transactions (trans_id, amount, date, remark, user_id, type_id,"
                                           " acc_id, cat_id) VALUES (?,?,?,?,?,?,?,?)",
                                           (self.ID, self.amount, today.strftime("%Y-%m-%d"),
                                            self.remark_entry.get(), user, self.typeid, self.accountid,
                                            self.categoryid))
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
                                           " u.user_id AND t.type_id = ty.type_id AND t.type_id = 1 AND u.user_id = 1")
                            self.total_in_Amount = cursor.fetchall()
                            self.total_in_amount = round(float(self.total_in_Amount[0][0]), 2)
                            self.total_in_a.config(text=str(self.total_in_amount))

                            # get total expense from database
                            cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id ="
                                           " u.user_id AND t.type_id = ty.type_id AND t.type_id = 2 AND u.user_id = 1")
                            self.total_ex_Amount = cursor.fetchall()
                            self.total_ex_amount = round(float(self.total_ex_Amount[0][0]), 2)
                            self.total_ex_a.config(text=str(self.total_ex_amount))

                        except ValueError:
                            messagebox.showerror('Error', 'Please reenter the amount in number.')
                            self.root.destroy()

    def add(self):
        self.root = Toplevel()
        self.root.geometry("425x215")
        self.root.title("Iccountant - Add New Transaction")
        self.root.configure(bg='#1A1A1A')
        self.title_l = Label(self.root, font=('lato', 15), bg='#1A1A1A', text='New Transaction', fg='white')
        self.title_l.grid(row=0, column=0)
        self.account_l = Label(self.root, font=('lato', 12), bg='#1A1A1A', text='Account :', fg='white')
        self.account_l.grid(row=1, column=0)
        self.account_get = pd.read_sql_query("SELECT a.acc_name AS Account FROM transactions t, account a, user u WHERE"
                                             " a.acc_id = t.acc_id AND u.user_id = t.user_id AND t.user_id = 1 GROUP BY"
                                             " t.acc_id", connect)
        self.account_df = pd.DataFrame(self.account_get)
        self.account_list = self.account_df['Account'].values.tolist()
        self.account_cbox = ttk.Combobox(self.root, values=self.account_list, font=('lato', 12), state='readonly',
                                         justify='center')
        self.account_cbox.grid(row=1, column=1)
        self.account_cbox.set("Select Account")
        self.category_l = Label(self.root, font=('lato', 12), bg='#1A1A1A', text='Category :', fg='white')
        self.category_l.grid(row=2, column=0)
        self.category_get = pd.read_sql_query("SELECT c.cat_name AS Category FROM category c, transactions t, user u "
                                              "WHERE c.cat_id = t.cat_id AND t.user_id = u.user_id AND u.user_id = 1 "
                                              "GROUP BY t.cat_id", connect)
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
        # validate input
        if self.amount_entry.get() == '':
            messagebox.showerror('Error', 'Please enter an amount.')
            self.root.destroy()
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
                               "a.user_id = 1 AND a.acc_name = ?", (self.account_cbox.get(),))
                self.accountID = cursor.fetchall()
                self.accountid = self.accountID[0][0]

                # get the category id that user input from the database
                cursor.execute("SELECT c.cat_id FROM category c, user u WHERE c.user_id = u.user_id AND"
                               " c.user_id = 1 AND c.cat_name = ?", (self.category_cbox.get(),))
                self.categoryID = cursor.fetchall()
                self.categoryid = self.categoryID[0][0]
                user=1

                # update transaction table in database
                cursor.execute("UPDATE transactions SET amount= ?, date = ?, remark = ?, user_id = ?, type_id = ?, "
                               "acc_id = ?, cat_id = ? WHERE trans_id = ?",
                               (self.amount_entry.get(), self.date_entry.get(), self.remark_entry.get(), user,
                                self.typeid, self.accountid, self.categoryid, self.transid, ))
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
                cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id ="
                               " u.user_id AND t.type_id = ty.type_id AND t.type_id = 1 AND u.user_id = 1")
                self.total_in_Amount = cursor.fetchall()
                self.total_in_amount = round(float(self.total_in_Amount[0][0]), 2)
                self.total_in_a.config(text=str(self.total_in_amount))

                # get total expense from database
                cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id ="
                               " u.user_id AND t.type_id = ty.type_id AND t.type_id = 2 AND u.user_id = 1")
                self.total_ex_Amount = cursor.fetchall()
                self.total_ex_amount = round(float(self.total_ex_Amount[0][0]), 2)
                self.total_ex_a.config(text=str(self.total_ex_amount))

            except ValueError:
                messagebox.showerror('Error', 'Please reenter the amount in number.')
                self.root.destroy()

    def edit(self):
        # if the user did not select a row in the treeview
        if not self.transaction_list.selection():
            messagebox.showerror("Error", "Please select a row to edit.")
        else:

            # get the value of the selected row
            selected = self.transaction_list.focus()
            values = self.transaction_list.item(selected)
            selection = values["values"]
            user = 1
            cursor.execute("SELECT t.trans_id FROM transactions t, type ty, account a, category c WHERE ty.type_id = "
                           "t.type_id AND a.acc_id = t.acc_id AND c.cat_id = t.cat_id AND t.amount= ? AND t.date = ? "
                           "AND t.remark = ? AND t.user_id = ? AND ty.type_name = ? AND a.acc_name = ? AND c.cat_name ="
                           " ?", (selection[4], selection[0], selection[5], user, selection[3], selection[1],
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
                                                 "WHERE a.acc_id = t.acc_id AND u.user_id = t.user_id AND t.user_id = 1"
                                                 " GROUP BY t.acc_id", connect)
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
                                                  "= 1 GROUP BY t.cat_id", connect)
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
                user = 1

                # get account amount that selected
                self.account_amount = selection[4]

                # get the transaction id of the selected row from the database
                cursor.execute("SELECT t.trans_id FROM transactions t, type ty, account a, category c WHERE ty.type_id "
                               "= t.type_id AND a.acc_id = t.acc_id AND c.cat_id = t.cat_id AND t.amount= ? AND t.date "
                               "= ? AND t.remark = ? AND t.user_id = ? AND ty.type_name = ? AND a.acc_name = ? AND "
                               "c.cat_name = ?", (selection[4], selection[0], selection[5], user, selection[3],
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
                cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id ="
                               " u.user_id AND t.type_id = ty.type_id AND t.type_id = 1 AND u.user_id = 1")
                self.total_in_Amount = cursor.fetchall()
                self.total_in_amount = round(float(self.total_in_Amount[0][0]), 2)
                self.total_in_a.config(text=str(self.total_in_amount))

                # get total expense from database
                cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id ="
                               " u.user_id AND t.type_id = ty.type_id AND t.type_id = 2 AND u.user_id = 1")
                self.total_ex_Amount = cursor.fetchall()
                self.total_ex_amount = round(float(self.total_ex_Amount[0][0]), 2)
                self.total_ex_a.config(text=str(self.total_ex_amount))

    def sort(self):
        # verify conditions to filter out data
        # query to display the transaction with condition in the treeview
        self.query = "SELECT t.date, a.acc_name, c.cat_name, ty.type_name, t.amount, t.remark FROM transactions t, " \
                     "account a, category c, type ty, user u WHERE t.acc_id = a.acc_id AND t.cat_id = c.cat_id AND " \
                     "t.type_id = ty.type_id AND t.user_id = u.user_id AND t.user_id = 1 "

        # query to get the total income amount
        self.query1 = "SELECT sum(t.amount) FROM transactions t, account a, category c, type ty, user u WHERE " \
                      "t.acc_id = a.acc_id AND t.cat_id = c.cat_id AND t.type_id = ty.type_id AND t.user_id = " \
                      "u.user_id AND t.type_id = 1 AND t.user_id = 1 "

        # query to get the total expense amount
        self.query2 = "SELECT sum(t.amount) FROM transactions t, account a, category c, type ty, user u WHERE " \
                      "t.acc_id = a.acc_id AND t.cat_id = c.cat_id AND t.type_id = ty.type_id AND t.user_id = " \
                      "u.user_id AND t.type_id = 2 AND t.user_id = 1 "

        # a list to store the condition variable
        self.variable_list = []

        # verify the condition
        if self.account_cbox.get() == 'None':
            pass
        else:
            # get the account id that user input
            cursor.execute("SELECT a.acc_id FROM account a, user u WHERE a.user_id = u.user_id AND a.user_id = 1 AND "
                           "a.acc_name = ?", (self.account_cbox.get(),))
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
            cursor.execute("SELECT c.cat_id FROM category c, user u WHERE c.user_id = u.user_id AND c.user_id = 1 AND "
                           "c.cat_name = ?", (self.category_cbox.get(),))
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
            cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id = u.user_id AND "
                           "t.type_id = ty.type_id AND t.type_id = 1 AND u.user_id = 1")
            self.total_in_Amount = cursor.fetchall()
            self.total_in_amount = round(float(self.total_in_Amount[0][0]), 2)
            self.total_in_a.config(text=str(self.total_in_amount))

            # get total expense from database
            cursor.execute("SELECT sum(t.amount) FROM transactions t, user u, type ty WHERE t.user_id = u.user_id AND "
                           "t.type_id = ty.type_id AND t.type_id = 2 AND u.user_id = 1")
            self.total_ex_Amount = cursor.fetchall()
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

            # get total expense from database
            cursor.execute(self.query2, (var0,))
            self.total_ex_Amount = cursor.fetchall()
        except:
            try:
                cursor.execute(self.query, (var0, var1,))
                self.rows = cursor.fetchall()

                # get total income from database
                cursor.execute(self.query1, (var0, var1,))
                self.total_in_Amount = cursor.fetchall()

                # get total expense from database
                cursor.execute(self.query2, (var0, var1,))
                self.total_ex_Amount = cursor.fetchall()
            except:
                try:
                    cursor.execute(self.query, (var0, var1, var2,))
                    self.rows = cursor.fetchall()

                    # get total income from database
                    cursor.execute(self.query1, (var0, var1,))
                    self.total_in_Amount = cursor.fetchall()

                    # get total expense from database
                    cursor.execute(self.query2, (var0, var1,))
                    self.total_ex_Amount = cursor.fetchall()
                except:
                    try:
                        cursor.execute(self.query, (var0, var1, var3,))
                        self.rows = cursor.fetchall()

                        # get total income from database
                        cursor.execute(self.query1, (var0, var1, var3,))
                        self.total_in_Amount = cursor.fetchall()

                        # get total expense from database
                        cursor.execute(self.query2, (var0, var1, var3,))
                        self.total_ex_Amount = cursor.fetchall()
                    except:
                        try:
                            cursor.execute(self.query, (var0, var1, var3, var4,))
                            self.rows = cursor.fetchall()

                            # get total income from database
                            cursor.execute(self.query1, (var0, var1, var3, var4,))
                            self.total_in_Amount = cursor.fetchall()

                            # get total expense from database
                            cursor.execute(self.query2, (var0, var1, var3, var4,))
                            self.total_ex_Amount = cursor.fetchall()
                        except:
                            pass
        self.total_in_amount = round(float(self.total_in_Amount[0][0]), 2)
        self.total_in_a.config(text=str(self.total_in_amount))
        self.total_ex_amount = round(float(self.total_ex_Amount[0][0]), 2)
        self.total_ex_a.config(text=str(self.total_ex_amount))

        # loop to display the transaction with the condition in treeview
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
                                             "WHERE a.acc_id = t.acc_id AND u.user_id = t.user_id AND t.user_id = 1"
                                             " GROUP BY t.acc_id", connect)
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
                                              "= 1 GROUP BY t.cat_id", connect)
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
                                          "u.user_id = t.user_id AND t.user_id = 1 GROUP BY strftime('%Y', t.date)",
                                          connect)
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


# Defining the buttons for menu bar in Home page
logo_l = Label(menuFrame, image=logo, bg='#000000').grid(row=1)
dashboard_b = Button(menuFrame, image=dashboard, bg='#000000', relief='flat').grid(row=2)
statistic_b = Button(menuFrame, image=statistic, bg='#000000', relief='flat').grid(row=3)
transaction_b = Button(menuFrame, image=transaction, bg='#000000', relief='flat', command=trans).grid(row=4)
category_b = Button(menuFrame, image=category, bg='#000000', relief='flat').grid(row=5)
account_b = Button(menuFrame, image=account, bg='#000000', relief='flat').grid(row=6)
currency_b = Button(menuFrame, image=currency, bg='#000000', relief='flat', command=con).grid(row=7)
calculator_b = Button(menuFrame, image=calculator, bg='#000000', relief='flat', command=cal).grid(row=8)
customer_b = Button(menuFrame, image=customer, bg='#000000', relief='flat').grid(row=9)
tips_b = Button(menuFrame, image=tips, bg='#000000', relief='flat').grid(row=10)
logout_b = Button(menuFrame, image=logout, bg='#000000', relief='flat').place(x=1, y=570)
user_b = Button(menuFrame, image=user, bg='#000000', relief='flat').place(x=10, y=610)

# So that it does not depend on the widgets inside the frame
menuFrame.grid_propagate(False)
Transaction(window)
window.mainloop()
