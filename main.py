import random
from queue import Queue

class Car:
    def __init__(self):
        self.time = 0
    def wait(self):
        self.time += 1
    def get_time(self):
        return self.time

class TrafficLight:
    def __init__(self, state, sensor):
        self.state = state
        self.sensor = sensor
    def change_state(self):
        if self.state == "GREEN":
            self.state = "RED"
        else:
            self.state = "GREEN"




if __name__ == '__main__':
    def random_gen(goal):
        rdm = random.randint(1, 10)
        if rdm <= goal:
            return True
    def average(list):
        return sum(list) / len(list)

    NorthTL = TrafficLight("GREEN", "false") #init of North light at Green no sensor
    EastTL = TrafficLight("RED", "false") #init of East light at Red no sensor
    #Green last 25 ticks
    #Red last 25 tick
    #while loop                                                    beginning
    #on State Change - Cycle state change for TL
    #For loop for light cycle - 25 tick                            beginning
    #Add car to queue with RDM num gen for N & E separately
    #Remove car from green queue and record time in list
    #Wait call on car in queue - lines 51-56


    #end while - while is a full light cycle
    NorthQue = []
    EastQue = []
    northWaitTimes = []
    eastWaitTimes = []
    removedCar = Car


    countdown = 0
    while countdown < 999:
        print("Running Light Cycle: " + str(countdown))

        NorthTL.change_state() #North to Red on first call
        EastTL.change_state() #East to Green on first call
        timer = 25 #25 ticks of Red/Green light

        for i in range(timer):
            if NorthQue: #checks queue for empty
                for x in NorthQue: #updates car wait
                    x.wait()
                    # print('time: ', x.get_time())

            if EastQue: #checks queue for empty
                for x in EastQue:
                    x.wait()
                    # print('time: ', x.get_time())

            if random_gen(10): #generates car for North Light
                if random_gen(5):
                    NorthQue.append(Car())
                else:
                    EastQue.append(Car())


            if NorthTL.state == "GREEN": #removes car from QUEUE if light is Green
                if NorthQue:
                    removedCar = NorthQue.pop()
                    waitTime = removedCar.get_time()
                    print("Wait time:")
                    print(waitTime)
                    northWaitTimes.append(waitTime) #records wait time for cars


            elif EastTL.state == "GREEN": #removes car from QUEUE if light is Green
                if EastQue:
                    removedCar = EastQue.pop()
                    waitTime = removedCar.get_time()
                    print("Wait time:")
                    print(waitTime)
                    eastWaitTimes.append(waitTime)  # records wait time for cars
        countdown += 1
    print("Average of North wait =", round(average(northWaitTimes), 2))
    print("Average of East wait =", round(average(eastWaitTimes), 2))