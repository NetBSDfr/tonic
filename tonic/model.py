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

"""Model for Tonic."""

from pykgin import Pykgin

class TonicModel(object):
    """Model to manage packages."""
    instance = None

    def __new__(cls, *args, **kargs):
        """Create instance of the class."""
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kargs)
        return cls.instance

    def __init__(self):
        """Constructor."""
        self.pykgin = Pykgin()
        self.installed_pkgs = []
        self.marked_pkgs = {}
        self.remove_pkgs = []

        self.__init_marked_pkgs()

    def __init_marked_pkgs(self):
        """Retrieve installed packages and create first marked list."""
        pkg_list = self.pykgin.list()
        for pkg in pkg_list:
            self.installed_pkgs.append(pkg["name"])
            self.marked_pkgs[pkg["name"]] = []

    def get_categories(self):
        """Return only categories name."""
        return self.pykgin.show_all_categories()

    def get_pkgs_from_cat(self, cat):
        """Return packages from one category."""
        return self.pykgin.show_category(cat)

    def get_all_pkgs(self):
        """Return a list of all packages."""
        return self.pykgin.avail()

    def mark_pkg(self, pkg):
        """Add a pkg in marked list for future install."""
        if not pkg in self.marked_pkgs.keys():
            self.marked_pkgs[pkg] = []

    def mark_pkgs(self, pkg, deps):
        """Add several pkgs in marked list."""
        self.marked_pkgs[pkg] = deps

    def unmark_pkg(self, pkg):
        """Remove a pkg in marked list for future install."""
        if pkg in self.marked_pkgs.keys():
            self.marked_pkgs.pop(pkg)

    def unmark_all(self):
        """Remove a pkg in marked list for future install."""
        self.marked_pkgs.clear()
        for pkg in self.installed_pkgs:
            self.marked_pkgs[pkg] = []
        del self.remove_pkgs[:]

    def remove_pkg(self, pkg):
        """Add a pkg in remove list for future uninstall."""
        if not pkg in self.remove_pkgs:
            self.remove_pkgs.append(pkg)

    def unremove_pkg(self, pkg):
        """Remove a pkg in remove list for future uninstall."""
        if pkg in self.remove_pkgs:
            self.remove_pkgs.remove(pkg)

    def get_deps_name(self, pkg):
        """Return a list of package's name dependencies."""
        deps = self.pykgin.show_full_deps(pkg)
        return [item["name"] for item in deps]

    def get_deps_raw(self, pkg):
        """Return a list of package dependencies."""
        deps = self.pykgin.show_full_deps_raw(pkg)
        return deps

    def get_all_marked_pkgs(self):
        """Return a single list of all marked packages."""
        result = self.marked_pkgs.keys()
        for pkg in self.marked_pkgs.values():
            result.extend(pkg)

        return result

    def search_in_deps(self, pkg):
        """Search if the pkg is a dependency. Return the main pkg"""
        for main,pkgs in self.marked_pkgs.items():
            if pkg in pkgs:
                return main

        return None

    def get_desc(self, pkg):
        """Retrieve the full-desc of the package."""
        desc = self.pykgin.pkg_descr(pkg)
        return desc

    def get_content(self, pkg):
        """Retrieve the contents of the package."""
        content = self.pykgin.pkg_content(pkg)
        return content

    def get_build_infos(self, pkg):
        """Retrieve build infos of the package."""
        infos = self.pykgin.pkg_build_defs(pkg)
        return infos

    def install(self, pkg):
        """Install a package."""
        self.pykgin.install(pkg)
        self.installed_pkgs.append(pkg)
        for dep in self.marked_pkgs[pkg]:
            self.installed_pkgs.append(dep)

    def remove(self, pkg):
        """Install a package."""
        self.pykgin.remove(pkg)
        self.installed_pkgs.remove(pkg)
        self.remove_pkgs.remove(pkg)
        for dep in self.marked_pkgs[pkg]:
            self.marked_pkgs[dep] = []
        self.marked_pkgs.pop(pkg)
