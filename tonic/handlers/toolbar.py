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

"""Events handler for TonicToolBar."""

import wx

class TonicToolBarEvents(object):
    """Provide callbacks for TonicToolBar."""
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def on_unmark_all(self, event):
        """Unmark all packages."""
        self.model.unmark_all()
        self.view.list_pkg.refresh(self.model.get_all_marked_pkgs(), self.model.remove_pkgs)

    def on_apply(self, event):
        """Apply changes."""
        ### Install
        progress_max = len(self.model.marked_pkgs)-len(self.model.installed_pkgs)
        if progress_max != 0:
            dialog = wx.ProgressDialog("Apply :: installing [1/2]", \
                                       "Loading...", \
                                       progress_max, \
                                       self.view, \
                                       wx.PD_ELAPSED_TIME)
            count = 0
            index = 0
            keep_going = True
            while keep_going and count < progress_max:
                    pkg = self.model.marked_pkgs.keys()[index]
                    index += 1
                    if not pkg in self.model.installed_pkgs:
                        msg = "Installing %s (%d/%d)" % (pkg, count, progress_max)
                        keep_going = dialog.Update(count, pkg)
                        self.model.install(pkg)
                        count += 1

                    if count == progress_max:
                        keep_going = dialog.Update(count, "Done.")

            self.view.list_pkg.refresh(self.model.get_all_marked_pkgs(), self.model.remove_pkgs)
            dialog.Destroy()

        ### Remove
        progress_max = len(self.model.remove_pkgs)
        if progress_max != 0:
            dialog = wx.ProgressDialog("Apply :: removing [2/2]", \
                                   "Loading...", \
                                   progress_max, \
                                   self.view, \
                                   wx.PD_ELAPSED_TIME)
        count = 0
        keep_going = True
        while keep_going and count < progress_max:
                pkg = self.model.remove_pkgs[count]
                msg = "Removing %s (%d/%d)" % (pkg, count, progress_max)
                keep_going = dialog.Update(count, pkg)
                self.model.remove(pkg)
                count += 1

                if count == progress_max:
                    keep_going = dialog.Update(count, "Done.")

        self.view.list_pkg.refresh(self.model.get_all_marked_pkgs(), self.model.remove_pkgs)
        dialog.Destroy()
