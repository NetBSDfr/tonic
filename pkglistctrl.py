#!/usr/bin/env python

import wx
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin

class TonicPkgListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    """ Tonic menubar. """
    def __init__(self, parent, style):
        """ Constructor. """
        wx.ListCtrl.__init__(self, parent,
                             style = wx.LC_REPORT | wx.SUNKEN_BORDER)
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)
        self.__add_columns()


    def __add_columns(self):
        """ Create columns. """
        self.InsertColumn(0, "Package", width=150)
        self.InsertColumn(1, "Version", width=70)
        # small description
        self.InsertColumn(2, "Description", width=200)
        self.InsertColumn(3, "State", width=50)

