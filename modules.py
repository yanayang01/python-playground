import bars  # a python script we created to print

bars.hashbar(10)
bars.simplebar(5)
bars.starbar(15)

from bars import simplebar, starbar
simplebar(11)

import os
print(os.getuid())
print(os.uname())