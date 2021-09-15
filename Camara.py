from PIL import ImageTk, Image
import os
import cv2
import imutils
import db
from deepface import DeepFace

path = os.path.dirname(os.path.abspath(__file__))





class camara():
    
    def captura_imagen():
        camara_port=0
        cap = cv2.VideoCapture(camara_port, cv2.CAP_DSHOW)
        user_reg_img = f"{path}\img\\new"
        user_reg_img2 = f"{path}\img\\new2"
        img = f"{user_reg_img}.jpg"
        img2 = f"{user_reg_img2}.jpg"
        os.remove(img)
        os.remove(img2)
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
        reconocer = 0
        while True:
            ret, frame = cap.read()
            if ret == False: break
            frame =  imutils.resize(frame, width=640)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            auxFrame = frame.copy()
            faces = faceClassif.detectMultiScale(gray,1.3,5,minSize=(200, 200))
            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                rostro = auxFrame[y:y+h,x:x+w]
                rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
                reconocer = reconocer + 1
            cv2.imshow("Registro Facial", frame)
            if cv2.waitKey(1) == 27:
                # if cv2.waitKey(1) == 27 or reconocer == 5:
                break
        cv2.imwrite(img, frame)
        cv2.imwrite(img2, frame)
        cap.release()
        cv2.destroyAllWindows()
        

    def captura_imagen_login(usuario):
        camara_port=0
        cap = cv2.VideoCapture(camara_port, cv2.CAP_DSHOW)
        path2 = f"{path}\img"
        user_reg_img_login = f"{path}\img\\login"
        user_reg_img_user = f"{path}\img\\cmp"
        img_login = f"{user_reg_img_login}.jpg"
        img = f"{user_reg_img_user}.jpg"
        
        
        if os.path.exists(img_login) == True:
            os.remove(img_login)
        if os.path.exists(img) == True:
            os.remove(img)
        
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
        reconocer = 0
        while True:
            ret, frame = cap.read()
            if ret == False: break
            frame =  imutils.resize(frame, width=640)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            auxFrame = frame.copy()
            faces = faceClassif.detectMultiScale(gray,1.3,5,minSize=(200, 200))
            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                rostro = auxFrame[y:y+h,x:x+w]
                rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
                reconocer = reconocer + 1
            cv2.imshow("Registro Facial", frame)
            if cv2.waitKey(1) == 27 or reconocer == 20:
                
                break
        
        
        cv2.imwrite(img_login, frame)
        cap.release()
        cv2.destroyAllWindows()
        res_db = db.getUser(usuario)#, path + img_user)
        if(res_db["affected"]):
            face_reg = cv2.imread(img, 0)
            face_log = cv2.imread(img_login, 0)

            backends = ['opencv', 'ssd', 'dlib', 'mtcnn']
            obj = DeepFace.verify(img, img_login, detector_backend = 'mtcnn')
            result = obj['verified']
            
                
            if result == True:
                mensaje = "Imagen Verificada"
             
            else:
                mensaje = "Vuelva a intentarlo"
            
        else:
            mensaje = "¡Error! Usuario no encontrado"
        
        return mensaje


    

    def abrir_imagen():
        path2 = f"{path}\\img\\new.jpg"
        img = ImageTk.PhotoImage(Image.open(path2))
        return img



