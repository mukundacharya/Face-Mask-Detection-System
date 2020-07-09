import pickle
import cv2
with open('faces.pkl', 'rb') as f:
    faces = pickle.load(f)
print(len(faces))
for i in range(0,len(faces)):
    faces[i][0]=cv2.resize(faces[i][0],(640,480))
    cv2.imshow("ex",faces[i][0])
    print(faces[i][1])
    print(faces[i][2])
    print(faces[i][4])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    faces[i][3]=cv2.resize(faces[i][3],(640,480))
    cv2.imshow("ex",faces[i][3])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
  
    
    