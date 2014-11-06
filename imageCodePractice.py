#-*-coding:utf-8-*-
from gui.imageInputPracticeBase import *
import os
import sys
import time
import threading
import random

class imgInputPractice(imgInputPracticeBase):

    STAT_ALL_CNT, STAT_CORRECT_CNT, STAT_ERR_CNT, STAT_ACCURATE, STAT_FASTEST, STAT_SLOWEST = range(6)
    MODE_PRACTICE, MODE_BID = range(2)


    def __init__(self, parent):
        imgInputPracticeBase.__init__(self, parent)


        self.statsInfo = [
                            (self.STAT_ALL_CNT,      u"总数:"),
                            (self.STAT_ERR_CNT,      u"错误:"),
                            (self.STAT_ACCURATE,     u"准确率:"),
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
        self.mode = self.MODE_PRACTICE
        self.showAnswer = False
        self.bidAmount = 73200

        self.showAnswerDisable()
        self.addAllStats()
        self.getAllFileList()
        #self.addDisplayPanel()

        self.displayImage()

        self.doClock()
        self.onModeSelect()


    def getNewImage(self):
        self.currentIndex = random.randint(0, self.fileCnt - 1)
        imgPath = self.fileList[self.currentIndex]
        self.currentCode = os.path.split(imgPath)[1].split(".")[0]


    def resetClock(self):
        self.clockBeginTime = time.time()


    def displayImage(self):
        self.getNewImage()
        imgPath = self.fileList[self.currentIndex]
        img = wx.Image(imgPath)
        #self.imgBmp.SetBitmapLabel(wx.BitmapFromImage(img))
        self.imgBmp.SetBitmap(wx.BitmapFromImage(img))
        self.imgBmp.Fit()
        self.resetClock()
        self.displayAnswer()
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


    def checkAnswer(self, answer):
        isErr = 0
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

            isErr = 0
        else:
            if not self.inError:
                self.errCnt += 1
                self.inError = 1
            isErr = 1

        self.updateAllStats()
        return isErr

    def onPracticeAnswer( self, event ):
        print "onAnsser"
        answer = self.answerTxt.GetValue()
        err = self.checkAnswer(answer)

        if err:
            wx.MessageBox(u'错了','Error',wx.OK|wx.ICON_ERROR)
        else:
            self.displayImage()


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



    def addDisplayPanel(self):
        panel = bidPanelBase(self.disPanel)
        #self.dispSizer.Add( panel, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
        self.dispSizer.Add( panel, 1, wx.EXPAND |wx.ALL, 5 )
        panel = practicePanelBase(self.disPanel)
        #self.dispSizer.Add( panel, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

        self.dispSizer.Add( panel, 1, wx.EXPAND |wx.ALL, 5 )



    def onModeBid(self, evt):
        self.mode = self.MODE_BID
        self.onModeSelect()

    def onModePractice(self, evt):
        self.mode = self.MODE_PRACTICE
        self.onModeSelect()

    def onModeSelect(self):
        if self.mode == self.MODE_PRACTICE:
            self.bidPanel.Show(False)
            self.practicePanel.Show(True)

        if self.mode == self.MODE_BID:
            self.bidPanel.Show(True)
            self.practicePanel.Show(False)

        self.dispSizer.Fit( self.disPanel )
        self.resetClock()


    def checkBidAmount(self, amount):
        try:
            num = int(amount)
            print num
        except Exception,e:
            return False

        if num%100 > 0:
            return False

        if num > self.bidAmount + 300 or num  <  self.bidAmount -300:
            return False

        return True

    def onBid( self, event ):
        self.getNewImage()
        imgPath = self.fileList[self.currentIndex]
        amount = self.bidAmountTxt.GetValue()

        print "amount:", amount

        valid = self.checkBidAmount(amount)

        if not valid:
            wx.MessageBox(u'错了','Error',wx.OK|wx.ICON_ERROR)
            return


        dialog = ImageCodeDialog(None, imgPath, amount)
        result = dialog.ShowModal()
        err = 0
        if result == wx.ID_OK:
            answer =  dialog.getInput()
            print answer
            err = self.checkAnswer(answer)
        else:
            pass
        dialog.Destroy()

        self.bidAmountTxt.Clear()

        if err:
            wx.MessageBox(u'错了','Error',wx.OK|wx.ICON_ERROR)

        pass


    def showAnswerDisable(self):
        self.showAnswer = False
        self.answerCB.SetValue(False)

    def displayAnswer(self):
        if self.showAnswer:
            print self.currentCode
            self.showAnswerText.SetLabel(self.currentCode)
        else:
            self.showAnswerText.SetLabel("")


    def onShowAnswer(self, event):
        if self.answerCB.IsChecked():
            self.showAnswer = True
        else:
            self.showAnswer = False

        self.displayAnswer()
        pass

    def onDec300(self, evt):
        amount = self.bidAmount - 300
        self.updateBidAmount(amount)

    def onDec200(self, evt):
        amount = self.bidAmount - 200
        self.updateBidAmount(amount)

    def onDec100(self, evt):
        amount = self.bidAmount - 100
        self.updateBidAmount(amount)

    def onAdd300(self, evt):
        amount = self.bidAmount + 300
        self.updateBidAmount(amount)

    def onAdd200(self, evt):
        amount = self.bidAmount + 200
        self.updateBidAmount(amount)

    def onAdd100(self, evt):
        amount = self.bidAmount + 100
        self.updateBidAmount(amount)

    def updateBidAmount(self, bidAmount):
        self.bidAmountTxt.SetLabel(str(bidAmount))

class ImageCodeDialog(ImageCodeDialogBase):
    def __init__(self, parent, fileName, amount):
        ImageCodeDialogBase.__init__(self, parent)

        self.setImage(fileName)
        self.code_text.SetFocus()
        self.setInfo(amount)

    def getInput(self):
        return self.code_text.GetValue()

    def setImage(self, fileName):

        img = wx.Image(fileName)
        #self.imgBmp.SetBitmapLabel(wx.BitmapFromImage(img))
        self.bid_imageBmp.SetBitmap(wx.BitmapFromImage(img))
        self.bid_imageBmp.Fit()

        pass


    def setInfo(self, amount):
        info = u"您的出价金额为:%s元"%str(amount)
        self.infoText.SetLabel(info)


if __name__ == "__main__":
    app = wx.App(0)
    frame = imgInputPractice(None)

    #frame.addImage("tmp/111.jpg")

    #frame.addAllImages("tmp/parse/result")

    frame.Show()
    app.MainLoop()