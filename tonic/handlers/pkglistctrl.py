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

"""Events handler for TonicPkgListCtrl."""

class TonicPkgListCtrlEvents(object):
    """Provide callbacks for TonicPkgListCtrl."""
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def on_check_item(self, index, flag):
        pkg = self.view.list_pkg.get_package_name(index)
        # Checked
        if flag:
            if pkg in self.model.installed_pkgs:
                self.view.list_pkg.SetItemBackgroundColour(index, "white")
                self.model.unremove_pkg(pkg)
            else:
                self.view.list_pkg.SetItemBackgroundColour(index, "green")
                self.model.mark_pkg(pkg)
        # Unchecked
        else:
            if pkg in self.model.installed_pkgs:
                self.view.list_pkg.SetItemBackgroundColour(index, "red")
                self.model.remove_pkg(pkg)
            elif pkg in self.model.marked_pkgs:
                self.view.list_pkg.SetItemBackgroundColour(index, "white")
                self.model.unmark_pkg(pkg)


