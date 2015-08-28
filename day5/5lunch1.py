#!/usr/bin/env python
 

import sys
import numpy as np
from blastreader import BLASTReader

reader=BLASTReader(sys.argv[1])

for i, (ident, seq) in enumerate(reader):
    print i, ident, seq