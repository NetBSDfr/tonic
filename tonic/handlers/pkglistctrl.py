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

import wx

class TonicPkgListCtrlEvents(object):
    """Provide callbacks for TonicPkgListCtrl."""
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def on_item_selected(self, event):
        pkg = event.GetText()
        pkg_desc = self.view.list_pkg.GetItem(event.GetIndex(), 2).GetText()
        pkg_deps = self.model.get_deps_raw(pkg)

        self.view.notebook.text_tab_desc.SetValue(pkg_desc)
        self.view.notebook.text_tab_dep.SetValue(pkg_deps)
        # reset values
        self.view.notebook.text_tab_cont.SetValue("")
        self.view.notebook.text_tab_bconf.SetValue("")
        self.view.notebook.desc_progressbar.SetValue(0)
        self.view.notebook.cont_progressbar.SetValue(0)
        self.view.notebook.bconf_progressbar.SetValue(0)

    def on_check_item(self, index, flag):
        pkg = self.view.list_pkg.get_package_name(index)
        # Checked
        if flag:
            if pkg in self.model.installed_pkgs:
                self.view.list_pkg.SetItemBackgroundColour(index, "white")
                self.model.unremove_pkg(pkg)
            elif not pkg in self.model.get_all_marked_pkgs():
                deps = list(set(self.model.get_deps_name(pkg)) - set(self.model.marked_pkgs.keys()))
                print deps
                if deps and not pkg in self.model.marked_pkgs.keys():
                    dlg = wx.SingleChoiceDialog(self.view, _("deps_dialog_title"), \
                                                    _("deps_add_dialog_caption"), \
                                                    deps, \
                                                    wx.CHOICEDLG_STYLE
                                                )
                    if dlg.ShowModal() == wx.ID_OK:
                        self.model.mark_pkgs(pkg, deps)
                        self.view.list_pkg.refresh(self.model.get_all_marked_pkgs(), self.model.remove_pkgs)
                    else:
                        self.view.list_pkg.CheckItem(index, False)
                    dlg.Destroy()
                else:
                    self.view.list_pkg.SetItemBackgroundColour(index, "green")
                    self.model.mark_pkg(pkg)
            else:
                self.view.list_pkg.SetItemBackgroundColour(index, "green")
        # Unchecked
        else:
            # Package already installed on the system
            if pkg in self.model.installed_pkgs:
                self.view.list_pkg.SetItemBackgroundColour(index, "red")
                self.model.remove_pkg(pkg)
            # Main package check
            elif pkg in self.model.marked_pkgs.keys():
                deps = self.model.marked_pkgs[pkg]

                # Uncheck all dependencies
                if len(deps) != 0:
                    dlg = wx.SingleChoiceDialog(self.view, _("deps_dialog_title"), \
                                                    _("deps_remove_dialog_caption"), \
                                                    deps, \
                                                    wx.CHOICEDLG_STYLE
                                                )
                    if dlg.ShowModal() == wx.ID_OK:
                        self.model.unmark_pkg(pkg)
                        self.view.list_pkg.refresh(self.model.get_all_marked_pkgs(), self.model.remove_pkgs)
                    else:
                        self.view.list_pkg.CheckItem(index, True)
                    dlg.Destroy()
                else:
                    self.model.unmark_pkg(pkg)
                    self.view.list_pkg.SetItemBackgroundColour(index, "white")
            # Dependency of another package checked
            else:
                main_pkg = self.model.search_in_deps(pkg)
                deps = self.model.marked_pkgs[main_pkg]
                deps.append(main_pkg)
                deps.remove(pkg)

                # Uncheck all dependencies
                dlg = wx.SingleChoiceDialog(self.view, _("deps_dialog_title"), \
                                                _("deps_remove_dialog_caption"), \
                                                deps, \
                                                wx.CHOICEDLG_STYLE
                                            )
                if dlg.ShowModal() == wx.ID_OK:
                    self.model.unmark_pkg(main_pkg)
                    self.view.list_pkg.refresh(self.model.get_all_marked_pkgs(), self.model.remove_pkgs)
                else:
                    self.view.list_pkg.CheckItem(index, True)
                dlg.Destroy()

