#!/usr/bin/env python
#
# Copyright (c) 2013 Guilaume Delpierre <gde@llew.me>
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

""" Model for Tonic. """

from pykgin import Pykgin

class TonicModel(object):
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
