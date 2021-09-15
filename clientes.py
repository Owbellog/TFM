
import tkinter as tk
from tkinter import ttk
import db as db
from tkcalendar import Calendar
from tkinter import messagebox as msg
import variables




class Cliente(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        
        
        edu = variables.variables.variableedu()
        oficio = variables.variables.variableoficio()
        gen = variables.variables.variablegen()
        estcivil = variables.variables.variableestcivil()
        provincias =variables.variables.variableprovincias()

        ro_w = 1


        ttk.Label(self, text="Primer Nombre:").grid(   row=ro_w,column=0)
        ttk.Label(self, text="Segundo Nombre:").grid(  row=ro_w,column=1)
        ttk.Label(self, text="Primer Apellido:").grid( row=ro_w,column=2)
        ttk.Label(self, text="Segundo Apellido:").grid(row=ro_w,column=3)
        ttk.Entry(self, textvariable = E_P_nombre).grid(row=ro_w+1,column=0, sticky='W',pady=10, padx=20,ipadx=10)
        ttk.Entry(self, textvariable = E_S_nombre).grid(row=ro_w+1,column=1, sticky='W',pady=10, padx=20,ipadx=10)
        ttk.Entry(self, textvariable = E_P_Apellido).grid(row=ro_w+1,column=2, sticky='W',pady=10, padx=20,ipadx=10)
        ttk.Entry(self, textvariable = E_S_Apellido).grid(row=ro_w+1,column=3, sticky='W',pady=10, padx=20,ipadx=10)

        

        ttk.Label(self, text="Identificacion:").grid(   row=ro_w+2,column=0)
        ttk.Label(self, text="Email:").grid(  row=ro_w+2,column=1)
        ttk.Label(self, text="Genero:").grid( row=ro_w+2,column=2)
        ttk.Label(self, text="Estado Civil:").grid(row=ro_w+2,column=3)
        
        ttk.Entry(self, textvariable = E_identificacion).grid(row=ro_w+3,column=0, sticky='W',pady=10, padx=20,ipadx=10)
        ttk.Entry(self, textvariable = E_email).grid(         row=ro_w+3,column=1, sticky='W',pady=10, padx=20,ipadx=10)
        ttk.Combobox(self,textvariable = E_genero,values=gen,state='readonly').grid(row=ro_w+3,column=2, sticky='W',pady=10, padx=20)
        ttk.Combobox(self,textvariable = E_estado_civil,values=estcivil,state='readonly').grid(row=ro_w+3,column=3, sticky='W',pady=10, padx=20)
        

        ttk.Label(self, text="Codigo Postal:").grid(   row=ro_w+4,column=0)
        ttk.Label(self, text="Direccion:").grid(  row=ro_w+4,column=1)
        ttk.Label(self, text="Provincia:").grid( row=ro_w+4,column=2)
        ttk.Label(self, text="Localidad:").grid(row=ro_w+4,column=3)
        ttk.Entry(self, textvariable = E_cp).grid(       row=ro_w+5,column=0, sticky='W',pady=10, padx=20,ipadx=10)
        ttk.Entry(self, textvariable = E_direccion).grid(row=ro_w+5,column=1, sticky='W',pady=10, padx=20,ipadx=10)
        
        ttk.Combobox(self,textvariable = E_provincia,values=provincias,state='readonly').grid(row=ro_w+5,column=2, sticky='W',pady=10, padx=20)
        ttk.Entry(self, textvariable = E_localidad).grid(row=ro_w+5,column=3, sticky='W',pady=10, padx=20,ipadx=10)
        
        

        

        ttk.Label(self, text="Codigo Pais:").grid(   row=ro_w+6,column=0)
        ttk.Label(self, text="Telefono:").grid(  row=ro_w+6,column=1)
        ttk.Label(self, text="Educacion:").grid( row=ro_w+6,column=2)
        ttk.Label(self, text="Ocupación:").grid(row=ro_w+6,column=3)
        
        ttk.Entry(self, textvariable = E_cod_tel_pais).grid(  row=ro_w+7,column=0, sticky='W',pady=10, padx=20,ipadx=10)
        ttk.Entry(self, textvariable = E_telefono).grid(      row=ro_w+7,column=1, sticky='W',pady=10, padx=20,ipadx=10)
        ttk.Combobox(self,textvariable = E_educacion,values=edu,state='readonly').grid(row=ro_w+7,column=2, sticky='W',pady=10, padx=20)
        ttk.Combobox(self,textvariable = E_oficio_laboral,values=oficio,state='readonly').grid(row=ro_w+7,column=3, sticky='W',pady=10, padx=20)
        
        cal = Calendar(self, selectmode = 'day', 
               year = 2021, month = 8, 
               day = 22,date_pattern='y-mm-dd' )

        def grad_date(): 
            date.config(E_fecha_nacimiento.set(cal.get_date()))

        cal.grid(row=ro_w+11,column=2)
        get = ttk.Button(self, text = "Get Date",command = grad_date)
        get.grid(row=ro_w+10,column=0)

        ttk.Label(self, text = "Fecha de Nacimiento").grid(row=ro_w+8,column=0)
        date = ttk.Entry(self, textvariable=E_fecha_nacimiento )
        date.grid(row=ro_w+9,column=0, sticky='W',pady=10, padx=20,ipadx=10) 


        
        

class financiero(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        ro_w = 1
        E_Credito_personal2 = tk.BooleanVar()

        ttk.Label(self, text="Ingresos:").grid(row=ro_w,column=0)
        ttk.Label(self, text="Egresos:").grid(row=ro_w,column=1)
        ttk.Label(self, text="Saldo Promedio:").grid(row=ro_w,column=2)
        ttk.Label(self, text="Numero de tarjetas de credito:").grid(row=ro_w,column=3)
        ttk.Entry(self, textvariable = E_Ingresos).grid(row=ro_w+1,column=0, sticky='W',pady=10, padx=20,ipadx=10)
        ttk.Entry(self, textvariable = E_Egresos).grid(row=ro_w+1,column=1, sticky='W',pady=10, padx=20,ipadx=10)
        ttk.Entry(self, textvariable = E_Saldo_promedio).grid(row=ro_w+1,column=2, sticky='W',pady=10, padx=20,ipadx=10)
        ttk.Entry(self, textvariable = E_N_tarjetas_credito).grid(row=ro_w+1,column=3, sticky='W',pady=10, padx=20,ipadx=10)



        
        ttk.Checkbutton(self,text="Credito Personal",variable=E_Credito_personal,onvalue=1, offvalue=0).grid(row=ro_w+3,column=0, sticky='E',pady=10,ipadx=15)#, textvariable = E_Credito_personal2,onvalue=True, offvalue=False).grid(row=ro_w+3,column=0, sticky='E',pady=10,ipadx=15)
        ttk.Checkbutton(self,text="Credito Hipotecario",variable=E_Credito_hipotecario,onvalue=1, offvalue=0).grid(row=ro_w+3,column=1, sticky='E',pady=10,ipadx=15)
        ttk.Checkbutton(self,text="Credito en Mora",variable=E_Mora,onvalue=1, offvalue=0).grid(row=ro_w+3,column=2, sticky='E',pady=10,ipadx=15)
        
        


class Application(tk.Toplevel):


    def __init__(self, window, *args, **kwargs):
        self.win = window

        global E_P_nombre 
        global E_S_nombre 
        global E_P_Apellido 
        global E_S_Apellido 
        global E_identificacion 
        global E_fecha_nacimiento 
        global E_email 
        global E_genero 
        global E_estado_civil 
        global E_cp 
        global E_direccion 
        global E_provincia 
        global E_localidad 
        global E_cod_tel_pais 
        global E_telefono 
        global E_educacion 
        global E_oficio_laboral 
        global E_Ingresos 
        global E_Egresos 
        global E_Saldo_promedio 
        global E_Credito_hipotecario 
        global E_Credito_personal 
        global E_N_tarjetas_credito 
        global E_Mora 
                
        E_P_nombre = tk.StringVar()
        E_S_nombre =  tk.StringVar()
        E_P_Apellido = tk.StringVar()
        E_S_Apellido = tk.StringVar()
        E_identificacion = tk.StringVar()
        E_fecha_nacimiento = tk.StringVar()
        E_email = tk.StringVar()
        E_genero = tk.StringVar()
        E_estado_civil = tk.StringVar()
        E_cp = tk.StringVar()
        E_direccion = tk.StringVar()
        E_provincia = tk.StringVar()
        E_localidad = tk.StringVar()
        E_cod_tel_pais = tk.StringVar()
        E_telefono = tk.StringVar()
        E_educacion = tk.StringVar()
        E_oficio_laboral = tk.StringVar()  
        E_Ingresos = tk.StringVar()
        E_Egresos =  tk.StringVar()
        E_Saldo_promedio = tk.StringVar()
        E_Credito_hipotecario = tk.IntVar()
        E_Credito_personal = tk.IntVar()
        E_N_tarjetas_credito = tk.IntVar()
        E_Mora = tk.IntVar()

        def guardar():
            respuesta = db.save_cliente( 
                             p_nombre= E_P_nombre.get()
                            ,s_nombre= E_S_nombre.get()
                            ,p_apellido= E_P_Apellido.get()
                            ,s_apellido= E_S_Apellido.get()
                            ,Identificacion= E_identificacion.get()
                            ,Fecha_nacimiento= E_fecha_nacimiento.get()
                            ,Genero= E_genero.get()
                            ,Estado_civil= E_estado_civil.get()
                            ,CP= E_cp.get()
                            ,Direccion_domicilio= E_direccion.get()
                            ,Provincia= E_provincia.get()
                            ,Localidad= E_localidad.get()
                            ,Cod_Tel_Pais= E_cod_tel_pais.get()
                            ,Telefono= E_telefono.get()
                            ,Educacion= E_educacion.get()
                            ,Oficio_laboral= E_oficio_laboral.get()
                            ,email= E_email.get()
                            ,Ingresos = E_Ingresos.get()
                            ,Egresos = E_Egresos.get()
                            ,Saldo_promedio = E_Saldo_promedio.get()
                            ,N_tarjetas = E_N_tarjetas_credito.get()
                            ,credito_personal = E_Credito_personal.get()
                            ,credito_hipotecario = E_Credito_hipotecario.get()
                            ,credito_en_mora = E_Mora.get()
                            )
            msg.showinfo(message=respuesta)

        self.win.title("Panel de pestañas en Tcl/Tk")
        
        notebook = ttk.Notebook(self.win)
        
        t1 = Cliente(notebook)
        notebook.add(t1,text="Información Personal")
        t2 = financiero(notebook)
        notebook.add(t2,text="Información Financiera")
        
        notebook.pack(padx=10, pady=10)

        tk.Button(self.win,text='Guardar', command= guardar).pack()


