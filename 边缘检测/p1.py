# 导入 PIL 库的 Image 模块
from PIL import Image

# 打开一个彩色图片
image_file = Image.open("color_1.png")

# 将图片转换为灰度模式
image_file = image_file.convert("L")

# 将图片转换为黑白模式
image_file = image_file.convert("1")

# 保存转换后的图片
image_file.save("black_and_white_image.jpg")
