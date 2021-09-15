import tkinter as tk
import os
from PIL import ImageTk, Image
from tkinter import messagebox as msg
import Camara
import menu




path = os.path.dirname(os.path.abspath(__file__))   
path2 = f"{path}\\img\\new.jpg"

class main(tk.Frame):

    def __init__(self,parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("CRM Project TFM")
        global e_login
        e_login = tk.StringVar()

        tk.Label(self,text="Usuario:").pack(side = tk.TOP, expand=True)
        tk.Entry(self, textvariable = e_login).pack(side = tk.TOP, expand=True)
        login = tk.Button(self,text="Login",command=self.login )
        login.pack(side = tk.TOP, expand=True)
        self.parent.state('zoomed')
        
    

    def login(self):
        mensaje = Camara.camara.captura_imagen_login(e_login.get())
        if mensaje== "Imagen Verificada":
            menu.menu(self.parent)
        else: 
            msg.showinfo(message="Su rostro no concuerda con el usuario indicado")

if __name__ == '__main__':
    ventana = tk.Tk()
    imagen = ImageTk.PhotoImage(Image.open(f'{path}\\img\\logo.png'))
    tk.Label(ventana, image=imagen,width=450,height=450).pack(side='top', fill='both', expand='yes')
    main(ventana).pack(side="top", fill="both", expand=True)
    ventana.mainloop()
    
