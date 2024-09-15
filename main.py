class Car:
    def __init__(self, time=0):
        self.time = time
    def wait(self):
        self.time += 1

class TrafficLight:
    def __init__(self, state, sensor):
        self.state = state
        self.sensor = sensor
    def ChangeState(self):
        if state == "GREEN":
            self.state = "YELLOW"
        elif state == "YELLOW":
            self.state = "RED"
        elif state == "RED":
            self.state = "GREEN"


if __name__ == '__main__':
    NorthTL = TrafficLight("YELLOW", false) #init of North light at Green no sensor
    EastTL = TrafficLight("RED", false) #init of East light at Red no sensor
    #Green last 24 ticks
    #Yellow last 1 tick
    #Red last 25 tick
    #while loop                                                    beginning
    #on State Change - Cycle state change for TL
    #For loop for light cycle - 25 tick                            beginning
    #Add car to queue with RDM num gen for N & E separately
    #Remove car from green queue and record time in list
    #Wait call on car in Red queue


    #while be full cycles
    #nested for while doing traffic flow - 25 ticks



    countdown = 1000
    while countdown > 0:
        NorthTL.ChangeState() #North to Red on first call
        EastTL.ChangeState() #East to Green on first call
        timer = 25
        for i in range(timer):

            # Add car to queue with RDM num gen for N & E separately
            # Remove car from green queue and record time in list
            # Wait call on car in Red queue

            if i == 23:
                if NorthTL.state == "GREEN":
                    NorthTL.ChangeState()
                else:
                    EastTL.ChangeState()
        countdown -= 1