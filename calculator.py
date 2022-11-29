import tkinter as tk

btn_params = {'padx': 16, 'pady': 1, 'bd': 4, 'fg': 'white', 'bg': '#666666', 'font': ('arial', 12), 'width': 4,
              'height': 2, 'relief': 'flat', 'activebackground': "#666666"}


class Calculator:
    def __init__(self, master):
        # expression that will be displayed on screen
        self.expression = ""
        # be used to store data in memory
        self.recall = ""
        # be used to store current data in memory
        self.current = ""
        # self.answer
        self.sum_up = ""
        # create string for text input
        self.text_input = tk.StringVar()
        # assign instance to master
        self.master = master
        # set frame showing inputs and title
        top_frame = tk.Frame(master, width=500, height=20, bd=4, relief='flat', bg='#666666')
        top_frame.pack(side=tk.TOP)
        # set frame showing all buttons
        bottom_frame = tk.Frame(master, width=650, height=470, bd=4, relief='flat', bg='#666666')
        bottom_frame.pack(side=tk.BOTTOM)
        # name of calculator
        my_item = tk.Label(top_frame, text="Calculator", font=('arial', 14), fg='white', width=26, bg='#666666')
        my_item.pack()
        # entry interface for inputs
        txt_display = tk.Entry(top_frame, font=('arial', 23), relief='flat', bg='#999999', fg='black',
                               textvariable=self.text_input, width=55, bd=4, justify='right', state='readonly')
        txt_display.pack()

        # row 0
        # clears self.expression
        self.btn_clear = tk.Button(bottom_frame, **btn_params, text="C", command=self.btn_clear_all)
        self.btn_clear.grid(row=0, column=4)
        # deletes last string input
        self.btn_del = tk.Button(bottom_frame, **btn_params, text="del", command=self.btn_clear1)
        self.btn_del.grid(row=0, column=5)
        # inputs a negative sign to the next entry
        self.btn_change_sign = tk.Button(bottom_frame, **btn_params, text=chr(177), command=self.change_signs)
        self.btn_change_sign.grid(row=0, column=6)
        # division
        self.btn_div = tk.Button(bottom_frame, **btn_params, text="/", command=lambda: self.btn_click('/'))
        self.btn_div.grid(row=0, column=7)
        # stores previous expression as an answer value
        self.btn_ans = tk.Button(bottom_frame, **btn_params, text="ans", command=self.answer)
        self.btn_ans.grid(row=0, column=8)

        # row 1
        # seven
        self.btn_7 = tk.Button(bottom_frame, **btn_params, text="7", command=lambda: self.btn_click(7))
        self.btn_7.configure(activebackground="#4d4d4d", bg='#4d4d4d')
        self.btn_7.grid(row=1, column=4)
        # eight
        self.btn_8 = tk.Button(bottom_frame, **btn_params, text="8", command=lambda: self.btn_click(8))
        self.btn_8.configure(activebackground="#4d4d4d", bg='#4d4d4d')
        self.btn_8.grid(row=1, column=5)
        # nine
        self.btn_9 = tk.Button(bottom_frame, **btn_params, text="9", command=lambda: self.btn_click(9))
        self.btn_9.configure(activebackground="#4d4d4d", bg='#4d4d4d')
        self.btn_9.grid(row=1, column=6)
        # multiplication
        self.btn_mult = tk.Button(bottom_frame, **btn_params, text="x", command=lambda: self.btn_click('*'))
        self.btn_mult.grid(row=1, column=7)
        # 'memory clear' button. Wipes self.recall to an empty string
        self.btn_MC = tk.Button(bottom_frame, **btn_params, text="MC", command=self.memory_clear)
        self.btn_MC.grid(row=1, column=8)

        # row 2
        # four
        self.btn_4 = tk.Button(bottom_frame, **btn_params, text="4", command=lambda: self.btn_click(4))
        self.btn_4.configure(activebackground="#4d4d4d", bg='#4d4d4d')
        self.btn_4.grid(row=2, column=4)
        # five
        self.btn_5 = tk.Button(bottom_frame, **btn_params, text="5", command=lambda: self.btn_click(5))
        self.btn_5.configure(activebackground="#4d4d4d", bg='#4d4d4d')
        self.btn_5.grid(row=2, column=5)
        # six
        self.btn_6 = tk.Button(bottom_frame, **btn_params, text="6", command=lambda: self.btn_click(6))
        self.btn_6.configure(activebackground="#4d4d4d", bg='#4d4d4d')
        self.btn_6.grid(row=2, column=6)
        # subtraction
        self.btnSub = tk.Button(bottom_frame, **btn_params, text="-", command=lambda: self.btn_click('-'))
        self.btnSub.grid(row=2, column=7)
        # outputs what is in self.recall
        self.btn_MR = tk.Button(bottom_frame, **btn_params, text="MR", command=self.memory_recall)
        self.btn_MR.grid(row=2, column=8)

        # row 3
        # one
        self.btn_1 = tk.Button(bottom_frame, **btn_params, text="1", command=lambda: self.btn_click(1))
        self.btn_1.configure(activebackground="#4d4d4d", bg='#4d4d4d')
        self.btn_1.grid(row=3, column=4)
        # two
        self.btn_2 = tk.Button(bottom_frame, **btn_params, text="2", command=lambda: self.btn_click(2))
        self.btn_2.configure(activebackground="#4d4d4d", bg='#4d4d4d')
        self.btn_2.grid(row=3, column=5)
        # three
        self.btn_3 = tk.Button(bottom_frame, **btn_params, text="3", command=lambda: self.btn_click(3))
        self.btn_3.configure(activebackground="#4d4d4d", bg='#4d4d4d')
        self.btn_3.grid(row=3, column=6)
        # addition
        self.btn_add = tk.Button(bottom_frame, **btn_params, text="+", command=lambda: self.btn_click('+'))
        self.btn_add.grid(row=3, column=7)
        # adds current self.expression to self.recall string
        self.btn_M_plus = tk.Button(bottom_frame, **btn_params, text="M+", command=self.memory_add)
        self.btn_M_plus.grid(row=3, column=8)

        # row 4
        # zero
        self.btn_0 = tk.Button(bottom_frame, **btn_params, text="0", command=lambda: self.btn_click(0))
        self.btn_0.configure(activebackground="#4d4d4d", bg='#4d4d4d', width=7, bd=5)
        self.btn_0.grid(row=4, column=4, columnspan=2)
        # equals button
        self.btn_eq = tk.Button(bottom_frame, **btn_params, text="=", command=self.btn_equal)
        self.btn_eq.configure(bg='#ff9980', activebackground='#ff9980')
        self.btn_eq.grid(row=4, column=6)
        # decimal to convert to float
        self.btn_dec = tk.Button(bottom_frame, **btn_params, text=".", command=lambda: self.btn_click('.'))
        self.btn_dec.grid(row=4, column=7)
        # subtracts current self.expression to self.recall string
        self.btn_M_sub = tk.Button(bottom_frame, **btn_params, text="M-", command=self.memory_minus)
        self.btn_M_sub.grid(row=4, column=8)

    # ============ functions ================
    # allows button you click to be put into self.expression
    def btn_click(self, expression_val):
        if len(self.expression) >= 23:
            self.expression = self.expression
            self.text_input.set(self.expression)
        else:
            self.expression = self.expression + str(expression_val)
            self.text_input.set(self.expression)

    # validate number of dots
    def val_dot(self, expression_val):
        self.current = self.expression
        while "." in self.expression:
            self.text_input.set(self.current)
        self.btn_click('.')

    # clears last item in string
    def btn_clear1(self):
        self.expression = self.expression[:-1]
        self.text_input.set(self.expression)

    # adds in a negative sign
    def change_signs(self):
        self.expression = '-' + self.expression
        self.text_input.set(self.expression)

    # clears memory_recall
    def memory_clear(self):
        self.recall = ""

    # adds whatever is on the screen to self.recall
    def memory_add(self):
        self.recall = self.recall + '+' + self.expression

    # minus whatever is on the screen to self.recall
    def memory_minus(self):
        self.recall = self.recall + '-' + self.expression

    # uses whatever is stored in memory_recall
    def answer(self):
        self.answer = self.sum_up
        self.expression = self.expression + self.answer
        self.text_input.set(self.expression)

    # uses whatever is stored in memory_recall
    def memory_recall(self):
        if self.expression == "":
            self.text_input.set('0' + self.expression + self.recall)
        else:
            self.text_input.set(self.expression + self.recall)

    # clears self.expression
    def btn_clear_all(self):
        self.expression = ""
        self.text_input.set("")

    # converts self.expression into a mathematical expression and evaluates it
    def btn_equal(self):
        self.sum_up = str(eval(self.expression))
        self.text_input.set(self.sum_up)
        self.expression = self.sum_up

# tkinter layout
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("410x360")
root.resizable(False, False)
root.iconphoto(False, tk.PhotoImage(file="logo_refined.png"))
Calculator(root)
root.mainloop()
