import random
from queue import Queue

class Car:
    def __init__(self): #initial setup with time = 0
        self.time = 0
    def wait(self): #increases time by 1
        self.time += 1
    def get_time(self): #returns time for Car
        return self.time

class TrafficLight:
    def __init__(self, state, sensor): #initial setup
        self.state = state
        self.sensor = sensor
    def change_state(self): #changes light state from Red -> Green/Green -> Red
        if self.state == "GREEN":
            self.state = "RED"
        else:
            self.state = "GREEN"




if __name__ == '__main__':
    def random_gen(goal): #random number gen with goal, goal lets set frequency of true, 10%, 20%, 30%, ... , 100%
        rdm = random.randint(1, 10)
        if rdm <= goal:
            return True
    def average(list): #returns average of given list
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
    while countdown < 999: #runs light cycle 999 times for data collection
        print("Running Light Cycle: " + str(countdown))

        NorthTL.change_state() #North to Red on first call
        EastTL.change_state() #East to Green on first call
        timer = 25 #25 ticks of Red/Green light

        for i in range(timer): #runs single light cycle for timer amount of ticks. In timer-based 25 ticks, for sensor timer will change
            if NorthQue: #checks queue for empty
                for x in NorthQue: #updates car wait
                    x.wait() #increases car wait time for data collection
                    # print('time: ', x.get_time()) #testing purposes

            if EastQue: #checks queue for empty
                for x in EastQue:
                    x.wait() #increases car wait time for data collection
                    # print('time: ', x.get_time()) #testing purposes

            if random_gen(10): #generates car for Traffic Lights
                if random_gen(5): #50/50 on who gets the car. True N gets car, False E gets car
                    NorthQue.append(Car())
                else:
                    EastQue.append(Car())


            if NorthTL.state == "GREEN": #removes car from QUEUE if light is Green
                if NorthQue: #checks if empty
                    removedCar = NorthQue.pop() #removes car from queue
                    waitTime = removedCar.get_time() #gets the wait time for car removed
                    #print("Wait time:") #testing purposes
                    #print(waitTime) #testing purposes
                    northWaitTimes.append(waitTime) #records wait time for cars to list for data collection


            elif EastTL.state == "GREEN": #removes car from QUEUE if light is Green
                if EastQue: #checks if empty
                    removedCar = EastQue.pop() #removes car from queue
                    waitTime = removedCar.get_time() #gets the wait time for car removed
                    #print("Wait time:") #testing purposes
                    #print(waitTime) #testing purposes
                    eastWaitTimes.append(waitTime)  # records wait time for cars
        countdown += 1 #increase light cycle count
    print("Average of North wait =", round(average(northWaitTimes), 2)) #data collection of wait times rounded to 2 decimals
    print("Average of East wait =", round(average(eastWaitTimes), 2)) #data collection of wait times rounded to 2 decimals