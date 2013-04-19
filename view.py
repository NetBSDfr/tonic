#!/usr/bin/env python

import time
import wx

def timenow():
    """ """
    return time.time()

class View(wx.Frame):
    """ HMI for Tonic """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title,
                              pos=(-1, -1), size=(600,400))

        # Creating the statusbar in the bottom of the window
        self.CreateStatusBar()
        t0 = timenow()
        self.SetStatusText("Initialized in %6.4f secs" % (timenow()-t0))

        # Setting up the menu.
        # File menu
        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open",
                                       " Open a file to edit")
        self.menuExit = filemenu.Append(wx.ID_EXIT,
                                   "E&xit"," Terminate the program")

        # Edit menu
        editmenu = wx.Menu()
        menuUnmarkAll = editmenu.Append(wx.ID_UNDO, "&Unmark All", "")
        editmenu.AppendSeparator()
        menuUpdate = editmenu.Append(wx.ID_REFRESH, "&Update", "")
        editmenu.AppendSeparator()
        menuApply = editmenu.Append(wx.ID_APPLY, "&Apply", "")

        # Settings menu
        settingsmenu = wx.Menu()
        menuRepository = settingsmenu.Append(wx.NewId(), "&Repository", "")

        # Help menu
        helpmenu = wx.Menu()
        self.menuAbout= helpmenu.Append(wx.ID_ABOUT,
                                   "&About"," Information about this program")

        # Creating the menubar.
        # Adding the "filemenu" to the MenuBar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File")
        menuBar.Append(editmenu,"&Edit")
        menuBar.Append(settingsmenu,"&Settings")
        menuBar.Append(helpmenu,"&Help")
        # Adding the MenuBar to the Frame content.
        self.SetMenuBar(menuBar)

        # Toolbar
        # Create toolbar
        toolbar = self.CreateToolBar()
        # Create icons
        open_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN,
                                            wx.ART_TOOLBAR, (16,16))
        exit_ico = wx.ArtProvider.GetBitmap(wx.ART_QUIT,
                                            wx.ART_TOOLBAR, (16,16))
        undo_ico = wx.ArtProvider.GetBitmap(wx.ART_UNDO,
                                            wx.ART_TOOLBAR, (16,16))

        # setup toolbar
        opentool = toolbar.AddSimpleTool(wx.ID_OPEN, open_ico, 
                                         "Open", "")
        exittool = toolbar.AddSimpleTool(wx.ID_EXIT, exit_ico, 
                                         "Exit", "")
        
        toolbar.AddSeparator()
        undotool = toolbar.AddSimpleTool(wx.ID_UNDO, undo_ico,
                                         "Unmark All", "")
        # show the toolbar to the frame 
        toolbar.Realize()


        # Split the windows
        splitter = wx.SplitterWindow(self, style = wx.SP_BORDER)
        leftPanel = wx.Panel(splitter)
        rightPanel = wx.Panel(splitter)

        localTree = wx.TreeCtrl(leftPanel)
        leftSizer = wx.BoxSizer(wx.VERTICAL)
        leftSizer.Add(localTree, 1, wx.EXPAND | wx.ALL)
        leftPanel.SetSizer(leftSizer)

        flickrTree  = wx.TreeCtrl(rightPanel)
        rightSizer = wx.BoxSizer(wx.VERTICAL)
        rightSizer.Add(flickrTree, 1, wx.EXPAND | wx.ALL)
        rightPanel.SetSizer(rightSizer)

        splitter.SplitVertically(leftPanel, rightPanel)      
 
        # Tadam 
        self.Refresh()
        self.Show(True)
