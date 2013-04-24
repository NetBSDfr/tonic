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

"""View for Tonic toolbar."""

import wx

class TonicToolBar(wx.ToolBar):
    """Tonic toolbar."""
    def __init__(self, parent):
        """Constructor."""
        wx.ToolBar.__init__(self, parent,
                            style=wx.TB_HORZ_TEXT)

        self.open_ico = None
        self.exit_ico = None
        self.undo_ico = None
        self.apply_ico = None

        self.__create_icons()
        self.__fill_toolbar()

    def __create_icons(self):
        """Create icons."""
        self.open_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN,
                                                 wx.ART_TOOLBAR, (16,16))
        self.exit_ico = wx.ArtProvider.GetBitmap(wx.ART_QUIT,
                                                 wx.ART_TOOLBAR, (16,16))
        self.undo_ico = wx.ArtProvider.GetBitmap(wx.ART_UNDO,
                                                 wx.ART_TOOLBAR, (16,16))
        self.apply_ico = wx.ArtProvider.GetBitmap(wx.ART_TICK_MARK,
                                                  wx.ART_TOOLBAR, (16,16))

    def __fill_toolbar(self):
        """Insert elements in toolbar."""
        self.AddSimpleTool(wx.ID_OPEN, self.open_ico, _("open"), "")
        self.AddSimpleTool(wx.ID_EXIT, self.exit_ico, _("exit"), "")
        self.AddSeparator()
        self.AddSimpleTool(wx.ID_UNDO, self.undo_ico, _("unmark_all"), "")
        self.AddSeparator()
        self.AddSimpleTool(wx.ID_APPLY, self.apply_ico, _("install"), "")
        self.AddSeparator()
