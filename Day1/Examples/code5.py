# Anything after “return” does not get executed


def run():
    print("Up")
    return
    print("down")
    
run()