import tkinter as tk
import clientes
import Recapturar
import Consultarregistros
import Campanas


class menu(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.title("Menu")
        self.geometry("568x550")
        self.protocol("WM_DELETE_WINDOW", self.volver)  
        self.menubar = tk.Menu()

        self.Archivo =  tk.Menu( tearoff=0)
        self.menubar.add_cascade(label="Archivo",menu=self.Archivo)
        self.Archivo.add_command(label="Salir",command=self.salir )

        
        
        self.filemenu = tk.Menu( tearoff=0)
        self.menubar.add_cascade(label="Clientes",menu=self.filemenu)
        self.filemenu.add_command(label="Agregar Clientes", command=self.ingresarcn)
        self.filemenu.add_command(label="Consultar Clientes", command=self.consultarcn)
        
        
        
        self.admin =  tk.Menu( tearoff=0)
        self.menubar.add_cascade(label="Administrar",menu=self.admin)
        self.admin.add_command(label="Usuarios Nuevos", command=self.recapturar)
        
        self.campaing =  tk.Menu( tearoff=0)
        self.menubar.add_cascade(label="Campañas",menu=self.campaing)
        self.campaing.add_command(label="Agregar Campaña Nueva", command = self.get_Campaña)


        
        self.configure(menu=self.menubar)
        
        
        self.state('zoomed')
        self.parent.withdraw()

            
    
    def ingresarcn(self):
        for widget in self.winfo_children():
            widget.destroy()
        clientes.Application(self)

    def consultarcn(self):
        for widget in self.winfo_children():
            widget.destroy()
        Consultarregistros.Product(self)

    def get_Campaña(self):
        for widget in self.winfo_children():
            widget.destroy()
        Campanas.Campaña(self)
    
    def recapturar(self):
        Recapturar.recaptura(self,img2 = None)
    
    def salir(self):
        self.parent.destroy()


    def volver(self):
        self.parent.destroy()