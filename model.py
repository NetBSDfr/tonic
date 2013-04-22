#!/usr/bin/env python

from pykgin import Pykgin

class Model(object):
    def __init__(self):
        self.pykgin = Pykgin()
        self.packages = None

    def update(self):
        self.pykgin.update()

    def refresh(self):
        # all packages
        avail = self.pykgin.avail()
        # packages sorted by categories
        self.packages = self.pykgin.avail_categories()
        # fusion
        for cat in self.packages:
            for pkg in self.packages[cat]:
                pkg_full = (item for item in avail if item["name"] == pkg["name"]).next()
                pkg["desc"] = pkg_full["description"]

    def get_categories(self):
        return self.packages.keys()

    def get_pkgs_from_cat(self, cat):
        return self.packages[cat]

    def get_all_pkgs(self):
        result = []
        for key in self.packages.keys():
            for pkg in self.packages[key]:
                result.append(pkg)

        return result
