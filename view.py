#!/usr/bin/env python

import wx

class View(wx.Frame):
    """ HMI for Tonic """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title,
                              pos=(-1, -1), size=(600,400))

        # Creating the statusbar in the bottom of the window
        self.CreateStatusBar()

        # Setting up the menu.
        # File menu
        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open",
                                       " Open a file to edit")
        self.menuExit = filemenu.Append(wx.ID_EXIT,
                                   "E&xit"," Terminate the program")

        # Edit menu
        editmenu = wx.Menu()
        menuUnmarkAll = editmenu.Append(wx.ID_UNDO, "&Unmark All", "")
        editmenu.AppendSeparator()
        menuUpdate = editmenu.Append(wx.ID_REFRESH, "&Update", "")
        editmenu.AppendSeparator()
        menuApply = editmenu.Append(wx.ID_APPLY, "&Apply", "")

        # Settings menu
        settingsmenu = wx.Menu()
        menuRepository = settingsmenu.Append(wx.NewId(), "&Repository", "")

        # Help menu
        helpmenu = wx.Menu()
        self.menuAbout= helpmenu.Append(wx.ID_ABOUT,
                                   "&About"," Information about this program")

        # Creating the menubar.
        # Adding the "filemenu" to the MenuBar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File")
        menuBar.Append(editmenu,"&Edit")
        menuBar.Append(settingsmenu,"&Settings")
        menuBar.Append(helpmenu,"&Help")
        # Adding the MenuBar to the Frame content.
        self.SetMenuBar(menuBar)
        self.Show(True)

