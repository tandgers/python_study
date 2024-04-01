# 导入 OpenCV 库
import cv2
import numpy as np

# 读取一张彩色图片
image = cv2.imread("color_2.jpg")

# 将图片转换为灰度模式
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用 Canny 算法检测边缘
edges = cv2.Canny(gray_image, 55, 255)

# 查找图像中的所有轮廓
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 如果找到了轮廓
if len(contours) > 0:
    # 计算所有轮廓的面积
    areas = [cv2.contourArea(c) for c in contours]
    # 找到面积最大的轮廓的索引
    max_index = np.argmax(areas)
    # 获取最大轮廓
    max_contour = contours[max_index]
    # 在原图上用绿色画出最大轮廓
    cv2.drawContours(image, [max_contour], -1, (0, 255, 0), 2)

# 保存画出最大轮廓后的图片
cv2.imwrite("max_contour_image3.jpg", image)
