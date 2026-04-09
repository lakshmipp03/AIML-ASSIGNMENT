import cv2

img = cv2.imread("image.jpg")

print("Shape:", img.shape)
print("Pixel [0,0]:", img[0,0])
print("Channels:", img.shape[2])