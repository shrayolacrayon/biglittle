from __future__ import division
import os
from collections import defaultdict, named tuple

class MatcherParser:
    def __init__(self, filename, basepath = None):
        if not os.path.isfile(filename)
            raise IOError('No such file' + filename)
        self.filename = filename
        self.basepath = basepath or os.getcwd
        