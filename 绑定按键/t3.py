import keyboard
import time 

def jiaxue():
    # 这里可以根据自己的需求修改要输入的内容
    # time.sleep(0.3)

    keyboard.press('y')
    keyboard.release('y')
    time.sleep(0.1)

    text = "/rygive /admin "

    # # 清空当前选中的文本（如果有）
    # keyboard.press('backspace')
    # keyboard.release('backspace')
    
    # 输入指定的内容
    for char in text:
        keyboard.write(char)
    time.sleep(0.1)    
    keyboard.press('enter')
    keyboard.release('enter')
    time.sleep(0.2) 
    keyboard.press('5')
    keyboard.release('5')
    time.sleep(0.3) 
    keyboard.press('1')
    keyboard.release('1')
    time.sleep(0.3) 
    keyboard.press('1')
    keyboard.release('1')


def on_press(event):
    if event.name == 'f2':
        # 这里可以根据自己的需求修改要输入的内容





        jiaxue()

    if event.name == 'f3':
        # 这里可以根据自己的需求修改要输入的内容

        keyboard.press('y')
        keyboard.release('y')
        time.sleep(0.1)

        text = "/rygive /admin "

        # # 清空当前选中的文本（如果有）
        # keyboard.press('backspace')
        # keyboard.release('backspace')
        
        # 输入指定的内容
        for char in text:
            keyboard.write(char)
        time.sleep(0.1)    
        keyboard.press('enter')
        keyboard.release('enter')
        time.sleep(0.2) 
        keyboard.press('6')
        keyboard.release('6')
        time.sleep(0.2) 
        keyboard.press('4')
        keyboard.release('4')
        time.sleep(0.2)
        keyboard.press('1')
        keyboard.release('1')


    

    if event.name == 'f4':
        # 这里可以根据自己的需求修改要输入的内容
        time.sleep(0.3)

        keyboard.press('y')
        keyboard.release('y')
        time.sleep(0.1)

        text = "/rygive /admin "

        # # 清空当前选中的文本（如果有）
        # keyboard.press('backspace')
        # keyboard.release('backspace')
        
        # 输入指定的内容
        for char in text:
            keyboard.write(char)
        time.sleep(0.1)    
        keyboard.press('enter')
        time.sleep(0.1) 


# 注册按键事件处理函数
keyboard.on_press(on_press)
 
# 保持程序运行状态，等待按键事件
keyboard.wait()