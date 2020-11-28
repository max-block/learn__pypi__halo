import sys
import time

from halo import Halo

spinner = Halo(text="Loading", spinner="dots", stream=sys.stderr)
spinner.start()

time.sleep(1)
spinner.text = "processed 1"
time.sleep(1)
spinner.text = "processed 2"
time.sleep(1)

spinner.stop()
print("done!")
