import random
from queue import Queue

class Car:
    def __init__(self, time):
        self.time = time
    def wait(self):
        self.time += 1
    def __gettime__(self):
        return self.time

class TrafficLight:
    def __init__(self, state, sensor):
        self.state = state
        self.sensor = sensor
    def ChangeState(self):
        if self.state == "GREEN":
            self.state = "YELLOW"
        elif self.state == "YELLOW":
            self.state = "RED"
        elif self.state == "RED":
            self.state = "GREEN"




if __name__ == '__main__':
    def random_gen(goal):
        rdm = random.randint(1, 10)
        print(rdm)
        if rdm <= goal:
            return True
    def average(list):
        return sum(list) / len(list)

    NorthTL = TrafficLight("YELLOW", "false") #init of North light at Green no sensor
    EastTL = TrafficLight("RED", "false") #init of East light at Red no sensor
    #Green last 24 ticks
    #Yellow last 1 tick
    #Red last 25 tick
    #while loop                                                    beginning
    #on State Change - Cycle state change for TL
    #For loop for light cycle - 25 tick                            beginning
    #Add car to queue with RDM num gen for N & E separately
    #Remove car from green queue and record time in list
    #Wait call on car in queue - lines 51-56


    #while be full cycles
    #nested for while doing traffic flow - 25 ticks
    NorthQue = []
    EastQue = []
    northWaitTimes = []
    eastWaitTimes = []



    countdown = 0
    while countdown < 100:
        print("Running Light Cycle: " + str(countdown))

        NorthTL.ChangeState() #North to Red on first call
        EastTL.ChangeState() #East to Green on first call
        timer = 25 #25 ticks of Red/Green light

        for i in range(timer):
            wait = 0
            if NorthQue: #checks queue for empty
                for x in NorthQue: #updates car wait time
                    wait = Car.__gettime__(NorthQue.pop())
                    wait += 1
                    NorthQue.append(Car(wait))
                    wait = 0
            if EastQue:
                for x in EastQue:
                    wait = Car.__gettime__(EastQue.pop())
                    wait += 1
                    EastQue.append(Car(wait))
                    wait = 0

            if random_gen(5): #generates car for North Light
                NorthQue.append(Car(0))
            if random_gen(8): #generates car for East Light
                EastQue.append(Car(0))

            if NorthTL.state == "GREEN" or NorthTL.state == "YELLOW": #removes car from QUEUE if light is Green/Yellow
                if NorthQue:
                    northWaitTimes.append(Car.__gettime__(NorthQue.pop())) #records wait time for cars
                    #NorthQue.pop()

            elif EastTL.state == "GREEN" or EastTL.state == "YELLOW": #removes car from QUEUE if light is Green/Yellow
                if EastQue:
                    eastWaitTimes.append(Car.__gettime__(EastQue.pop())) #records wait time for cars
                    #EastQue.pop()

            if i == 23: #sets green light to yellow
                if NorthTL.state == "GREEN":
                    NorthTL.ChangeState()
                else:
                    EastTL.ChangeState()
        countdown += 1
    print("Average of North wait =", round(average(northWaitTimes), 2))
    print("Average of East wait =", round(average(eastWaitTimes), 2))