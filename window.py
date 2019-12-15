import tkinter as tk
import dishwasher as dsh

class ApplicationWindow(tk.Frame):

    #const
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self)
        frame.pack(side="left")
        
        self.left_panel()
        self.right_panel()

    # TODO: Left panel will include: member_funcs, plots,  etc.
    def left_panel(self):
        self.miktar_label = tk.Label(self, text="Bulaşık Miktarı %")
        self.miktar_input = tk.Spinbox(self, from_=1, to=100)
        self.kirlilik_label = tk.Label(self, text="Kirlilik Derecesi %")
        self.kirlilik_input = tk.Spinbox(self, from_=1, to=100)
        self.cins_label = tk.Label(self, text="Bulaşık Cinsi(Dayanıklılık) %")
        self.cins_input = tk.Spinbox(self, from_=1, to=100)

        self.show_input_MF_button = tk.Button(self, text="Giriş Üyelik Fonksiyonları", command=dsh.input_plot)
        self.show_output_MF_button = tk.Button(self, text="Çıkış Üyelik Fonsiyonları", command=dsh.output_plot)
        self.hesapla = tk.Button(self, text="Hesapla", command=self.calculate)
        
        
        self.miktar_label.pack()
        self.miktar_input.pack()
        self.kirlilik_label.pack()
        self.kirlilik_input.pack()
        self.cins_label.pack()
        self.cins_input.pack()
        self.show_input_MF_button.pack()
        self.show_output_MF_button.pack()
        self.hesapla.pack()

    
    # TODO: Rigth panel will include: geneleral info like fuzzy defuzzy functions and  formulas.
    def right_panel(self):
        #self.zaman_label_text = StringVar()
        #self.zaman_label_text.set("Zaman")

        self.zaman_label = tk.Label(self, text="Zaman Output")
        self.deterjan_label = tk.Label(self, text="Deterjan Output")
        self.sicaklik_label = tk.Label(self, text="Su Sıcaklığı Output")
        self.alt_label = tk.Label(self, text="Alt Pompa Output")
        self.ust_label = tk.Label(self, text="Üst Pompa Output")
        
        self.show_result_plot_button = tk.Button(self, text="Sonuç Gösterimi", command=dsh.show_result_plot)
        self.plot_3d_button = tk.Button(self, text="3B Gösterim", command=dsh.show_result_3d)
        
        self.zaman_label.pack()
        self.deterjan_label.pack()
        self.sicaklik_label.pack()
        self.alt_label.pack()
        self.ust_label.pack()
        self.show_result_plot_button.pack()
        self.plot_3d_button.pack()
        print()
        
    def calculate(self):
        
        dsh.input_miktar = float(self.miktar_input.get())
        dsh.input_kirlilik = float(self.kirlilik_input.get())
        dsh.input_cins = float(self.cins_input.get())
        dsh.calculate()
        self.zaman_label["text"]= "Zaman: "+ str(dsh.zaman_defuzz)
        self.deterjan_label["text"] = "Deterjan: " + str(dsh.deterjan_defuzz)
        self.sicaklik_label["text"] = "Su Sıcaklığı: " + str(dsh.sicaklik_defuzz)
        self.alt_label["text"] = "Alt Pompa: " + str(dsh.alt_pompa_defuzz)
        self.ust_label["text"] = "Üst Pompa: " + str(dsh.ust_pompa_defuzz)
        

#window settings
root = tk.Tk()
root.geometry("500x500+700+300")
app = ApplicationWindow(master=root)
app.mainloop()

