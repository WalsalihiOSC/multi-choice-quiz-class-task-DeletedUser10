"""Multi Choice quiz task"""


from tkinter import*

class MultiChoice:
    def __init__(self, parent):
        main_frame = Frame(parent)
        main_frame.grid()
        
        f1 = Frame(main_frame, height= 180, width = 180)
        f1.grid(column=1, sticky=E)

        ques = Label(f1, text = "What is the capital of New Zealand?")
        ques.grid()
        self.ans = ["Manurewa", "Auckland", "Wellington", "Botany", "Mt Wellington"]
        self.ans_var= StringVar()
        self.ans_var.set(self.ans)

        for answer in self.ans:
            Radiobutton(f1, text = answer, variable=self.ans_var,
                                        value= answer,
                                        command=self.show_label).grid(sticky=W)

        self.check = Label(main_frame, text = " ")
        self.check.grid(column=1, sticky=W)
    def show_label(self):
        if self.ans_var.get() == self.ans[2]:
            self.check.configure(text = "correct")
        else:
            self.check.configure(text = "Incorrect")
            




def main():
    root = Tk()
    MultiChoice(root)
    root.mainloop()
 
main()