import sys
import os

sys.path.append(os.path.realpath(f"./Model/"))
sys.path.append(os.path.realpath(f"./View/"))
sys.path.append(os.path.realpath(f"./Controller/"))
sys.path.append(os.path.realpath(f"./Model/sys/"))

from View.view_facade import View_interface as View
View.run()


