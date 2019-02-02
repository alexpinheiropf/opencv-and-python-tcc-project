#!/usr/bin/env python
import numpy as np
import mahotas
import cv2
import os
if __name__ == '__main__':
    import sys, getopt
    cap = cv2.VideoCapture('../Videomonitoramento/Dia_29-10/13.45_a_14.00.mp4')
    car_cascade = cv2.CascadeClassifier("cascade.xml")
    paused = False
    step = True
    rota1 = 0
    rota2 = 0
    rota3 = 0

    while True:

        if not paused or step:
            flag, img = cap.read()
            if img.any() == None: break

            height, width, c = img.shape
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cars = car_cascade.detectMultiScale(gray, 1.3, 5)
#            carCont = 1
#            for (x,y,w,h) in cars:

#                carro = cv2.rectangle(img,(x,y),(x+45,y+45),(0,0,255),1)
#                car = cv2.putText(img,"Car: " + str(carCont)+ ' - x: '+str(x)+ 'y: '+str(y),(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255))
#                if (x>148 and x<=310) and (y>=47 and y<=400):
#                if (x>320 and x<=420) and (y>=40 and y<=100):
#                    rota1 = carCont + 1

#                    os.system('cls' if os.name == 'nt' else 'clear')
#                    print('Rota1:', rota1)
#                    print('Rota2:', rota2)
#                    print('Rota3:', rota3)
            carCont = 0
            for (x,y,w,h) in cars:
                carCont+=1
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                cv2.putText(img,"Car:" + str(carCont)+ 'x:'+str(x)+ 'y:'+str(y),(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255))
                if (x>380 and x<=420) and (y>=60 and y<=100):
#                if (x>115 and x<200) and (y<100):
                    rota1 = rota1 + 1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Rota1:', rota1)
                    print('Rota2:', rota2)
                    print('Rota3:', rota3)

                if (x>0 and x<40) and (y>110 and y<130):
                    rota2 = rota2 + 1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Rota1:', rota1)
                    print('Rota2:', rota2)
                    print('Rota3:', rota3)

                if (x>100 and x<250) and (y>170 and y<250):
                    rota3 = rota3 + 1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Rota1:', rota1)
                    print('Rota2:', rota2)
                    print('Rota3:', rota3)

#            cv2.rectangle(img, (380, 60), (420, 100), (255, 0, 0),-1)
#            cv2.rectangle(img, (0, 113), (40, 130), (255, 0, 0),-1)
#            cv2.rectangle(img, (100, 170), (250, 250), (255, 0, 0),-1)

            imS = cv2.resize(img, (800, 452))
            #desenha a linha diagonal
            cv2.line(imS, (500, 115), (440, 125), (0, 255, 0),3)#Rota1
            cv2.line(imS, (380, 140), (280, 210), (0, 255, 0),3)#Rota2
            cv2.line(imS, (740, 630), (100, 300), (0, 255, 0),6)#Rota3
            cv2.imshow('edge', imS)

        step = False
        ch = cv2.waitKey(5)
        if ch == 13:
            step = True
        if ch == 32:
            paused = not paused
        if ch == 27:
            break
    cv2.destroyAllWindows()
