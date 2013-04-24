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

""" Controller for Tonic. """

import wx

from view import TonicView
from model import TonicModel

class TonicController(object):
    """ Tonic controller. """
    def __init__(self, app):
        """ Constructor. """
        self.model = TonicModel()
        self.view = TonicView(None, "Tonic")

        # Set events
        self.view.Bind(wx.EVT_MENU, self.on_about,
                       self.view.GetMenuBar().about_menu)
        self.view.Bind(wx.EVT_MENU, self.on_exit,
                       self.view.GetMenuBar().exit_menu)

        # retrieve packages
        self.model.refresh()
        # populate each lists
        self.__populate_list_pkg()
        self.__populate_list_cat()

    def on_about(self, event):
        """ blabla some stuff about tonic """
        dial_about = wx.MessageDialog(self, "Tonic rulez the world",
                                     "About", wx.OK)
        dial_about.ShowModal()
        dial_about.Destroy()

    def on_exit(self, event):
        """ action on exit """
        self.view.Close(True)

    def __populate_list_pkg(self):
        """ Populate the package list. """
        pkgs = self.model.get_all_pkgs()
        for pkg in pkgs:
            pos = self.view.list_pkg.InsertStringItem(0, pkg["name"])
            self.view.list_pkg.SetStringItem(pos, 1, pkg["version"])
            self.view.list_pkg.SetStringItem(pos, 2, pkg["desc"])

    def __populate_list_cat(self):
        """ Populate the category list. """
        cats = self.model.get_categories()
        for cat in cats:
            self.view.list_category.InsertStringItem(0, cat)
        self.view.list_category.InsertStringItem(0, "--")
        self.view.list_category.InsertStringItem(0, "all")
