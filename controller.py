#!/usr/bin/env python

import wx
from view import View
from model import Model

class Controller(object):
    """ Tonic controller. """
    def __init__(self, app):
        """ Constructor. """
        self.model = Model()

        self.view = View(None, "Tonic")

        # Set events
        self.view.Bind(wx.EVT_MENU, self.OnAbout,
                       self.view.GetMenuBar().menuAbout)
        self.view.Bind(wx.EVT_MENU, self.OnExit,
                       self.view.GetMenuBar().menuExit)

        # retrieve packages
        self.model.refresh()
        self.__populate_list_pkg()

    def OnAbout(self, event):
        """ blabla some stuff about tonic """
        # Just a close button
        dialAbout = wx.MessageDialog(self, "Tonic rulez the world",
                                     "About", wx.OK)
        dialAbout.ShowModal()
        dialAbout.Destroy()

    def OnExit(self, event):
        """ action on exit """
        self.view.Close(True)

    def __populate_list_pkg(self):
        """ Populate the package list. """
        pkgs = self.model.get_all_pkgs()
        for pkg in pkgs:
            pos = self.view.list_pkg.InsertStringItem(0, pkg["name"])
            self.view.list_pkg.SetStringItem(pos, 1, pkg["version"])
            self.view.list_pkg.SetStringItem(pos, 2, pkg["desc"])
