#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk, gobject
from pykgin import Pykgin

class Tonic(gtk.Window):
    def __init__(self):
        super(Tonic, self).__init__()

        self.connect("destroy", gtk.main_quit)
        self.set_size_request(600, 400)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_title("Tonic - pkgin GUI")

        self.__create_widgets()
        self.__populate_pkg_list()

    def __create_widgets(self):
        # new container
        self.main_vbox = gtk.VBox(False, 1)
        self.add(self.main_vbox)

        # create each elements
        menubar = self.__create_menu_bar()
        toolbar = self.__create_toolbar()
        pkglist = self.__create_pkg_list()

        # place each elements
        self.main_vbox.pack_start(menubar, False, True, 0)
        self.main_vbox.pack_start(toolbar, False, True, 0)
        self.main_vbox.add(pkglist)

    def __create_menu_bar(self):

        # Keyboard shortcuts
        self.shortcuts = gtk.AccelGroup()

        # Create an item factory
        self.item_factory = gtk.ItemFactory(gtk.MenuBar, "<main>", self.shortcuts)

        # Create each items
        self.entries = (
            ( "/_File",         None,         None, 0, "<Branch>" ),
            ( "/File/_Nouveau",     "<control>N", None, 0, None ),
            ( "/File/_Ouvrir",    "<control>O", None, 0, None ),
            ( "/File/_Enregistrer",    "<control>S", None, 0, None ),
            ( "/File/Enregistrer _sous", None,         None, 0, None ),
            ( "/File/sep1",     None,         None, 0, "<Separator>" ),
            ( "/File/Quitter",     "<control>Q", gtk.main_quit, 0, None ),
            ( "/_Settings",      None,         None, 0, "<Branch>" ),
            ( "/Settings/Test",  None,         None, 0, None ),
            ( "/_Help",         None,         None, 0, "<Branch>" ),
            ( "/_Help/A propos",   None,         None, 0, None ),
            )
        self.item_factory.create_items(self.entries)

        # Add the menu bar in the window
        return self.item_factory.get_widget("<main>")

    def __create_toolbar(self):
        # Create the toolbar
        self.toolbar = gtk.Toolbar()
        self.toolbar.set_orientation(gtk.ORIENTATION_HORIZONTAL)

        # Insert elements
        apply_img = gtk.Image()
        apply_img.set_from_stock(gtk.STOCK_APPLY, gtk.ICON_SIZE_SMALL_TOOLBAR)
        self.toolbar.append_item(
            None,
            "Apply",
            None,
            apply_img,
            self.__apply)

        cancel_img = gtk.Image()
        cancel_img.set_from_stock(gtk.STOCK_CANCEL, gtk.ICON_SIZE_SMALL_TOOLBAR)
        self.toolbar.append_item(
            None,
            "Cancel",
            None,
            cancel_img,
            self.__apply)


        refresh_img = gtk.Image()
        refresh_img.set_from_stock(gtk.STOCK_REFRESH, gtk.ICON_SIZE_SMALL_TOOLBAR)
        self.toolbar.append_item(
            None,
            "Refresh",
            None,
            refresh_img,
            self.__apply)

        self.toolbar.append_space()

        rb_all = gtk.RadioButton(None, "all")
        rb_all.set_active(True)
        self.toolbar.append_widget(rb_all, "All packages", "Private")

        rb_list = gtk.RadioButton(rb_all, "installed")
        rb_list.set_active(False)
        self.toolbar.append_widget(rb_list, "Installed packages", "Private")

        # TODO : Insert blank space to set the searchbox to the end of the toolbar
        separator = gtk.SeparatorToolItem()
        separator.set_expand(True)

        self.toolbar.append_space()

        searchbox_label = gtk.Label("Search : ")
        self.toolbar.append_widget(searchbox_label,  "Search a package", "Private")

        searchbox = gtk.Entry()
        self.toolbar.append_widget(searchbox,  "Search a package", "Private")

        return self.toolbar

    def __create_pkg_list(self):
        # Create the data container
        self.liststore = gtk.TreeStore(bool, str, str, str)

        # Create the view
        self.treeview = gtk.TreeView(self.liststore)
        self.treeview.set_rules_hint(True)
        self.treeview.set_headers_clickable(False)
        self.treeview.set_enable_search(False)

        # Create the scrollbar container
        self.scrollwin = gtk.ScrolledWindow()
        self.scrollwin.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        # Add the treeview into the scrollbar container
        self.scrollwin.add(self.treeview)

        # Create selection column
        renderer_toggle = gtk.CellRendererToggle()
        renderer_toggle.connect("toggled", self.__on_cell_sel_toggled)
        self.column_toggle = gtk.TreeViewColumn(None, renderer_toggle, active=0)
        self.treeview.append_column(self.column_toggle)

        # Create pkg name column
        renderer_text = gtk.CellRendererText()
        self.column_name = gtk.TreeViewColumn("Name", renderer_text, text=1)
        self.column_name.set_resizable(True)
        self.column_name.set_min_width(50)
        self.column_name.set_sort_column_id(1)
        self.treeview.append_column(self.column_name)

        # Create pkg desc column
        self.column_desc = gtk.TreeViewColumn("Description", renderer_text, text=2)
        self.column_desc.set_resizable(True)
        self.treeview.append_column(self.column_desc)

        # Create pkg version column
        self.column_version = gtk.TreeViewColumn("Version", renderer_text, text=3)
        self.column_version.set_resizable(True)
        self.treeview.append_column(self.column_version)

        # Add the pkg list in the window
        return self.scrollwin

    def __on_cell_sel_toggled(self, widget, path):
        self.liststore[path][0] = not self.liststore[path][0]

    def __apply(self, event):
        print("Apply !")

    def __populate_pkg_list(self):
        self.pykgin = Pykgin()
        avail = self.pykgin.avail()
        avail_cat = self.pykgin.avail_categories()
        for category in avail_cat.keys():
            # create parent
            parent = self.liststore.append(None, [None, category, None, None])
            for pkg in avail_cat[category]:
                # retrieve the description
                pkg_full = (item for item in avail if item["name"] == pkg["name"]).next()
                # add the package in the list
                self.liststore.append(parent, [False, pkg_full["name"], pkg_full["description"], pkg_full["version"]])



if __name__ == "__main__":
    # Initialize the UI
    win = Tonic()
    # Show the UI
    win.show_all()
    # Main loop
    gtk.main()
