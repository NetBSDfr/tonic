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

"""Events handler for TonicNotebook."""

import wx

class TonicNotebookEvents(object):
    """Provide callbacks for TonicNotebook."""
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def on_long_desc_click(self, event):
        """Show long desc."""
        pkg_id = self.view.list_pkg.GetFirstSelected()
        pkg = self.view.list_pkg.GetItem(pkg_id).GetText()
        pkg_desc = self.model.get_desc(pkg)
        self.view.text_tab_desc.SetValue(pkg_desc)
	#self.view.progressbar.Show()

    def on_content_click(self, event):
        """Show package content."""
        pkg_id = self.view.list_pkg.GetFirstSelected()
        pkg = self.view.list_pkg.GetItem(pkg_id).GetText()
        pkg_content = "\n".join(self.model.get_content(pkg))
        self.view.text_tab_cont.SetValue(pkg_content)

    def on_bconf_click(self, event):
        """Show build infos."""
        pkg_id = self.view.list_pkg.GetFirstSelected()
        pkg = self.view.list_pkg.GetItem(pkg_id).GetText()
        pkg_bconf = self.model.get_build_infos(pkg)
        content = ""
        for info in pkg_bconf.keys():
            content += info
            content += ' =\n'
            for value in pkg_bconf[info]:
                content += '\t'
                content += value
                content += '\n'
        self.view.text_tab_bconf.SetValue(content)

