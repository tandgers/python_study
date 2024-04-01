# _*_ coding:utf-8 _*_
__author__ = 'lomiss'
__data__ = '2018/12/10 19:10'
 
import random
import sys
import copy
import os
import pygame
from pygame.locals import *
from Python_BFS import BFS
from C_DLL import C_algo
 
 
pygame.init()
 
# 帧率
FPS = 30
# 宽高
WINWIDTH = 600
WINHEIGHT = 500
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)
 
# 定义游戏地图中每个方块的大小
TILEWIDTH = 50
TILEHEIGHT = 85
# 瓷板地板高度
TILEFLOORHEIGHT = 40
 
OUTSIDE_DECORATION_PCT = 20
 
# 颜色定义
BRIGHTBLUE = (156, 156, 156)
WHITE = (255, 255, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE
 
# 方向定义
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
 
# 地图文本
level_text_list = []
 
 
# 主函数(预处理工作)
def main():
    ……
 
# 运行地图
def runLevel(levels, levelNum):
    global currentImage
    # 获取当前关卡对象
    levelObj = levels[levelNum]
    # 装饰地图
    mapObj = decorateMap(levelObj['mapObj'], levelObj['startState']['player'])
    # 将地图关键信息拷贝，以便游戏进行时修改
    gameStateObj = copy.deepcopy(levelObj['startState'])
    # 初始化变量，重新绘制为真
    mapNeedsRedraw = True
    # 定义地图额外信息
    levelSurf = BASICFONT.render('Level %s of %s' % (levelNum + 1, len(levels)), 1, TEXTCOLOR)
    levelRect = levelSurf.get_rect()
    levelRect.bottomleft = (20, WINHEIGHT - 35)
    # 初始化关卡通过为False
    levelIsComplete = False
    # 定义视角偏移参数
    cameraOffsetX = 0
    cameraOffsetY = 0
    # 初始化路径
    path = ""
 
    # 游戏主循环
    while True:
        # 重置变量
        playerMoveTo = None
        keyPressed = False
        # 开始事件监听
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
 
            elif event.type == KEYDOWN:
                # 获取人物移动方向
                keyPressed = True
                if event.key == K_LEFT:
                    playerMoveTo = UP
                elif event.key == K_RIGHT:
                    playerMoveTo = DOWN
                elif event.key == K_UP:
                    playerMoveTo = LEFT
                elif event.key == K_DOWN:
                    playerMoveTo = RIGHT
 
                elif event.key == K_n:
                    return 'next'
                elif event.key == K_b:
                    return 'back'
                # 暂停
                elif event.key == K_ESCAPE:
                    terminate()
                # 重置
                elif event.key == K_BACKSPACE:
                    return 'reset'
                # 更换人物皮肤
                elif event.key == K_p:
                    currentImage += 1
                    if currentImage >= len(PLAYERIMAGES):
                        # 若为最后一个，跳至第一个
                        currentImage = 0
                    mapNeedsRedraw = True
                # 若为1键，开始C_BFS算法
                elif event.key == K_1:
                    auto_game = C_algo(level_text_list[levelNum], levels[levelNum].get('width'))
                    path = auto_game.C_BFS()
                # 若为2键，开始C_Astar算法
                elif event.key == K_2:
                    auto_game = C_algo(level_text_list[levelNum], levels[levelNum].get('width'))
                    path = auto_game.C_Astar()
                # 若为3键，开始C_DFS算法
                elif event.key == K_3:
                    auto_game = C_algo(level_text_list[levelNum], levels[levelNum].get('width'))
                    path = auto_game.C_DFS()
                # 若为4键，开始Py_BFS算法
                elif event.key == K_4:
                    auto_game = BFS(level_text_list[levelNum], levels[levelNum].get('width'))
                    path = auto_game.gen_shortest_paths()[0]
 
        if path != "":
            for each in path:
                pygame.time.delay(150)
                if each == 'u' or each == 'U':
                    playerMoveTo = LEFT
                elif each == 'd' or each == 'D':
                    playerMoveTo = RIGHT
                elif each == 'l' or each == 'L':
                    playerMoveTo = UP
                elif each == 'r' or each == 'R':
                    playerMoveTo = DOWN
                moved = makeMove(mapObj, gameStateObj, playerMoveTo)
                if moved:
                    gameStateObj['stepCounter'] += 1
                    mapNeedsRedraw = True
                DISPLAYSURF.fill(BGCOLOR)
                if mapNeedsRedraw:
                    mapSurf = drawMap(mapObj, gameStateObj, levelObj['goals'])
                    mapNeedsRedraw = False
                mapSurfRect = mapSurf.get_rect()
                mapSurfRect.center = (HALF_WINWIDTH + cameraOffsetX, HALF_WINHEIGHT + cameraOffsetY)
 
                DISPLAYSURF.blit(mapSurf, mapSurfRect)
                DISPLAYSURF.blit(levelSurf, levelRect)
                stepSurf = BASICFONT.render('Steps: %s' % (gameStateObj['stepCounter']), 1, TEXTCOLOR)
                stepRect = stepSurf.get_rect()
                stepRect.bottomleft = (20, WINHEIGHT - 10)
                DISPLAYSURF.blit(stepSurf, stepRect)
                pygame.display.update()
                FPSCLOCK.tick()
            playerMoveTo = None
            levelIsComplete = True
            keyPressed = False
            path = ""
 
        if playerMoveTo != None and not levelIsComplete:
            # 控制移动
            moved = makeMove(mapObj, gameStateObj, playerMoveTo)
 
            # 步数加一
            if moved:
                gameStateObj['stepCounter'] += 1
                mapNeedsRedraw = True
 
            # 判断游戏是否结束
            if isLevelFinished(levelObj, gameStateObj):
                levelIsComplete = True
                keyPressed = False
 
        DISPLAYSURF.fill(BGCOLOR)
        # 是否重新绘制
        if mapNeedsRedraw:
            mapSurf = drawMap(mapObj, gameStateObj, levelObj['goals'])
            mapNeedsRedraw = False
 
        mapSurfRect = mapSurf.get_rect()
        mapSurfRect.center = (HALF_WINWIDTH + cameraOffsetX, HALF_WINHEIGHT + cameraOffsetY)
 
        DISPLAYSURF.blit(mapSurf, mapSurfRect)
 
        DISPLAYSURF.blit(levelSurf, levelRect)
        stepSurf = BASICFONT.render('Steps: %s' % (gameStateObj['stepCounter']), 1, TEXTCOLOR)
        stepRect = stepSurf.get_rect()
        stepRect.bottomleft = (20, WINHEIGHT - 10)
        DISPLAYSURF.blit(stepSurf, stepRect)
 
        if levelIsComplete:
            solvedRect = IMAGESDICT['solved'].get_rect()
            solvedRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)
            DISPLAYSURF.blit(IMAGESDICT['solved'], solvedRect)
 
            if keyPressed:
                return 'solved'
 
        pygame.display.update()
        FPSCLOCK.tick()
 
 
# 是否是墙
def isWall(mapObj, x, y):
    """判断当前坐标是否为墙"""
    ……
 
 
# 装饰地图
def decorateMap(mapObj, startxy):
    """拷贝一份以便修改：
         1.角落的墙壁变成了角落。
         2.外部/内部地板砖不同。
         3.树/岩石装饰随机添加到外部坐标上。"""
 
    ……
 
 
# 是否可以移动
def isBlocked(mapObj, gameStateObj, x, y):
    """如果地图上的（x，y）位置是可以移动的，则返回True
     被墙或者箱子阻挡，否则返回False。"""
 
    ……
 
 
# 控制移动
def makeMove(mapObj, gameStateObj, playerMoveTo):
    """给定一个地图和游戏状态对象，并且人物的移动方向。 如果可以移动，
    则更改人物位置（和任何推动的星的位置），如果玩家移动则返回True，
    否则返回False。"""
 
    ……
 
# 开始界面
def startScreen():
    """显示开始屏幕，直到用户按下任意键后进入游戏"""
    ……
 
 
# 读文本地图
def readLevelsFile(filename):
    ……
 
 
# 对墙内元素递归替换
def floodFill(mapObj, x, y, oldCharacter, newCharacter):
    """
    采用递归的方式将文本替换
    """
    ……
 
 
# 绘制地图
def drawMap(mapObj, gameStateObj, goals):
    ……
 
 
# 判断关卡是否结束
def isLevelFinished(levelObj, gameStateObj):
    ……
 
 
# 退出游戏
def terminate():
    pygame.quit()
    sys.exit()
 
 
if __name__ == '__main__':
    main()