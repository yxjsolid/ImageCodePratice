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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
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
		
		self.m_radioBtn2 = wx.RadioButton( self.m_panel38, wx.ID_ANY, u"2模式", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		
		
		self.m_panel39.SetSizer( sbSizer1 )
		self.m_panel39.Layout()
		sbSizer1.Fit( self.m_panel39 )
		gbSizer3.Add( self.m_panel39, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_panel5 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		gbSizer28 = wx.GridBagSizer( 0, 0 )
		gbSizer28.SetFlexibleDirection( wx.BOTH )
		gbSizer28.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel34 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.RAISED_BORDER|wx.TAB_TRAVERSAL )
		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel41 = wx.Panel( self.m_panel34, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer62 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button1 = wx.Button( self.m_panel41, wx.ID_ANY, u"开始", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer62.Add( self.m_button1, 0, wx.ALL, 5 )
		
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
		gbSizer28.Add( self.m_panel34, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel51 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer16 = wx.GridBagSizer( 0, 0 )
		gbSizer16.SetFlexibleDirection( wx.BOTH )
		gbSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.imgBmp = wx.StaticBitmap( self.m_panel51, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer16.Add( self.imgBmp, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.answerTxt = wx.TextCtrl( self.m_panel51, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		gbSizer16.Add( self.answerTxt, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.m_panel51.SetSizer( gbSizer16 )
		self.m_panel51.Layout()
		gbSizer16.Fit( self.m_panel51 )
		gbSizer28.Add( self.m_panel51, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		
		gbSizer28.AddGrowableCol( 0 )
		
		self.m_panel5.SetSizer( gbSizer28 )
		self.m_panel5.Layout()
		gbSizer28.Fit( self.m_panel5 )
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
		self.answerTxt.Bind( wx.EVT_TEXT_ENTER, self.onAnswer )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onAnswer( self, event ):
		event.Skip()
	

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer60 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer16 = wx.GridBagSizer( 0, 0 )
		gbSizer16.SetFlexibleDirection( wx.BOTH )
		gbSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.imgBmp = wx.StaticBitmap( self.m_panel5, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer16.Add( self.imgBmp, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.answerTxt = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		gbSizer16.Add( self.answerTxt, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.clockText = wx.StaticText( self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.clockText.Wrap( -1 )
		gbSizer16.Add( self.clockText, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.m_panel5.SetSizer( gbSizer16 )
		self.m_panel5.Layout()
		gbSizer16.Fit( self.m_panel5 )
		bSizer60.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer60 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.answerTxt.Bind( wx.EVT_TEXT_ENTER, self.onAnswer )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onAnswer( self, event ):
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
	

