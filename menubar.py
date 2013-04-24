#!/usr/bin/env python

""" Menubar view for Tonic. """

import wx

class TonicMenuBar(wx.MenuBar):
    """ Tonic menubar. """
    def __init__(self):
        """ Constructor. """
        wx.MenuBar.__init__(self)
        
        self.file_menu = None
        self.open_menu = None
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
        """ Create all menus. """
        # File menu
        self.file_menu = wx.Menu()
        self.open_menu = self.file_menu.Append(wx.ID_OPEN, "&Open",
                                       " Open a file to edit")
        self.exit_menu = self.file_menu.Append(wx.ID_EXIT,
                                   "E&xit"," Terminate the program")

        # Edit menu
        self.edit_menu = wx.Menu()
        self.unmark_all_menu = self.edit_menu.Append(wx.ID_UNDO, \
                                                        "&Unmark All", "")
        self.edit_menu.AppendSeparator()
        self.update_menu = self.edit_menu.Append(wx.ID_REFRESH, "&Update", "")
        self.edit_menu.AppendSeparator()
        self.apply_menu = self.edit_menu.Append(wx.ID_APPLY, "&Apply", "")

        # Settings menu
        self.settings_menu = wx.Menu()
        self.repository_menu = self.settings_menu.Append(wx.NewId(), \
                                                            "&Repository", "")

        # Help menu
        self.help_menu = wx.Menu()
        self.about_menu = self.help_menu.Append(wx.ID_ABOUT,
                                   "&About"," Information about this program")

    def __fill_menubar(self):
        """ Place menus in menubar. """
        self.Append(self.file_menu, "&File")
        self.Append(self.edit_menu, "&Edit")
        self.Append(self.settings_menu, "&Settings")
        self.Append(self.help_menu, "&Help")

