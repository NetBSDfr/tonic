#!/usr/pkg/bin/python2.7

"""
Simple GUI for pkgin
"""

import pygtk
pygtk.require('2.0')
import gtk, gobject

class View(gtk.Window):
    """HMI for Tonic"""

    def __init__(self):
        """Default constructor"""
        super(View, self).__init__()

        # configure the windows
        self.connect("destroy", gtk.main_quit)
        self.set_size_request(600, 400)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_title("Tonic - pkgin GUI")

        # create and pack widgets
        self.__init()

    def mainloop(self):
        # Show the UI
        self.show_all()
        # Main loop
        gtk.main()

    def __init(self):
        """Create and place widgets"""

        # create the main container
        self.main_vbox = gtk.VBox(False, 1)
        self.add(self.main_vbox)

        # menubar
        self.__create_menu_bar()
        self.main_vbox.pack_start(self.menubar, False, True, 0)

    def __create_menu_bar(self):

        # keyboard shortcuts
        shortcuts = gtk.AccelGroup()

        # create an item factory
        item_factory = gtk.ItemFactory(gtk.MenuBar, "<main>", shortcuts)

        # create each items
        entries = (
            ( "/_File",         None,         None, 0, "<Branch>" ),
            ( "/File/_Export",     "<control>E", None, 0, None ),
            ( "/File/_Import",    "<control>I", None, 0, None ),
            ( "/File/sep1",     None,         None, 0, "<Separator>" ),
            ( "/File/Quit",     "<control>Q", gtk.main_quit, 0, None ),
            ( "/_Edit",         None,         None, 0, "<Branch>" ),
            ( "/Edit/Unmark all",  None,         None, 0, None ),
            ( "/Edit/sep2",     None,         None, 0, "<Separator>" ),
            ( "/Edit/Update",  None,         None, 0, None ),
            ( "/Edit/Update",  None,         None, 0, None ),
            ( "/Edit/sep3",     None,         None, 0, "<Separator>" ),
            ( "/Edit/Apply",  None,         None, 0, None ),
            ( "/_Settings",      None,         None, 0, "<Branch>" ),
            ( "/Settings/Repository",  None,         None, 0, None ),
            ( "/_Help",         None,         None, 0, "<Branch>" ),
            ( "/_Help/About",   None,         None, 0, None ),
            )
        item_factory.create_items(entries)

        # retrieve the menubar widget
        self.menubar = item_factory.get_widget("<main>")


