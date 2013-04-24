#!/usr/bin/env python

""" Model for Tonic. """

from pykgin import Pykgin

class Model(object):
    """ Model to manage packages. """
    def __init__(self):
        """ Constructor. """
        self.pykgin = Pykgin()
        self.packages = None

    def update(self):
        """ Update pkgin. """
        self.pykgin.update()

    def refresh(self):
        """ Retrieve all packages in one list. """
        # all packages
        avail = self.pykgin.avail()
        # packages sorted by categories
        self.packages = self.pykgin.avail_categories()
        # fusion
        for cat in self.packages:
            for pkg in self.packages[cat]:
                pkg_full = (item for item in avail \
                                if item["name"] == pkg["name"]).next()
                pkg["desc"] = pkg_full["description"]

    def get_categories(self):
        """ Return only categories name. """
        return self.packages.keys()

    def get_pkgs_from_cat(self, cat):
        """ Return packages from one category. """
        return self.packages[cat]

    def get_all_pkgs(self):
        """ Return a list of all packages. """
        result = []
        for key in self.packages.keys():
            for pkg in self.packages[key]:
                result.append(pkg)

        return result
