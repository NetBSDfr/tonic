#!/usr/bin/env python
#
# Copyright (c) 2013 Guilaume Delpierre <gde@llew.me>
# Copyright (c) 2013 Sylvain Mora <sylvain.mora@solevis.net>
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer
# in this position and unchanged.
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR(S) ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR(S) BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

""" Main Tonic view. """

try:
    import wx
except ImportError:
    raise ImportError,"The wxPython module is required to run this program"

import widgets

class TonicView(wx.Frame):
    """ HMI for Tonic """
    def __init__(self, parent, title):
        """ Constructor. """
        wx.Frame.__init__(self, parent, title=title,
                              pos=(-1, -1), size=(800,600))
        # Creating the categories list
        self.list_category = widgets.TonicCatListCtrl(self, 
                                              style=wx.LC_REPORT|
                                                    wx.LC_NO_HEADER|
                                                    wx.LC_LIST|
                                                    wx.SUNKEN_BORDER)
                                        
        # Creating the searchbox
        self.search_box = wx.SearchCtrl(self, -1, "")
        
        # Creating the packages list
        self.list_pkg = widgets.TonicPkgListCtrl(self,
                                         style=wx.LC_REPORT|
                                               wx.SUNKEN_BORDER)
                                         
        # Creating suppl. informations about package panel
        self.description_tab = wx.Notebook(self, -1, style=wx.NB_BOTTOM)
        self.description_tab_desc = wx.Panel(self.description_tab, -1, 
                                             style=wx.SUNKEN_BORDER|
                                                   wx.TAB_TRAVERSAL)
        self.description_tab_dep = wx.Panel(self.description_tab, -1,
                                             style=wx.SUNKEN_BORDER|
                                                   wx.TAB_TRAVERSAL)
        self.description_tab_chg = wx.Panel(self.description_tab, -1,
                                             style=wx.SUNKEN_BORDER|
                                                   wx.TAB_TRAVERSAL)

        # Creating the statusbar
        self.CreateStatusBar()

        # Creating the menubar
        menubar = widgets.TonicMenuBar()
        self.SetMenuBar(menubar)

        # Creating the toolbar
        toolbar = widgets.TonicToolBar(self)
        self.SetToolBar(toolbar)
        toolbar.Realize()

        # Layout
        self.__set_layout_properties()
        self.__do_layout()

        # Tadam
        self.Show(True)

    def __set_layout_properties(self):
        """ Set layout properties """
        self.list_category.SetMinSize((300, 460))
        self.search_box.SetMinSize((450, 25))

    def __do_layout(self):
        """ Construct the layout """
        # main box.
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        # The second box split in 2 horizontal box.
        h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # The third box split in 3 vertical box. YODAWG.
        v_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Addings tabs
        self.description_tab.AddPage(self.description_tab_desc,
                                     "Description")
        self.description_tab.AddPage(self.description_tab_dep,
                                     "Dependencies")
        self.description_tab.AddPage(self.description_tab_chg,
                                     "Changes List")

        # Adding items
        h_sizer.Add(self.list_category, 0, wx.ALL | wx.EXPAND, 2)
        v_sizer.Add(self.search_box, 0, wx.ALL | wx.EXPAND, 2)
        v_sizer.Add(self.list_pkg, 1, wx.ALL | wx.EXPAND, 2)
        v_sizer.Add(self.description_tab, 1, wx.EXPAND, 0)
        h_sizer.Add(v_sizer, 1, wx.EXPAND, 0)
        
        # mainbox container
        main_sizer.Add(h_sizer, 1, wx.ALL | wx.EXPAND, 4)
                
        self.SetSizer(main_sizer)
        self.Layout()
        self.Centre()