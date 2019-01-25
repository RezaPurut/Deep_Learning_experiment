import cv2, os

def faceCrop(frame, fname, savepath):
    # saved file name 

    # Select one of the haarcascade files:
    #   haarcascade_frontalface_alt.xml
    #   haarcascade_frontalface_alt2.xml
    #   haarcascade_frontalface_alt_tree.xml
    #   haarcascade_frontalface_default.xml
    #   haarcascade_profileface.xml
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    
    if len(faces)<=0:
        print('NO FACES FOUND:', frame)
    else:    
        n=1
        for x,y,w,h in faces:
    
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,255), 3)
            sub_face = frame[y:y+h, x:x+w]
            face_filename = savepath + fname
            print(face_filename)
            cv2.imwrite(face_filename, sub_face)
        n+=1     
 

#ext = ".jpg" 
srcpath = 'data/Tzuyu/' 
savepath = 'data/temp/'

"""
n = 1
for imgfile in os.listdir(srcpath):
    os.rename(srcpath+imgfile, srcpath+str(n)+'.jpg')
    n += 1
"""

for imgfile in os.listdir(srcpath):
    img = cv2.imread(srcpath+imgfile)
    faceCrop(img, imgfile, savepath)