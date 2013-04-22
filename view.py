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
                              pos=(-1, -1), size=(800,600))
        self.list_category = wx.ListCtrl(self, -1, style=wx.LC_REPORT|wx.LC_NO_HEADER)
        self.list_category.InsertColumn(0, 'Categories')
        self.search_box = wx.SearchCtrl(self, -1, "")
        self.list_pkg = TonicPkgListCtrl(self,
                                         style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.description_tab = wx.Notebook(self, -1, style=wx.NB_BOTTOM)
        self.description_tab_desc = wx.Panel(self.description_tab, -1)
        self.description_tab_dep = wx.Panel(self.description_tab, -1)
        self.description_tab_chg = wx.Panel(self.description_tab, -1)

        # Creating the statusbar
        self.CreateStatusBar()

        # Creating the menubar
        menuBar = TonicMenuBar()
        self.SetMenuBar(menuBar)

        # Creating the toolbar
        toolbar = TonicToolBar(self)
        self.SetToolBar(toolbar)
        toolbar.Realize()

        # Layout
        self.__set_layout_properties()
        self.__do_layout()

        # Tadam
        self.Show(True)

    def __set_layout_properties(self):
        """ Set layout properties """
        self.list_category.SetMinSize((250, 524))
        self.search_box.SetMinSize((550, 25))

    def __do_layout(self):
        """ Construct the layout """
        # main box.
        h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # The second box, the box into the box, yodawg.
        v_sizer = wx.BoxSizer(wx.VERTICAL)

        h_sizer.Add(self.list_category, 0, 0, 0)
        v_sizer.Add(self.search_box, 0, 0, 0)
        v_sizer.Add(self.list_pkg, 1, wx.EXPAND, 0)
        self.description_tab.AddPage(self.description_tab_desc,
                                     "Description")
        self.description_tab.AddPage(self.description_tab_dep,
                                     "Dependencies")
        self.description_tab.AddPage(self.description_tab_chg,
                                     "Changes List")
        v_sizer.Add(self.description_tab, 1, wx.EXPAND, 0)
        h_sizer.Add(v_sizer, 1, wx.EXPAND, 0)
        self.SetSizer(h_sizer)
        self.Layout()
