# 导入 turtle 库
import turtle
# 导入 random 库
import random 
# 导入 winsound 库，用来播放声音
import winsound 
# 创建一个屏幕对象，设置背景颜色和大小
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(800, 600)
# 创建一个拉布拉多犬对象，继承自 turtle.Turtle 类
class Labrador(turtle.Turtle):
    # 初始化方法，设置形状、颜色、速度等属性
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("yellow")
        self.speed(0)
        self.penup()
        self.goto(0, 0)
        self.direction = random.choice(["up", "down", "left", "right"])

    # 定义一个移动方法，让拉布拉多犬根据方向随机地移动一定的距离
    def move(self):
        # 如果方向是上，就向上移动
        if self.direction == "up":
            self.setheading(90)
            self.forward(random.randint(10, 20))
        # 如果方向是下，就向下移动
        elif self.direction == "down":
            self.setheading(270)
            self.forward(random.randint(10, 20))
        # 如果方向是左，就向左移动
        elif self.direction == "left":
            self.setheading(180)
            self.forward(random.randint(10, 20))
        # 如果方向是右，就向右移动
        elif self.direction == "right":
            self.setheading(0)
            self.forward(random.randint(10, 20))
        # 如果到达屏幕的边缘，就改变方向
        if self.xcor() > 380 or self.xcor() < -380 or self.ycor() > 280 or self.ycor() < -280:
            self.direction = random.choice(["up", "down", "left", "right"])

    # 定义一个抓老鼠的方法，如果拉布拉多犬和老鼠的距离小于 20，就抓住老鼠，并播放一声叫声
    def catch(self, mouse):
        if self.distance(mouse) < 20:
            mouse.hideturtle()
            winsound.PlaySound("dog.wav", winsound.SND_ASYNC)
# 创建一个老鼠对象，继承自 turtle.Turtle 类
class Mouse(turtle.Turtle):
    # 初始化方法，设置形状、颜色、速度等属性
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("gray")
        self.speed(0)
        self.penup()
        self.goto(random.randint(-380, 380), random.randint(-280, 280))
        self.direction = random.choice(["up", "down", "left", "right"])

    # 定义一个移动方法，让老鼠根据方向随机地移动一定的距离
    def move(self):
        # 如果方向是上，就向上移动
        if self.direction == "up":
            self.setheading(90)
            self.forward(random.randint(10, 20))
        # 如果方向是下，就向下移动
        elif self.direction == "down":
            self.setheading(270)
            self.forward(random.randint(10, 20))
        # 如果方向是左，就向左移动
        elif self.direction == "left":
            self.setheading(180)
            self.forward(random.randint(10, 20))
        # 如果方向是右，就向右移动
        elif self.direction == "right":
            self.setheading(0)
            self.forward(random.randint(10, 20))
        # 如果到达屏幕的边缘，就改变方向
        if self.xcor() > 380 or self.xcor() < -380 or self.ycor() > 280 or self.ycor() < -280:
            self.direction = random.choice(["up", "down", "left", "right"])

# 定义一个逃跑的方法，如果老鼠和拉布拉多犬的距离小于 50，就逃跑，并播放一声惊叫
    def escape(self, labrador):
        if self.distance(labrador) < 50:
            self.direction = random.choice(["up", "down", "left", "right"])
            winsound.PlaySound("mouse.wav", winsound.SND_ASYNC)
# 创建一个拉布拉多犬的实例
labrador = Labrador()# 创建一个老鼠的列表，包含 10 个老鼠的实例
mice = []
for i in range(10):
    mice.append(Mouse())
# 定义一个主循环，让拉布拉多犬和老鼠不断地移动和交互
while True:
    # 让拉布拉多犬移动
    labrador.move()
    # 遍历老鼠列表
    for mouse in mice:
        # 如果老鼠没有被抓住，就让它移动和逃跑
        if mouse.isvisible():
            mouse.move()
            mouse.escape(labrador)
        # 如果老鼠被抓住，就让拉布拉多犬抓住它
        else:
            labrador.catch(mouse)
    # 更新屏幕
    screen.update()

