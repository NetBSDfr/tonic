#!/usr/bin/env python

""" View for Tonic categories list. """

import wx
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin

class TonicCatListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin):
    """ Tonic categories list. """
    def __init__(self, parent, style):
        """ Constructor. """
        wx.ListCtrl.__init__(self, parent, style = style)
        ListCtrlAutoWidthMixin.__init__(self)
        self.__add_columns()


    def __add_columns(self):
        """ Create columns. """
        self.InsertColumn(0, "Categories", width=150)
