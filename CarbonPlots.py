# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd

china = pd.read_csv("china.csv")
usa = pd.read_csv("usa.csv")
both = pd.read_csv("both.csv",index_col=0)

# <codecell>

both.plot()

# <codecell>


