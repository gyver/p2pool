from __future__ import division

import os
import sqlite3
import time

from p2pool.util import db
from p2pool import p2p

print 'main'
x = p2p.AddrStore(db.SQLiteDict(sqlite3.connect(os.path.join(os.path.dirname(__file__), 'addrs.dat'), isolation_level=None), 'addrs'))

for i, (k, v) in enumerate(sorted(x.iteritems(), key=lambda (k, v): time.time() - v[-1])):
    print i, k, v, (time.time() - v[-1])/24/60/60

print
print 'testnet'
x = p2p.AddrStore(db.SQLiteDict(sqlite3.connect(os.path.join(os.path.dirname(__file__), 'addrs.dat'), isolation_level=None), 'addrs_testnet'))

for i, (k, v) in enumerate(sorted(x.iteritems(), key=lambda (k, v): time.time() - v[-1])):
    print i, k, v, (time.time() - v[-1])/24/60/60
