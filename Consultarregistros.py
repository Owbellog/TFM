from tkinter import ttk
from tkinter import *
from ttkthemes import ThemedTk
import db
import variables
import requests
import json
from json import JSONEncoder
import numpy as np


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)



# class Product:
class Product(Toplevel):
    def __init__(self, window, *args, **kwargs):
        
        self.win = window
        self.win.title('Consulta de registros de campañas')
        
        frame = LabelFrame(self.win, text=' FILTROS CLIENTES: ')
        frame.grid(row = 0, column = 0, columnspan = 4, pady = 15, ipadx = 5, ipady = 5)

        frame4 = LabelFrame(self.win, text=' FILTROS CAMPAÑA: ')    
        frame4.grid(row = 0, column = 0, columnspan = 4, pady = 15, ipadx = 5, ipady = 5)

        
        edu = variables.variables.variableedu()
        oficio = variables.variables.variableoficio()
        gen = variables.variables.variablegen()
        estcivil = variables.variables.variableestcivil()
        
        
        campañas = db.get_campana()

        # VARIABLES COMBOBOX
        global edu_v
        global oficio_v
        global gen_v
        global estcivil_v
        global campaña_v
        global n_varobj
        

        edu_v = StringVar()
        oficio_v = StringVar()
        gen_v = StringVar()
        estcivil_v = StringVar()
        provincias_v = StringVar()
        campaña_v = StringVar()
        n_varobj = StringVar()

        n_varobj = ''

        # LABEL
        ttk.Label(frame,text='Educacion:').grid(row = 4)
        ttk.Label(frame,text='Oficio:').grid(row = 5)
        ttk.Label(frame,text='Genero:').grid(row = 6)
        ttk.Label(frame,text='Estado Civil:').grid(row = 7)
                
        # BOTON AGREGAR PRODUCTO
        ttk.Combobox(frame,values=edu,textvariable =edu_v).grid(row = 4, columnspan=3)
        ttk.Combobox(frame,values=oficio,textvariable =oficio_v).grid(row = 5, columnspan=3)
        ttk.Combobox(frame,values=gen,textvariable =gen_v).grid(row = 6, columnspan=3)
        ttk.Combobox(frame,values=estcivil,textvariable =estcivil_v).grid(row = 7, columnspan=3)
        # ttk.Combobox(frame,values=provincias,textvariable =provincias_v).grid(row = 8, columnspan=3)
        

        

        ttk.Button(frame, text='FILTRAR', command= self.getprospecto_filtro).grid(row = 9, column=0, ipadx=40, pady = 10)
        ttk.Button(frame, text='TODOS LOS REGISTROS', command= self.getprospecto).grid(row = 9,column=1, ipadx=40, pady = 10)
        
        

        # LABEL PARA MENSAJES DE SALIDA
        self.message = Label(self.win,text = '')
        self.message.grid(row = 6, column = 0, columnspan = 5, sticky = W + E, padx = 150)


    #     # TABLA
        frame2 = LabelFrame(self.win, text=' LISTADO DE PRODUCTOS: ')
        frame2.grid(row = 7, column = 0, columnspan = 3, padx = 20, pady = 15)

        self.tree = ttk.Treeview(frame2, height = 8, columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11"))
        self.tree.grid(row = 7, column = 0, columnspan = 2, padx = 20, pady = 10)
        self.tree.column("#0",width= 60,minwidth=60, anchor = CENTER)
        self.tree.column("#1",width= 190,minwidth=190, anchor = CENTER)
        self.tree.column("#2",width= 30,minwidth=30, anchor = CENTER)
        self.tree.column("#3",width= 100,minwidth=100, anchor = CENTER)
        self.tree.column("#4",width= 100,minwidth=100, anchor = CENTER)
        self.tree.column("#5",width= 100,minwidth=100, anchor = CENTER)
        self.tree.column("#6",width= 100,minwidth=100, anchor = CENTER)
        self.tree.column("#7",width= 120,minwidth=120, anchor = CENTER)
        self.tree.column("#8",width= 100,minwidth=100, anchor = CENTER)
        self.tree.column("#9",width= 120,minwidth=120, anchor = CENTER)
        self.tree.column("#10",width= 120,minwidth=120, anchor = CENTER)
        
        self.tree.heading("#0", text="ID", anchor = CENTER)         
        self.tree.heading("#1", text="Nombre Completo", anchor = CENTER)         
        self.tree.heading("#2", text="Años", anchor = CENTER)
        self.tree.heading("#3", text="Ocupación", anchor = CENTER)
        self.tree.heading("#4", text="Estado Civil", anchor = CENTER)
        self.tree.heading("#5", text="Educación", anchor = CENTER)
        self.tree.heading("#6", text="Credito en Mora", anchor = CENTER)
        self.tree.heading("#7", text="Ingresos Promedio", anchor = CENTER)
        self.tree.heading("#8", text="Credito Personal", anchor = CENTER)
        self.tree.heading("#9", text="Credito Hipotecario", anchor = CENTER)
        self.tree.heading("#10", text=n_varobj, anchor = CENTER)
        


        


        # # SCROLL VERTICAL TREEVIEW
        scrolvert = Scrollbar(frame2, command = self.tree.yview)
        scrolvert.grid(row=7, column=2, sticky="nsew")
        self.tree.config(yscrollcommand=scrolvert.set)

        #  # SCROLL HORIZONTAL TREEVIEW
        scrolhoriz = Scrollbar(frame2, command = self.tree.xview, orient='horizontal')
        scrolhoriz.grid(row=12, column=0, columnspan=2, sticky="news")
        self.tree.config(xscrollcommand=scrolhoriz.set)


          # TABLA
        frame3 = LabelFrame(self.win)
        frame3.grid(row = 13, column = 0, padx = 60, pady = 15)
        # BOTONES
        ttk.Button(frame3,text='DELETE',command=self.del_product).grid(row = 14, column = 0, columnspan=2, ipadx = 50, pady = 10)
        ttk.Button(frame3,text='AGREGAR A CAMPAÑA',command=self.guardarcampaña).grid(row = 14, column = 2, columnspan=2, ipadx = 50, pady = 10)
        ttk.Combobox(frame3,values=campañas,textvariable =campaña_v).grid(row = 14,column=4, columnspan=2, ipadx = 50, pady = 10)

        
    def getprospecto(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        self.tree.heading("#10", text="", anchor = CENTER)
        db_rows = db.get_prospectos()
        for row in db_rows:
            self.tree.insert('',0,text = row[0], values = ( row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))        


    def guardarcampaña(self):
        registros = db.guardarcampaña(campaña_v.get())
        for row in registros:
            f = json.loads(Product.obtenervarobj(age=row["años"],job=row["Ocupacion"],marital=row["Estado_civil"],education=row["educacion"],default=row["credito_en_mora"],housing=row["credito_hipotecario"],loan=row["credito_personal"],contact=row["CONTACT"],month=row["MONTH"],day_of_week=row["DAY_OF_WEEK"],duration=row["DURATION"],campaign=row["CAMPAIGN"],pdays=row["PDAYS"],previous=row["PREVIOUS"],poutcome=row["POUTCOME"],empvarrate=row["EMP_VAR_ATE"],conspriceidx=row["CONS_PRICE_IDX"],consconfidx=row["CONS_CONF_IDX"],euribor3m=row["EURIBOR3M"],nremployed=row["NR_EMPLOYED"],id=row["ID"]))
            finalNumpyArray = np.asarray(f)
            db.update_varobj(obj=int(finalNumpyArray[0]),id=int(finalNumpyArray[1]))
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        db_rows = db.get_campaña(campaña_v.get())
        self.tree.heading("#10", text="Var Objetivo", anchor = CENTER)
        for row in db_rows:
            self.tree.insert('',0,text = row[0], values = ( row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))        
        


    def obtenervarobj(age,job,marital,education,default,housing,loan,contact,month,day_of_week,duration,campaign,pdays,previous,poutcome,empvarrate,conspriceidx,consconfidx,euribor3m,nremployed,id):    
        
        payload = f'age={age}'
        payload = payload + f'&job={job}'
        payload = payload + f'&marital={marital}'
        payload = payload + f'&education={education}'
        payload = payload + f'&default={default}'
        payload = payload + f'&housing={housing}'
        payload = payload + f'&loan={loan}'
        payload = payload + f'&contact={contact}'
        payload = payload + f'&month={month}'
        payload = payload + f'&day_of_week={day_of_week}'
        payload = payload + f'&duration={duration}'
        payload = payload + f'&campaign={campaign}'
        payload = payload + f'&pdays={pdays}'
        payload = payload + f'&previous={previous}'
        payload = payload + f'&poutcome={poutcome}'
        payload = payload + f'&empvarrate={empvarrate}'
        payload = payload + f'&conspriceidx={conspriceidx}'
        payload = payload + f'&consconfidx={consconfidx}'
        payload = payload + f'&euribor3m={euribor3m}'
        payload = payload + f'&nremployed={nremployed}'
        payload = payload + f'&id={id}'


        
        url = 'http://127.0.0.1:5001/query-example'

        
        response = requests.get(url, params = payload)
        rget = str(response.text.encode('utf8')).replace('"','').replace("'","")[1:100]

        return rget



    def getprospecto_filtro(self):
        records = self.tree.get_children()
        self.tree.heading("#10", text="", anchor = CENTER)
        for element in records:
            self.tree.delete(element)
        db_rows = db.get_prospectos_filtro(edu=edu_v.get(),oficio=oficio_v.get(),gen=gen_v.get(),estcivil=estcivil_v.get(),provincias=None)
        for row in db_rows:
            self.tree.insert('',0,text = row[0], values = ( row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))        

    def getprospecto_2(self):
        records = self.tree.get_children()
        self.tree.heading("#10", text="", anchor = CENTER)
        for element in records:
            self.tree.delete(element)
        db_rows = db.get_selprospectos()
        
        for row in db_rows:
            self.tree.insert('',0,text = row[0], values = ( row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))        
    


        # ELIMINAR PRODUCTOS
    def del_product(self):
        self.message['text'] = ''
        id = self.tree.item(self.tree.selection())['text']
        
        

        if isinstance(id,str)==True:
            self.message['text'] = 'Por favor selecciona un registro'
            self.message['font'] = ('Consolas',11)
            self.message['bg'] ='#f7d7da'
            self.message['fg'] ='#89312f'
    

        if isinstance(id,int)==True:
        
            db.delete_prospecto(id)
            self.message['text'] = 'Se ha eliminado el registro'
            self.message['font'] = ('Consolas',11)
            self.message['bg'] ='#d4edda'
            self.message['fg'] ='#116158'
    
            self.getprospecto_2()
    
    def volver(self):
        self.win.destroy()
        



# if __name__ == "__main__":
#     window = Tk()#ThemedTk(theme='Equilux')
#     aplication = Product(window)
#     window.mainloop()
