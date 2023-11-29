# import tkinter as ttk
# from tkinter import font
# att_app=ttk.Tk()
# att_app.geometry('800x800')
# att_app.title('Attendance System')
# font_=font.Font(size=20)

# ttk.Label(att_app,text='Face Recognition System',font=font_).pack(expand=True)





# att_app.mainloop()


#live image capturing

import cv2
import face_recognition as fr
import pandas as pd
import numpy as np

#we are making the data frame on saving the image detail becous image jo hoga who list ka form ma aaya ga 1D array

def attanduss():
    fname='feature.csv'
    at_file="attendance.csv"
    try:
        at=pd.read_csv(at_file)
    except :
        at=pd.DataFrame({'name':[],'timestamp':[]})

    try:
        df=pd.read_csv(fname)
    except:
        print('Face Data is not found')
    else:



        fd=cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalface_default.xml')
        vid=cv2.VideoCapture(0)
        count=0
        old_name=''
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
                        feats_data=df['enc'].apply(lambda x:eval(x)).values.tolist()

                        matches=fr.compare_faces(face_enc, np.array(feats_data))
                        if True in matches:
                            match_ind=matches.index(True)
                            name=df['name'][match_ind]
                        else:
                            name='UnKnown'  

                        if old_name==name:
                            count+=1
                        else:
                            count==1
                            old_name=name
                        if count==5 and name!='UnKnown': 
                            from datetime import datetime as dt
                            new_at=pd.DataFrame({'name':[name],'timestamp':(str(dt.now()))})
                            at=pd.concat([at,new_at],ignore_index=True,axis=0)
                            at.to_csv(at_file,index=False)

                            print("Attendance Captured")
                            break

                        cv2.putText(img,name,(150,150)  ,   
                            cv2.FONT_HERSHEY_PLAIN,10,(0,0,255),5)



                cv2.imshow('preview',img)  #depends on requirement
                key=cv2.waitKey(1)
                if key==ord('x'):
                    break
    cv2.destroyAllWindows();  cv2.waitKey(1)
    vid.release()