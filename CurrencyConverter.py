import re  # import regrex
import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
from PIL import Image, ImageTk
import customtkinter
customtkinter.set_appearance_mode("dark")

class Converter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

        amount = round(amount * self.currencies[to_currency], 4)
        return amount


class CurrencyConverter(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title("ICCOUNTANT - Currency Converter")
        self.currency_converter = converter
        self.configure(background='black')
        self.geometry("550x300")
        self.iconphoto(False, tk.PhotoImage(file="logo_refined.png"))

        # declaring variables
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("Currency")  # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("Currency")  # default value

        # Close button
        self.closeimg = ImageTk.PhotoImage(Image.open('close.png').resize((30, 30), resample=Image.LANCZOS))
        self.close_button = tk.Button(self, image=self.closeimg, bg='#000000', relief='flat', command=lambda : self.destroy())
        self.close_button.pack(anchor=NE)

        # Heading Label
        self.heading_label = Label(self, text ='CURRENCY CONVERTOR', fg='#F2F3F4', bg='black')
        self.heading_label.config(font=tkFont.Font(family='Lato', size=25, weight="bold", slant="italic"))
        self.heading_label.pack()

        # Date Label
        self.date_label = Label(self, text=f"Date : {self.currency_converter.data['date']}", fg='white', bg='black')
        self.date_label.config(font=tkFont.Font(family='Lato', size=15))
        self.date_label.pack(pady=3)

        font = tkFont.Font(family='Lato', size=15, weight="normal", slant="italic")
        self.option_add('*TCombobox*Listbox.font', font)
        # Define the style for combobox widget
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground="red", background="grey")

        # dropdown box for choosing currency
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,
                                                   values=list(self.currency_converter.currencies.keys()), font=font,
                                                   state='readonly', width=12, justify=tk.CENTER, foreground='black')
        self.from_currency_dropdown.pack(side=LEFT, anchor=N, padx=25)

        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,
                                                 values=list(self.currency_converter.currencies.keys()), font=font,
                                                 state='readonly', width=12, justify=tk.CENTER, foreground='black')
        self.to_currency_dropdown.pack(side=RIGHT, anchor=N, padx=25)

        # Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')  # validation on entry value
        self.amount_field = Entry(self, width=12, bd=3, relief=tk.FLAT, justify=tk.CENTER, validate='key',
                                  validatecommand=valid)
        self.amount_field.configure(font=tkFont.Font(family='Lato', size=15, weight="bold", slant="italic"), fg='white',
                                    bg='grey')
        self.amount_field.place(x=30, y=150)

        # to_currecy amount field
        self.converted_amount_field_label = Label(self, relief=tk.FLAT, justify=tk.CENTER, width=11,
                                                  borderwidth=3)
        self.converted_amount_field_label.configure(font=tkFont.Font(family='Lato', size=15, weight="bold",
                                                                     slant="italic"), fg='white', bg='grey')
        self.converted_amount_field_label.place(x=378, y=150)

        # Convert button
        self.convert_button = customtkinter.CTkButton(self, text="Convert", width=50, height=30, text_font=('Lato', 11),
                                                      fg_color="#464E63", hover_color="#667190", command=self.convert)
        self.convert_button.pack(anchor=CENTER, pady=30)

        # Clear button
        self.clear_button = customtkinter.CTkButton(self, text="Clear All", width=50, height=30, text_font=('Lato', 11),
                                                    fg_color="#464E63", hover_color="#667190", command=self.clear_all)
        self.clear_button.pack(anchor=CENTER)


    def close(self):
        self.destroy()

    def clear_all(self):
        self.amount_field.delete(0, END)
        self.converted_amount_field_label.config(text="")
        self.from_currency_variable.set("Currency")
        self.to_currency_variable.set("Currency")

    def convert(self):
        # fetch the values enter by user
        self.amount_field.get()
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()
        # if the entries are empty
        if not self.amount_field.get() or self.from_currency_variable.get() == "Currency" or self.to_currency_variable.get() == "Currency":
            messagebox.showerror('Error', "Please fill in all the fields!")
        else:
            amount = float(self.amount_field.get())
            converted = self.currency_converter.convert
            converted_amount = self.currency_converter.convert(from_curr, to_curr, amount)
            converted_amount = round(converted_amount, 2)
            self.converted_amount_field_label.config(text=str(converted_amount))


    def restrictNumberOnly(self, action, string):
        # compile a regular expression pattern
        regex_pattern = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        # regex pattern in string format
        # Some digits or spaces first: ^[0-9 ]*
        # then, a comma or a point: (\.|,)?
        # Then, some more digits and/or spaces, and the end of the expression: [0-9 ]*$
        result = regex_pattern.match(string)
        return string == "" or (string.count('.') <= 1 and result is not None)


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = Converter(url)

    CurrencyConverter(converter)
    mainloop()