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
        self.space = tk.Label(self, text="                                                     ")
        self.space.pack(side="top")

    # TODO: Left panel will include: member_funcs, plots,  etc.
    def left_panel(self):
        self.left = tk.Frame(self,)
        self.miktar_label = tk.Label(self.left, text="Bulaşık Miktarı %")
        self.miktar_input = tk.Spinbox(self.left, from_=1, to=100)
        self.kirlilik_label = tk.Label(self.left, text="Kirlilik Derecesi %")
        self.kirlilik_input = tk.Spinbox(self.left, from_=1, to=100)
        self.cins_label = tk.Label(self.left, text="Bulaşık Cinsi(Dayanıklılık) %")
        self.cins_input = tk.Spinbox(self.left, from_=1, to=100)

        self.show_input_MF_button = tk.Button(self.left, text="Giriş Üyelik Fonksiyonları", command=dsh.input_plot)
        self.show_output_MF_button = tk.Button(self.left, text="Çıkış Üyelik Fonsiyonları", command=dsh.output_plot)
        self.hesapla = tk.Button(self.left, text="Hesapla", command=self.calculate)
        
        self.left.pack(side="left")
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
        self.right = tk.Frame(self)
        self.zaman_label = tk.Label(self.right, text="Zaman ")
        self.deterjan_label = tk.Label(self.right, text="Deterjan ")
        self.sicaklik_label = tk.Label(self.right, text="Su Sıcaklığı ")
        self.alt_label = tk.Label(self.right, text="Alt Pompa ")
        self.ust_label = tk.Label(self.right, text="Üst Pompa ")
        
        self.show_result_plot_button = tk.Button(self.right, text="Sonuç Gösterimi", command=dsh.show_result_plot)
        self.plot_3d_button = tk.Button(self.right, text="3B Gösterim", command=dsh.show_result_3d)
        
        self.right.pack(side="right")
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
        self.zaman_label["text"]= "Zaman: "+ str(round(dsh.zaman_defuzz, 2)) + "dk"
        self.deterjan_label["text"] = "Deterjan: " + str(round(dsh.deterjan_defuzz, 2)) + "%"
        self.sicaklik_label["text"] = "Su Sıcaklığı: " + str(round(dsh.sicaklik_defuzz, 2)) + "C"
        self.alt_label["text"] = "Alt Pompa: " + str(round(dsh.alt_pompa_defuzz, 2)) + "dvr/dk"
        self.ust_label["text"] = "Üst Pompa: " + str(round(dsh.ust_pompa_defuzz, 2)) + "dvr/dk"
        

#window settings
root = tk.Tk()
root.title("Bulanık Mantık İle Bulaşık Makinesi Uygulaması")
root.geometry("700x300+700+300")
app = ApplicationWindow(master=root)
app.mainloop()

