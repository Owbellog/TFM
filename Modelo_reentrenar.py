import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.linear_model import LinearRegression
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
#from pandas.tools.plotting import scatter_matrix
from sklearn.metrics import accuracy_score, auc, confusion_matrix, f1_score, precision_score, recall_score, roc_curve
import pyodbc 


def connectsql():
    direccion_servidor = 'localhost\BI2019'
    nombre_bd = "TFM"
    nombre_usuario = "sa"
    password = "1q2w3e4r*"
    conn = pyodbc.connect('Driver={SQL Server};Server='+ direccion_servidor +';Database='+ nombre_bd +'; UID='+ nombre_usuario +';PWD='+ password +'; Encrypt=no;')
    return conn

def get_prospectos():
    conn = connectsql()
    cursor = conn.cursor()
    cursor.execute("CR.SP_ALLDATOS")
    outp = cursor.fetchall()
    conn.commit()
    conn.close()
    return outp


datos=pd.DataFrame(get_prospectos())

var_obj=datos['y']

var_obj = var_obj.replace('no', 'True')#convertimos var_obj en binario
var_obj = var_obj.replace('yes', 'False')

var_obj = var_obj.replace('True', 0)
var_obj = var_obj.replace('False', 1)

datos=datos.drop(['y'], axis=1)

datos['var_obj'] = var_obj

pd.set_option('display.max_columns',None)#Sin esto no se ven todas las columnas

# Pasamos las variables categóricas a numéricas

datos_tratado=datos

datos_tratado.month.replace(('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'),
                      (1,2,3,4,5,6,7,8,9,10,11,12),inplace=True)

datos_tratado.default.replace(('unknown','yes','no'),(0,1,2),inplace=True)

datos_tratado.housing.replace(('unknown','yes','no'),(0,1,2),inplace=True)

datos_tratado.loan.replace(('unknown','yes','no'),(0,1,2),inplace=True)

datos_tratado.education.replace(('unknown','university.degree','high.school','basic.9y',
                                 'professional.course','basic.4y','basic.6y','illiterate'),
                                (0,1,2,3,4,5,6,7),inplace=True)

datos_tratado.job.replace(('unknown','admin.','blue-collar','technician',
                            'services','management','retired','entrepreneur',
                           'self-employed','housemaid','unemployed','student'),
                                (0,1,2,3,4,5,6,7,8,9,10,11),inplace=True)

datos_tratado.marital.replace(('unknown','married','single','divorced'),(0,1,2,3),inplace=True)

datos_tratado.contact.replace(('cellular','telephone'),(1,2),inplace=True)

datos_tratado.day_of_week.replace(('mon','tue','wed','thu','fri'),(1,2,3,4,5), inplace = True)

datos_tratado.poutcome.replace(('nonexistent','failure','success'),(1,2,3),inplace=True)

def saca_metricas(y1, y2):
    print('matriz de confusión')
    print(confusion_matrix(y1, y2))
    print('accuracy')
    print(accuracy_score(y1, y2))
    print('precision')
    print(precision_score(y1, y2))
    print('recall')
    print(recall_score(y1, y2))
    print('f1')
    print(f1_score(y1, y2))
    false_positive_rate, recall, thresholds = roc_curve(y1, y2)
    roc_auc = auc(false_positive_rate, recall)
    print('AUC')
    print(roc_auc)
    plt.plot(false_positive_rate, recall, 'b')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.title('AUC = %0.2f' % roc_auc)  

    #Separamos el dataset en train y test
#Quitamos var_obj también
datos_tratado=datos_tratado.drop(['var_obj'], axis=1)
X_train, X_test, y_train, y_test = train_test_split( datos_tratado,
                                                    var_obj,
                                                    test_size=0.2,
                                                    random_state=42,
                                                    stratify = var_obj)

model2 = RandomForestClassifier(max_depth=2, random_state=0)
model2.fit(X_train, y_train)

y_pred = model2.predict(X_test)
saca_metricas(y_test, y_pred)


filename = 'model2.pickel'
pickle.dump(model2, open(filename, 'wb'))