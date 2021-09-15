import tkinter as tk
import Camara as cap
from tkinter import messagebox as msg
import os
from PIL import ImageTk, Image
import db

path = os.path.dirname(os.path.abspath(__file__))



class recaptura(tk.Toplevel):
    def __init__(self, parent, img2 = None, *args, **kwargs):
        super().__init__(parent, img2 = None, *args, **kwargs)
        self.parent = parent
        self.title("Registro de Usuarios")
        self.geometry("568x550")
        self.protocol("WM_DELETE_WINDOW", self.volver)
        if img2 == None or img2== "0":
            path2 = f"{path}\\img\\x.png"
        if img2 == "1":
            path2 = f"{path}\\img\\new.jpg"
            #path2cara = f"{path}\\img\\new2.jpg"
        
        image = Image.open(path2)
        [imageSizeWidth, imageSizeHeight] = image.size
        n=0.5
        same = True
        ro_w= 1
        tk.Label(self,text="REGISTRO USUARIOS").grid(row=0,pady=20)
        f= ('Times', 14)
        
        newImageSizeWidth = int(imageSizeWidth*n)
        if same:
            newImageSizeHeight = int(imageSizeHeight*n) 
        else:
            newImageSizeHeight = int(imageSizeHeight/n) 

        image = image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS) 

        imagen = ImageTk.PhotoImage(image)
        
        btn = tk.Button(self,text="n", image=imagen,width=250,height=250)
        btn.img_ref = imagen
        btn.place(x=300,y=75)
        
        E_P_nombre = tk.StringVar()
        E_S_nombre =  tk.StringVar()
        E_P_Apellido = tk.StringVar()
        E_S_Apellido = tk.StringVar()
        E_identificacion = tk.StringVar()
        E_email = tk.StringVar()
        E_usuario = tk.StringVar()
        E_password = tk.StringVar()

        def guardarn():
            respuesta = db.save_data(
            p_nombre = E_P_nombre.get(),
            s_nombre = E_S_nombre.get(),
            p_apellido = E_P_Apellido.get(),
            s_apellido = E_S_Apellido.get(),
            id = E_identificacion.get(),
            email = E_email.get(),
            login = E_usuario.get(),
            passw = E_password.get(),
            photo = path2
            #photocara = path2cara
            )
            msg.showinfo(message=respuesta)
            self.refresh(img2="0")

            
                        

        tk.Label(self,text="Primer Nombre:").grid(row=ro_w,column=0, sticky='W', pady=10)
        tk.Entry(self, textvariable = E_P_nombre).grid(row=ro_w,column=1, sticky='W',pady=10, padx=20)
        
        tk.Label(self,text="Segundo Nombre:").grid(row=ro_w+1,column=0, sticky='W',pady=10)
        tk.Entry(self,textvariable = E_S_nombre ).grid(row=ro_w+1,column=1, pady=10, padx=20)

        tk.Label(self,text="Primer Apellido:").grid(row=ro_w+2,column=0,sticky='W', pady=10)
        tk.Entry(self,textvariable = E_P_Apellido).grid(row=ro_w+2,column=1,sticky='W', pady=10, padx=20)

        tk.Label(self,text="Segundo Apellido:").grid(row=ro_w+3,column=0,sticky='W', pady=10)
        tk.Entry(self,textvariable = E_S_Apellido).grid(row=ro_w+3,column=1,sticky='W', pady=10, padx=20)

        tk.Label(self,text="DNI/NIE:").grid(row=ro_w+4,column=0, sticky='W',pady=10)
        tk.Entry(self,textvariable = E_identificacion ).grid(row=ro_w+4,column=1,sticky='W', pady=10, padx=20)

        tk.Label(self,text="Email:").grid(row=ro_w+5,column=0,sticky='W', pady=10)
        tk.Entry(self,textvariable = E_email).grid(row=ro_w+5,column=1, pady=10, padx=20)

        tk.Label(self,text="Usuario:").grid(row=ro_w+6,column=0,sticky='W', pady=10)
        tk.Entry(self,textvariable = E_usuario).grid(row=ro_w+6,column=1, pady=10, padx=20)

        tk.Label(self,text="Password:").grid(row=ro_w+7,column=0,sticky='W', pady=10)
        tk.Entry(self,show='*',textvariable = E_password).grid(row=ro_w+7,column=1, pady=10, padx=20)



        tk.Button(self, text="Guardar",width=12,command= guardarn ).grid(row=ro_w+8,column=0,pady=10, padx=20)
        tk.Button(self, text="Capturar Foto",width=12, command = self.capturar ).grid(row=ro_w+8,column=1,pady=10, padx=20)
        tk.Button(self, text="Salir",width=12,command= self.volver ).grid(row=ro_w+8,column=2,pady=10, padx=20)

        # self.resizable (0,0)
        # self.parent.withdraw()

    
                                                                                        
    

    def capturar(self):
        cap.camara.captura_imagen()
        self.refresh(img2="1")

    
    def refresh(self,img2):
        self.destroy()
        self.__init__(self.parent,img2)
        


    def volver(self):
        self.parent.deiconify()
        self.parent.state('zoomed')
        self.destroy()

