import tkinter as tk
import dishwasher

class ApplicationWindow(tk.Frame):

    #const
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.left_panel()
        self.right_panel()
        self.top_panel()
        self.mid_panel()


    # TODO: Left panel will include: member_funcs, plots,  etc.
    def left_panel(self):
        # Button "Show Plot"
        self.plot = tk.Button(self, text="Show Plot", command=self.show_plot)
        self.plot.pack(side="top")
        

        # Button Quit
        #self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        #self.quit.pack(side="bottom")

    
    # TODO: Rigth panel will include: geneleral info like fuzzy defuzzy functions and  formulas.
    def right_panel(self):
        #jasdf
        print()


    # washing machine start button input out
    def mid_panel(self):
        print()


    def top_panel(self):
        print()


    

    def show_plot(self):
        print("plot is showing!")



#window settings
root = tk.Tk()
root.geometry("500x500+700+300")
app = ApplicationWindow(master=root)
app.mainloop()

