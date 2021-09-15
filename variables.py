global edu
global oficio
global gen
global estcivil
global provincias


class variables:
    def variableedu():
        edu = ['','Sin Datos','Universitario','Bachillerato','ESO','Master','Primaria','Secundaria','Sin Estudios']
        return edu
    def eduindicador(texto):
        switcher = {
            'Sin Datos':0,
            'Universitario':1,
            'Bachillerato':2,
            'ESO':3,
            'Master':4,
            'Primaria':5,
            'Secundaria':6,
            'Sin Estudios':7
            }

        return switcher.get(texto, "")

    


    def variableoficio():
        oficio = ['','Sin Informacion',
            'Administrativo',
            'Obrero',
            'Tecnico',
            'Servicios',
            'Administradores',
            'Jubilado',
            'Empresario',
            'Autonomo',
            'Empreada Domestica',
            'Desempleado',
            'Estudiante']
        return oficio
    
    def oficioindicador(texto):
        switcher = {
            'Sin Informacion':0,
            'Administrativo':1,
            'Obrero':2,
            'Tecnico':3,
            'Servicios':4,
            'Administradores':5,
            'Jubilado':6,
            'Empresario':7,
            'Autonomo':8,
            'Empreada Domestica':9,
            'Desempleado':10,
            'Estudiante':11
                       
            }

        return switcher.get(texto, "")


    def variablegen():
        gen = ['','M','F']
        return gen


    def variableestcivil():
        estcivil = ['','Casado','Soltero','Separado','Desconocido']
        return estcivil


    def estcivilindicador(texto):
        switcher = {
            'Casado':1,
            'Soltero':2,
            'Separado':3,
            'Desconocido':0
                       
            }

        return switcher.get(texto, "")
    
    
        
    def variableprovincias():
        provincias =['',"Álava", "Albacete", "Alicante", "Almería", "Asturias", "Ávila", "Badajoz", "Barcelona", "Burgos", "Cáceres", "Cádiz", "Cantabria", "Castellón", "Ciudad Real", "Córdoba", "Cuenca", "Gerona", "Granada", "Guadalajara", "Guipúzcoa", "Huelva", "Huesca", "Islas Baleares", "Jaén", "La Coruña", "La Rioja", "Las Palmas", "León", "Lérida", "Lugo", "Madrid", "Málaga", "Murcia", "Navarra", "Orense", "Palencia", "Pontevedra", "Salamanca", "Santa Cruz de Tenerife", "Segovia", "Sevilla", "Soria", "Tarragona", "Teruel", "Toledo", "Valencia", "Valladolid", "Vizcaya", "Zamora", "Zaragoza"]
        return provincias
        


