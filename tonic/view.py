#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2013 Guillaume Delpierre <gde@llew.me>
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

"""Main Tonic view."""

import wx
import widgets

class TonicView(wx.Frame):
    """ HMI for Tonic. """
    def __init__(self, parent, title):
        """ Constructor. """
        wx.Frame.__init__(self, parent, title=title,\
                          pos=(-1, -1), size=(800, 600),\
                         style=wx.DEFAULT_FRAME_STYLE)

        # Creating panel.
        self.main_panel = wx.SplitterWindow(self, wx.ID_ANY,\
                                            style=wx.SP_3D | wx.SP_BORDER)
        self.left_panel = wx.Panel(self.main_panel, wx.ID_ANY)
        self.right_panel = wx.Panel(self.main_panel, wx.ID_ANY)

        self.split_panel_pkg = wx.SplitterWindow(self.right_panel,\
                                                 wx.ID_ANY,\
                                                 style=wx.SP_3D |\
                                                 wx.SP_BORDER)
        self.pkg_panel = wx.Panel(self.split_panel_pkg, wx.ID_ANY)
        self.tab_panel = wx.Panel(self.split_panel_pkg, wx.ID_ANY)
        self.notebook = widgets.TonicNotebook(self.tab_panel, wx.ID_ANY,\
                                          style=wx.NB_BOTTOM)

        # Creating category list.
        self.list_category = widgets.TonicCatListCtrl(self.left_panel,\
                                                      style=wx.LC_REPORT|\
                                                      wx.LC_NO_HEADER |\
                                                      wx.LC_LIST |\
                                                      wx.SUNKEN_BORDER|\
                                                      wx.LC_SORT_ASCENDING|\
                                                      wx.LC_SINGLE_SEL)
        # Creating packages list.
        self.list_pkg = widgets.TonicPkgListCtrl(self.pkg_panel,\
                                                 style=wx.LC_REPORT|\
                                                 wx.SUNKEN_BORDER|\
                                                 wx.LC_SORT_ASCENDING)

        # Creating searchbox.
        self.searchbox = wx.SearchCtrl(self.right_panel, wx.ID_ANY, "")

        # Creating the statusbar.
        self.statusbar = self.CreateStatusBar()

        # Creating the menubar.
        menubar = widgets.TonicMenuBar()
        self.SetMenuBar(menubar)

        # Creating the toolbar.
        toolbar = widgets.TonicToolBar(self)
        self.SetToolBar(toolbar)
        toolbar.Realize()

        # Set the layout.
        self.__set_properties()
        self.__do_layout()

        # Show the frame.
        self.Show(True)

    def __set_properties(self):
        """ Set layout properties. """
        self.SetTitle(_("Tonic"))
        # frame size.
        self.SetSize((800, 600))
        # main panel size.
        self.main_panel.SetMinSize((800, 595))
        # left and right panel size.
        self.left_panel.SetMinSize((200, 595))
        self.right_panel.SetMinSize((595, 595))
        # split panel pkg size.
        self.split_panel_pkg.SetMinSize((595, 570))
        # pkg panel size (split, inside split panel).
        self.pkg_panel.SetMinSize((595, 265))
        # tab panel size (split, inside split panel).
        self.tab_panel.SetMinSize((595, 295))
        # category list size (inside left panel).
        self.list_category.SetMinSize((195, 590))
        # searchbox size (inside right panel).
        self.searchbox.SetMinSize((590, 25))
        # pkg list size (inside right panel).
        self.list_pkg.SetMinSize((590, 265))

    def __do_layout(self):
        """ Contruct the layout. """
        # mainbox content main panel.
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        searchbox_sizer = wx.BoxSizer(wx.VERTICAL)

        # inside tab panel.
        panel_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # inside pkg panel.
        pkg_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # content category list.
        list_category_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Addings items to sizer.
        list_category_sizer.Add(self.list_category, 1,\
                           wx.ALL | wx.EXPAND, 2)
        searchbox_sizer.Add(self.searchbox, 0,\
                            wx.ALL | wx.EXPAND |\
                            wx.ALIGN_CENTER_HORIZONTAL |\
                            wx.ALIGN_CENTER_VERTICAL, 2)
        pkg_sizer.Add(self.list_pkg, 1,\
                      wx.ALL | wx.EXPAND |\
                      wx.ALIGN_CENTER_HORIZONTAL |\
                      wx.ALIGN_CENTER_VERTICAL, 2)
        panel_sizer.Add(self.notebook, 1, wx.EXPAND, 0)

        # Populate panel w/ right size.
        self.left_panel.SetSizer(list_category_sizer)
        self.pkg_panel.SetSizer(pkg_sizer)
        self.tab_panel.SetSizer(panel_sizer)

        # split pkg panel.
        self.split_panel_pkg.SplitHorizontally(self.pkg_panel,\
                                               self.tab_panel)
        searchbox_sizer.Add(self.split_panel_pkg, 1, wx.EXPAND, 0)
        self.right_panel.SetSizer(searchbox_sizer)

        # split main panel.
        self.main_panel.SplitVertically(self.left_panel,\
                                        self.right_panel)
        main_sizer.Add(self.main_panel, 1,\
                       wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL |\
                       wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetSizer(main_sizer)
        main_sizer.SetSizeHints(self)
        self.Layout()
        self.Centre()
