#!/usr/bin/env python

import wx

class TonicPkgListCtrl(wx.ListCtrl):
    """ Tonic menubar. """
    def __init__(self, parent, style):
        """ Constructor. """
        wx.ListCtrl.__init__(self, parent, style=style)

        self.__add_columns()


    def __add_columns(self):
        """ Create columns. """
        self.InsertColumn(0, "Package", width=150)
        self.InsertColumn(1, "Version", width=25)
        self.InsertColumn(2, "Description", width=200)
        self.InsertColumn(3, "State", width=50)

