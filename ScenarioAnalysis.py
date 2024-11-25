import random
from itertools import cycle


class Car:
    def __init__(self):
        self.time = 0
    def wait(self):
        self.time += 1
    def get_time(self):
        return self.time

class TrafficLight:
    def __init__(self, state):
        self.state = state
    def change_state(self):
        if self.state == "GREEN":
            self.state = "RED"
        else:
            self.state = "GREEN"


def full_cycle(north_sensor,east_sensor,north_traffic,east_traffic):
    north_que = []
    east_que = []
    north_wait_times = []
    east_wait_times = []
    arrival = 0
    countdown = 0
    while countdown < 289: # for 25 ticks 289 cycles would be ~2 hours in the real world

        NorthTL.change_state()  # North to Red on first call
        EastTL.change_state()  # East to Green on first call
        timer = 20
        if NorthTL.state=="GREEN": #if sensor is true will change timer based on queue size
            if north_sensor:
                if len(north_que) <= 5: #5 or less timer is 5
                    timer = 5
                else: # >5 cars timer will be 25
                    timer = 20
        elif EastTL.state == "GREEN":
            if east_sensor:
                if len(east_que) <= 5:
                    timer = 5
                else:
                    timer = 20


        for i in range(timer):
            arrival+=1

            if north_traffic == "Busy" and east_traffic == "Busy":
                if random_gen():  # adds car to North 50/50
                    north_que.append(Car())
                else:
                    east_que.append(Car())
            elif north_traffic == "Normal" and east_traffic == "Normal" and arrival % 2 == 0: #generates a car every other time
                if random_gen():  # adds car to North 50/50
                    north_que.append(Car())
                else:
                    east_que.append(Car())
            elif north_traffic == "Normal" and east_traffic == "Busy":
                if random_gen():
                    if arrival % 2 == 0:
                        north_que.append(Car())
                else:
                    east_que.append(Car())
            elif north_traffic == "Busy" and east_traffic == "Normal":
                if random_gen():
                    north_que.append(Car())
                elif arrival % 2 == 0:
                    east_que.append(Car())

            if NorthTL.state == "GREEN":  # removes car from QUEUE if light is Green
                if north_que:
                    removed_car = north_que.pop(0)
                    waitTime = removed_car.get_time()
                    north_wait_times.append(waitTime)  # records wait time for cars


            elif EastTL.state == "GREEN":  # removes car from QUEUE if light is Green
                if east_que:
                    removed_car = east_que.pop(0)
                    waitTime = removed_car.get_time()
                    east_wait_times.append(waitTime)  # records wait time for cars

            if north_que:  # checks queue for empty
                for x in north_que:  # updates car wait
                    x.wait()
                    # print('time: ', x.get_time())

            if east_que:  # checks queue for empty
                for x in east_que:
                    x.wait()
                    # print('time: ', x.get_time())
        countdown += 1


    average_north = round(average(north_wait_times), 2)
    #print("Average of North wait =",average_north )
    average_east = round(average(east_wait_times), 2)
    #print("Average of East wait  =", average_east )
    average_traffic = round((average_east+average_north)/2, 2)
    averages = [average_east,average_north,average_traffic]
    return averages


if __name__ == '__main__':
    def random_gen():
        rdm = random.randint(1, 100)
        if rdm % 2 == 0:
            return True
        else:
            return False
    def average(input_list):
        return sum(input_list) / len(input_list)

    NorthTL = TrafficLight("GREEN") #init of North light at Green
    EastTL = TrafficLight("RED") #init of East light at Red
    east_average = []
    north_average = []
    all_average = []

    for l in range(30):
        temp = full_cycle(north_sensor = False,north_traffic = "Normal",east_sensor = False,east_traffic = "Busy")
        east_average.append(temp[0])
        north_average.append(temp[1])
        all_average.append(temp[2])
    print("East Average:"+str(round(average(east_average),2)))
    print("North Average:"+str(round(average(north_average),2)))
    print("All Average:"+str(round(average(all_average),2)))