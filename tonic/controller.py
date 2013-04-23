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

"""Controller for Tonic."""

import os

import wx

from view import TonicView
from model import TonicModel

wildcard = "Tonic files (*.tonic)|*.tonic | "\
           "Conf files (*.conf)|*.conf |"\
           "All files (*.*)|*.*"

class TonicController(object):
    """Tonic controller."""
    def __init__(self, app):
        """Constructor."""
        self.model = TonicModel()
        self.view = TonicView(None, _("tonic_title"))

        # Set events
        self.view.Bind(wx.EVT_MENU, self.on_about,
                       self.view.GetMenuBar().about_menu)
        self.view.Bind(wx.EVT_MENU, self.on_exit,
                       self.view.GetMenuBar().exit_menu)
        self.view.Bind(wx.EVT_MENU, self.on_import_file,
                       self.view.GetMenuBar().import_menu)
        self.view.Bind(wx.EVT_MENU, self.on_export_file,
                       self.view.GetMenuBar().export_menu)
        self.view.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_cat_list_click, self.view.list_category)

        # retrieve packages
        self.model.refresh()
        # populate each lists
        self.__populate_list_pkg()
        self.__populate_list_cat()

        self.current_directory = os.getcwd()

    def on_import_file(self, event):
        """ Open File dialog """
        dlg = wx.FileDialog(self.view,
                            message="Choose a file",
                            defaultDir=self.current_directory,
                            defaultFile="",
                            wildcard=wildcard,
                            style=wx.FD_OPEN |\
                            wx.FD_MULTIPLE |\
                            wx.FD_CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            print "You chose the following file(s):"
            for path in paths:
                print path
        dlg.Destroy()

    def on_export_file(self, event):
        """ Save file dialog """
        dlg = wx.FileDialog(self.view,
                           message="Save file as ...",
                           defaultDir=self.current_directory,
                           defaultFile="",
                           wildcard=wildcard,
                           style=wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
           path = dlg.GetPath()
           print "You chose the following filename: %s" % path
        dlg.Destroy()

    def on_about(self, event):
        """blabla some stuff about tonic"""
        dial_about = wx.MessageDialog(self.view, _("tonic_about_msg"),
                                      "About", wx.OK)
        dial_about.ShowModal()
        dial_about.Destroy()

    def on_exit(self, event):
        """action on exit"""
        self.view.Close(True)

    def on_cat_list_click(self, event) :
        category = event.GetText()
        if category == "--":
            pass
        elif category == "All":
            self.__populate_list_pkg()
        else:
            self.__populate_list_pkg(category)

    def __populate_list_pkg(self, cat=None):
        """Populate the package list."""
        if not cat:
            pkgs = self.model.get_packages()
        else:
            pkgs = self.model.get_pkgs_from_cat(cat)
        item_data_map = {}
        index = 0
        for cat in pkgs.values():
            for pkg in cat:
                pos = self.view.list_pkg.InsertStringItem(0, pkg["name"])
                self.view.list_pkg.SetStringItem(pos, 1, pkg["version"])
                self.view.list_pkg.SetStringItem(pos, 2, pkg["description"])
                self.view.list_pkg.SetItemData(pos, index)
                item_data_map[index] = (pkg["name"], pkg["version"], pkg["description"])
                index += 1

        self.view.list_pkg.itemDataMap = item_data_map

    def __populate_list_cat(self):
        """Populate the category list."""
        cats = sorted(self.model.get_categories(), reverse=True)
        for cat in cats:
            self.view.list_category.InsertStringItem(0, cat)
        self.view.list_category.InsertStringItem(0, "--")
        self.view.list_category.InsertStringItem(0, _("all_category_name"))
