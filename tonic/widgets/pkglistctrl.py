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

"""View for Tonic packages list."""

import wx

from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin, ColumnSorterMixin

class TonicPkgListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin, ColumnSorterMixin):
    """Tonic packages list."""
    def __init__(self, parent, style):
        """Constructor."""
        wx.ListCtrl.__init__(self, parent, style=style)
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)
        ColumnSorterMixin.__init__(self, 3)

        self.__add_columns()
        self.itemDataMap = {}

    def __add_columns(self):
        """Create columns."""
        self.InsertColumn(0, _("package"), width=150)
        self.InsertColumn(1, _("version"), width=70)
        # small description
        self.InsertColumn(2, _("description"), width=200)

    def GetListCtrl(self):
        return self

    def populate_list(self, pkgs, marked):
        """Populate the package list."""
        # safety clear the list
        self.DeleteAllItems()
        index = 0
        for pkg in pkgs:
            # insert a new row
            pos = self.InsertStringItem(0, pkg["name"])
            if pkg["name"] in marked:
                self.CheckItem(pos, True)
            self.SetStringItem(pos, 1, pkg["version"])
            self.SetStringItem(pos, 2, pkg["description"])
            self.SetItemData(pos, index)
            # store content for future storing
            self.itemDataMap[index] = (pkg["name"], pkg["version"], pkg["description"])
            index += 1

    def get_package_name(self, index):
        return self.GetItem(index, 0).GetText()
