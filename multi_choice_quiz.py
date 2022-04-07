"""Multi Choice quiz task"""


from tkinter import*

class Interface:
    def __init__(self, parent):
        self.quiz = Quiz()

        main_frame = Frame(parent)
        main_frame.grid()
        
        f1 = Frame(main_frame, height= 180, width = 180)
        f1.grid(column=1, sticky=E)

        ques = Label(f1, text = "What is the capital of New Zealand?")
        ques.grid()
        self.ans_var= StringVar()
        self.ans_var.set(self.quiz.ans)

        for answer in self.quiz.ans:
            Radiobutton(f1, text = answer, variable=self.ans_var,
                                        value= answer,
                                        command=self.check_answer).grid(sticky=W)

        self.check = Label(main_frame, text = " ")
        self.check.grid(column=1, sticky=W)

        
    def check_answer(self):
        if self.quiz.is_answer_correct(self.ans_var.get()):
            self.check.configure(text = "Correct", font = "Arial")
        else:
            self.check.configure(text = "Incorrect", font = "Arial")

            
        
"""Second class that returns the correct answer"""
class Quiz:
    
    def __init__(self):
        self.ans = ["Manurewa", "Auckland", "Wellington", "Botany", "Mt Wellington"]
    
    def is_answer_correct(self,answer):
        return answer == self.ans[2]


def main():
    root = Tk()
    Interface(root)
    root.mainloop()
 
main()