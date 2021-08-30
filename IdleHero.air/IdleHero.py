# 1600 * 900 ,打开老板键,快捷方式url为steam://rungameid/1335240
# -*- encoding=utf8 -*-
__author__ = "Administrator"

import os 
from util import *
from airtest.core.api import *

auto_setup(__file__)

import logging

logger1=logging.getLogger("airtest")
logger1.setLevel(logging.INFO)
ST.LOG_FILE = "log.txt"
# ST.CVSTRATEGY = ['tpl']
ST.THRESHOLD = 0.7

#todo kill unresponse program
def killIdleHero():
    res = os.popen("taskkill.exe /im \"NobrainerHeroes2-Win32-Shipping.exe\" /f").readlines()
    logger.info(res)
    if len(res) > 0:
        res = res[0]
    if '成功' in res:
        return True
    return False
# killIdleHero()

#start the program
def startIdleHero():
    res = os.popen("start explorer steam://rungameid/1335240").readlines()
    if len(res) == 0:
        return True
    return False

#get the window of game
def connectIdleHero():
#     dev = connect_device("Windows:///?title_re=NobrainerHeroes1.*") #没用，找不到图片
    dev = connect_device("Windows:///")
    print(dev)
def checkGameStatus():
    for _ in range(3):
        wait_click("角色",Template(r"tpl1630289910963.png", record_pos=(0.032, 0.209), resolution=(1920, 1080)))
        if wait_click("属性和装备",Template(r"tpl1630289934472.png", record_pos=(-0.307, -0.191), resolution=(1920, 1080))):
            wait_click("关闭",Template(r"tpl1630289952346.png", record_pos=(-0.021, -0.174), resolution=(1920, 1080)),3)
            return True
        sleep(5)
    return False


def beginGame():
    wait_click("开始游戏",[Template(r"tpl1630285038930.png", record_pos=(0.005, 0.076), resolution=(1600, 900)),Template(r"tpl1630288336219.png", record_pos=(-0.285, 0.053), resolution=(1920, 1080))],10)
    
    
    wait_click("读取存档",Template(r"tpl1630288068584.png", record_pos=(-0.251, 0.026), resolution=(1920, 1080)),3)

    wait_click("远征",Template(r"tpl1630288446180.png", record_pos=(-0.284, 0.205), resolution=(1920, 1080)))

    wait_click("远征战斗",Template(r"tpl1630288540740.png", record_pos=(-0.473, -0.154), resolution=(1920, 1080)))

    wait_click("挂机",Template(r"tpl1630288580642.png", record_pos=(-0.307, 0.051), resolution=(1920, 1080)),3)

    
    wait_click("退出战斗界面",Template(r"tpl1630288733373.png", record_pos=(-0.459, -0.202), resolution=(1920, 1080)),3)

    wait_click("远征",Template(r"tpl1630288446180.png", record_pos=(-0.284, 0.205), resolution=(1920, 1080)))
    wait_click("月之秘境",Template(r"tpl1630288825445.png", record_pos=(-0.157, -0.147), resolution=(1920, 1080)))

    wait_click("挂机",Template(r"tpl1630288580642.png", record_pos=(-0.307, 0.051), resolution=(1920, 1080)),3)
    wait_click("退出战斗界面",Template(r"tpl1630289270047.png", record_pos=(-0.459, -0.204), resolution=(1920, 1080)),3)

    wait_click("远征",Template(r"tpl1630288446180.png", record_pos=(-0.284, 0.205), resolution=(1920, 1080)))
    wait_click("矿洞",Template(r"tpl1630288907232.png", record_pos=(-0.235, -0.149), resolution=(1920, 1080)))

    wait_click("战斗开始",Template(r"tpl1630289022738.png", record_pos=(-0.218, 0.086), resolution=(1920, 1080)),3)

    wait_click("退出战斗界面",Template(r"tpl1630289246500.png", record_pos=(-0.459, -0.203), resolution=(1920, 1080)),3)

    wait_click("远征",Template(r"tpl1630288446180.png", record_pos=(-0.284, 0.205), resolution=(1920, 1080)))
    wait_click("丛林",Template(r"tpl1630288922394.png", record_pos=(-0.195, -0.147), resolution=(1920, 1080)))

    wait_click("战斗开始",Template(r"tpl1630289022738.png", record_pos=(-0.218, 0.086), resolution=(1920, 1080)),3)
    wait_click("退出战斗界面",Template(r"tpl1630289118707.png", record_pos=(-0.459, -0.204), resolution=(1920, 1080)),3)

    wait_click("远征",Template(r"tpl1630288446180.png", record_pos=(-0.284, 0.205), resolution=(1920, 1080)))
    wait_click("太阳秘境",Template(r"tpl1630288936627.png", record_pos=(-0.12, -0.148), resolution=(1920, 1080)))

    wait_click("挂机",Template(r"tpl1630288580642.png", record_pos=(-0.307, 0.051), resolution=(1920, 1080)),3)
    wait_click("退出战斗界面",Template(r"tpl1630289220441.png", record_pos=(-0.458, -0.205), resolution=(1920, 1080)),3)
def exitDialog():
    wait_click("TeamViewer发起会话",[Template(r"tpl1630301803630.png", record_pos=(0.086, -0.001), resolution=(1920, 1080))],1)



# connectIdleHero()
# beginGame()
# wait_click("月之秘境",Template(r"tpl1630288825445.png", record_pos=(-0.157, -0.147), resolution=(1920, 1080)))
# checkGameStatus()
# snapshot(filename='D://test.jpg',msg='这里是massage')
# exitDialog()
# sleep(100)

connectIdleHero()
exitDialog()
keyevent("%r")
# beginGame()
status = checkGameStatus()
logger.info(f"check status = {status}")
if status == False:
    logger.info(f"kill Idle Hero")
    killIdleHero()
    sleep(10)
    logger.info(f"start Idle Hero")
    startIdleHero()
    sleep(10)
    logger.info(f"begin the game")
    beginGame()
keyevent("%f")

