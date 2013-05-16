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
import wx.lib.dialogs
import os
from wx.lib.delayedresult import startWorker

WILDCARD = ["Tonic files (*.tonic)|*.tonic", "Conf files (*.conf)|*.conf", "All files (*.*)|*.*o"]
EXTS = [".tonic", ".conf"]

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
                            wildcard = "|".join(WILDCARD), \
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
                            wildcard = "|".join(WILDCARD), \
                            style = wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            path, ext = os.path.splitext(dlg.GetPath())
            if not ext in EXTS:
                if dlg.GetFilterIndex() != 2:
                    path += ext + EXTS[dlg.GetFilterIndex()]
            print path
            self.model.export(path)
            dlg.Destroy()

    def on_about(self, event):
        """Blabla some stuff about tonic."""

        dlg_about = wx.AboutDialogInfo()

        description = """Pkgin aims to provide a GUI for pkgin."""

        license = """
        Copyright (c) 2013 Guillaume Delpierre <gde@llew.me>
        Copyright (c) 2013 Sylvain Mora <sylvain.mora@solevis.net>
        All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
    1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer
    in this position and unchanged.
    2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR(S) ``AS IS'' AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED.
IN NO EVENT SHALL THE AUTHOR(S) BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
OF THE POSSIBILITY OF SUCH DAMAGE. """

        dev = """Sylvain Mora \nGuillaume Delpierre"""

        # Set dialog window properties.
        dlg_about.SetName('Pkgin')
        dlg_about.SetVersion('0.1')
        dlg_about.SetDescription(description)
        dlg_about.SetWebSite('http://tonic.pkgin.net')
        dlg_about.SetLicence(license)
        dlg_about.AddDeveloper(dev)
        dlg_about.AddDocWriter(dev)
        dlg_about.AddTranslator(dev)

        wx.AboutBox(dlg_about)

    def on_exit(self, event):
        """Action on exit."""
        self.view.Close(True)

    def on_unmark_all(self, event):
        """Unmark all packages."""
        self.model.unmark_all()
        self.view.list_pkg.refresh([], [])

    def on_update(self, event):
        """Update packages list."""
        dialog = wx.ProgressDialog("Update", \
                                   "Updating...", \
                                   100, \
                                   self.view, \
                                   wx.PD_ELAPSED_TIME)
        thread = startWorker(self.__after_update, self.__update)
        while(thread.is_alive()):
            dialog.Pulse()
            wx.Yield()
            wx.Sleep(0.1)

        dialog.Destroy()

    def __update(self):
        """Get build conf from pykgin."""
        self.model.update()

    def __after_update(self, result):
        """Update build conf."""
        self.view.list_pkg.refresh(self.model.get_all_marked_pkgs(), self.model.remove_pkgs)

    def on_upgrade(self, event):
        """Upgrade packages."""
        """pkgs_full = self.model.get_upgrade_pkgs()["packages_installed"]
        pkgs = [pkg["name"] for pkg in pkgs_full]
        dlg = wx.lib.dialogs.MultipleChoiceDialog(self.view, _("upgrade_dialog_title"), \
                _("upgrade_dialog_caption"), \
                pkgs
        )
        if dlg.ShowModal() == wx.ID_OK:
            print dlg.GetValue()
            print dlg.GetValueString()
            #for pkg in pkgs:
                #    self.model.mark_pkg(pkg)
                #self.view.list_pkg.refresh(self.model.get_all_marked_pkgs(), self.model.remove_pkgs)"""

