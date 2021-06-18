# -*- coding: utf-8 -*-

import cv2
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

youtuberList = ["최현우 'HyunWoo Choi'","소련여자 Soviet girl in Seoul","지덥","이영자 채널 LYJ CH.","노마드 코더 Nomad Coders","김준표","뻑가 PPKKa","코미꼬"]


for youtuberName in youtuberList:
    print(youtuberName)
    path = 'D:/Pycharm Projects/cropFaceUsingOpenCV/' + youtuberName +'/' # 폴더 경로
    os.chdir(path) # 해당 폴더로 이동
    files = os.listdir(path) # 해당 폴더에 있는 파일 이름을 리스트 형태로 받음

    photoCount = 0;
    for file in files:
        photoCount += 1
        img = cv2.imread(file)
        try:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        except:
            continue

        imgNum  = 0
        for (x,y,w,h) in faces:
           cropped = img[y - int(h / 4):y + h + int(h / 4), x - int(w / 4):x + w + int(w / 4)]
           # 이미지를 저장
           try:
            cv2.imwrite('face' + str(photoCount) + ".jpg", cropped)
           except:
               print("error" + str(photoCount))
           imgNum += 1
        print(photoCount)
        #print(photoCount)
        #cv2.imshow('Image view', img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
