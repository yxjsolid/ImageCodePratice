# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class imgInputPracticeBase
###########################################################################

class imgInputPracticeBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 644,467 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer51 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel38 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel38, wx.ID_ANY, u"模式" ), wx.VERTICAL )
		
		self.m_radioBtn1 = wx.RadioButton( self.m_panel38, wx.ID_ANY, u"练习模式", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn1.SetValue( True ) 
		sbSizer4.Add( self.m_radioBtn1, 0, wx.ALL, 5 )
		
		self.m_radioBtn2 = wx.RadioButton( self.m_panel38, wx.ID_ANY, u"拍牌模式", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_radioBtn2, 0, wx.ALL, 5 )
		
		
		self.m_panel38.SetSizer( sbSizer4 )
		self.m_panel38.Layout()
		sbSizer4.Fit( self.m_panel38 )
		gbSizer3.Add( self.m_panel38, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel39 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel39, wx.ID_ANY, u"统计" ), wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self.m_panel39, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.statSizer = wx.BoxSizer( wx.VERTICAL )
		
		
		self.m_panel4.SetSizer( self.statSizer )
		self.m_panel4.Layout()
		self.statSizer.Fit( self.m_panel4 )
		sbSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_button30 = wx.Button( self.m_panel39, wx.ID_ANY, u"重置", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_button30, 0, wx.ALL, 5 )
		
		
		self.m_panel39.SetSizer( sbSizer1 )
		self.m_panel39.Layout()
		sbSizer1.Fit( self.m_panel39 )
		gbSizer3.Add( self.m_panel39, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_panel5 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.gbsizer = wx.GridBagSizer( 0, 0 )
		self.gbsizer.SetFlexibleDirection( wx.BOTH )
		self.gbsizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel34 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.RAISED_BORDER|wx.TAB_TRAVERSAL )
		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel41 = wx.Panel( self.m_panel34, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer62 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText98 = wx.StaticText( self.m_panel41, wx.ID_ANY, u"计时:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText98.Wrap( -1 )
		bSizer62.Add( self.m_staticText98, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.clockText = wx.StaticText( self.m_panel41, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.clockText.Wrap( -1 )
		bSizer62.Add( self.clockText, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.m_panel41.SetSizer( bSizer62 )
		self.m_panel41.Layout()
		bSizer62.Fit( self.m_panel41 )
		bSizer61.Add( self.m_panel41, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel34.SetSizer( bSizer61 )
		self.m_panel34.Layout()
		bSizer61.Fit( self.m_panel34 )
		self.gbsizer.Add( self.m_panel34, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		self.disPanel = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.RAISED_BORDER|wx.TAB_TRAVERSAL )
		self.dispSizer = wx.GridBagSizer( 0, 0 )
		self.dispSizer.SetFlexibleDirection( wx.BOTH )
		self.dispSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		self.dispSizer.SetEmptyCellSize( wx.Size( 0,0 ) )
		
		self.practicePanel = wx.Panel( self.disPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		gbSizer16 = wx.GridBagSizer( 0, 0 )
		gbSizer16.SetFlexibleDirection( wx.BOTH )
		gbSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.imgBmp = wx.StaticBitmap( self.practicePanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer16.Add( self.imgBmp, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.answerTxt = wx.TextCtrl( self.practicePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.SIMPLE_BORDER )
		gbSizer16.Add( self.answerTxt, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_panel46 = wx.Panel( self.practicePanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		bSizer34 = wx.BoxSizer( wx.VERTICAL )
		
		self.answerCB = wx.CheckBox( self.m_panel46, wx.ID_ANY, u"看答案", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.answerCB.SetValue(True) 
		bSizer34.Add( self.answerCB, 0, wx.ALL, 5 )
		
		self.showAnswerText = wx.StaticText( self.m_panel46, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.showAnswerText.Wrap( -1 )
		self.showAnswerText.SetMinSize( wx.Size( 60,-1 ) )
		
		bSizer34.Add( self.showAnswerText, 0, wx.ALL, 5 )
		
		
		self.m_panel46.SetSizer( bSizer34 )
		self.m_panel46.Layout()
		bSizer34.Fit( self.m_panel46 )
		gbSizer16.Add( self.m_panel46, wx.GBPosition( 0, 1 ), wx.GBSpan( 2, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		
		self.practicePanel.SetSizer( gbSizer16 )
		self.practicePanel.Layout()
		gbSizer16.Fit( self.practicePanel )
		self.dispSizer.Add( self.practicePanel, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		self.bidPanel = wx.Panel( self.disPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer31 = wx.GridBagSizer( 0, 0 )
		gbSizer31.SetFlexibleDirection( wx.BOTH )
		gbSizer31.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel77 = wx.Panel( self.bidPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		gbSizer36 = wx.GridBagSizer( 0, 0 )
		gbSizer36.SetFlexibleDirection( wx.BOTH )
		gbSizer36.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel42 = wx.Panel( self.m_panel77, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer65 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText99 = wx.StaticText( self.m_panel42, wx.ID_ANY, u"目前最低可成交价：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText99.Wrap( -1 )
		self.m_staticText99.SetFont( wx.Font( 18, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText99.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		bSizer65.Add( self.m_staticText99, 0, wx.ALL, 5 )
		
		self.m_staticText100 = wx.StaticText( self.m_panel42, wx.ID_ANY, u"73200元", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText100.Wrap( -1 )
		self.m_staticText100.SetFont( wx.Font( 18, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText100.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		bSizer65.Add( self.m_staticText100, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.m_panel42.SetSizer( bSizer65 )
		self.m_panel42.Layout()
		bSizer65.Fit( self.m_panel42 )
		gbSizer36.Add( self.m_panel42, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel48 = wx.Panel( self.m_panel77, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText109 = wx.StaticText( self.m_panel48, wx.ID_ANY, u"减价快捷键", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText109.Wrap( -1 )
		bSizer71.Add( self.m_staticText109, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self.m_panel48, wx.ID_ANY, u"-300", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		bSizer71.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self.m_panel48, wx.ID_ANY, u"-200", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		bSizer71.Add( self.m_button3, 0, wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self.m_panel48, wx.ID_ANY, u"-100", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button4.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		bSizer71.Add( self.m_button4, 0, wx.ALL, 5 )
		
		
		self.m_panel48.SetSizer( bSizer71 )
		self.m_panel48.Layout()
		bSizer71.Fit( self.m_panel48 )
		gbSizer36.Add( self.m_panel48, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel481 = wx.Panel( self.m_panel77, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer711 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1091 = wx.StaticText( self.m_panel481, wx.ID_ANY, u"减价快捷键", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1091.Wrap( -1 )
		bSizer711.Add( self.m_staticText1091, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button21 = wx.Button( self.m_panel481, wx.ID_ANY, u"+300", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer711.Add( self.m_button21, 0, wx.ALL, 5 )
		
		self.m_button31 = wx.Button( self.m_panel481, wx.ID_ANY, u"+200", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer711.Add( self.m_button31, 0, wx.ALL, 5 )
		
		self.m_button41 = wx.Button( self.m_panel481, wx.ID_ANY, u"+100", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer711.Add( self.m_button41, 0, wx.ALL, 5 )
		
		
		self.m_panel481.SetSizer( bSizer711 )
		self.m_panel481.Layout()
		bSizer711.Fit( self.m_panel481 )
		gbSizer36.Add( self.m_panel481, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel4811 = wx.Panel( self.m_panel77, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText10911 = wx.StaticText( self.m_panel4811, wx.ID_ANY, u"自行输入价格：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10911.Wrap( -1 )
		bSizer7111.Add( self.m_staticText10911, 0, wx.ALL, 5 )
		
		self.bidAmountTxt = wx.TextCtrl( self.m_panel4811, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bidAmountTxt.SetMinSize( wx.Size( 150,-1 ) )
		
		bSizer7111.Add( self.bidAmountTxt, 0, wx.ALL, 5 )
		
		self.btn_bid = wx.Button( self.m_panel4811, wx.ID_ANY, u"出 价", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		self.btn_bid.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		self.btn_bid.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.btn_bid.SetBackgroundColour( wx.Colour( 83, 83, 255 ) )
		
		bSizer7111.Add( self.btn_bid, 0, wx.ALL, 5 )
		
		
		self.m_panel4811.SetSizer( bSizer7111 )
		self.m_panel4811.Layout()
		bSizer7111.Fit( self.m_panel4811 )
		gbSizer36.Add( self.m_panel4811, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel77.SetSizer( gbSizer36 )
		self.m_panel77.Layout()
		gbSizer36.Fit( self.m_panel77 )
		gbSizer31.Add( self.m_panel77, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.m_panel79 = wx.Panel( self.bidPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer37 = wx.GridBagSizer( 0, 0 )
		gbSizer37.SetFlexibleDirection( wx.BOTH )
		gbSizer37.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel55 = wx.Panel( self.m_panel79, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel55.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer76 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText114 = wx.StaticText( self.m_panel55, wx.ID_ANY, u"投标拍卖", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText114.Wrap( -1 )
		self.m_staticText114.SetFont( wx.Font( 18, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText114.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_staticText114.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer76.Add( self.m_staticText114, 0, wx.ALL, 5 )
		
		
		self.m_panel55.SetSizer( bSizer76 )
		self.m_panel55.Layout()
		bSizer76.Fit( self.m_panel55 )
		gbSizer37.Add( self.m_panel55, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), 0, 5 )
		
		self.m_panel80 = wx.Panel( self.m_panel79, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel80.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		self.m_panel80.SetMinSize( wx.Size( 360,2 ) )
		
		gbSizer37.Add( self.m_panel80, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		
		self.m_panel79.SetSizer( gbSizer37 )
		self.m_panel79.Layout()
		gbSizer37.Fit( self.m_panel79 )
		gbSizer31.Add( self.m_panel79, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		
		self.bidPanel.SetSizer( gbSizer31 )
		self.bidPanel.Layout()
		gbSizer31.Fit( self.bidPanel )
		self.dispSizer.Add( self.bidPanel, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		
		self.disPanel.SetSizer( self.dispSizer )
		self.disPanel.Layout()
		self.dispSizer.Fit( self.disPanel )
		self.gbsizer.Add( self.disPanel, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		
		self.gbsizer.AddGrowableCol( 0 )
		
		self.m_panel5.SetSizer( self.gbsizer )
		self.m_panel5.Layout()
		self.gbsizer.Fit( self.m_panel5 )
		gbSizer3.Add( self.m_panel5, wx.GBPosition( 0, 1 ), wx.GBSpan( 2, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		
		gbSizer3.AddGrowableCol( 1 )
		gbSizer3.AddGrowableRow( 1 )
		
		self.m_panel2.SetSizer( gbSizer3 )
		self.m_panel2.Layout()
		gbSizer3.Fit( self.m_panel2 )
		bSizer51.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer51 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_radioBtn1.Bind( wx.EVT_RADIOBUTTON, self.onModePractice )
		self.m_radioBtn2.Bind( wx.EVT_RADIOBUTTON, self.onModeBid )
		self.m_button30.Bind( wx.EVT_BUTTON, self.onStatReset )
		self.answerTxt.Bind( wx.EVT_TEXT_ENTER, self.onPracticeAnswer )
		self.answerCB.Bind( wx.EVT_CHECKBOX, self.onShowAnswer )
		self.m_button2.Bind( wx.EVT_BUTTON, self.onDec300 )
		self.m_button3.Bind( wx.EVT_BUTTON, self.onDec200 )
		self.m_button4.Bind( wx.EVT_BUTTON, self.onDec100 )
		self.m_button21.Bind( wx.EVT_BUTTON, self.onAdd300 )
		self.m_button31.Bind( wx.EVT_BUTTON, self.onAdd200 )
		self.m_button41.Bind( wx.EVT_BUTTON, self.onAdd100 )
		self.btn_bid.Bind( wx.EVT_BUTTON, self.onBid )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onModePractice( self, event ):
		event.Skip()
	
	def onModeBid( self, event ):
		event.Skip()
	
	def onStatReset( self, event ):
		event.Skip()
	
	def onPracticeAnswer( self, event ):
		event.Skip()
	
	def onShowAnswer( self, event ):
		event.Skip()
	
	def onDec300( self, event ):
		event.Skip()
	
	def onDec200( self, event ):
		event.Skip()
	
	def onDec100( self, event ):
		event.Skip()
	
	def onAdd300( self, event ):
		event.Skip()
	
	def onAdd200( self, event ):
		event.Skip()
	
	def onAdd100( self, event ):
		event.Skip()
	
	def onBid( self, event ):
		event.Skip()
	

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, u"label" ), wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText16 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"总数：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		bSizer2.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer2.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText161 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"正确：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )
		bSizer21.Add( self.m_staticText161, 0, wx.ALL, 5 )
		
		self.m_staticText171 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"100", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171.Wrap( -1 )
		bSizer21.Add( self.m_staticText171, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer21, 1, wx.EXPAND, 5 )
		
		bSizer211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1611 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"错误", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1611.Wrap( -1 )
		bSizer211.Add( self.m_staticText1611, 0, wx.ALL, 5 )
		
		self.m_staticText1711 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1711.Wrap( -1 )
		bSizer211.Add( self.m_staticText1711, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer211, 1, wx.EXPAND, 5 )
		
		bSizer2111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText16111 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16111.Wrap( -1 )
		bSizer2111.Add( self.m_staticText16111, 0, wx.ALL, 5 )
		
		self.m_staticText17111 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17111.Wrap( -1 )
		bSizer2111.Add( self.m_staticText17111, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2111, 1, wx.EXPAND, 5 )
		
		bSizer21111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText161111 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161111.Wrap( -1 )
		bSizer21111.Add( self.m_staticText161111, 0, wx.ALL, 5 )
		
		self.m_staticText171111 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171111.Wrap( -1 )
		bSizer21111.Add( self.m_staticText171111, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer21111, 1, wx.EXPAND, 5 )
		
		bSizer21112 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText161112 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161112.Wrap( -1 )
		bSizer21112.Add( self.m_staticText161112, 0, wx.ALL, 5 )
		
		self.m_staticText171112 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171112.Wrap( -1 )
		bSizer21112.Add( self.m_staticText171112, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer21112, 1, wx.EXPAND, 5 )
		
		bSizer21113 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText161113 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161113.Wrap( -1 )
		bSizer21113.Add( self.m_staticText161113, 0, wx.ALL, 5 )
		
		self.m_staticText171113 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171113.Wrap( -1 )
		bSizer21113.Add( self.m_staticText171113, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer21113, 1, wx.EXPAND, 5 )
		
		
		self.m_panel4.SetSizer( bSizer1 )
		self.m_panel4.Layout()
		bSizer1.Fit( self.m_panel4 )
		sbSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		gbSizer3.Add( sbSizer1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.m_panel5 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer16 = wx.GridBagSizer( 0, 0 )
		gbSizer16.SetFlexibleDirection( wx.BOTH )
		gbSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.imgBmp = wx.StaticBitmap( self.m_panel5, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer16.Add( self.imgBmp, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.answerTxt = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer16.Add( self.answerTxt, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.clockText = wx.StaticText( self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.clockText.Wrap( -1 )
		gbSizer16.Add( self.clockText, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.m_panel5.SetSizer( gbSizer16 )
		self.m_panel5.Layout()
		gbSizer16.Fit( self.m_panel5 )
		gbSizer3.Add( self.m_panel5, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel2.SetSizer( gbSizer3 )
		self.m_panel2.Layout()
		gbSizer3.Fit( self.m_panel2 )
		gbSizer2.Add( self.m_panel2, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( gbSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ImageCodeDialogBase
###########################################################################

class ImageCodeDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 513,337 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gbSizer22 = wx.GridBagSizer( 0, 0 )
		gbSizer22.SetFlexibleDirection( wx.BOTH )
		gbSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_panel41 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel41.SetBackgroundColour( wx.Colour( 77, 77, 255 ) )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		self.txxxt = wx.StaticText( self.m_panel41, wx.ID_ANY, u"输入校验码", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txxxt.Wrap( -1 )
		self.txxxt.SetFont( wx.Font( 18, 70, 90, 92, False, wx.EmptyString ) )
		self.txxxt.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer29.Add( self.txxxt, 0, wx.ALL, 5 )
		
		
		self.m_panel41.SetSizer( bSizer29 )
		self.m_panel41.Layout()
		bSizer29.Fit( self.m_panel41 )
		gbSizer22.Add( self.m_panel41, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel42 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
		gbSizer23 = wx.GridBagSizer( 0, 0 )
		gbSizer23.SetFlexibleDirection( wx.BOTH )
		gbSizer23.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel43 = wx.Panel( self.m_panel42, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel43.SetBackgroundColour( wx.Colour( 215, 223, 232 ) )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		self.infoText = wx.StaticText( self.m_panel43, wx.ID_ANY, u"您的出价金额为：73500元", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.infoText.Wrap( -1 )
		self.infoText.SetFont( wx.Font( 16, 70, 90, 92, False, wx.EmptyString ) )
		self.infoText.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		self.infoText.SetBackgroundColour( wx.Colour( 211, 223, 243 ) )
		
		bSizer30.Add( self.infoText, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.m_panel43.SetSizer( bSizer30 )
		self.m_panel43.Layout()
		bSizer30.Fit( self.m_panel43 )
		gbSizer23.Add( self.m_panel43, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.m_panel44 = wx.Panel( self.m_panel42, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText39 = wx.StaticText( self.m_panel44, wx.ID_ANY, u"请输入验证码：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		self.m_staticText39.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText39.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )
		
		bSizer31.Add( self.m_staticText39, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.code_text = wx.TextCtrl( self.m_panel44, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.code_text.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer31.Add( self.code_text, 0, wx.ALL, 5 )
		
		self.bid_imageBmp = wx.StaticBitmap( self.m_panel44, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.bid_imageBmp, 0, wx.ALL, 5 )
		
		
		self.m_panel44.SetSizer( bSizer31 )
		self.m_panel44.Layout()
		bSizer31.Fit( self.m_panel44 )
		gbSizer23.Add( self.m_panel44, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 50 )
		
		
		gbSizer23.AddGrowableCol( 0 )
		
		self.m_panel42.SetSizer( gbSizer23 )
		self.m_panel42.Layout()
		gbSizer23.Fit( self.m_panel42 )
		gbSizer22.Add( self.m_panel42, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel45 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button26 = wx.Button( self.m_panel45, wx.ID_OK, u"确 定", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button26.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_button26.SetBackgroundColour( wx.Colour( 50, 50, 255 ) )
		
		gSizer1.Add( self.m_button26, 0, wx.ALIGN_RIGHT|wx.RIGHT, 30 )
		
		self.m_button27 = wx.Button( self.m_panel45, wx.ID_CANCEL, u"取 消", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button27.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_button27.SetBackgroundColour( wx.Colour( 50, 50, 255 ) )
		
		gSizer1.Add( self.m_button27, 0, wx.ALIGN_LEFT|wx.LEFT, 30 )
		
		
		self.m_panel45.SetSizer( gSizer1 )
		self.m_panel45.Layout()
		gSizer1.Fit( self.m_panel45 )
		gbSizer22.Add( self.m_panel45, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 15 )
		
		
		gbSizer22.AddGrowableCol( 0 )
		
		self.SetSizer( gbSizer22 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

