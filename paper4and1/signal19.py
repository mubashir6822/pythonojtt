color = input('enter colour :')
def traffic_signal(func):
    def wrapper(color):
        print(color," : ", end="")
        func(color)
    return wrapper

@traffic_signal
def signal(color):
    if color == "red":
        print("STOP")
    elif color == "yellow":
        print("SLOW DOWN")
    elif color == "green":
        print("GO")
    else:
        print("give proper color")

signal(color)
# stop= traffic_signal(stop)

# @traffic_signal
# def slow_down(color):
#     print("SLOW DOWN")

# @traffic_signal
# def go(color):
#     print("GO")

# stop("red")
# slow_down("yellow")
# go("green")


#if i give it will acording to colour