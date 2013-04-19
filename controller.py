#!/usr/bin/env python

import wx
from view import View

class Controller(object):
    """ Tonic controller. """
    def __init__(self, app):
        """ Constructor. """
        self.model = None

        self.view = View(None, "Tonic")

        # Set events
        self.view.Bind(wx.EVT_MENU, self.OnAbout, self.view.GetMenuBar().menuAbout)
        self.view.Bind(wx.EVT_MENU, self.OnExit, self.view.GetMenuBar().menuExit)

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

