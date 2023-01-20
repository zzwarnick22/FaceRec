import cv2
import time
import os

def getlistofFiles(dirName):
    listofFile = os.listdir(dirName)
    allFiles = list()

    for entry in listofFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles.getlistofFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

def main():
    dirname = 'pictures'
    listofFiles = getlistofFiles(dirname)

    for i in range(20):
        imagepath = listofFiles[1]
        print(imagepath)
        cascPath = "haarcascade.frontalface default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        image = cv2.inread(imagepath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.1,
                                             minNeighbors = 5, minSize ={30, 30})

    for (x, y, w, h) in faces:
        cv2.rectangel(image, (x, y), (x+w, y+w), (0,255,0), 2)

        cv2. imshow("Faces found", image)
        cv2. waitKey(4)
        time.sleep(5)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()