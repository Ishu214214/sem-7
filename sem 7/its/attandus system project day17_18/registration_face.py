# import tkinter as ttk
# from tkinter import font
# from login_admin import submit 
# #import login_admin as l
# reg_app=ttk.Tk()
# reg_app.geometry('800x800')
# reg_app.title('Registration Face')
# font_=font.Font(size=20)

# ttk.Label(reg_app,text='Face Recognition System',font=font_).pack()

# #print(l.submit)
# reg_app.mainloop()



#live image capturing

import cv2
import face_recognition as fr
import pandas as pd
import numpy as np

#we are making the data frame on saving the image detail becous image jo hoga who list ka form ma aaya ga 1D array
def register(name):

    fname='feature.csv'
    try:
        df=pd.read_csv(fname)
    except:
        df=pd.DataFrame({'name':[],'enc':[]})


    counter =0
    names=[]
    feats=[]
    #name=input('Enter the name: ')


    fd=cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalface_default.xml')
    vid=cv2.VideoCapture(0)
    while True:
        ack,img=vid.read()
        if ack:
            #do the entire processing
            faces=fd.detectMultiScale(img,1.2,2,minSize=(150,150))
            #faces= [(x,y,w,h),(x2,y2,w2,h2)]

            if len(faces)==1:
                x,y,w,h=faces[0]
                faces_img=img[y:y+h,x:x+w,:].copy()
                face_enc=fr.face_encodings(faces_img)

                if len(face_enc)==1:
                    counter+=1
                    names+=[name]
                    feats+=[face_enc[0].tolist()]

                if counter==20:
                    f=pd.DataFrame({'name':names, 'enc':feats})  
                    df=pd.concat([df,f],axis=0,ignore_index=True)  
                    df.to_csv(fname)
                    break


            cv2.imshow('preview',img)  #depends on requirement
            key=cv2.waitKey(1)
            if key==ord('x'):
                break
    cv2.destroyAllWindows();  cv2.waitKey(1)
    vid.release()