from johnny_lib import *

waiting_for_swing = True

while waiting_for_swing:
    if IsSomeoneOnSwing() in ["Y", "YES"]:
        PlayOnTheSlide()
    else:
        PlayOnTheSwing()
        waiting_for_swing = False


``