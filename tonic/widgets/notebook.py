#!/usr/bin/env python
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

"""View for Tonic bottom notebook."""

import wx

class TonicNotebook(wx.Notebook):
    """Tonic packages list."""
    def __init__(self, parent, id, style):
        """Constructor."""
        wx.Notebook.__init__(self, parent, id=id, style=style)

        self.__create_widgets()
        self.__set_properties()
        self.__do_layout()


    def __do_layout(self):
        """Place each widgets."""
        # notebook tab sizer.
        desc_tab_sizer = wx.BoxSizer(wx.VERTICAL)
        desc_ctrl_sizer = wx.BoxSizer(wx.HORIZONTAL)
        dep_sizer = wx.BoxSizer(wx.HORIZONTAL)
        cont_tab_sizer = wx.BoxSizer(wx.VERTICAL)
        cont_ctrl_sizer = wx.BoxSizer(wx.HORIZONTAL)
        bconf_tab_sizer = wx.BoxSizer(wx.VERTICAL)
        bconf_ctrl_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Addings tabs.
        self.AddPage(self.desc_panel, _("Description"))
        self.AddPage(self.dep_panel, _("Dependencies"))
        self.AddPage(self.cont_panel, _("Content"))
        self.AddPage(self.bconf_panel, _("Build Config"))

        # sizers
        desc_ctrl_sizer.Add(self.desc_progressbar, 1,\
                            wx.ALL | wx.ALIGN_CENTER_HORIZONTAL |\
                            wx.ALIGN_CENTER_VERTICAL, 2)
        desc_ctrl_sizer.Add(self.button_desc, 0,\
                            wx.ALL | wx.ALIGN_RIGHT |\
                            wx.ALIGN_CENTER_HORIZONTAL |\
                            wx.ALIGN_CENTER_VERTICAL, 2)
        desc_tab_sizer.Add(desc_ctrl_sizer, 1, wx.EXPAND, 0)
        desc_tab_sizer.Add(self.text_tab_desc, 6, wx.EXPAND, 0)
        dep_sizer.Add(self.text_tab_dep, 1, wx.EXPAND, 0)
        cont_ctrl_sizer.Add(self.cont_progressbar, 1,\
                            wx.ALL | wx.ALIGN_CENTER_HORIZONTAL |\
                            wx.ALIGN_CENTER_VERTICAL, 2)
        cont_ctrl_sizer.Add(self.button_cont, 0,\
                            wx.ALL | wx.ALIGN_RIGHT |\
                            wx.ALIGN_CENTER_HORIZONTAL |\
                            wx.ALIGN_CENTER_VERTICAL, 2)
        cont_tab_sizer.Add(cont_ctrl_sizer, 1, wx.EXPAND, 0)
        cont_tab_sizer.Add(self.text_tab_cont, 6, wx.EXPAND, 0)
        bconf_ctrl_sizer.Add(self.bconf_progressbar, 1,\
                             wx.ALL | wx.ALIGN_CENTER_HORIZONTAL |\
                             wx.ALIGN_CENTER_VERTICAL, 2)
        bconf_ctrl_sizer.Add(self.button_bconf, 0,\
                             wx.ALL | wx.ALIGN_RIGHT |\
                             wx.ALIGN_CENTER_HORIZONTAL |\
                             wx.ALIGN_CENTER_VERTICAL, 2)
        bconf_tab_sizer.Add(bconf_ctrl_sizer, 1, wx.EXPAND, 0)
        bconf_tab_sizer.Add(self.text_tab_bconf, 6, wx.EXPAND, 0)

        self.desc_panel.SetSizer(desc_tab_sizer)
        self.dep_panel.SetSizer(dep_sizer)
        self.cont_panel.SetSizer(cont_tab_sizer)
        self.bconf_panel.SetSizer(bconf_tab_sizer)

    def __set_properties(self):
        """Set properties for each widgets."""
        # notebook panel size (inside tab panel).
        self.SetMinSize((594, 295))
        # notebook tab panel size.
        self.desc_panel.SetMinSize((590, 265))
        self.dep_panel.SetMinSize((590, 265))
        self.cont_panel.SetMinSize((590, 265))
        self.bconf_panel.SetMinSize((590, 265))
        # progressbar size (inside notebook tab panel).
        self.desc_progressbar.SetMinSize((395, 25))
        self.cont_progressbar.SetMinSize((395, 25))
        self.bconf_progressbar.SetMinSize((395, 25))
        # button size (inside notebook tab panel).
        self.button_desc.SetMinSize((145, 30))
        self.button_cont.SetMinSize((145, 30))
        self.button_bconf.SetMinSize((145, 30))

    def __create_widgets(self):
        """Create all notebook's widgets."""
         # Creating suppl. informations about package panel.
        self.desc_panel = wx.Panel(self, wx.ID_ANY)
        self.dep_panel = wx.Panel(self, wx.ID_ANY)
        self.cont_panel = wx.Panel(self, wx.ID_ANY)
        self.bconf_panel = wx.Panel(self, wx.ID_ANY)

        # Creating text area.
        self.text_tab_desc = wx.TextCtrl(self.desc_panel,\
                                     wx.ID_ANY, "",\
                                     style=wx.TE_MULTILINE|\
                                     wx.HSCROLL|wx.TE_READONLY|\
                                     wx.NO_BORDER)
        self.text_tab_dep = wx.TextCtrl(self.dep_panel,\
                                    wx.ID_ANY, "",\
                                    style=wx.TE_MULTILINE|\
                                    wx.HSCROLL|wx.TE_READONLY|\
                                    wx.NO_BORDER)
        self.text_tab_cont = wx.TextCtrl(self.cont_panel,\
                                     wx.ID_ANY, "",\
                                     style=wx.TE_MULTILINE|\
                                     wx.HSCROLL|wx.TE_READONLY|\
                                     wx.NO_BORDER)
        self.text_tab_bconf = wx.TextCtrl(self.bconf_panel,\
                                      wx.ID_ANY, "",\
                                      style=wx.TE_MULTILINE|\
                                      wx.HSCROLL|wx.TE_READONLY|\
                                      wx.NO_BORDER)

        # Creating desc/content/bconf progressbar.
        self.desc_progressbar = wx.Gauge(self.desc_panel,\
                                         wx.ID_ANY, 10,\
                                         style=wx.GA_HORIZONTAL|\
                                         wx.GA_SMOOTH)
        self.cont_progressbar = wx.Gauge(self.cont_panel,\
                                         wx.ID_ANY, 10,\
                                         style=wx.GA_HORIZONTAL|\
                                         wx.GA_SMOOTH)
        self.bconf_progressbar = wx.Gauge(self.bconf_panel,\
                                          wx.ID_ANY, 10,\
                                          style=wx.GA_HORIZONTAL|\
                                          wx.GA_SMOOTH)

        # Creating desc/content/bconf button.
        self.button_desc = wx.Button(self.desc_panel, wx.ID_ANY,\
                                     _("Show full description"))
        self.button_cont = wx.Button(self.cont_panel, wx.ID_ANY,\
                                     _("Show content"))
        self.button_bconf = wx.Button(self.bconf_panel, wx.ID_ANY,\
                                      _("Show build config"))

