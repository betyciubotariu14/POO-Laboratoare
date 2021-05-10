import cv2
clasificator = cv2.CascadeClassifier('clasificatori/data/haarcascade_frontalface_alt2.xml')
cap=cv2.VideoCapture(0)
print(cv2.__file__)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('fereastra video', frame)
    fete = clasificator.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for(x, y, w, h) in fete:
        print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w]
        img_item = "imaginea_mea.png"
        cv2.imwrite(img_item, roi_gray)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()