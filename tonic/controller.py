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

import wx
import handlers
from view import TonicView
from model import TonicModel

class TonicController(object):
    """Tonic controller."""
    def __init__(self, app):
        """Constructor."""
        self.model = TonicModel()
        self.view = TonicView(None, _("tonic_title"))

        ### Set events

        # Toolbar
        toolbar_evt = handlers.TonicToolBarEvents(self.view, self.model)
        self.view.Bind(wx.EVT_MENU, toolbar_evt.on_unmark_all, \
                       self.view.GetToolBar().unmark_tool)
        self.view.Bind(wx.EVT_MENU, toolbar_evt.on_apply, \
                       self.view.GetToolBar().apply_tool)
        # Menubar
        menubar_evt = handlers.TonicMenuBarEvents(self.view, self.model)
        self.view.Bind(wx.EVT_MENU, menubar_evt.on_about, \
                       self.view.GetMenuBar().about_menu)
        self.view.Bind(wx.EVT_MENU, menubar_evt.on_exit, \
                       self.view.GetMenuBar().exit_menu)
        self.view.Bind(wx.EVT_MENU, menubar_evt.on_import_file, \
                       self.view.GetMenuBar().import_menu)
        self.view.Bind(wx.EVT_MENU, menubar_evt.on_export_file, \
                       self.view.GetMenuBar().export_menu)
        self.view.Bind(wx.EVT_MENU, toolbar_evt.on_unmark_all, \
                       self.view.GetMenuBar().unmark_all_menu)
        self.view.Bind(wx.EVT_MENU, menubar_evt.on_update, \
                       self.view.GetMenuBar().update_menu)
        self.view.Bind(wx.EVT_MENU, menubar_evt.on_upgrade, \
                       self.view.GetMenuBar().upgrade_menu)

        # Category list
        cat_list_evt =  handlers.TonicCatListCtrlEvents(self.view, self.model)
        self.view.Bind(wx.EVT_LIST_ITEM_SELECTED, cat_list_evt.on_item_selected, \
                       self.view.list_category)
        # TODO: Create custom event => EVT_WIDGET_CREATED
        cat_list_evt.on_create()

        # Packages list
        pkg_list_evt =  handlers.TonicPkgListCtrlEvents(self.view, self.model)
        self.view.list_pkg.OnCheckItem = pkg_list_evt.on_check_item
        self.view.Bind(wx.EVT_LIST_ITEM_SELECTED, pkg_list_evt.on_item_selected, \
                       self.view.list_pkg)

        # Notebook
        notebook_evt = handlers.TonicNotebookEvents(self.view, self.model)
        self.view.Bind(wx.EVT_BUTTON, notebook_evt.on_long_desc_click, \
                       self.view.notebook.button_desc)
        self.view.Bind(wx.EVT_BUTTON, notebook_evt.on_content_click, \
                       self.view.notebook.button_cont)
        self.view.Bind(wx.EVT_BUTTON, notebook_evt.on_bconf_click, \
                       self.view.notebook.button_bconf)
