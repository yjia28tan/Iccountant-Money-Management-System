from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import customtkinter


class Chatbot:
    def __init__(self, root):
        self.root = root
        self.root.resizable(0, 0)
        self.root.title("Chatbot")
        self.root.configure(bg="#383e4f")
        
        self.v = Scrollbar(self.root)
        # attach Scrollbar to root window on the side
        self.v.grid(column=2, sticky=N + S + E)
        
        self.txt = Text(self.root)
        self.txt.configure(fg='white', bg="#232731", width=100, wrap=NONE, font=tkFont.Font(family='Lato', size=11),
                           yscrollcommand=self.v.set)
        self.txt.grid(row=0, column=0, columnspan=2)
        self.txt.insert(END, "\n" + "   🤖 🢂 Hi user!")
        self.txt.insert(END, "\n" + "   🤖 🢂 This is your personal chatbot that provides guidance in using the app!")
        self.chatbot_menu()
        self.disabled_state()
        self.e = Entry(self.root, width=85, fg='white', bg="#7d8391", insertbackground='white',
                       font=tkFont.Font(family='Lato', size=11))
        self.sendbtn = customtkinter.CTkButton(master=self.root, text="SEND", width=90, height=30, command=self.send)
        self.sendbtn.grid(row=1, column=1)
        self.send = "   👤 🢂 " + self.e.get()
        self.txt.insert(END, "\n" + self.send)
        self.e.grid(row=1, column=0)

    def chatbot_menu(self):
        self.txt.insert(END, "\n" + "   🤖 🢂 Select the options by typing the numbers!")
        self.txt.insert(END, "\n\n" + "\t\t\t\t\t1. Dashboard")
        self.txt.insert(END, "\n" + "\t\t\t\t\t2. Statistics")
        self.txt.insert(END, "\n" + "\t\t\t\t\t3. Transactions")
        self.txt.insert(END, "\n" + "\t\t\t\t\t4. Categories")
        self.txt.insert(END, "\n" + "\t\t\t\t\t5. Accounts")
        self.txt.insert(END, "\n" + "\t\t\t\t\t6. Currency Calculator")
        self.txt.insert(END, "\n" + "\t\t\t\t\t7. User Account")
        self.txt.insert(END, "\n   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def dashboard(self):
        self.normal_state()

        self.txt.insert(END, "\n\n" + "   🤖 🢂 The dashboard page displays the total amount of transactions of "
                                      "categories and accounts in pie chart.")
        self.txt.insert(END, "\n\n" + "   🤖 🢂 The data displayed in both pie charts can be filtered using the 'Filter"
                                      " Data' button.")
        self.txt.insert(END, "\n" + "            You can filter the by selecting year and month, and then press the "
                                    "'Confirm' button.")
        self.txt.insert(END, "\n" + "            Selecting a month is not necessary, but if a month is selected, the "
                                    "year must be selected too.")
        self.txt.insert(END, "\n\n" + "   🤖 🢂 In the pie charts, you can use the toolbar that has several functions:")
        self.txt.insert(END, "\n" + "            1. Save figure: where you can export and save the pie chart as an "
                                    "image")
        self.txt.insert(END, "\n" + "            2. Subplot configuration plot: where you can click on slides to adjust"
                                    " plot param")
        self.txt.insert(END, "\n" + "            3. Zoom: where you can zoom in and out about the figure")
        self.txt.insert(END, "\n" + "            4. Arrows up down left right: where you can press the left key to pans"
                                    ", and right key to zoom")
        self.txt.insert(END, "\n" + "            5. Reset original view: where you can reset the display into its "
                                    "original view")

        # ending
        self.txt.insert(END, "\n\n" + "   🤖 🢂 You've reached the end of the guide for Dashboard!")
        self.txt.insert(END, "\n   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.txt.insert(END, "\n\n" + "   🤖 🢂 Select the other options by typing the numbers, or press 'X' button to "
                                      "close!")
        self.chatbot_menu()

    def statistics(self):
        self.normal_state()
        self.txt.insert(END, "\n\n" + "   🤖 🢂 The statistics page displays the summary of all income and expenses in "
                                      "piecharts and barcharts.")
        self.txt.insert(END, "\n\n" + "   🤖 🢂 In the statistics, you can view several types of summary using the "
                                      "buttons which are:")
        self.txt.insert(END, "\n" + "            1. Total")
        self.txt.insert(END, "\n" + "            2. Yearly")
        self.txt.insert(END, "\n" + "            3. Monthly")
        self.txt.insert(END, "\n\n" + "   🤖 🢂 The monthly and yearly types have their own filter button for you to "
                                      "select.")
        self.txt.insert(END, "\n" + "            The monthly filter allows you to view data for which month in which "
                                    "year.")
        self.txt.insert(END, "\n" + "            While the yearly filter allows you to view data for which year")
        self.txt.insert(END, "\n\n" + "   🤖 🢂 In the charts, you can use the toolbar that has several functions:")
        self.txt.insert(END, "\n" + "            1. Save figure: where you can export and save the pie chart as an "
                                    "image")
        self.txt.insert(END, "\n" + "            2. Subplot configuration plot: where you can click on slides to adjust"
                                    " plot param")
        self.txt.insert(END, "\n" + "            3. Zoom: where you can zoom in and out about the figure")
        self.txt.insert(END, "\n" + "            4. Arrows up down left right: where you can press the left key to pans"
                                    ", and right key to zoom")
        self.txt.insert(END, "\n" + "            5. Reset original view: where you can reset the display into its "
                                    "original view")

        # ending
        self.txt.insert(END, "\n\n" + "   🤖 🢂 You've reached the end of the guide for Statistics!")
        self.txt.insert(END, "\n   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.txt.insert(END, "\n\n" + "   🤖 🢂 Select the other options by typing the numbers, or press 'X' button to "
                                      "close!")
        self.chatbot_menu()

    def transactions(self):
        self.normal_state()
        self.txt.insert(END, "\n\n" + "   🤖 🢂 The transactions page displays the list of transaction records in "
                                      "tabular form.")
        self.txt.insert(END, "\n" + "            You can filter the by selecting year, month, transaction type, account"
                                    ", and category ,and then press the 'Confirm' \n            button.")
        self.txt.insert(END, "\n" + "            Selecting a month is not necessary, but if a month is selected, the "
                                    "year must be selected too.")
        self.txt.insert(END, "\n\n" + "   🤖 🢂 The transactions is where you can manage your income and expenses.")
        self.txt.insert(END, "\n" + "            You can add a new transaction by pressing the 'add' button.")
        self.txt.insert(END, "\n" + "            You can edit a transaction by selecting the desired transaction record"
                                    " in the table and then pressing the 'edit' button to edit.")
        self.txt.insert(END, "\n" + "            You can delete a transaction by selecting the desired transaction "
                                    "record in the table and then pressing the 'delete' button.")
        self.txt.insert(END, "\n" + "")

        # ending
        self.txt.insert(END, "\n" + "   🤖 🢂 You've reached the end of the guide for Transactions!")
        self.txt.insert(END, "\n   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.txt.insert(END, "\n" + "   🤖 🢂 Select the other options by typing the numbers, or press 'X' button to "
                                    "close!")
        self.chatbot_menu()

    def categories(self):
        self.normal_state()
        self.txt.insert(END, "\n\n" + "   🤖 🢂 The categories page displays the list of categories in tabular form.")
        self.txt.insert(END, "\n\n" + "   🤖 🢂 The categories is where you can sort which transactions belong to which"
                                      " category.")
        self.txt.insert(END, "\n" + "            You can add a new category by pressing the 'add' button. The category "
                                    "only requires its name input by you.")
        self.txt.insert(END, "\n" + "            You can edit a category by selecting the desired category in the table"
                                    " and then pressing the 'edit' button to edit.")
        self.txt.insert(END, "\n" + "            You can delete a category by selecting the desired category in the "
                                    "table and then pressing the 'delete' button to \n            delete.")

        # ending
        self.txt.insert(END, "\n\n" + "   🤖 🢂 You've reached the end of the guide for Categories!")
        self.txt.insert(END, "\n\n   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.txt.insert(END, "\n\n" + "   🤖 🢂 Select the other options by typing the numbers, or press 'X' button to "
                                      "close!")
        self.chatbot_menu()

    def accounts(self):
        self.normal_state()
        self.txt.insert(END, "\n\n" + "   🤖 🢂 The accounts page displays the list of accounts in tabular form.")
        self.txt.insert(END, "\n\n" + "   🤖 🢂 The accounts is where you can sort which transactions belong to which "
                                      "account.")
        self.txt.insert(END, "\n" + "            You can add a new account by pressing the 'add' button. The account "
                                    "only requires its name and amount input by you.")
        self.txt.insert(END, "\n" + "            You can edit a account by selecting the desired account in the table "
                                    "and then pressing the 'edit' button to edit.")
        self.txt.insert(END, "\n" + "            You can delete a account by selecting the desired account in the table"
                                    " and then pressing the 'delete' button to \n            delete.")

        # ending
        self.txt.insert(END, "\n\n" + "   🤖 🢂 You've reached the end of the guide for Accounts!")
        self.txt.insert(END, "\n   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.txt.insert(END, "\n\n" + "   🤖 🢂 Select the other options by typing the numbers, or press 'X' button to "
                                      "close!")
        self.chatbot_menu()

    def currency(self):
        self.normal_state()
        self.txt.insert(END, "\n\n" + "   🤖 🢂 The currency converter calculator page is where you can use the "
                                      "real-time currency converter calculator for quick \n            conversion of "
                                      "any currency into any other currency to do any trading that uses foreign "
                                      "currencies.")
        self.txt.insert(END, "\n" + "            This calculator requires the before currency, after currency, and the "
                                    "amount you want to convert.")

        # ending
        self.txt.insert(END, "\n\n" + "   🤖 🢂 You've reached the end of the guide for Currency Calculator!")
        self.txt.insert(END, "\n   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.txt.insert(END, "\n\n" + "   🤖 🢂 Select the other options by typing the numbers, or press 'X' button to "
                                      "close!")
        self.chatbot_menu()

    def user(self):
        self.normal_state()
        self.txt.insert(END, "\n\n" + "   🤖 🢂 The user account page displays your name, username and email. You can "
                                      "edit your username and password.")
        self.txt.insert(END, "\n\n" + "   🤖 🢂 To edit your username, click 'edit username' to enter the details to "
                                      "edit. ")
        self.txt.insert(END, "\n\n" + "   🤖 🢂 To edit password, click 'edit password' to enter the details to edit.")
        self.txt.insert(END, "\n" + "            Editing your password requires OTP verification that will be sent to "
                                    "your email registered in your user account.")
        self.txt.insert(END, "\n")

        # ending
        self.txt.insert(END, "\n\n" + "   🤖 🢂 You've reached the end of the guide for User Account!")
        self.txt.insert(END, "\n   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.txt.insert(END, "\n\n" + "   🤖 🢂 Select the other options by typing the numbers, or press 'X' button to "
                                      "close!")
        self.chatbot_menu()

    def send(self):
        self.normal_state()
        self.txt.insert(END, "\n\n" + "   👤 🢂 " + self.e.get())
        if self.e.get() == '1':
            self.txt.insert(END, "\n\n" + "   🤖 🢂 Dashboard selected!")
            self.dashboard()

        elif self.e.get() == '2':
            self.txt.insert(END, "\n\n" + "   🤖 🢂 Statistics selected!")
            self.statistics()

        elif self.e.get() == '3':
            self.txt.insert(END, "\n\n" + "   🤖 🢂 Transactions selected!")
            self.transactions()

        elif self.e.get() == '4':
            self.txt.insert(END, "\n\n" + "   🤖 🢂 Categories selected!")
            self.categories()

        elif self.e.get() == '5':
            self.txt.insert(END, "\n\n" + "   🤖 🢂 Accounts selected!")
            self.accounts()

        elif self.e.get() == '6':
            self.txt.insert(END, "\n\n" + "   🤖 🢂 Currency Calculator selected!")
            self.currency()

        elif self.e.get() == '7':
            self.txt.insert(END, "\n\n" + "   🤖 🢂 User Account selected!")
            self.user()

        else:
            self.txt.insert(END, "\n" + "   🤖 🢂 Invalid input! You can only enter 1 to 7!")

        self.e.delete(0, END)
        self.disabled_state()

    def normal_state(self):
        self.txt.configure(state=NORMAL)

    def disabled_state(self):
        self.txt.configure(state=DISABLED)

    def delete(self):
        self.txt.delete("1.0", "end")


def main():
    root = tk.Tk()
    root.iconphoto(False, tk.PhotoImage(file="robotpict.png"))
    Chatbot(root)
    root.mainloop()


if __name__ == '__main__':
    main()
