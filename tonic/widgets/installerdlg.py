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

import wx

class InstallDialog(wx.Dialog):
    """ Installer dialog. """
    def __init__(self):
        """ Constructor. """
        self.pkg_info = wx.TextCtrl(self, -1, "",\
                                    style=wx.TE_MULTILINE|\
                                          wx.TE_READONLY)
        self.install_info = wx.TextCtrl(self, -1, "",\
                                        style=wx.TE_MULTILINE|\
                                              wx.TE_READONLY|\
                                              wx.HSCROLL|\
                                              wx.TE_PROCESS_TAB)
        self.gauge = wx.Gauge(self, -1, 10,
                              style=wx.GA_VERTICAL)

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        """ Set dialog element properties. """
        self.SetTitle("_pkg_name_")
        self.SetSize((400, 450))
        self.SetFocus()
        self.pkg_info.SetMinSize((390, 50))
        self.install_info.SetMinSize((390, 350))
        self.gauge.SetMinSize((390, 10))

        # FG & BG color
        self.install_info.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.install_info.SetBackgroundColour(wx.Colour(255, 255, 255))

    def __do_layout(self):
        """ Create layout. """
        v_sizer = wx.BoxSizer(wx.VERTICAL)
        v_sizer.Add(self.pkg_info, 0, wx.ALL | wx.EXPAND, 5)
        v_sizer.Add(self.gauge, 0, wx.ALL | wx.EXPAND, 5)
        v_sizer.Add(self.install_info, 0, wx.ALL | wx.EXPAND, 5)
        
        self.SetSizer(v_sizer)
        self.Layout()
