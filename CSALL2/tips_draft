# Python Program to make a scrollable frame
# using Tkinter
import webbrowser
from tkinter import *
import tkinter.font as tkFont

class Tips:
     
    # constructor
    def __init__(self):
         
        # create root window
        self.root = Tk()
        self.root.geometry("1280x720")

        self.tipsframe = Frame(self.root, bg = 'black')
        self.tipsframe.pack(fill = BOTH, expand = TRUE)
  
        # create a horizontal scrollbar by
        # setting orient to horizontal
        #self.h = Scrollbar(self.root,orient = 'horizontal')
  
        # attach Scrollbar to root window at
        # the bootom
        #self.h.pack(side = BOTTOM, fill = X)
  
        # create a vertical scrollbar-no need
        # to write orient as it is by
        # default vertical
        self.v = Scrollbar(self.tipsframe)
  
        # attach Scrollbar to root window on
        # the side
        self.v.pack(side = RIGHT, fill = Y)
          
  
        # create a Text widget with 15 chars
        # width and 15 lines height
        # here xscrollcomannd is used to attach Text
        # widget to the horizontal scrollbar
        # here yscrollcomannd is used to attach Text
        # widget to the vertical scrollbar
        #txt.configure(bg = 'light grey')


        #height depends on how many lines needed for Tips.
        
        self.t = Text(self.tipsframe,height = 300,wrap = NONE,font= tkFont.Font(family='Lato', size=10), yscrollcommand = self.v.set)
        
        self.T = Text(self.tipsframe,height = 300,wrap = NONE,font= tkFont.Font(family='Lato', size=20), yscrollcommand = self.v.set)


  
        # insert some text into the text widget

        #The 50/30/20 rule simplifies budgeting by dividing your after-tax income into just three spending categories: needs, wants and savings or debts.
        
    
        self.t.insert(END,"\n  The 50/30/20 rule simplifies budgeting by dividing your after-tax income into just three spending categories: needs, wants and savings or debts.\n")
        self.t.insert(END,"\n\nSpend 50% of your money on needs\n")
        self.t.insert(END,"Simply put, needs are expenses that you can’t avoid—payments for all the essentials that would be difficult to live without. 50% of your after-tax income should cover your most\n necessary costs.\n")
        self.t.insert(END,"Needs may include:\nMonthly rent, electricity and gas bills, transportation, insurances, minimum loan payments, basic groceries\n")
        self.t.insert(END,"This budget may differ from one person to another. If you find that your needs add up to much more than 50% of your take-home income, you may be able to make some changes to \nbring those expenses down a bit. ")
        self.t.insert(END,"This could be as simple as swapping to a different energy provider or finding some new ways to save money while grocery shopping. It could also \nmean deeper life changes, such as looking for a less-expensive living situation.\n")
        self.t.insert(END,"\n\nSpend 30% of your money on wants\n")
        self.t.insert(END,"These may include:\nDining out, clothes shopping, holidays, gym membership, entertainment subscriptions, groceries\n")
        self.t.insert(END,"Using the same example as above, if your monthly after-tax income is RM 2000, you can spend RM 600 for your wants. And if you discover that you’re spending too much on\nwhat you want, it’s worth thinking about which of those you could cut back on. ")
        self.t.insert(END,"As a side note, following the 50/30/20 rule doesn’t mean not being able to enjoy your life. It simply means \nbeing more conscious about your money by finding areas in your budget where you’re needlessly overspending. ")
        self.t.insert(END,"If you’re confused about whether something is a need \nor a want, simply ask yourself, “Could I live without this?” If the answer is yes, that’s probably a want.\n")
        self.t.insert(END,"\n\nStash 20% of your money for savings\n")
        self.t.insert(END,"With 50% of your monthly income going towards your needs and 30% allocated to your wants, the remaining 20% can be put towards achieving your savings goals or paying back any outstanding debts. \n")
        self.t.insert(END,"Although minimum repayments are considered needs, any extra repayments reduce your existing debt and future interest, so they are classified as savings.\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.T.insert(END,"yyyyyyyyyyyyyy\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        self.t.insert(END,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")

        
        self.hyperlink = Label(self.tipsframe, text = 'the hyperlink', fg = 'blue', bg = 'pink', height = 2,width = 22, cursor = 'hand2', font = ('Times',20, 'underline'))
        self.hyperlink.pack(side = BOTTOM)
        self.hyperlink.bind('<Button-1>',
                       lambda x :webbrowser.open_new("https://n26.com/en-eu/blog/cost-of-buying-a-house"))
        
        
        # attach Text widget to root window at top
        self.t.pack(side=TOP, fill=X)
  
        # here command represents the method to
        # be executed xview is executed on
        # object 't' Here t may represent any
        # widget
        #self.h.config(command=self.t.xview)
  
        # here command represents the method to
        # be executed yview is executed on
        # object 't' Here t may represent any
        # widget
        self.v.config(command=self.t.yview)
  
        # the root window handles the mouse
        # click event
        self.root.mainloop()
 
# create an object to Scrollbar class
s = Tips()
        
