#!/usr/bin/env python

import wx
from controller import Controller

if __name__ == '__main__':
    app = wx.App(False)
    tonic = Controller(app)
    app.MainLoop()

