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

"""Events handler for TonicMenuBar."""

import wx
import os

WILDCARD = "Tonic files (*.tonic)|*.tonic |"\
           "Conf files (*.conf)|*.conf |"\
           "All files (*.*)|*.*"

class TonicMenuBarEvents(object):
    """Provide callbacks for TonicMenuBar."""
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.current_directory = os.getcwd()

    def on_import_file(self, event):
        """Open File dialog."""
        dlg = wx.FileDialog(self.view, \
                            message = "Choose a file", \
                            defaultDir = self.current_directory, \
                            defaultFile = "", \
                            wildcard = WILDCARD, \
                            style = wx.FD_OPEN\
                            |wx.FD_MULTIPLE\
                            |wx.FD_CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            print "You chose the following file(s):"
            for path in paths:
                print path
        dlg.Destroy()

    def on_export_file(self, event):
        """Save file dialog."""
        dlg = wx.FileDialog(self.view, \
                           message = "Save file as ...", \
                           defaultDir = self.current_directory, \
                           defaultFile = "", \
                           wildcard = WILDCARD, \
                           style = wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
           path = dlg.GetPath()
           print "You chose the following filename: %s" % path
        dlg.Destroy()

    def on_about(self, event):
        """Blabla some stuff about tonic."""
        dial_about = wx.MessageDialog(self.view, _("tonic_about_msg"), \
                                      "About", wx.OK)
        dial_about.ShowModal()
        dial_about.Destroy()

    def on_exit(self, event):
        """Action on exit."""
        self.view.Close(True)
