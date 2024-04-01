# 导入 OpenCV 库
import cv2

# 读取一张彩色图片
image = cv2.imread("edged_image_1.jpg")

# 将图片转换为灰度模式
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 设置阈值参数
low_threshold = 22
high_threshold = 28

# 应用 Canny 算法
edged_image = cv2.Canny(gray_image, low_threshold, high_threshold)

# 保存边缘检测后的图片
cv2.imwrite("edged_image_3.jpg", edged_image)
