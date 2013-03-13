#!/usr/bin/env python

from view import View

class Tonic(object):
    def __init__(self):
        self.view = View()
        self.view.mainloop()

if __name__ == "__main__":
    tonic = Tonic()
