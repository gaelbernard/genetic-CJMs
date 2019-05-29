#! /usr/bin/env python

"""
Usage:
    prefixspan.py (frequent | top-k) <threshold>
"""

from __future__ import print_function

import sys
from collections import defaultdict
from heapq import heappop, heappush

from docopt import docopt

#https://github.com/chuanconggao/PrefixSpan-py

class PrefixSpan:



    def __init__(self, db, minsup):
        self.db = db
        self.minsup = minsup
        self.results = []



    def frequent_rec(self, patt, mdb):

        self.results.append((len(mdb), patt, len(patt)*len(mdb)))

        occurs = defaultdict(list)
        for (i, startpos) in mdb:
            seq = self.db[i]
            for j in xrange(startpos, len(seq)):
                l = occurs[seq[j]]
                if len(l) == 0 or l[-1][0] != i:
                    l.append((i, j + 1))

        for (c, newmdb) in occurs.iteritems():
            if len(newmdb) >= self.minsup:
                self.frequent_rec(patt + [c], newmdb)

        self.results.sort(key=lambda x: x[2], reverse=True)

    def topk_rec(self, patt, mdb):
        heappush(self.results, (len(mdb), patt))
        if len(self.results) > self.k:
            heappop(self.results)

        occurs = defaultdict(list)
        for (i, startpos) in mdb:
            seq = self.db[i]
            for j in xrange(startpos, len(seq)):
                l = occurs[seq[j]]
                if len(l) == 0 or l[-1][0] != i:
                    l.append((i, j + 1))

        for (c, newmdb) in sorted(occurs.iteritems(), key=(lambda (c, newmdb): len(newmdb)), reverse=True):
            if len(self.results) == self.k and len(newmdb) <= self.results[0][0]:
                break

            self.topk_rec(patt + [c], newmdb)