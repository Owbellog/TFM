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
class Campaña(Toplevel):
    def __init__(self, window, *args, **kwargs):
        
        self.win = window
        self.win.title('Consulta de registros de campañas')

        frame = LabelFrame(self.win, text=' CREACIÓN DE CAMPAÑAS: ')
        frame.grid(row = 0, column = 0, columnspan = 4, pady = 15, ipadx = 5, ipady = 5)

        global e_nombrecampaña
        global fecha_ini
        global fecha_fin
        global activo
        global activo_k

        e_nombrecampaña = StringVar()
        fecha_ini = StringVar()
        fecha_fin = StringVar()
        activo = StringVar()
        activo_k = ["Activo","Inactivo"]



        ttk.Label(frame,text='NOMBRE CAMPAÑA:').grid(row = 4, column = 0)
        ttk.Label(frame,text='FECHA INICIAL:').grid(row = 5, column = 0)
        ttk.Label(frame,text='FECHA FIN:').grid(row = 6, column = 0)
        ttk.Label(frame,text='ACTIVO:').grid(row = 7, column = 0)

        ttk.Entry(frame, textvariable = e_nombrecampaña).grid(row = 4, column=1)
        ttk.Entry(frame, textvariable = fecha_ini).grid(row = 5, column=1)
        ttk.Entry(frame, textvariable = fecha_fin).grid(row = 6, column=1)
        ttk.Combobox(frame,values=activo_k,textvariable =activo).grid(row = 7, column=1)

        ttk.Button(frame, text='GUARDAR',command=self.guardar_campaña).grid(row = 9, column=0,columnspan=2, ipadx=40, pady = 10)

    def guardar_campaña(self):
        db.guardar_campañanew()
    
if __name__ == "__main__":
    window = Tk()
    aplication = Campaña(window)
    window.mainloop()