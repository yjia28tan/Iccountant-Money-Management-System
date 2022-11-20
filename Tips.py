import webbrowser

class Tips(tk.Frame):
    def __init__(self, master, controller):
        self.controller = controller
        Frame.__init__(self, master)
        self.menuFrame = Frame(self, bg='#000000', width=180, height=master.winfo_height(),
                               highlightbackground='#1A1A1A')
        self.menuFrame.pack(side=LEFT, fill=BOTH)
        self.sideFrame = Frame(self, bg='#1A1A1A',highlightbackground='#1A1A1A', highlightcolor = "#1A1A1A",width=1100, height=780)
        self.sideFrame.pack(side=RIGHT, fill=BOTH, expand=TRUE)

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
        self.statistic_b = Button(self.menuFrame, image=self.statistic, bg='#000000', relief='flat',
                                  command=lambda: controller.show_frame(Statistic1))
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
        self.tips_b = Button(self.menuFrame, image=self.tips, bg='#000000', relief='flat',
                             command=lambda: self.controller.show_frame(Tips))
        self.tips_b.grid(row=10)
        self.logout_b = Button(self.menuFrame, image=self.logout, bg='#000000', relief='flat',
                               command=self.logout_system)
        self.logout_b.place(x=1, y=570)
        self.user_b = Button(self.menuFrame, image=self.user, bg='#000000', relief='flat',
                             command=lambda: self.controller.show_frame(UserAccount))
        self.user_b.place(x=10, y=610)

        # So that it does not depend on the widgets inside the frame
        self.menuFrame.grid_propagate(False)

        
        self.my_canvas = Canvas(self.sideFrame,bg='#1A1A1A', highlightcolor = "#1A1A1A")
        self.my_canvas.pack(side = LEFT, fill = BOTH, expand = 1)

        self.scrollbar = ttk.Scrollbar(self.sideFrame, orient = VERTICAL, command = self.my_canvas.yview)
        self.scrollbar.pack(side = RIGHT, fill = Y)


        self.my_canvas.config(yscrollcommand = self.scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.config(scrollregion = self.my_canvas.bbox("all")))
        self.second_frame= Frame(self.my_canvas,bg='#1A1A1A',highlightbackground='#1A1A1A', highlightcolor = "#1A1A1A" )

        self.my_canvas.create_window((0,0), window = self.second_frame,anchor = "nw")


        #page title
        pgtitle = Label(self.second_frame, bg='#1A1A1A', text='Tips', fg='white',
                              font=tkFont.Font(family='Lato', size=20, weight="bold", slant="italic"))
        pgtitle.grid(row = 0, column = 0, sticky = 'w', padx = 15, pady = 15)

        #50/30/20 calculator function
        self.buttons()

        #tips in image
        self.budgetim = ImageTk.PhotoImage(Image.open("503020rule.png").resize((1062, 1258), resample=Image.LANCZOS))
        self.budgetim2 = Label(self.second_frame, image=self.budgetim, bg = '#1A1A1A')
        self.budgetim2.grid(row =3,column=0, pady = 20)

                

        #other sources label
        self.linktitle = Label(self.second_frame, bg='#1A1A1A', text='Other sources to help budgeting in specific aspects:', fg='white',
                              font=tkFont.Font(family='Lato', size=15, weight = 'bold',slant="italic"))
        self.linktitle.grid(row = 4, column = 0, sticky = 'w', padx = 10, pady = 2)


        #hyperlinks to other sources
        self.hyperlink1 = Label(self.second_frame, text = 'Cost of buying a house', fg = '#00f7ff', bg = '#1A1A1A', height = 2, cursor = 'hand2',font = ('Lato',12, 'underline'))
        self.hyperlink1.grid(row = 5, column = 0, sticky = 'w', padx = 10, pady = 2)
        self.hyperlink1.bind('<Button-1>',lambda x :webbrowser.open_new("https://n26.com/en-eu/blog/cost-of-buying-a-house"))



        self.hyperlink2 = Label(self.second_frame, text = 'How to save for retirement', fg = '#00f7ff', bg = '#1A1A1A', height = 2, cursor = 'hand2',font = ('Lato',12, 'underline'))
        self.hyperlink2.grid(row = 6, column = 0, sticky = 'w', padx = 10, pady = 2)
        self.hyperlink2.bind('<Button-1>',lambda x :webbrowser.open_new("https://n26.com/en-eu/blog/how-much-to-save-for-retirement"))


        self.hyperlink3 = Label(self.second_frame, text = 'Cost of home renovation', fg = '#00f7ff', bg = '#1A1A1A', height = 2, cursor = 'hand2',font = ('Lato',12, 'underline'))
        self.hyperlink3.grid(row = 7, column = 0, sticky = 'w', padx = 10, pady = 2)
        self.hyperlink3.bind('<Button-1>',lambda x :webbrowser.open_new("https://n26.com/en-eu/blog/cost-of-home-renovation"))


        self.hyperlink4 = Label(self.second_frame, text = 'Cost of owning a car', fg = '#00f7ff', bg = '#1A1A1A', height = 2, cursor = 'hand2',font = ('Lato',12, 'underline'))
        self.hyperlink4.grid(row = 8, column = 0, sticky = 'w', padx = 10, pady = 2)
        self.hyperlink4.bind('<Button-1>',lambda x :webbrowser.open_new("https://n26.com/en-eu/blog/cost-of-owning-a-car"))


        self.hyperlink5 = Label(self.second_frame, text = 'Moving in together and manage monthly expenses', fg = '#00f7ff', bg = '#1A1A1A', height = 2, cursor = 'hand2',font = ('Lato',12, 'underline'))
        self.hyperlink5.grid(row = 9, column = 0, sticky = 'w', padx = 10, pady = 2)
        self.hyperlink5.bind('<Button-1>',lambda x :webbrowser.open_new("https://n26.com/en-eu/blog/moving-in-together-managing-monthly-expenses"))

        self.hyperlink1 = Label(self.second_frame, text = '', fg = '#00f7ff',bg = '#1A1A1A')
        self.hyperlink1.grid(row = 10, column = 0, sticky = 'w', padx = 10, pady = 6)

    # ==================================== Function =================================================
    def buttons(self):
        #display labels of 50/30/20 budget
        self.frame = tk.Frame(self.second_frame, height=1, width=50, bg='#1A1A1A')
        self.frame.grid(row=2, column=0)
        
        self.label = tk.Label(self.frame, text='Your 50/30/20 Rule Budget:', fg = 'white', bg='#1A1A1A',font=tkFont.Font(family='Lato', size=16, weight="bold") )
        self.label.grid(row=0, column=0)
        
        self.entry = tk.Entry(self.frame, font=12)
        self.entry.grid(row=1, column=0, pady =50)
        
        self.viewBudget = customtkinter.CTkButton(master=self.frame, text='View Budget Plan',width=20, height=40,
                                                  fg_color="#464E63", hover_color="#667190", command=self.viewBudgetPlan)
        self.viewBudget.grid(row=2, column=0)
        
        
    def viewBudgetPlan(self):
        #calculate result of 50/30/20 budget
        self.budget = float(self.entry.get() or 0)
        self.spending = self.budget * 0.5
        self.savings = self.budget * 0.3
        self.extra = self.budget - self.spending - self.savings
        self.draw(f"\n\tTotal Budget\t\t: RM {'{:.2f}'.format(self.budget)}\n\tSpending Money\t\t: RM {'{:.2f}'.format(self.spending)} \
            \n\tTo Save\t\t: RM {'{:.2f}'.format(self.savings)}\n\tExtra\t\t: RM {'{:.2f}'.format(self.extra)}")

    def draw(self, msg):
        #display result of 50/30/20 budget
        self.textBox = tk.Text(self.frame, height=6, width=40, relief='flat',fg = 'white', bg='#1A1A1A', font=tkFont.Font(family='Lato', size=12, weight="bold"))
        self.textBox.insert(1.0, msg)
        self.textBox.config(state='disabled')
        self.textBox.grid(row =1, column=1)


    def con(self):
        os.system('CurrencyConverter.py')

    def cal(self):
        os.system('python calculator.py')

    def logout_system(self):
        answer = messagebox.askyesno(title='Confirmation', message='Are you sure that you want to logout?')
        if answer:
            messagebox.showinfo('Log Out', 'You have successfully Logged Out!')
            self.controller.show_frame(LoginPage)
