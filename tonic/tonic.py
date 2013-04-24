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

"""Main script for Tonic."""

try:
    import wx
except ImportError:
    raise ImportError,"The wxPython module is required to run this program"

import os, sys
import gettext
from controller import TonicController

def setup_i18n():
    basepath = os.path.abspath(os.path.dirname(__file__))
    localedir = os.path.join(basepath, "locale")
    print localedir
    # Default OS lang
    langid = wx.LANGUAGE_DEFAULT
    # Set locale for wxWidgets
    mylocale = wx.Locale(langid)
    # Set up Python's gettext
    translation = gettext.translation("tonic", localedir, \
                                            [mylocale.GetCanonicalName()], \
                                            fallback = True)
    translation.install()

def main():
    """Main function."""
    setup_i18n()
    app = wx.App(False)
    tonic = TonicController(app)
    app.MainLoop()

if __name__ == '__main__':
    main()