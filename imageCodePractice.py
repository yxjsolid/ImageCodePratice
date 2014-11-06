#-*-coding:utf-8-*-
from gui.imageInputPracticeBase import *
import os
import sys

class imgInputPractice(imgInputPracticeBase):
    def __init__(self, parent):
        imgInputPracticeBase.__init__(self, parent)
        self.index = 0
        self.fileList = []
        self.currentCode = None
        self.getAllFileList()
        self.displayImage()

    def displayImage(self):
        imgPath = self.fileList[self.index]
        self.index += 1

        img = wx.Image(imgPath)
        #self.imgBmp.SetBitmapLabel(wx.BitmapFromImage(img))
        self.imgBmp.SetBitmap(wx.BitmapFromImage(img))
        self.imgBmp.Fit()
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


    def onAnswer( self, event ):
        answer = self.answerTxt.GetValue()


        if answer == self.currentCode:
            self.displayImage()
            self.answerTxt.Clear()
        else:
            wx.MessageBox(u'错了','Error',wx.OK|wx.ICON_ERROR)
            print "\n error"
            print "input:", answer
            print "correct:", self.currentCode







        pass



if __name__ == "__main__":
    app = wx.App(0)
    frame = imgInputPractice(None)

    #frame.addImage("tmp/111.jpg")

    #frame.addAllImages("tmp/parse/result")

    frame.Show()
    app.MainLoop()