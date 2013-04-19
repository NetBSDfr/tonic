#!/usr/bin/env python

import wx
from menubar import TonicMenuBar
from toolbar import TonicToolBar

class View(wx.Frame):
    """ HMI for Tonic """
    def __init__(self, parent, title):
        """ Constructor. """
        wx.Frame.__init__(self, parent, title=title,
                              pos=(-1, -1), size=(600,400))

        # Creating the statusbar
        self.CreateStatusBar()

        # Creating the menubar
        menuBar = TonicMenuBar()
        self.SetMenuBar(menuBar)

        # Creating the toolbar
        toolbar = TonicToolBar(self)
        self.SetToolBar(toolbar)
        toolbar.Realize()

        # Tadam
        self.Show(True)
