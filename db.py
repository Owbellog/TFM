import pyodbc 
import os
import variables


def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData
    
def write_file(data, path):
    with open(path, 'wb') as file:
        file.write(data)


def connectsql():
    direccion_servidor = 'localhost\BI2019'
    nombre_bd = "TFM"
    nombre_usuario = "sa"
    password = "1q2w3e4r*"
    conn = pyodbc.connect('Driver={SQL Server};Server='+ direccion_servidor +';Database='+ nombre_bd +'; UID='+ nombre_usuario +';PWD='+ password +'; Encrypt=no;')
    return conn

def get_prospectos_filtro(edu,oficio,gen,estcivil,provincias=None):
    conn = connectsql()
    edu = variables.variables.eduindicador(edu)
    oficio = variables.variables.oficioindicador(oficio)
    estcivil = variables.variables.estcivilindicador(estcivil)
    cursor = conn.cursor()
    cursor.execute("CR.SP_GETCLIENT_FIL ?,?,?,?,?", edu,oficio,gen,estcivil,provincias)
    outp = cursor.fetchall()
    conn.commit()
    conn.close()
    return outp


def get_prospectos():
    conn = connectsql()
    cursor = conn.cursor()
    cursor.execute("CR.SP_GETCLIENT")
    outp = cursor.fetchall()
    conn.commit()
    conn.close()
    return outp

def guardar_campañanew(nombre,fechaini,fechafin,estado):
    conn = connectsql()
    cursor = conn.cursor()
    cursor.execute("CR.SPGUARDARCAMPAÑANEW ?,?,?,?",nombre,fechaini,fechafin,estado)
    outp = cursor.fetchall()
    conn.commit()
    conn.close()
    return outp


def guardarcampaña(campaña, one=False):
    conn = connectsql()
    cursor = conn.cursor()
    cursor.execute('CR.SPGUARDARCAMPAÑA ?',campaña)
    r = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    conn.commit()
    conn.close()
    return (r[0] if r else None) if one else r

def get_campaña(campaña, one=False):
    conn = connectsql()
    cursor = conn.cursor()
    cursor.execute('CR.SPGETREGISTROCAMPAÑA ?',campaña)
    outp = cursor.fetchall()
    conn.commit()
    conn.close()
    return outp


    

def get_campana(args=(), one=False):
    conn = connectsql()
    cursor = conn.cursor()
    cursor.execute("exec CR.SPCAMPAÑAS")
    r=[]
    for row in cursor.fetchall():
        r.append(row[0])
    cursor.connection.close()
    return r


def update_varobj(id,obj,args=(), one=False):
    conn = connectsql()
    cursor = conn.cursor()
    cursor.execute('exec CR.SPUPDATEOBJ ?,?',id,obj)
    conn.commit()
    conn.close()
    


def get_selprospectos():
    conn = connectsql()
    cursor = conn.cursor()
    cursor.execute("CR.SP_selprospecto")
    outp = cursor.fetchall()
    conn.commit()
    conn.close()
    return outp


def delete_prospecto(ID):
    conn = connectsql()
    cursor = conn.cursor()
    cursor.execute("CR.SP_DELCLIENT ?",ID)
    conn.commit()
    conn.close()



def save_data(      p_nombre
                    ,s_nombre
                    ,p_apellido
                    ,s_apellido
                    ,id
                    ,email
                    ,login
                    ,passw
                    ,photo

                    ):
    conn = connectsql()
    cursor = conn.cursor()
    pic = convertToBinaryData(photo)
    cursor.execute('exec CR.uspAddUser ?,?,?,?,?,?,?,?,?'
                    ,login
                    ,passw
                    ,p_nombre
                    ,p_apellido
                    ,s_nombre
                    ,s_apellido
                    ,email
                    ,pic
                    ,id
                    )
    outp = cursor.fetchone()
    conn.commit()
    conn.close()
    return outp



def save_cliente(    p_nombre
                    ,s_nombre
                    ,p_apellido
                    ,s_apellido
                    ,Identificacion
                    ,Fecha_nacimiento
                    ,Genero
                    ,Estado_civil
                    ,CP
                    ,Direccion_domicilio
                    ,Provincia
                    ,Localidad
                    ,Cod_Tel_Pais
                    ,Telefono
                    ,Educacion
                    ,Oficio_laboral
                    ,email
                    ,Ingresos
                    ,Egresos
                    ,Saldo_promedio
                    ,N_tarjetas
                    ,credito_personal
                    ,credito_hipotecario
                    ,credito_en_mora
                    
                    ):
    conn = connectsql()
    cursor = conn.cursor()
    cursor.execute('exec CR.SP_NEWCLIENT ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?'
                    ,p_nombre
                    ,s_nombre
                    ,p_apellido
                    ,s_apellido
                    ,Identificacion
                    ,Fecha_nacimiento
                    ,Genero
                    ,Estado_civil
                    ,CP
                    ,Direccion_domicilio
                    ,Provincia
                    ,Localidad
                    ,Cod_Tel_Pais
                    ,Telefono
                    ,Educacion
                    ,Oficio_laboral
                    ,email
                    ,Ingresos
                    ,Egresos
                    ,Saldo_promedio
                    ,N_tarjetas
                    ,credito_personal
                    ,credito_hipotecario
                    ,credito_en_mora
                    )
    
    outp2 = cursor.fetchall()
    conn.commit()
    conn.close()
    return outp2[0][0]






def getUser(name):
    id = 0
    rows = 0
    
    path = os.path.dirname(os.path.abspath(__file__))
    path2 = f"{path}\\img\\cmp.jpg"
    try:
        con = connectsql()
        cursor = con.cursor()
        cursor.execute('exec CR.getuser ?', name)
        records = cursor.fetchall()
        
        for row in records:
            id = row[0]
            write_file(row[1], path2)
        rows = len(records)
    except pyodbc.Error as e:
        print(f"Failed to read image: {e}")
    finally:
        
        cursor.close()
        con.close()
    return {"id": id, "affected": rows}


