#!/usr/bin/env python

import wx

class TonicMenuBar(wx.MenuBar):
    """ Tonic menubar. """
    def __init__(self):
        """ Constructor. """
        wx.MenuBar.__init__(self)

        self.__create_menus()
        self.__fill_menubar()

    def __create_menus(self):
        """ Create all menus. """
        # File menu
        self.filemenu = wx.Menu()
        self.menuOpen = self.filemenu.Append(wx.ID_OPEN, "&Open",
                                       " Open a file to edit")
        self.menuExit = self.filemenu.Append(wx.ID_EXIT,
                                   "E&xit"," Terminate the program")

        # Edit menu
        self.editmenu = wx.Menu()
        self.menuUnmarkAll = self.editmenu.Append(wx.ID_UNDO, "&Unmark All", "")
        self.editmenu.AppendSeparator()
        self.menuUpdate = self.editmenu.Append(wx.ID_REFRESH, "&Update", "")
        self.editmenu.AppendSeparator()
        self.menuApply = self.editmenu.Append(wx.ID_APPLY, "&Apply", "")

        # Settings menu
        self.settingsmenu = wx.Menu()
        self.menuRepository = self.settingsmenu.Append(wx.NewId(), "&Repository", "")

        # Help menu
        self.helpmenu = wx.Menu()
        self.menuAbout= self.helpmenu.Append(wx.ID_ABOUT,
                                   "&About"," Information about this program")

    def __fill_menubar(self):
        """ Place menus in menubar. """
        self.Append(self.filemenu, "&File")
        self.Append(self.editmenu, "&Edit")
        self.Append(self.settingsmenu, "&Settings")
        self.Append(self.helpmenu, "&Help")

