import cv2
import datetime

mode = input("Enter 1 for Live Webcam, 2 for Image input, 3 for Video file: ")

if mode == "1":
    cap = cv2.VideoCapture(0)
elif mode == "2":
    image_path = input("Enter image path: ")
    cap = cv2.VideoCapture(image_path)
elif mode == "3":
    video_path = input("Enter video path: ")
    cap = cv2.VideoCapture(video_path)
else:
    print("Invalid choice!")
    exit()

first_frame = None
font = cv2.FONT_HERSHEY_SIMPLEX

ret, frame = cap.read()
if not ret:
    print("Failed to load input!")
    exit()

height, width = frame.shape[:2]
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('motion_capture.avi', fourcc, 20.0, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        if mode == "2":
            print("Reference image loaded.")
        continue

    frame_delta = cv2.absdiff(first_frame, gray)
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    motion_detected = False

    for contour in contours:
        if cv2.contourArea(contour) < 1500:
            continue
        motion_detected = True
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    timestamp = str(datetime.datetime.now())
    cv2.putText(frame, timestamp, (10, height - 10), font, 0.5, (0, 0, 255), 1)

    cv2.imshow("Security Feed", frame)
    cv2.imshow("Threshold", thresh)
    cv2.imshow("Frame Delta", frame_delta)

    if motion_detected:
        out.write(frame)

    key = cv2.waitKey(0 if mode == "2" else 30) & 0xFF
    if key == ord('q'):
        break

    if mode == "2":
        break

cap.release()
out.release()
cv2.destroyAllWindows()
