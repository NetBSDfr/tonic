#!/usr/bin/env python

""" Main script for Tonic. """

import wx
from controller import Controller

def main():
    """ Main function. """
    app = wx.App(False)
    tonic = Controller(app)
    app.MainLoop()

if __name__ == '__main__':
    main()
