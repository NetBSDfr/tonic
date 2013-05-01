What is Tonic
=============

Tonic aims to provide a GUI for pkgin.

License
=======

```
Copyright (c) 2013 Guilaume Delpierre <gde@llew.me>
Copyright (c) 2013 Sylvain Mora <sylvain.mora@solevis.net>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer
in this position and unchanged.
2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR(S) ``AS IS'' AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE AUTHOR(S) BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

Internationalization
====================

```bash
mkdir -p tonic/locale/de/LC_MESSAGES
cp tonic/locale/en/LC_MESSAGES/tonic.pot tonic/locale/de/LC_MESSAGES/
poedit tonic/locale/de/LC_MESSAGES/tonic.pot
```

TODO
====

 - Apply changes (actions and progress dialog)
 - Unmark / Redo / Undo (keep changes in memory)
 - Filters (store packages status)
 - Import / Export (bind with pykgin import/export)
 - Update (bind with pykgin.update())
 - Upgrade (show upgrades, bind with pykgin.upgrade and progress dialog)
 - Repository Settings (TextCtrl for edit /usr/pkg/etc/pkgin/repositories.cong)
 - Preferences 
 - Changes List
 - Translation (fix missing gettext sentences, add more languages)
 - Moar test (as a monkey)
 - Unit tests (dowant)
