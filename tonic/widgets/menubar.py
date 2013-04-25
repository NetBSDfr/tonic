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

"""Menubar view for Tonic."""

import wx

class TonicMenuBar(wx.MenuBar):
    """Tonic menubar."""
    def __init__(self):
        """Constructor."""
        wx.MenuBar.__init__(self)

        self.file_menu = None
        self.import_menu = None
        self.export_menu = None
        self.exit_menu = None
        self.edit_menu = None
        self.unmark_all_menu = None
        self.update_menu = None
        self.apply_menu = None
        self.settings_menu = None
        self.repository_menu = None
        self.help_menu = None
        self.about_menu = None

        self.__create_menus()
        self.__fill_menubar()

    def __create_menus(self):
        """Create all menus."""
        # File menu
        self.file_menu = wx.Menu()
        self.import_menu = self.file_menu.Append(wx.ID_OPEN, \
                                                 _("import_menu"), \
                                                 _("import_menu_tooltip"))
        self.export_menu = self.file_menu.Append(wx.ID_SAVE, \
                                                 _("export_menu"), \
                                                 _("export_menu_tooltip"))
        self.file_menu.AppendSeparator()
        self.exit_menu = self.file_menu.Append(wx.ID_EXIT, \
                                               _("exit_menu"),\
                                               _("exit_menu_tooltip"))

        # Edit menu
        self.edit_menu = wx.Menu()
        self.undo_menu = self.edit_menu.Append(wx.ID_UNDO, \
                                                     _("undo_menu"), \
                                                     _("undo_menu_tooltip"))
        self.redo_menu = self.edit_menu.Append(wx.ID_REDO, \
                                                     _("redo_menu"), \
                                                     _("redo_menu_tooltip"))
        self.unmark_all_menu = self.edit_menu.Append(wx.ID_ANY, \
                                                     _("unmark_all_menu"), \
                                                     _("unmark_all_menu_tooltip"))
        self.edit_menu.AppendSeparator()
        self.update_menu = self.edit_menu.Append(wx.ID_REFRESH, \
                                                 _("update_menu"), \
                                                 _("update_menu_tooltip"))
        self.upgrade_menu = self.edit_menu.Append(wx.ID_ANY, \
                                                  _("upgrade_menu"), \
                                                  _("upgrade_menu_tooltip"))
        self.edit_menu.AppendSeparator()
        self.apply_menu = self.edit_menu.Append(wx.ID_APPLY, \
                                                _("apply_menu"), \
                                                _("apply_menu_tooltip"))

        # Settings menu
        self.settings_menu = wx.Menu()
        self.pref_menu = self.settings_menu.Append(wx.ID_ANY,\
                                                   _("pref_menu"),\
                                                   _("pref_menu_tooltip"))
        self.repo_menu = self.settings_menu.Append(wx.ID_ANY, \
                                                   _("repo_menu"), \
                                                   _("repo_menu_tooltip"))

        # Help menu
        self.help_menu = wx.Menu()
        self.about_menu = self.help_menu.Append(wx.ID_ABOUT,\
                                                _("about_menu"), \
                                                _("about_menu_tooltip"))

    def __fill_menubar(self):
        """Place menus in menubar."""
        self.Append(self.file_menu, _("file_menu"))
        self.Append(self.edit_menu, _("edit_menu"))
        self.Append(self.settings_menu, _("settings_menu"))
        self.Append(self.help_menu, _("help_menu"))

