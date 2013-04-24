#!/usr/bin/env python

""" View for Tonic packages list. """

import wx
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin

class TonicPkgListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    """ Tonic packages list. """
    def __init__(self, parent, style):
        """ Constructor. """
        wx.ListCtrl.__init__(self, parent, style = style)
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)
        self.__add_columns()


    def __add_columns(self):
        """ Create columns. """
        self.InsertColumn(0, "Package", width=150)
        self.InsertColumn(1, "Version", width=70)
        # small description
        self.InsertColumn(2, "Description", width=200)
