import time
from progressbar import ProgressBar

max_range = 100
pb = ProgressBar()

for i in range(1, max_range + 1):
    pb.printBar(i, max_range)
    time.sleep(0.1)

print("\nDone")