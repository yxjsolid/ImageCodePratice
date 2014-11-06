#-*-coding:utf-8-*-
from gui.imageInputPracticeBase import *
import os
import sys
import time
import threading
import random

class imgInputPractice(imgInputPracticeBase):

    STAT_ALL_CNT, STAT_CORRECT_CNT, STAT_ERR_CNT, STAT_ACCURATE, STAT_FASTEST, STAT_SLOWEST = range(6)

    def __init__(self, parent):
        imgInputPracticeBase.__init__(self, parent)


        self.statsInfo = [
                            (self.STAT_ALL_CNT,      u"总数:"),
                            (self.STAT_ERR_CNT,      u"错误:"),
                            (self.STAT_ACCURATE,       u"准确率:"),
                            (self.STAT_FASTEST,      u"最快:"),
                            (self.STAT_SLOWEST,      u"最慢:"),
                          ]

        self.statsDic = {}
        self.fileList = []
        self.fileCnt = 0
        self.currentCode = None
        self.currentIndex = 0
        self.clockBeginTime = 0

        self.totalCnt = 0
        self.errCnt = 0
        self.correctCnt = 0
        self.fast = 9999
        self.slow = 0
        self.accurate = 0
        self.inError = 0


        self.addAllStats()

        self.getAllFileList()
        self.displayImage()

        self.doClock()


    def getNextImageIndex(self):
        index = random.randint(0, self.fileCnt - 1)
        return index


    def resetClock(self):
        self.clockBeginTime = time.time()


    def displayImage(self):
        self.currentIndex = self.getNextImageIndex()
        imgPath = self.fileList[self.currentIndex]
        img = wx.Image(imgPath)
        #self.imgBmp.SetBitmapLabel(wx.BitmapFromImage(img))
        self.imgBmp.SetBitmap(wx.BitmapFromImage(img))
        self.imgBmp.Fit()
        self.resetClock()
        self.currentCode = os.path.split(imgPath)[1].split(".")[0]
        pass


    def getRootPath(self):
        if getattr(sys, 'frozen', None):
            basedir = sys._MEIPASS
        else:
            basedir = os.path.dirname(__file__)

        return basedir

    def getAllFileList(self):
        self.fileList = []
        rootDir = self.getRootPath()
        imgDir = os.path.join(rootDir, "image/10_18")
        for fileName in os.listdir(imgDir):
            path = os.path.join(imgDir, fileName)
            if os.path.isfile(path):
                self.fileList.append(path)

        self.fileCnt = len(self.fileList)


    def onAnswer( self, event ):
        print "onAnsser"
        answer = self.answerTxt.GetValue()
        if answer == self.currentCode:
            self.correctCnt += 1
            diff = time.time() - self.clockBeginTime
            self.fast = min(diff, self.fast)
            self.slow = max(diff, self.slow)

            print "spend %f s"%(diff)
            self.displayImage()
            self.answerTxt.Clear()
            self.inError = 0
            self.totalCnt += 1
        else:
            if not self.inError:
                self.errCnt += 1
                self.inError = 1

            wx.MessageBox(u'错了','Error',wx.OK|wx.ICON_ERROR)
            print "\n error"
            print "input:", answer
            print "correct:", self.currentCode

        self.updateAllStats()

    def updateStats(self, statType, stat):
        text = self.statsDic[statType]
        text.SetLabel(stat)

    def updateAllStats(self):
        self.updateStats(self.STAT_ALL_CNT,str(self.totalCnt))
        self.updateStats(self.STAT_ERR_CNT, str(self.errCnt))
        if self.totalCnt:
            rate = "%.1f%%"%((self.totalCnt - self.errCnt)/float(self.totalCnt)*100)
        else:
            rate = "0"

        self.updateStats(self.STAT_ACCURATE, rate)
        slow = "%.2f s"%(self.slow)
        self.updateStats(self.STAT_SLOWEST, slow)
        fast = "%.2f s"%(self.fast)
        self.updateStats(self.STAT_FASTEST, fast)

        pass

    def __doClock(self):
        diff = 0
        while True:
            label = "%f"%diff
            self.clockText.SetLabel(label)
            time.sleep(0.01)
            diff = time.time() - self.clockBeginTime
        pass


    def doClock(self):
        self.__runTask(self.__doClock, ())


    def __runTask(self, func, arg):
        tsk = threading.Thread(target=func, args=arg)
        tsk.start()
        return tsk


    def addStatElem(self, statInfo):
        statId, label = statInfo
        bSizer = wx.BoxSizer( wx.HORIZONTAL )
        statNameText = wx.StaticText( self.m_panel4, wx.ID_ANY, label, wx.DefaultPosition, wx.DefaultSize, 0 )
        statNameText.Wrap( -1 )
        statNameText.SetMinSize( wx.Size( 40,-1 ) )
        bSizer.Add( statNameText, 0, wx.ALL, 5 )

        #index = str(random.randint(0, 1000))

        statDispText = wx.StaticText( self.m_panel4, wx.ID_ANY, "0", wx.DefaultPosition, wx.DefaultSize, 0 )
        statDispText.Wrap( -1 )
        statDispText.SetMinSize( wx.Size( 40,-1 ) )

        bSizer.Add( statDispText, 0, wx.ALL, 5 )
        self.statSizer.Add( bSizer, 1, wx.EXPAND, 5 )

        self.statsDic[statId] = statDispText


    def addAllStats(self):
        for statInfo in self.statsInfo:
            self.addStatElem(statInfo)


if __name__ == "__main__":
    app = wx.App(0)
    frame = imgInputPractice(None)

    #frame.addImage("tmp/111.jpg")

    #frame.addAllImages("tmp/parse/result")

    frame.Show()
    app.MainLoop()