import random

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

class LightCycle:
    def __init__(self,sensor,traffic):
        self.sensor = sensor
        north_que = []
        east_que = []
        north_wait_times = []
        east_wait_times = []

        countdown = 0
        while countdown < 499:

            NorthTL.change_state()  # North to Red on first call
            EastTL.change_state()  # East to Green on first call
            if sensor:
                if NorthTL.state == "GREEN":
                    if len(north_que) <= 5:
                        timer = 5
                    else:
                        timer = 25
                else:
                    if len(east_que) <= 5:
                        timer = 5
                    else:
                        timer = 25
            else:
                timer = 25  # 25 ticks of Red/Green light

            for i in range(timer):
                if north_que:  # checks queue for empty
                    for x in north_que:  # updates car wait
                        x.wait()
                        # print('time: ', x.get_time())

                if east_que:  # checks queue for empty
                    for x in east_que:
                        x.wait()
                        # print('time: ', x.get_time())

                if traffic == "Busy":  # generates car every time
                    if random_gen(50):  # adds car to North 50/50
                        north_que.append(Car())
                    else:
                        east_que.append(Car())
                elif traffic == "Normal" and i % 2 == 0: #generates a car every other time
                    if random_gen(50):  # adds car to North 50/50
                        north_que.append(Car())
                    else:
                        east_que.append(Car())

                if NorthTL.state == "GREEN":  # removes car from QUEUE if light is Green
                    if north_que:
                        removedCar = north_que.pop()
                        waitTime = removedCar.get_time()
                        north_wait_times.append(waitTime)  # records wait time for cars


                elif EastTL.state == "GREEN":  # removes car from QUEUE if light is Green
                    if east_que:
                        removedCar = east_que.pop()
                        waitTime = removedCar.get_time()
                        east_wait_times.append(waitTime)  # records wait time for cars
            countdown += 1

        print("Average of North wait =", round(average(north_wait_times), 2))
        print("Average of East wait  =", round(average(east_wait_times), 2))


if __name__ == '__main__':
    def random_gen(goal):
        rdm = random.randint(1, 100)
        if rdm <= goal:
            return True
    def average(input_list):
        return sum(input_list) / len(input_list)

    NorthTL = TrafficLight("GREEN") #init of North light at Green
    EastTL = TrafficLight("RED") #init of East light at Red
    # --------------------------------------Timer-Based Busy Traffic--------------------------------------------
    print("Timer-based data busy traffic:")
    timer_busy = LightCycle(False,"Busy") #sensor false, traffic busy (car shows up every tick)

    #--------------------------------------Timer-Based Normal Traffic-------------------------------------------
    print("Timer-based data normal traffic:")
    timer_normal = LightCycle(False, "Normal") #sensor false, traffic normal (car shows up every other tick)

    #----------------------------------Sensor-Based Heavy Traffic-----------------------------------------------
    print("Sensor-Based data busy traffic:")
    sensor_heavy = LightCycle(True, "Busy") #sensor true, traffic busy (car shows up every tick)

    # ----------------------------------Sensor-Based Normal Traffic---------------------------------------------
    print("Sensor-based data normal traffic:")
    sensor_normal = LightCycle(True, "Normal") #sensor true, traffic normal (car shows up every other tick)