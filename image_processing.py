import cv2
import numpy as np

image_path = r"C:\image-processing-file\shrek.jpeg"
original_image = cv2.imread(image_path)

if original_image is None:
    print("Не удалось загрузить изображение.")
    exit()


cv2.imshow("Original Image", original_image)
cv2.waitKey(0)


resized_image = cv2.resize(original_image, (500, 400))
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)


gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray_image)
cv2.waitKey(0)


red_only = original_image.copy()
red_only[:, :, 0] = 0  
red_only[:, :, 1] = 0  
cv2.imshow("Red Only Image", red_only)
cv2.waitKey(0)



blurred_image = cv2.GaussianBlur(original_image, (15, 15), 0)
cv2.imshow("Blurred Image", blurred_image)
cv2.waitKey(0)


inverted_image = cv2.bitwise_not(original_image)
cv2.imshow("Inverted Image", inverted_image)
cv2.waitKey(0)


noise = np.random.normal(0, 25, original_image.shape)
noisy_image = np.clip(original_image + noise, 0, 255).astype(np.uint8)
cv2.imshow("Atmosphere Image", noisy_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
