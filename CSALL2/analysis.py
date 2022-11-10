import sqlite3
conn = sqlite3.connect('Poh Cheong Tong DB')
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical
import matplotlib.pyplot as plt  # Built-in Matplotlib
import seaborn as sns  # For graphical
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import datetime
from datetime import timedelta
from tkcalendar import Calendar, DateEntry
import re
from tkinter import messagebox

window = Tk()
window.state("zoomed")
window.title("Poh Cheong Tong Medical Hall System")
window.configure(bg='#DFEEFF')

page1 = Frame(window)  # Log-in
page2 = Frame(window)  # Home
page3 = Frame(window)  # Inventory
page4 = Frame(window)  # Billing
page5 = Frame(window)  # Analysis
page6 = Frame(window)  # Register

for frame in (page1, page2, page3, page4, page5, page6):
    frame.grid(row=0, column=0, sticky='nsew')


def show_frame(frame):
    frame.tkraise()


# ========== Create the menubar ===========
min_w = 70  # Minimum width of the frame
max_w = 145  # Maximum width of the frame
cur_width = min_w  # Increasing width of the frame
expanded = False  # Check if it is completely expanded


def expandForHome():
    global cur_width, expanded
    cur_width += 10  # Increase the width by 10
    rep = window.after(5, expandForHome)  # Repeat this func every 5 ms
    frame.config(width=cur_width)  # Change the width to new increase width
    if cur_width >= max_w:  # If width is greater than maximum width
        expanded = True  # Frame is expended
        window.after_cancel(rep)  # Stop repeating the function
        fillForHome()


def contractForHome():
    global cur_width, expanded
    cur_width -= 10  # Reduce the width by 10
    rep = window.after(5, contractForHome)  # Call this func every 5 ms
    frame.config(width=cur_width)  # Change the width to new reduced width
    if cur_width <= min_w:  # If it is back to normal width
        expanded = False  # Frame is not expanded
        window.after_cancel(rep)  # Stop repeating the function
        fillForHome()


def fillForHome():
    if expanded:  # If the frame is expanded
        # Show the label, and remove the image
        logout_b.config(text='Log-Out', image='', font=('Lucida Fax', 12), fg=('#EFE2E2'))
        home_b.config(text='Home', image='', font=('Lucida Fax', 12), fg=('#EFE2E2'))
        billing_b.config(text='Billing', image='', font=('Lucida Fax', 12), fg=('#EFE2E2'))
        inventory_b.config(text='Inventory', image='', font=('Lucida Fax', 12), fg=('#EFE2E2'))
        analysis_b.config(text='Analysis', image='', font=('Lucida Fax', 12), fg=('#EFE2E2'))
        userInfo_b.config(text='User Info', image='', font=('Lucida Fax', 12), fg=('#EFE2E2'))
        register_b.config(text='Register\n New User', image='', font=('Lucida Fax', 12), fg=('#EFE2E2'))
    else:
        # Bring the image back
        logout_b.config(image=logout, font=(0, 30))
        home_b.config(image=home, font=(0, 30))
        billing_b.config(image=billing, font=(0, 30))
        inventory_b.config(image=inventory, font=(0, 30))
        analysis_b.config(image=analysis, font=(0, 30))
        userInfo_b.config(image=userInfo, font=(0, 30))
        register_b.config(image=register, font=(0, 30))


def MouseScrollWheel(event):
    scrollbar.yview("scroll", event.delta, "units")
    return "break"

# Current Date Chart that show when open sales report
def bar():
    # Current date and time
    date = datetime.datetime.now()
    year_choose = date.strftime('%Y')
    month_choose = date.strftime('%m')
    day_choose = date.strftime('%d')
    # Get data from database
    Bar_Month_Select = pd.read_sql_query("SELECT i.total AS 'Revenue', SUM((p.sell_price - p.buy_price)*i.quantity) AS "
                                         "'Profit' FROM invoice i, product p WHERE i.pro_id = p.pro_id AND strftime("
                                         "'%Y', i.date) = '{}' AND strftime('%m', i.date) = '{}' AND strftime('%d', "
                                         "i.date) = '{}' GROUP BY invoice_id".format(year_choose, month_choose,
                                                                                     day_choose), conn)
    # Change to float
    Bar_Month_Select["Profit"] = Bar_Month_Select["Profit"].astype(float)
    Bar_Month_Select["Revenue"] = Bar_Month_Select["Revenue"].astype(float)
    # Sum up the data value
    Bar_Month_s = Bar_Month_Select['Revenue'].sum()
    Bar_m_s = Bar_Month_Select['Profit'].sum()
    # Set to two decimal place
    R = '{:.2f}'.format(Bar_Month_s)
    P = '{:.2f}'.format(Bar_m_s)
    previous_day = int(day_choose) - 1
    Bar_PMonth_Select = pd.read_sql_query("SELECT i.total AS 'Revenue', SUM((p.sell_price - p.buy_price)*i.quantity) AS"
                                          " 'Profit' FROM invoice i, product p WHERE i.pro_id = p.pro_id AND strftime("
                                          "'%Y', i.date) = '{}' AND strftime('%m', i.date) = '{}' AND strftime('%d', "
                                          "i.date) = '{}' GROUP BY invoice_id".format(year_choose, month_choose,
                                                                                      previous_day), conn)
    Bar_PMonth_Select["Profit"] = Bar_PMonth_Select["Profit"].astype(float)
    Bar_PMonth_Select["Revenue"] = Bar_PMonth_Select["Revenue"].astype(float)
    Bar_PMonth_s = Bar_PMonth_Select['Revenue'].sum()
    Bar_Pm_s = Bar_PMonth_Select['Profit'].sum()
    PR = '{:.2f}'.format(Bar_PMonth_s)
    PP = '{:.2f}'.format(Bar_Pm_s)
    # Form data frame
    data = {'Day': {0: previous_day, 1: int(day_choose)}, 'Revenue': {0: PR, 1: R}, 'Profit': {0: PP, 1: P}}
    b_m_s = pd.DataFrame(data)
    dfl = (b_m_s.melt(id_vars='Day', var_name='Sales', value_name='RM').sort_values('RM', ascending=True)
           .reset_index(drop=True).sort_values('Day', ascending=True))
    dfl['RM'] = dfl['RM'].astype(str).astype(float)
    # Plot bar chart
    fig, ax = plt.subplots(figsize=(7, 5), dpi=100)
    plot = sns.barplot(x='Day', y='RM', data=dfl, hue='Sales', palette="Pastel1", ci=None)
    for c in ax.containers:
        ax.bar_label(c, fmt='%.2f')
    plot.set_ylabel("RM", fontsize=15)
    plot.set_xlabel("Day", fontsize=15)
    plot.set_title("Revenue and Profit Bar Chart in Day", fontsize=21)
    # Convert chart to figure
    canv = FigureCanvasTkAgg(fig, master=scroll_frame)
    canv.draw()
    canv.get_tk_widget().pack(padx=180, pady=100)
    # Add toolbar for the chart
    toolba = NavigationToolbar2Tk(canv, scroll_frame)
    toolba.update()
    toolba.place(x=740, y=1150)


# Pie Product Sold Day
def pie_product():
    date = datetime.datetime.now()
    year_choose = date.strftime('%Y')
    month_choose = date.strftime('%m')
    day_choose = date.strftime('%d')
    Sold_Day = pd.read_sql_query("SELECT p.product_name AS 'Product Name', sum(i.quantity) AS 'Quantity' FROM "
                                 "invoice i JOIN product p ON p.pro_id = i.pro_id WHERE strftime('%Y', i.date) IN "
                                 "('{}') AND strftime('%m', i.date) IN ('{}') AND strftime('%d', i.date) IN ('{}') "
                                 "GROUP BY i.pro_id".format(year_choose, month_choose, day_choose), conn)
    datframe = pd.DataFrame(Sold_Day)
    sold_day_pro = datframe['Product Name'].values.tolist()
    sold_day_quan = datframe['Quantity'].values.tolist()
    colors = sns.color_palette("Pastel1")
    pie_product_day = plt.figure(figsize=(5, 5), dpi=100)
    plt.pie(sold_day_quan, labels=sold_day_pro, autopct='%1.1f%%', colors=colors)
    plt.title("Product Sold in Day", fontsize=18)
    can = FigureCanvasTkAgg(pie_product_day, master=scroll_frame)
    can.draw()
    can.get_tk_widget().pack(padx=180, pady=100)
    toolb = NavigationToolbar2Tk(can, scroll_frame)
    toolb.update()
    toolb.place(x=740, y=2350)


# Pie Category Sold
def pie_category():
    date = datetime.datetime.now()
    year_choose = date.strftime('%Y')
    month_choose = date.strftime('%m')
    day_choose = date.strftime('%d')
    Sold_Cat_Day = pd.read_sql_query("SELECT c.cat_name AS 'Category', SUM(i.quantity) AS 'Quantity' FROM category "
                                     "c, invoice i, product p WHERE i.pro_id = p.pro_id AND p.cat_id = c.cat_id AND"
                                     " strftime('%Y', i.date) IN ('{}') AND strftime('%m', i.date) IN ('{}') AND "
                                     "strftime('%d', i.date) IN ('{}') GROUP BY c.cat_id"
                                     .format(year_choose, month_choose, day_choose), conn)
    datafram = pd.DataFrame(Sold_Cat_Day)
    sold_cat_day = datafram['Category'].values.tolist()
    sold_cat_day_quan = datafram['Quantity'].values.tolist()
    colors = sns.color_palette("Pastel1")
    pie_category_day = plt.figure(figsize=(5, 5), dpi=100)
    plt.pie(sold_cat_day_quan, labels=sold_cat_day, autopct='%1.1f%%', colors=colors)
    plt.title("Product Sold in Category in Day", fontsize=18)
    ca = FigureCanvasTkAgg(pie_category_day, master=scroll_frame)
    ca.draw()
    ca.get_tk_widget().pack(padx=180, pady=100)
    tool = NavigationToolbar2Tk(ca, scroll_frame)
    tool.update()
    tool.place(x=740, y=3550)


def sort_year():
    def sales_year():
        # Clear anything that on the frame
        for widget in scroll_frame.winfo_children():
            widget.destroy()
        year_choose = year_chosen.get()
        # Sales Bar Year
        Bar_Month_Select = pd.read_sql_query("SELECT i.total AS 'Revenue', SUM((p.sell_price - p.buy_price)*i.quantity)"
                                             " AS 'Profit' FROM invoice i, product p WHERE i.pro_id = p.pro_id AND "
                                             "strftime ('%Y', i.date) = '{}' GROUP BY invoice_id".format(year_choose),
                                             conn)
        Bar_Month_Select["Profit"] = Bar_Month_Select["Profit"].astype(float)
        Bar_Month_Select["Revenue"] = Bar_Month_Select["Revenue"].astype(float)
        Bar_Month_s = Bar_Month_Select['Revenue'].sum()
        Bar_m_s = Bar_Month_Select['Profit'].sum()
        R = '{:.2f}'.format(Bar_Month_s)
        P = '{:.2f}'.format(Bar_m_s)
        Bar_PMonth_Select = pd.read_sql_query("SELECT i.total AS 'Revenue', SUM((p.sell_price - p.buy_price)*"
                                              "i.quantity) AS 'Profit' FROM invoice i, product p WHERE i.pro_id = "
                                              "p.pro_id AND strftime ('%Y', i.date) = '{}' GROUP BY invoice_id".format
                                              (int(year_choose) - 1), conn)
        Bar_PMonth_Select["Profit"] = Bar_PMonth_Select["Profit"].astype(float)
        Bar_PMonth_Select["Revenue"] = Bar_PMonth_Select["Revenue"].astype(float)
        Bar_PMonth_s = Bar_PMonth_Select['Revenue'].sum()
        Bar_Pm_s = Bar_PMonth_Select['Profit'].sum()
        PR = '{:.2f}'.format(Bar_PMonth_s)
        PP = '{:.2f}'.format(Bar_Pm_s)
        data = {'Year': {0: int(year_choose) - 1, 1: int(year_choose)}, 'Revenue': {0: PR, 1: R},
                'Profit': {0: PP, 1: P}}
        b_m_s = pd.DataFrame(data)
        dfl = (b_m_s.melt(id_vars='Year', var_name='Sales', value_name='RM').sort_values('RM', ascending=False).
               reset_index(drop=True).sort_values('Year', ascending=True))
        dfl['RM'] = dfl['RM'].astype(str).astype(float)
        fig, ax = plt.subplots(figsize=(7, 5), dpi=100)
        plot = sns.barplot(x='Year', y='RM', data=dfl, hue='Sales', palette="Pastel1", ci=None)
        for c in ax.containers:
            plot.bar_label(c, fmt='%.2f')
        plot.set_ylabel("RM", fontsize=15)
        plot.set_xlabel("Year", fontsize=15)
        plot.set_title("Revenue and Profit Bar Chart in Year", fontsize=21)
        canv = FigureCanvasTkAgg(fig, master=scroll_frame)
        canv.draw()
        canv.get_tk_widget().pack(padx=180, pady=100)
        toolba = NavigationToolbar2Tk(canv, scroll_frame)
        toolba.update()
        toolba.place(x=740, y=1150)
        # Pie Product Sold Year
        Sold_Year = pd.read_sql_query("SELECT p.product_name AS 'Product Name', sum(i.quantity) AS 'Quantity' FROM "
                                      "invoice i JOIN product p ON p.pro_id = i.pro_id WHERE strftime('%Y', i.date) IN "
                                      "('{}') GROUP BY i.pro_id".format(year_choose), conn)
        dframe = pd.DataFrame(Sold_Year)
        sold_year_pro = dframe['Product Name'].values.tolist()
        sold_year_quan = dframe['Quantity'].values.tolist()
        colors = sns.color_palette("Pastel1")
        pie_product_year = plt.figure(figsize=(5, 5), dpi=100)
        plt.pie(sold_year_quan, labels=sold_year_pro, autopct='%1.1f%%', colors=colors)
        plt.title("Product Sold in Year", fontsize=18)
        can = FigureCanvasTkAgg(pie_product_year, master=scroll_frame)
        can.draw()
        can.get_tk_widget().pack(padx=180, pady=100)
        toolb = NavigationToolbar2Tk(can, scroll_frame)
        toolb.update()
        toolb.place(x=740, y=2350)
        # Pie Category Sold Year
        Sold_Cat_Year = pd.read_sql_query("SELECT c.cat_name AS 'Category', SUM(i.quantity) AS 'Quantity' FROM category"
                                          " c, invoice i, product p WHERE i.pro_id = p.pro_id AND p.cat_id = c.cat_id "
                                          "AND strftime('%Y', i.date) IN ('{}') GROUP BY c.cat_id".format(year_choose),
                                          conn)
        datafr = pd.DataFrame(Sold_Cat_Year)
        sold_cat_year = datafr['Category'].values.tolist()
        sold_cat_year_quan = datafr['Quantity'].values.tolist()
        colors = sns.color_palette("Pastel1")
        pie_category_year = plt.figure(figsize=(5, 5), dpi=100)
        plt.pie(sold_cat_year_quan, labels=sold_cat_year, autopct='%1.1f%%', colors=colors)
        plt.title("Product Sold in Category in Year", fontsize=18)
        ca = FigureCanvasTkAgg(pie_category_year, master=scroll_frame)
        ca.draw()
        ca.get_tk_widget().pack(padx=180, pady=100)
        tool = NavigationToolbar2Tk(ca, scroll_frame)
        tool.update()
        tool.place(x=740, y=3550)
        # Destroy the pop up window
        year_window.destroy()

    # Create pop up window
    year_window = Toplevel(window)
    year_window.geometry("450x225")
    year_window.title("Sales Report in Year")
    year_window.configure(bg='#DFEEFF')
    year_label = Label(year_window, text='Choose a year', font=('Arial', 15), bg='#DFEEFF')
    year_label.pack(pady=20)
    # Get list value from database
    year_value = pd.read_sql_query("SELECT strftime('%Y', date) AS Year FROM invoice GROUP BY strftime('%Y', date)",
                                   conn)
    year_df = pd.DataFrame(year_value)
    year_list = year_df['Year'].values.tolist()
    year_chosen = ttk.Combobox(year_window, width=27, values=year_list, font=('Arial', 12))
    year_chosen.set(datetime.datetime.now().year)
    year_chosen.pack(pady=10)
    Button(year_window, text='Confirm', font=('Arial', 15), command=sales_year).pack(pady=20)


def sort_month():
    def sales_month():
        for widget in scroll_frame.winfo_children():
            widget.destroy()
        year_choose = year_chosen.get()
        month_choose = month_chosen.get()
        # Sales Bar Month
        Bar_Month_Select = pd.read_sql_query("SELECT i.total AS 'Revenue', SUM((p.sell_price - p.buy_price)*i.quantity)"
                                             " AS 'Profit' FROM invoice i, product p WHERE i.pro_id = p.pro_id AND "
                                             "strftime('%Y', i.date) = '{}' AND strftime('%m', i.date) = '{}' GROUP "
                                             "BY invoice_id".format(year_choose, month_choose), conn)
        Bar_Month_Select["Profit"] = Bar_Month_Select["Profit"].astype(float)
        Bar_Month_Select["Revenue"] = Bar_Month_Select["Revenue"].astype(float)
        Bar_Month_s = Bar_Month_Select['Revenue'].sum()
        Bar_m_s = Bar_Month_Select['Profit'].sum()
        R = '{:.2f}'.format(Bar_Month_s)
        P = '{:.2f}'.format(Bar_m_s)
        index = month_list.index(month_choose) - 1
        Bar_PMonth_Select = pd.read_sql_query("SELECT i.total AS 'Revenue', SUM((p.sell_price - p.buy_price)*"
                                              "i.quantity) AS 'Profit' FROM invoice i, product p WHERE i.pro_id = "
                                              "p.pro_id AND strftime('%Y', i.date) = '{}' AND strftime('%m', i.date) = "
                                              "'{}' GROUP BY invoice_id".format(year_choose, month_list[index]), conn)
        Bar_PMonth_Select["Profit"] = Bar_PMonth_Select["Profit"].astype(float)
        Bar_PMonth_Select["Revenue"] = Bar_PMonth_Select["Revenue"].astype(float)
        Bar_PMonth_s = Bar_PMonth_Select['Revenue'].sum()
        Bar_Pm_s = Bar_PMonth_Select['Profit'].sum()
        PR = '{:.2f}'.format(Bar_PMonth_s)
        PP = '{:.2f}'.format(Bar_Pm_s)
        data = {'Month': {0: month_list[index], 1: month_choose}, 'Revenue': {0: PR, 1: R}, 'Profit': {0: PP, 1: P}}
        b_m_s = pd.DataFrame(data)
        dfl = (b_m_s.melt(id_vars='Month', var_name='Sales', value_name='RM').sort_values('RM', ascending=True)
               .reset_index(drop=True).sort_values('Month', ascending=True))
        dfl['RM'] = dfl['RM'].astype(str).astype(float)
        fig, ax = plt.subplots(figsize=(7, 5), dpi=100)
        plot = sns.barplot(x='Month', y='RM', data=dfl, hue='Sales', palette="Pastel1", ci=None)
        for c in ax.containers:
            ax.bar_label(c, fmt='%.2f')
        plot.set_ylabel("RM", fontsize=15)
        plot.set_xlabel("Month", fontsize=15)
        plot.set_title("Revenue and Profit Bar Chart in Month", fontsize=21)
        canv = FigureCanvasTkAgg(fig, master=scroll_frame)
        canv.draw()
        canv.get_tk_widget().pack(padx=180, pady=100)
        toolba = NavigationToolbar2Tk(canv, scroll_frame)
        toolba.update()
        toolba.place(x=740, y=1150)
        # Pie Product Sold Month
        Sold_Month = pd.read_sql_query("SELECT p.product_name AS 'Product Name', sum(i.quantity) AS 'Quantity' FROM "
                                       "invoice i JOIN product p ON p.pro_id = i.pro_id WHERE strftime('%Y', i.date) IN"
                                       " ('{}') AND strftime('%m', i.date) IN ('{}') GROUP BY i.pro_id".format
                                       (year_choose, month_choose), conn)
        daframe = pd.DataFrame(Sold_Month)
        sold_month_pro = daframe['Product Name'].values.tolist()
        sold_month_quan = daframe['Quantity'].values.tolist()
        colors = sns.color_palette("Pastel1")
        pie_product_month = plt.figure(figsize=(5, 5), dpi=100)
        plt.pie(sold_month_quan, labels=sold_month_pro, autopct='%1.1f%%', colors=colors)
        plt.title("Product Sold in Month", fontsize=18)
        can = FigureCanvasTkAgg(pie_product_month, master=scroll_frame)
        can.draw()
        can.get_tk_widget().pack(padx=180, pady=100)
        toolb = NavigationToolbar2Tk(can, scroll_frame)
        toolb.update()
        toolb.place(x=740, y=2350)
        # Pie Category Sold Month
        Sold_Cat_Month = pd.read_sql_query("SELECT c.cat_name AS 'Category', SUM(i.quantity) AS 'Quantity' FROM "
                                           "category c, invoice i, product p WHERE i.pro_id = p.pro_id AND p.cat_id = "
                                           "c.cat_id AND strftime('%Y', i.date) IN ('{}') AND strftime('%m', i.date) IN"
                                           " ('{}') GROUP BY c.cat_id".format(year_choose, month_choose), conn)
        datafra = pd.DataFrame(Sold_Cat_Month)
        sold_cat_month = datafra['Category'].values.tolist()
        sold_cat_month_quan = datafra['Quantity'].values.tolist()
        colors = sns.color_palette("Pastel1")
        pie_category_month = plt.figure(figsize=(5, 5), dpi=100)
        plt.pie(sold_cat_month_quan, labels=sold_cat_month, autopct='%1.1f%%', colors=colors)
        plt.title("Product Sold in Category in Month", fontsize=18)
        ca = FigureCanvasTkAgg(pie_category_month, master=scroll_frame)
        ca.draw()
        ca.get_tk_widget().pack(padx=180, pady=100)
        tool = NavigationToolbar2Tk(ca, scroll_frame)
        tool.update()
        tool.place(x=740, y=3550)
        month_window.destroy()

    month_window = Toplevel(window)
    month_window.geometry("450x225")
    month_window.title("Sales Report in Month")
    month_window.configure(bg='#DFEEFF')
    month_label = Label(month_window, text='Choose a year and a month', font=('Arial', 15), bg='#DFEEFF')
    month_label.pack(pady=20)
    year_value = pd.read_sql_query("SELECT strftime('%Y', date) AS Year FROM invoice GROUP BY strftime('%Y', date)",
                                   conn)
    year_df = pd.DataFrame(year_value)
    year_list = year_df['Year'].values.tolist()
    year_chosen = ttk.Combobox(month_window, width=27, values=year_list, font=('Arial', 12))
    year_chosen.set(datetime.datetime.now().year)
    year_chosen.pack(pady=10)
    month_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    month_chosen = ttk.Combobox(month_window, width=27, values=month_list, font=('Arial', 12))
    month_chosen.set('0' + str(datetime.datetime.now().month))
    month_chosen.pack()
    Button(month_window, text='Confirm', font=('Arial', 15), command=sales_month).pack(pady=20)


def sort_day():
    def sales_day():
        for widget in scroll_frame.winfo_children():
            widget.destroy()
        date_chosen = calendar.get_date()
        year_choose = date_chosen.strftime('%Y')
        month_choose = date_chosen.strftime('%m')
        day_choose = date_chosen.strftime('%d')
        # Sales Bar Day
        Bar_Month_Select = pd.read_sql_query("SELECT i.total AS 'Revenue', SUM((p.sell_price - p.buy_price)*i.quantity)"
                                             " AS 'Profit' FROM invoice i, product p WHERE i.pro_id = p.pro_id AND "
                                             "strftime('%Y', i.date) = '{}' AND strftime('%m', i.date) = '{}' AND "
                                             "strftime('%d', i.date) = '{}' GROUP BY invoice_id".format
                                             (year_choose, month_choose, day_choose), conn)
        Bar_Month_Select["Profit"] = Bar_Month_Select["Profit"].astype(float)
        Bar_Month_Select["Revenue"] = Bar_Month_Select["Revenue"].astype(float)
        Bar_Month_s = Bar_Month_Select['Revenue'].sum()
        Bar_m_s = Bar_Month_Select['Profit'].sum()
        R = '{:.2f}'.format(Bar_Month_s)
        P = '{:.2f}'.format(Bar_m_s)
        previous_day = int(day_choose) - 1
        Bar_PMonth_Select = pd.read_sql_query("SELECT i.total AS 'Revenue', SUM((p.sell_price - p.buy_price)*"
                                              "i.quantity) AS 'Profit' FROM invoice i, product p WHERE i.pro_id = "
                                              "p.pro_id AND strftime('%Y', i.date) = '{}' AND strftime('%m', i.date) = "
                                              "'{}' AND strftime('%d', i.date) = '{}' GROUP BY invoice_id".format
                                              (year_choose, month_choose, previous_day), conn)
        Bar_PMonth_Select["Profit"] = Bar_PMonth_Select["Profit"].astype(float)
        Bar_PMonth_Select["Revenue"] = Bar_PMonth_Select["Revenue"].astype(float)
        Bar_PMonth_s = Bar_PMonth_Select['Revenue'].sum()
        Bar_Pm_s = Bar_PMonth_Select['Profit'].sum()
        PR = '{:.2f}'.format(Bar_PMonth_s)
        PP = '{:.2f}'.format(Bar_Pm_s)
        data = {'Day': {0: previous_day, 1: int(day_choose)}, 'Revenue': {0: PR, 1: R}, 'Profit': {0: PP, 1: P}}
        b_m_s = pd.DataFrame(data)
        dfl = (b_m_s.melt(id_vars='Day', var_name='Sales', value_name='RM').sort_values('RM', ascending=True)
               .reset_index(drop=True).sort_values('Day', ascending=True))
        dfl['RM'] = dfl['RM'].astype(str).astype(float)
        fig, ax = plt.subplots(figsize=(7, 5), dpi=100)
        plot = sns.barplot(x='Day', y='RM', data=dfl, hue='Sales', palette="Pastel1", ci=None)
        for c in ax.containers:
            ax.bar_label(c, fmt='%.2f')
        plot.set_ylabel("RM", fontsize=15)
        plot.set_xlabel("Day", fontsize=15)
        plot.set_title("Revenue and Profit Bar Chart in Day", fontsize=21)
        canv = FigureCanvasTkAgg(fig, master=scroll_frame)
        canv.draw()
        canv.get_tk_widget().pack(padx=180, pady=100)
        toolba = NavigationToolbar2Tk(canv, scroll_frame)
        toolba.update()
        toolba.place(x=740, y=1150)
        # Pie Product Sold Day
        Sold_Day = pd.read_sql_query("SELECT p.product_name AS 'Product Name', sum(i.quantity) AS 'Quantity' FROM "
                                     "invoice i JOIN product p ON p.pro_id = i.pro_id WHERE strftime('%Y', i.date) IN "
                                     "('{}') AND strftime('%m', i.date) IN ('{}') AND strftime('%d', i.date) IN ('{}') "
                                     "GROUP BY i.pro_id".format(year_choose, month_choose, day_choose), conn)
        datframe = pd.DataFrame(Sold_Day)
        sold_day_pro = datframe['Product Name'].values.tolist()
        sold_day_quan = datframe['Quantity'].values.tolist()
        colors = sns.color_palette("Pastel1")
        pie_product_day = plt.figure(figsize=(5, 5), dpi=100)
        plt.pie(sold_day_quan, labels=sold_day_pro, autopct='%1.1f%%', colors=colors)
        plt.title("Product Sold in Day", fontsize=18)
        can = FigureCanvasTkAgg(pie_product_day, master=scroll_frame)
        can.draw()
        can.get_tk_widget().pack(padx=180, pady=100)
        toolb = NavigationToolbar2Tk(can, scroll_frame)
        toolb.update()
        toolb.place(x=740, y=2350)
        # Pie Category Sold
        Sold_Cat_Day = pd.read_sql_query("SELECT c.cat_name AS 'Category', SUM(i.quantity) AS 'Quantity' FROM category "
                                         "c, invoice i, product p WHERE i.pro_id = p.pro_id AND p.cat_id = c.cat_id AND"
                                         " strftime('%Y', i.date) IN ('{}') AND strftime('%m', i.date) IN ('{}') AND "
                                         "strftime('%d', i.date) IN ('{}') GROUP BY c.cat_id"
                                         .format(year_choose, month_choose, day_choose), conn)
        datafram = pd.DataFrame(Sold_Cat_Day)
        sold_cat_day = datafram['Category'].values.tolist()
        sold_cat_day_quan = datafram['Quantity'].values.tolist()
        colors = sns.color_palette("Pastel1")
        pie_category_day = plt.figure(figsize=(5, 5), dpi=100)
        plt.pie(sold_cat_day_quan, labels=sold_cat_day, autopct='%1.1f%%', colors=colors)
        plt.title("Product Sold in Category in Day", fontsize=18)
        ca = FigureCanvasTkAgg(pie_category_day, master=scroll_frame)
        ca.draw()
        ca.get_tk_widget().pack(padx=180, pady=100)
        tool = NavigationToolbar2Tk(ca, scroll_frame)
        tool.update()
        tool.place(x=740, y=3550)
        day_window.destroy()

    day_window = Toplevel(window)
    day_window.geometry("450x225")
    day_window.title("Sales Report in Day")
    day_window.configure(bg='#DFEEFF')
    day_label = Label(day_window, text='Choose a date', font=('Arial', 15), bg='#DFEEFF')
    day_label.pack(pady=20)
    calendar = DateEntry(day_window, selectmode='day', year=datetime.datetime.now().year,
                         month=datetime.datetime.now().month, day=datetime.datetime.now().day, font=('Arial', 15))
    calendar.pack()
    Button(day_window, text='Confirm', font=('Arial', 15), command=sales_day).pack(pady=20)


# Define and resize the icons to be shown in Menu bar
logout = ImageTk.PhotoImage(Image.open('Logout.png').resize((40, 40), resample=Image.LANCZOS))
home = ImageTk.PhotoImage(Image.open('Home.png').resize((40, 40), resample=Image.LANCZOS))
billing = ImageTk.PhotoImage(Image.open('Bill.png').resize((40, 40), resample=Image.LANCZOS))
inventory = ImageTk.PhotoImage(Image.open('Inventory.png').resize((40, 40), resample=Image.LANCZOS))
analysis = ImageTk.PhotoImage(Image.open('Analysis.png').resize((40, 40), resample=Image.LANCZOS))
userInfo = ImageTk.PhotoImage(Image.open('User.png').resize((40, 40), resample=Image.LANCZOS))
register = ImageTk.PhotoImage(Image.open('Register.png').resize((40, 40), resample=Image.LANCZOS))
logo = ImageTk.PhotoImage(Image.open('Logo.jpeg').resize((50, 50), resample=Image.LANCZOS))

window.update()  # For the width to get updated

menuFrame = Frame(window, bg='#492F7C', highlightbackground='white', highlightthickness=1)
menuFrame.place(x=0, y=100, width=150, height=875)

# Defining the buttons for menu bar in Home page
logout_b = Button(menuFrame, image=logout, bg='#252B61', relief='ridge')
home_b = Button(menuFrame, image=home, bg='#252B61', relief='ridge')
billing_b = Button(menuFrame, image=billing, bg='#252B61', relief='ridge')
inventory_b = Button(menuFrame, image=inventory, bg='#252B61', relief='ridge')
analysis_b = Button(menuFrame, image=analysis, bg='#252B61', relief='ridge')
userInfo_b = Button(menuFrame, image=userInfo, bg='#252B61', relief='ridge')
register_b = Button(menuFrame, image=register, bg='#252B61', relief='ridge')

# Placing button in menu bar
logout_b.place(x=25, y=10, width=100)
home_b.place(x=25, y=70, width=100)
billing_b.place(x=25, y=130, width=100)
inventory_b.place(x=25, y=190, width=100)
analysis_b.place(x=25, y=250, width=100)
userInfo_b.place(x=25, y=310, width=100)
register_b.place(x=25, y=370, width=100)

# Bind to the frame, if centered or left
menuFrame.bind('<Enter>', lambda e: expandForHome())
menuFrame.bind('<Leave>', lambda e: contractForHome())

# So that it does not depend on the widgets inside the frame
menuFrame.grid_propagate(False)

# Rectangle Frame
RectangleFrame = Frame(window, bg='#492F7C', highlightbackground='white', highlightthickness=1)
RectangleFrame.place(x=0, y=0, height=100, width=1920)
RectangleFrame2 = Frame(window, bg='#492F7C', highlightbackground='white', highlightthickness=1)
RectangleFrame2.place(x=0, y=0, height=100, width=150)
Logo = Label(window, image=logo)
Logo.place(x=45, y=18)
Lab = Label(window, text='Analysis', font=('Arial', 30), fg='white', bg='#492F7C')
Lab.place(x=160, y=30)

# Create notebook
notebook = ttk.Notebook(window)
notebook.grid(padx=150, pady=100)

# Create Frames and Add Scrollbar
frame1 = Frame(notebook, bg='#DFEEFF', width=1770, height=840)  # new frame for tab 1
container = Canvas(frame1, bg='#DFEEFF')
frame2 = Frame(notebook, bg='#DFEEFF', width=1770, height=840)  # new frame for tab 2
frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
scrollbar = Scrollbar(frame1, orient=VERTICAL, command=container.yview)
scroll_frame = Frame(container, bg='#DFEEFF')
scroll_frame.bind("<Configure>", lambda e: container.configure(scrollregion=container.bbox("all")))
container.create_window((0, 0), window=scroll_frame, anchor=NW)
container.configure(yscrollcommand=scrollbar.set)
container.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
scroll_frame.bind("<MouseWheel>", lambda e: MouseScrollWheel)

# Add frames to notebook
notebook.add(frame1, text="Sales Report")
notebook.add(frame2, text="Analytics")
style = ttk.Style()
style.theme_use('alt')
style.configure('.', font=('Arial', 18))

# Chart
#cursor = conn.cursor()

# Analytics
# Expiry Status Pie
Expiry = pd.read_sql_query("SELECT expiry_status AS 'Expiry Status', count(expiry_status) AS 'Number of Product' "
                           "FROM product GROUP BY expiry_status", conn)
dataf = pd.DataFrame(Expiry)
expiry = dataf['Expiry Status'].values.tolist()
numpro = dataf['Number of Product'].values.tolist()
colors = sns.color_palette("Pastel1")
pie_expiry = plt.figure(figsize=(3, 3), dpi=100)
plt.pie(numpro, labels=expiry, autopct='%1.1f%%', colors=colors)
plt.title("Product Expiry Status", fontsize=18)
canvas = FigureCanvasTkAgg(pie_expiry, master=frame2)
canvas.draw()
canvas.get_tk_widget().place(x=200, y=75)
toolbars = NavigationToolbar2Tk(canvas, frame2)
toolbars.update()
toolbars.place(x=335, y=725)
# Stock Level Status Pie
Stock = pd.read_sql_query("SELECT stock_level AS 'Stock Level', count(stock_level) AS 'Number of Product' FROM "
                          "product GROUP BY stock_level", conn)
dataframe = pd.DataFrame(Stock)
level = dataframe['Stock Level'].values.tolist()
numproduct = dataframe['Number of Product'].values.tolist()
pie_stock = plt.figure(figsize=(3, 3), dpi=100)
plt.pie(numproduct, labels=level, autopct='%1.1f%%', colors=colors)
plt.title("Stock Level Status", fontsize=18)
canva = FigureCanvasTkAgg(pie_stock, master=frame2)
canva.draw()
canva.get_tk_widget().place(x=950, y=75)
toolbar = NavigationToolbar2Tk(canva, frame2)
toolbar.update()
toolbar.place(x=1085, y=725)

# Sales Report
Button(frame1, text='Year', font=('Arial', 15), command=sort_year).place(x=1540, y=10)
Button(frame1, text='Month', font=('Arial', 15), command=sort_month).place(x=1615, y=10)
Button(frame1, text='Day', font=('Arial', 15), command=sort_day).place(x=1700, y=10)
# Show current day chart
bar()
pie_product()
pie_category()

window.mainloop()
