#!/usr/bin/env python

import wx
from menubar import TonicMenuBar
from toolbar import TonicToolBar
from pkglistctrl import TonicPkgListCtrl

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

        # Creating the packages list
        self.pkglist = TonicPkgListCtrl(self, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.control = self.pkglist

        # Tadam
        self.Show(True)
