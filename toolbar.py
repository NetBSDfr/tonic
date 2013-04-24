#!/usr/bin/env python

""" View for Tonic toolbar. """

import wx

class TonicToolBar(wx.ToolBar):
    """ Tonic toolbar. """
    def __init__(self, parent):
        """ Constructor. """
        wx.ToolBar.__init__(self, parent, 
                            style=wx.TB_HORZ_TEXT)
                            
        self.open_ico = None
        self.exit_ico = None
        self.undo_ico = None
        self.apply_ico = None

        self.__create_icons()
        self.__fill_toolbar()

    def __create_icons(self):
        """ Create icons. """
        self.open_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN,
                                            wx.ART_TOOLBAR, (16,16))
        self.exit_ico = wx.ArtProvider.GetBitmap(wx.ART_QUIT,
                                            wx.ART_TOOLBAR, (16,16))
        self.undo_ico = wx.ArtProvider.GetBitmap(wx.ART_UNDO,
                                            wx.ART_TOOLBAR, (16,16))
        self.apply_ico = wx.ArtProvider.GetBitmap(wx.ART_TICK_MARK,
                                            wx.ART_TOOLBAR, (16,16))

    def __fill_toolbar(self):
        """ Insert elements in toolbar. """
        self.AddSimpleTool(wx.ID_OPEN, self.open_ico, "Open", "")
        self.AddSimpleTool(wx.ID_EXIT, self.exit_ico, "Exit", "")
        self.AddSeparator()
        self.AddSimpleTool(wx.ID_UNDO, self.undo_ico, "Unmark All", "")
        self.AddSeparator()
        self.AddSimpleTool(wx.ID_APPLY, self.apply_ico, "Install", "Install")
        self.AddSeparator()
