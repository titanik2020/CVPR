import cv2

video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    raise Exception("Could not open video device")
ret, image = video_capture.read()
video_capture.release()
path = './capture.png'
cv2.imwrite(path, image)
image_gray_mode = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
mod_image = cv2.cvtColor(image_gray_mode, cv2.COLOR_GRAY2RGB)
height, width = mod_image.shape[:2]
cv2.line(mod_image, (0, 0), (width, height), (255, 0, 0), 7)
cv2.rectangle(mod_image, (25, 150), (140, 355), (0, 255, 0), 3)
cv2.imwrite('./capture_mod.png', mod_image)

