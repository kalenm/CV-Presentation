import cv2
print(f"OpenCV version: {cv2.__version__}")

max_cameras = 100
avaiable = []
for i in range(max_cameras):
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    
    if not cap.read()[0]:
        print(f"Camera index {i:02d} not found...")
        continue
    
    avaiable.append(i)
    cap.release()
    
    print(f"Camera index {i:02d} OK!")

print(f"Cameras found: {avaiable}")
