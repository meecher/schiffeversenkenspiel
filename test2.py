from typing import Sequence
import numpy as np

ySize = 10
xSize = 10



matchfield_visual = np.chararray((ySize, xSize))
matchfield_visual[:] = 1
#print(' '.join(map(str, matchfield_visual)))
#hurensohn = matchfield_visual.join()
#print(hurensohn)
matchfield_visual.astype(str)

for row in matchfield_visual.astype(str):
        string_ints = [str(int) for  int in row]
        stringli = ' '.join(string_ints)
        print(stringli)
