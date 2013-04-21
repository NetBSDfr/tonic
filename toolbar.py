#!/usr/bin/env python

import wx

class TonicToolBar(wx.ToolBar):
    """ Tonic toolbar. """
    def __init__(self, parent):
        """ Constructor. """
        wx.ToolBar.__init__(self, parent)

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

    def __fill_toolbar(self):
        """ Insert elements in toolbar. """
        self.AddSimpleTool(wx.ID_OPEN, self.open_ico, "Open", "")
        self.AddSimpleTool(wx.ID_EXIT, self.exit_ico, "Exit", "")
        self.AddSeparator()
        self.AddSimpleTool(wx.ID_UNDO, self.undo_ico, "Unmark All", "")

