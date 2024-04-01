# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:31:29 2021

@author: Juni Zhu (wechat:znix1116)
"""


import tkinter as tk
import copy
from tkinter.messagebox import showinfo

remake = 1 # 版本切换 0为原始模式，1为图片模式，2为像素动画模式(像素动画模式有点卡)

try:  # 同目录下搜寻m.txt地图扩充文件，若没有此文件就用内置地图
  with open("m.txt", "r") as f:
     game_map = f.read()
     game_map = eval(game_map)
except:
     game_map = [[
 [0, 0, 1, 1, 1, 0, 0, 0],
 [0, 0, 1, 4, 1, 0, 0, 0],
 [0, 0, 1, 0, 1, 1, 1, 1],
 [1, 1, 1, 3, 0, 3, 4, 1],
 [1, 4, 0, 3, 2, 1, 1, 1],
 [1, 1, 1, 1, 3, 1, 0, 0],
 [0, 0, 0, 1, 4, 1, 0, 0],
 [0, 0, 0, 1, 1, 1, 0, 0]
 ],[
 [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
 [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
 [1, 1, 4, 0, 3, 1, 1, 0, 1, 1],
 [1, 4, 4, 3, 0, 3, 0, 0, 2, 1],
 [1, 4, 4, 0, 3, 0, 3, 0, 1, 1],
 [1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
 [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
 ],[
 [0, 0, 1, 1, 1, 1, 0, 0],
 [0, 0, 1, 4, 4, 1, 0, 0],
 [0, 1, 1, 0, 4, 1, 1, 0],
 [0, 1, 0, 0, 3, 4, 1, 0],
 [1, 1, 0, 3, 0, 0, 1, 1],
 [1, 0, 0, 1, 3, 3, 0, 1],
 [1, 0, 0, 2, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1]
 ],[
 [1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 1, 0, 0, 0, 1],
 [1, 0, 3, 4, 4, 3, 0, 1],
 [1, 2, 3, 4, 5, 0, 1, 1],
 [1, 0, 3, 4, 4, 3, 0, 1],
 [1, 0, 0, 1, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1]
 ],[
 [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
 [0, 0, 0, 0, 0, 1, 0, 0, 3, 3, 0, 1, 0],
 [1, 1, 1, 1, 1, 1, 0, 3, 1, 0, 0, 1, 0],
 [1, 4, 4, 4, 1, 1, 1, 0, 1, 0, 0, 1, 1],
 [1, 4, 0, 0, 1, 0, 0, 3, 0, 1, 0, 0, 1],
 [1, 4, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 1],
 [1, 4, 0, 0, 1, 0, 0, 3, 0, 1, 0, 0, 1],
 [1, 4, 4, 4, 1, 1, 1, 0, 1, 0, 0, 1, 1],
 [1, 1, 1, 1, 1, 1, 0, 3, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 0, 1, 0, 2, 1, 0, 0, 1, 0],
 [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0], 
 ],[
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
 [1, 0, 4, 4, 4, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 4, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 5, 0, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
 ]]

    
# 8*8单元格的像素图（用于像素动画模式）
cell = [[
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0]
 ],[
 [1, 1, 1, 1, 7, 1, 1, 1],
 [1, 1, 1, 1, 7, 1, 1, 1],
 [7, 7, 7, 7, 7, 7, 7, 7],
 [1, 1, 7, 1, 1, 1, 1, 1],
 [1, 1, 7, 1, 1, 1, 1, 1],
 [7, 7, 7, 7, 7, 7, 7, 7],
 [1, 1, 1, 1, 7, 1, 1, 1],
 [1, 1, 1, 1, 7, 1, 1, 1]
 ],[
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 1, 1, 0, 0],
 [0, 1, 1, 2, 2, 1, 0, 0],
 [0, 0, 1, 2, 2, 1, 1, 0],
 [0, 0, 1, 1, 1, 1, 0, 0],
 [0, 0, 0, 1, 1, 0, 0, 0],
 [0, 1, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0]
 ],[
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 3, 3, 3, 3, 3, 3, 0],
 [0, 3, 3, 0, 0, 3, 3, 0],
 [0, 3, 0, 3, 3, 0, 3, 0],
 [0, 3, 0, 3, 3, 0, 3, 0],
 [0, 3, 3, 0, 0, 3, 3, 0],
 [0, 3, 3, 3, 3, 3, 3, 0],
 [0, 0, 0, 0, 0, 0, 0, 0]
 ],[
 [4, 4, 4, 4, 4, 4, 4, 4],
 [4, 4, 4, 4, 4, 4, 4, 4],
 [4, 4, 4, 4, 4, 4, 4, 4],
 [4, 4, 4, 4, 4, 4, 4, 4],
 [4, 4, 4, 4, 4, 4, 4, 4],
 [4, 4, 4, 4, 4, 4, 4, 4],
 [4, 4, 4, 4, 4, 4, 4, 4],
 [4, 4, 4, 4, 4, 4, 4, 4]
 ],[    
 [4, 4, 4, 4, 4, 4, 4, 4],
 [4, 5, 5, 5, 5, 5, 5, 4],
 [4, 5, 5, 4, 4, 5, 5, 4],
 [4, 5, 4, 5, 5, 4, 5, 4],
 [4, 5, 4, 5, 5, 4, 5, 4],
 [4, 5, 5, 4, 4, 5, 5, 4],
 [4, 5, 5, 5, 5, 5, 5, 4],
 [4, 4, 4, 4, 4, 4, 4, 4]
 ],[
 [4, 4, 4, 4, 4, 4, 4, 4],
 [4, 4, 1, 1, 1, 1, 4, 4],
 [4, 1, 1, 2, 2, 1, 4, 4],
 [4, 4, 1, 2, 2, 1, 1, 4],
 [4, 4, 1, 1, 1, 1, 4, 4],
 [4, 4, 4, 1, 1, 4, 4, 4],
 [4, 1, 1, 4, 4, 4, 4, 4],
 [4, 4, 4, 4, 4, 4, 4, 4]
 ]]
    
# 人物在空地上的动画效果（用于像素动画模式）
pe2 = [[
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 1, 1, 0, 0],
 [0, 1, 1, 2, 2, 1, 0, 0],
 [0, 0, 1, 2, 2, 1, 1, 0],
 [0, 0, 1, 1, 1, 1, 0, 0],
 [0, 0, 0, 1, 1, 0, 0, 0],
 [0, 1, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0]
 ],[
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 1, 1, 0, 0],
 [0, 0, 1, 5, 5, 1, 1, 0],
 [0, 1, 1, 5, 5, 1, 0, 0],
 [0, 0, 1, 1, 1, 1, 0, 0],
 [0, 0, 0, 1, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 1, 0],
 [0, 0, 0, 0, 0, 0, 0, 0]
 ]]

# 人物在终点上的动画效果（用于像素动画模式）
pe6 = [[
 [4, 4, 4, 4, 4, 4, 4, 4],
 [4, 4, 1, 1, 1, 1, 4, 4],
 [4, 1, 1, 2, 2, 1, 4, 4],
 [4, 4, 1, 2, 2, 1, 1, 4],
 [4, 4, 1, 1, 1, 1, 4, 4],
 [4, 4, 4, 1, 1, 4, 4, 4],
 [4, 1, 1, 4, 4, 4, 4, 4],
 [4, 4, 4, 4, 4, 4, 4, 4]
 ],[
 [4, 4, 4, 4, 4, 4, 4, 4],
 [4, 4, 1, 1, 1, 1, 4, 4],
 [4, 4, 1, 5, 5, 1, 1, 4],
 [4, 1, 1, 5, 5, 1, 4, 4],
 [4, 4, 1, 1, 1, 1, 4, 4],
 [4, 4, 4, 1, 1, 4, 4, 4],
 [4, 4, 4, 4, 4, 1, 1, 4],
 [4, 4, 4, 4, 4, 4, 4, 4]
 ]]

            
class Boxman():
    """ 推箱子游戏 """
    def __init__(self, game_stage):
        """ 游戏参数设置 """       
        self.p          = 8                 # 小方格内一行像素的数量（用于像素动画模式）
        self.s          = 6                 # 单像素的宽度（用于像素动画模式）
        self.game_stage = game_stage        # 游戏关卡
        self.canvas_bg  = '#d7d7d7'         # 游戏背景色
        self.cell_size  = self.p * self.s   # 方格单元格大小
        self.cell_gap   = 1                 # 方格间距
        self.frame_x    = 25                # 左右边距
        self.frame_y    = 25                # 上下边距
        self.max_cells  = 10                # 游戏画面长宽最大单元格数
        self.win_w_plus = 220               # 窗口右边额外多出的宽度 
        self.big_map    = 0                 # 判断当前地图是否是超出窗口大小。1为是，0为不是
        
        # 根据地图自动调整窗口大小
        self.canvas_w   = len(game_map[self.game_stage-1][0]) * self.cell_size + self.frame_x*2
        self.canvas_h   = len(game_map[self.game_stage-1]   ) * self.cell_size + self.frame_y*2
        
        self.color_dict = {0:  'white',     # 0表示空白
                           1:'#808080',     # 1表示墙
                           2: 'yellow',     # 2表示空地上的人
                           3:  'green',     # 3表示空地上的箱子
                           4:   'pink',     # 4表示终点
                           5:    'red',     # 5表示终点上的的箱子
                           6:'#ffa579',     # 6表示在终点上的人
                           7:'#d7d7d7'      # 额外的颜色（用于像素动画模式）
                           }
        
        # 若地图过大，窗口则根据max_cells值来设定大小
        if len(game_map[self.game_stage-1][0]) > self.max_cells:
            self.big_map  = 1
            self.canvas_w = self.cell_size*self.max_cells + self.frame_x*2
        if len(game_map[self.game_stage-1]) > self.max_cells:
            self.big_map  = 1
            self.canvas_h = self.cell_size*self.max_cells + self.frame_y*2 
                              
        self.win_w_size = self.canvas_w + self.win_w_plus
        self.win_h_size = self.canvas_h


    def create_pixel_map(self):
        """ 创建像素版的地图 """
        global pixel_map
        
        p = self.p  # 小方格内一行像素的数量
        gy = len(game_map[self.game_stage-1])
        gx = len(game_map[self.game_stage-1][0])
        
        pixel_map = []
        for i in range(0,gy*p):
            pixel_map.append([])
        for i in range(0,gy*p):
           for j in range(0,gx*p):
              pixel_map[i].append(j)   
              pixel_map[i][j] = 0   # 生成一个全是0的空数列
        
        
    def load_pixel_map(self):
        """ 加载像素版地图 """
        global pixel_map
        p = self.p
        gy = len(game_map[self.game_stage-1])
        gx = len(game_map[self.game_stage-1][0])
        
        for a in range(0,gy):
            for b in range(0,gx):
                for y in range(0,p):
                    for x in range(0,p):
                        pixel_map[y + p*a][x + p*b] = cell[game_map[self.game_stage-1][a][b]][y][x]
        
        
    def create_canvas(self): 
        """ 创建canvas """
        global canvas
        canvas = tk.Canvas(window, 
                           bg=self.canvas_bg, 
                           height=self.canvas_h,
                           width=self.canvas_w,
                           highlightthickness = 0)
                           
                            
    def create_pixel_cells(self,a,b): # a,b值为偏差值，若地图大于窗口的话，用于调节起始坐标
            """ 创建像素版的单元格 """
            p = self.p  # 小方格内一行像素的数量
            s = self.s  # 单像素的宽度
            gy = len(game_map[self.game_stage-1])
            gx = len(game_map[self.game_stage-1][0])
            
            for y in range(0,gy*p-b):
              for x in range(0,gx*p-a):
                
                if x % p != 0:
                    xp = 0
                else:
                    xp = self.cell_gap
                # 每8个单元格间隔一个gap（p = 8）
                if y % p != 0:
                    yp = 0
                else:
                    yp = self.cell_gap
                
                x1 = self.frame_x + s * x + xp
                y1 = self.frame_y + s * y + yp
                x2 = self.frame_x + s * (x+1)
                y2 = self.frame_y + s * (y+1)
                
                canvas.itemconfig(canvas.create_rectangle(x1,y1,x2,y2,
                                        fill    = self.color_dict[pixel_map[y+b][x+a]],
                                        outline = self.canvas_bg,
                                        width   = 0),
                                        fill    = self.color_dict[pixel_map[y+b][x+a]])
                                        
            canvas.place(x=0,y=0)
            
            
    def load_pixel_boxman(self,boxman_y,boxman_x):
        """ 加载像素版人物 """
        p = self.p
        for y in range(0,p):
            for x in range(0,p):
                pixel_map[y + p*(boxman_y)][x + p*boxman_x] = cell[game_map[self.game_stage-1][boxman_y][boxman_x]][y][x]
        

    def pixel_gif(self):
        """ 像素动画效果 """ # 2张像素图反复切换做出动画效果
        global p_gif
        p_gif = p_gif + 1
        if p_gif > 1:
            p_gif = 0
        cell[2] = pe2[p_gif]
        cell[6] = pe6[p_gif]
        Boxman(self.game_stage).load_pixel_boxman(boxman_y + 0,boxman_x + 0)
        
        
    def game_loop(self):
        """ 刷新游戏画面 """
        global loop
        if   remake == 0: # 简易模式
            pass # 静止画面不需要自动刷新
        elif remake == 1: # 图片模式
            canvas.delete('all') # 清除canvas，不清除的话时间久了有BUG
            Boxman(self.game_stage).create_pic_cells(px,py)
        else: # 像素模式
            canvas.delete('all') # 清除canvas
            Boxman(self.game_stage).pixel_gif()
            Boxman(self.game_stage).create_pixel_cells(px*self.p,py*self.p)
        
        loop = window.after(100, Boxman(self.game_stage).game_loop)


    def window_center(self,window,w_size,h_size):
        """ 窗口居中 """
        screenWidth  =  window.winfo_screenwidth()  # 获取显示区域的宽度
        screenHeight = window.winfo_screenheight()  # 获取显示区域的高度
        left =  (screenWidth - w_size) // 2
        top  = (screenHeight - h_size) // 2
        window.geometry("%dx%d+%d+%d" % (w_size, h_size, left, top))

        
    def create_game_cells(self,a,b): # a,b值为偏差值，若地图大于窗口的话，用于调节起始坐标
        """ 创建初始版的游戏单元格 """  # 通过game_map列表，对应字典color_dict里的颜色画出地图
        for y in range(0,len(game_map[self.game_stage-1])-b):
              for x in range(0,len(game_map[self.game_stage-1][0])-a):            
                canvas.itemconfig(canvas.create_rectangle(
                                        self.frame_x + self.cell_size * x + self.cell_gap,
                                        self.frame_y + self.cell_size * y + self.cell_gap,
                                        self.frame_x + self.cell_size * (x+1),
                                        self.frame_y + self.cell_size * (y+1),
                                        fill    = self.color_dict[game_map[self.game_stage-1][y+b][x+a]],
                                        outline = self.canvas_bg,
                                        width   = 0),
                                        fill    = self.color_dict[game_map[self.game_stage-1][y+b][x+a]])
                                        
        canvas.place(x=0,y=0)
        

    def create_pic_cells(self,a,b):
        """ 创建图片模式的单元格 """ 
        global man_gif,pic_dict
        
        man_2 = ["2.png","22.png"] # 两张空地上人的图片
        man_6 = ["6.png","66.png"] # 两张终点上人的图片
            
        man_gif = man_gif + 1
        if man_gif > 1:
            man_gif = 0
            
        man_2[0] = man_2[man_gif]
        man_6[0] = man_6[man_gif]
        
        pic_dict = {0: tk.PhotoImage(file =  '0.png'),
                    1: tk.PhotoImage(file =  '1.png'),
                    2: tk.PhotoImage(file = man_2[0]),
                    3: tk.PhotoImage(file =  '3.png'),
                    4: tk.PhotoImage(file =  '4.png'),
                    5: tk.PhotoImage(file =  '5.png'),
                    6: tk.PhotoImage(file = man_6[0])
                    }
        
        for y in range(0,len(game_map[self.game_stage-1])-b):
            for x in range(0,len(game_map[self.game_stage-1][0])-a): 
                n = game_map[self.game_stage-1][y+b][x+a] # 单元格的值
                canvas.create_image(self.frame_x*2 + self.cell_size*x + x*self.cell_gap, 
                                    self.frame_y*2 + self.cell_size*y + y*self.cell_gap,
                                    image = pic_dict[n]) 
        canvas.place(x=0,y=0)
        
        
    def boxman_xy(self):
        """ 获取人物坐标 """
        global boxman_x, boxman_y
        xy = []
        for i in range(0,len(game_map[self.game_stage-1])):
            try: # 查找数值为2的坐标，没有就返回0。为防止人物出现在0列，先加上1，最后再减去。
                x = game_map[self.game_stage-1][i].index(2) + 1
            except:
                x = 0
            xy.append(x)
        boxman_x = max(xy)
        boxman_y = xy.index(boxman_x)
        boxman_x = boxman_x - 1 # 之前加1，现在减回

        if boxman_x == -1: # 没有数值为2，说明人物在终点，即数值等于6
            xy = []
            for i in range(0,len(game_map[self.game_stage-1])):
                try:
                    x  = game_map[self.game_stage-1][i].index(6) + 1
                except:
                    x = 0
                xy.append(x)
            boxman_x = max(xy)
            boxman_y = xy.index(boxman_x)
            boxman_x = boxman_x - 1


    def move_action(self,event): 
        """ 按键控制 """
        def Boxman_move(event,key,x,y):
                """ 操控人物 """
                # 0表示空白,  1表示墙,  2表示人,  3表示箱子,  4表示终点,  5表示已完成的箱子,  6表示在终点上的人
                def operation_forward_none(f1,f2,f3,f4,f5):
                    """ 前方是空地或是终点 """
                    if             game_map[self.game_stage-1][boxman_y + y*1][boxman_x + x*1] == f1: ### 前方是空地或是终点
                        if         game_map[self.game_stage-1][boxman_y + y*0][boxman_x + x*0] == 2:  #   人站在空地上
                                   game_map[self.game_stage-1][boxman_y + y*0][boxman_x + x*0]  = f2  ### 人离开后是空地
                                   game_map[self.game_stage-1][boxman_y + y*1][boxman_x + x*1]  = f3  ### 前方是空地或是终点
                        else:                                                                         #   人站在终点上
                                   game_map[self.game_stage-1][boxman_y + y*0][boxman_x + x*0]  = f4  ### 身后是终点
                                   game_map[self.game_stage-1][boxman_y + y*1][boxman_x + x*1]  = f5  ### 前方是空地或是终点

                def operation_forward_box(f1,f2,f3,f4,f5,f6,f7):
                    """ 前方是空地上的箱子或是已完成的箱子 """
                    if             game_map[self.game_stage-1][boxman_y + y*1][boxman_x + x*1] == f1: ### 前方是空地上的箱子或是已完成的箱子
                        if         game_map[self.game_stage-1][boxman_y + y*0][boxman_x + x*0] == 2:  #   人站在空地
                            if     game_map[self.game_stage-1][boxman_y + y*2][boxman_x + x*2] == f2: ### 箱子的前方是空地或终点
                                   game_map[self.game_stage-1][boxman_y + y*0][boxman_x + x*0]  = 0   #   人离开后是空地
                                   game_map[self.game_stage-1][boxman_y + y*1][boxman_x + x*1]  = f3  ### 前方是空地或是终点
                                   game_map[self.game_stage-1][boxman_y + y*2][boxman_x + x*2]  = f4  ### 前方是空地上的箱子或是已完成的箱子
                        else:                                                                         ### 人站在终点上
                            if     game_map[self.game_stage-1][boxman_y + y*2][boxman_x + x*2] == f5: ### 箱子的前方是空地或是终点
                                   game_map[self.game_stage-1][boxman_y + y*0][boxman_x + x*0]  = 4   #   身后是终点
                                   game_map[self.game_stage-1][boxman_y + y*1][boxman_x + x*1]  = f6  ### 前方是空地或是终点
                                   game_map[self.game_stage-1][boxman_y + y*2][boxman_x + x*2]  = f7  ### 箱子的前方是空地或是终点

                
                
                if remake == 2:
                    Boxman(self.game_stage).load_pixel_boxman(boxman_y + y,boxman_x + x)
                
                
                direction = event.keysym
                if(direction == key):
                    operation_forward_none(0,0,2,4,2)
                    operation_forward_none(4,0,6,4,6)
                    operation_forward_box(3,0,2,3,0,2,3)
                    operation_forward_box(3,4,2,5,4,2,5)
                    operation_forward_box(5,0,6,3,0,6,3)
                    operation_forward_box(5,4,6,5,4,6,5)
                    
                    Boxman(self.game_stage).boxman_xy()   # 刷新坐标
                    
                    temp = [] # 记录每步的操作，供撤消使用。
                    temp.append(boxman_y) # 保存XY轴坐标值，即人物所在单元格的坐标
                    temp.append(boxman_x) # 后面6个分别是中，上，下，左，右和前方单元格的值
                    temp.append(game_map[self.game_stage-1][boxman_y + 0][boxman_x + 0])
                    temp.append(game_map[self.game_stage-1][boxman_y - 1][boxman_x + 0])
                    temp.append(game_map[self.game_stage-1][boxman_y + 1][boxman_x + 0])
                    temp.append(game_map[self.game_stage-1][boxman_y + 0][boxman_x - 1])
                    temp.append(game_map[self.game_stage-1][boxman_y + 0][boxman_x + 1])
                    temp.append(game_map[self.game_stage-1][boxman_y + y][boxman_x + x])
                    
                    record_list.append(temp)
                    
                    if len(record_list) > 1:
                        if record_list[-1] == record_list[-2]:
                          del record_list[-1]   # 删除连续相同的数据


        def game_select_stage(event,key):
            """ 返回游戏主页面 """
            global game_map
            direction = event.keysym
            if(direction == key): 
                game_map = copy.deepcopy(backup_map)
                window.after_cancel(loop)
                window.destroy()  # 窗口关闭并启动起始窗口
                Boxman(self.game_stage).index_game()


        def reset_stage(event,key):
            """ 重置关卡 """
            global game_map
            direction = event.keysym
            if(direction == key): 
                del record_list[:]
                game_map = copy.deepcopy(backup_map)
                Boxman(self.game_stage).boxman_xy() # 重置大地图时需要重新定位人物坐标
                Boxman(self.game_stage).big_map_check()
                if remake == 2:
                    Boxman(self.game_stage).load_pixel_map() # 像素模式下重新装载下地图
                

        def to_stage(event,key,stage): # 直接按数字键选关
            """ 选择游戏关卡 """
            global game_map
            direction = event.keysym
            if(direction == key): 
                del record_list[:]
                game_map = copy.deepcopy(backup_map)
                window.after_cancel(loop)
                window.destroy()
                Boxman(stage).window_open()


        def restore_stage(event,key):
            """ 撤销功能 """
            direction = event.keysym
            if(direction == key): 
                def restore(): 
                    """ 撤销步骤的函数 """
                    m = game_map[self.game_stage-1]
                    
                    before_forward = 0                   # 之前所面对的（0是临时值）
                    
                    before_stand   = record_list[-2][2]  # 之前所站的单元格的值
                    now_stand      = record_list[-1][2]  # 当前所站的单元格的值
                    now_forward    = record_list[-1][7]  # 当前所面对的单元格的值

                    before_x       = record_list[-2][1]  # 之前所站的X轴坐标
                    before_y       = record_list[-2][0]  # 之前所站的Y轴坐标
                    now_x          = record_list[-1][1]  # 当前所站的X轴坐标
                    now_y          = record_list[-1][0]  # 当前所站的Y轴坐标
                    
                    b_up           = record_list[-2][3]  # 之前上方单元格的值
                    b_dw           = record_list[-2][4]  # 之前下方单元格的值
                    b_lf           = record_list[-2][5]  # 之前左方单元格的值
                    b_rg           = record_list[-2][6]  # 之前右方单元格的值

                    #  推断出之前所面对的单元格的值

                    if     before_x         > now_x:
                           next_x           = now_x - 1
                           before_forward   = b_lf
                    elif   before_x         < now_x:
                           next_x           = now_x + 1
                           before_forward   = b_rg
                    else:
                           next_x           = now_x
                             
                    if     before_y         > now_y:
                           next_y           = now_y - 1
                           before_forward   = b_up
                    elif   before_y         < now_y:
                           next_y           = now_y + 1
                           before_forward   = b_dw
                    else:
                           next_y           = now_y
                    
                    # 0表示空白,  1表示墙,  2表示人,  3表示箱子,  4表示终点,  5表示已完成的箱子,  6表示在终点上的人
                    
                    m[before_y][before_x] = before_stand # 人退回之前的状态，2或者6
                    m[   now_y][   now_x] = before_forward
                    # 推断出当前面对的单元格的值
                    if                      before_forward == 3:
                        if                     now_forward == 3:
                            if                   now_stand == 2:
                                         m[next_y][next_x]  = 0
                            elif                 now_stand == 6:
                                         m[next_y][next_x]  = 0
                        elif                   now_forward == 5:
                            if                   now_stand == 2:
                                         m[next_y][next_x]  = 4
                            elif                 now_stand == 6:
                                         m[next_y][next_x]  = 0 
                                         
                    elif                    before_forward == 5:
                        if                     now_forward == 3:
                            if                   now_stand == 2:
                                         m[next_y][next_x]  = 0
                            elif                 now_stand == 6:
                                         m[next_y][next_x]  = 0
                        elif                   now_forward == 5:
                            if                   now_stand == 2:
                                         m[next_y][next_x]  = 0
                            elif                 now_stand == 6:
                                         m[next_y][next_x]  = 4
                restore()
                
                del record_list[-1]  # 每撤消一步就删除最后一组列表
                
                if remake == 2:
                    Boxman(self.game_stage).load_pixel_map() # 像素模式下重新装载下地图
                

        def game_pass(): # 通关条件为箱子数为0
            """ 获取箱子数量，等于0的话过关 """
            xy = []
            for i in range(0,len(game_map[self.game_stage-1])):
                x = game_map[self.game_stage-1][i].count(3)
                xy.append(x)
            box_number = sum(xy)
            if box_number == 0:
                pass_win()
        
        
        def pass_win():
            """ 箱子为零时，显示过关窗口 """
            global game_map
            showinfo('恭喜过关','返回首页')
            window.destroy()
            game_map = copy.deepcopy(backup_map)
            Boxman(0).index_game()
            

        def move_map_ws(event,key,a,b):
            """ 若是大地图，则上下移动地图 """
            global py
            direction = event.keysym
            if(direction == key):             
              my = len(game_map[self.game_stage-1])
              if    self.big_map == 1:  
                if      boxman_y  >= int(self.max_cells//2) + a:
                  if    boxman_y  < my - int(self.max_cells//2):
                      if game_map[self.game_stage-1][boxman_y + b*1][boxman_x] not in [1] and \
                         game_map[self.game_stage-1][boxman_y + b*2][boxman_x] not in [1,3,5]:
                          py  = boxman_y - int(self.max_cells//2) + b
                  elif  boxman_y >= my - int(self.max_cells//2):
                              py  = my - self.max_cells 
                else:
                              py  = 0
              else:
                              py  = 0


        def move_map_ad(event,key,a,b): 
            """ 若是大地图，则左右移动地图 """
            global px
            direction = event.keysym
            if(direction == key): 
              mx = len(game_map[self.game_stage-1][0])
              if      self.big_map == 1:
                if      boxman_x >= int(self.max_cells/2) + a:
                  if    boxman_x  < mx - int(self.max_cells//2):
                      if game_map[self.game_stage-1][boxman_y][boxman_x + b*1] not in [1] and \
                         game_map[self.game_stage-1][boxman_y][boxman_x + b*2] not in [1,3,5] :
                          px  = boxman_x - int(self.max_cells//2) + b
                  elif  boxman_x >= mx - int(self.max_cells//2):
                              px  = mx - self.max_cells
                else:
                              px  = 0
              else:
                              px  = 0


        def change_map(event,key): 
            """ 三个游戏版本的切换 """ # 版本切换 0为原始模式，1为图片模式，2为像素动画模式
            global remake
            direction = event.keysym
            if(direction == key):
                window.after_cancel(loop)
                window.destroy()
                remake = remake + 1
                if remake > 2:
                    remake = 0
                Boxman(self.game_stage).window_open()
                                            

        change_map(event, '0')

        move_map_ws(event,    'w',  1, -1)
        move_map_ws(event,    's',  0,  1)
        move_map_ad(event,    'a',  1, -1)
        move_map_ad(event,    'd',  0,  1)
        
        move_map_ws(event,    'W',  1, -1)
        move_map_ws(event,    'S',  0,  1)
        move_map_ad(event,    'A',  1, -1)
        move_map_ad(event,    'D',  0,  1)
        
        move_map_ws(event,   'Up',  1, -1)
        move_map_ws(event, 'Down',  0,  1)
        move_map_ad(event, 'Left',  1, -1)
        move_map_ad(event,'Right',  0,  1)
        
        
        Boxman_move(event,    'w',  0, -1)
        Boxman_move(event,    's',  0,  1)
        Boxman_move(event,    'a', -1,  0)
        Boxman_move(event,    'd',  1,  0)
        
        Boxman_move(event,    'W',  0, -1)
        Boxman_move(event,    'S',  0,  1)
        Boxman_move(event,    'A', -1,  0)
        Boxman_move(event,    'D',  1,  0)
        
        Boxman_move(event,   'Up',  0, -1)
        Boxman_move(event, 'Down',  0,  1)
        Boxman_move(event, 'Left', -1,  0)
        Boxman_move(event,'Right',  1,  0)
        
        game_select_stage(event, 'p')     # 返回主页面
        game_select_stage(event, 'P')
        reset_stage(event, 'j')           # 重置该关卡
        reset_stage(event, 'J')
        
        to_stage(event, '1', 1)
        to_stage(event, '2', 2)
        to_stage(event, '3', 3)
        to_stage(event, '4', 4)
        to_stage(event, '5', 5)
        to_stage(event, '6', 6)
        
        
        if  len(record_list) <= 1:
            reset_stage(event, 'r')
            reset_stage(event, 'R')
        else:
            restore_stage(event, 'r')
            restore_stage(event, 'R')
        
        move_map_ws(event,   'r', 0, 0)
        move_map_ad(event,   'r', 0, 0)
        move_map_ws(event,   'R', 0, 0)
        move_map_ad(event,   'R', 0, 0)
        
        
        if  remake == 0:
            Boxman(self.game_stage).create_canvas() # 不刷新的话在大地图中有小BUG
            canvas.delete('all')
            Boxman(self.game_stage).create_game_cells(px,py)
            
        Boxman(self.game_stage).boxman_xy() # 重新刷新人物坐标，不然会有BUG
        game_pass()
        
        
    def big_map_check(self):
        """ 大地图判断 """
        global px,py
        # 如果是大地图，更换起始坐标，以人物为中心建立地图
        mx = len(game_map[self.game_stage-1][0])
        my = len(game_map[self.game_stage-1])
        if      self.big_map == 1:
                if      boxman_x  > int(self.max_cells//2):
                  if    boxman_x  < mx - int(self.max_cells//2):
                              px  = boxman_x - int(self.max_cells//2)
                  elif  boxman_x >= mx - int(self.max_cells//2):
                              px  = mx - self.max_cells
                else:
                              px  = 0
        else:
                              px  = 0
        if      self.big_map == 1:                            
                if      boxman_y  > int(self.max_cells//2):
                  if    boxman_y  < my - int(self.max_cells//2):
                              py  = boxman_y - int(self.max_cells//2)
                  elif  boxman_y >= my - int(self.max_cells//2):
                              py  = my - self.max_cells
                else:
                              py  = 0
        else:
                              py  = 0

        
    def window_open(self):
        """ 开启游戏窗口 """
        global window,txt_lable,px,py,p_gif,man_gif
        window = tk.Tk()
        window.focus_force()
        window.title('Boxman')
        Boxman(self.game_stage).window_center(window,self.win_w_size,self.win_h_size)
        p_gif = 0
        man_gif = 0
        if self.game_stage == 0:  # 若等于0，代表是最后一关
            n = len(game_map)
        else:
            n = self.game_stage
        
        mode = { 0:'简易模式', 1:'图片模式', 2:'像素模式'}
        
        txt_lable = tk.Label(window, text=
                             mode[remake]
                             +"\n"
                             +"\n当前为第" + str(n) + "关"
                             +"\n白色单元格为空地"
                             +"\n灰色单元格为墙" 
                             +"\n黄色单元格为打工人"
                             +"\n绿色单元格为箱子"
                             +"\n粉色单元格为终点"
                             +"\n红色单元格为已完成的箱子"
                             +"\n橘色单元格为站在终点上的人"
                             +"\n"
                             +"\n字母ADSW或方向键移动"
                             +"\n字母键P返回主页面"
                             +"\n字母键J重置本关"
                             +"\n字母键R为撤消"
                             +"\n数字键0为切换游戏界面模式"
                             +"\n数字键1~6直接选择关卡"
                             +"\n（第六关为测试关）"
                             +"\n"
                             +"\n"
                             +"\nBy Juni Zhu"
                             +"\n微信： znix1116"
                             +"\n2022.06.08"
                             ,
                             font=('Arial', 11),anchor="ne", justify="left")
        txt_lable.pack(side='right')
        
        Boxman(self.game_stage).boxman_xy()
        Boxman(self.game_stage).big_map_check()
        Boxman(self.game_stage).create_canvas()
        
        if  remake == 0:
            Boxman(self.game_stage).create_game_cells(px,py)
        elif  remake == 1:
            Boxman(self.game_stage).create_pic_cells(px,py)      
        else:            
            Boxman(self.game_stage).create_pixel_map()
            Boxman(self.game_stage).load_pixel_map()
            Boxman(self.game_stage).create_pixel_cells(px*self.p,py*self.p)
            
        window.bind('<Key>', Boxman(self.game_stage).move_action)
        Boxman(self.game_stage).game_loop()
        
        def close_w():
            window.after_cancel(loop)
            window.destroy()
            
        window.protocol('WM_DELETE_WINDOW', close_w)
        window.mainloop()
        
        
    def run_game(self):
        """ Run Game """
        global backup_map,record_list
        
        record_list = [] # 记录每步的操作，供撤消用
        backup_map = []  # 备份地图，供恢复用
        backup_map = copy.deepcopy(game_map)  # 备份地图，需要用深度复制
        Boxman(self.game_stage).window_open()   
        

    def index_game(self):
        """ 起始界面 """  # 窗口大小会根据按键的数量自动调整
        for i in range(1,len(game_map)+1):  # 批量生成函数，to_game_1,2,3,4,5...
            exec("def to_game_" + str(i) + "():\n\
                 index_win.destroy()\n\
                 Boxman(" + str(i) + ").run_game()")
            
        global index_win
        index_win = tk.Tk()
        index_win.focus_force()
        index_win.title('Welcome')
        Boxman(self.game_stage).window_center(index_win,200,(len(game_map)+1)*30)
        
        for i in range(1,len(game_map)+1): # 批量添加按键
            exec("b" + str(i) + " = tk.Button(index_win, text='" + str(i) 
                 + "', font=('Arial', 12), width=10, height=1, command=to_game_" + str(i) + ")")
            exec("b" + str(i) + ".pack()")
        
        index_win.mainloop()
        
    
if __name__ == '__main__':

 Boxman(0).index_game()
