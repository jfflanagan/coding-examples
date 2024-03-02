def IsSomeoneOnSwing():
    print("Is someone on the swing? (Y/N)")
    reply = input().upper()
    while reply not in ["Y", "N", "NO", "YES"]:
        print("I don't understand '{0}' Is someone on the swing? (Y/N)".format(reply))
        reply = input().upper()

    return reply

def PlayOnTheSlide():
    print("I am playing on the slide")

def PlayOnTheSwing():
    print("I am playing on the swing")