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
    def __init__(self,sensor,traffic,sensor_target = 5,timer_length = 25):
        self.sensor = sensor
        north_que = []
        east_que = []
        north_wait_times = []
        east_wait_times = []
        arrival = 0
        countdown = 0
        while countdown < 289: # for 25 ticks 289 cycles would be ~2 hours in the real world

            NorthTL.change_state()  # North to Red on first call
            EastTL.change_state()  # East to Green on first call

            if sensor: #if sensor is true will change timer based on queue size
                if NorthTL.state == "GREEN":
                    if len(north_que) <= sensor_target: #5 or less timer is 5
                        timer = sensor_target
                    else: # >5 cars timer will be 25
                        timer = timer_length
                else:
                    if len(east_que) <= sensor_target:
                        timer = sensor_target
                    else:
                        timer = timer_length
            else:
                timer = timer_length  # 25 ticks is standard of Red/Green light

            for i in range(timer):
                arrival+=1

                if traffic == "Busy":
                    if random_gen():  # adds car to North 50/50
                        north_que.append(Car())
                    else:
                        east_que.append(Car())
                elif traffic == "Normal" and arrival % 2 == 0: #generates a car every other time
                    if random_gen():  # adds car to North 50/50
                        north_que.append(Car())
                    else:
                        east_que.append(Car())

                for p in range(1):

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

        print("Average of traffic =", average_traffic)

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
#---------------------------------------Timer-Based Busy Traffic--------------------------------------------------------
    print("Timer-based data BUSY traffic:")
    timer_busy = LightCycle(False,"Busy") #sensor false, traffic busy (car shows up every tick)

#--------------------------------------Timer-Based Normal Traffic-------------------------------------------------------
    print("Timer-based data NORMAL traffic:")
    timer_normal = LightCycle(False, "Normal") #sensor false, traffic normal (car shows up every other tick)

#--------------------------------------Sensor-Based Heavy Traffic-------------------------------------------------------
    print("Sensor-Based data BUSY traffic:")
    sensor_heavy = LightCycle(True, "Busy",5) #sensor true, traffic busy (car shows up every tick)

#-------------------------------------Sensor-Based Normal Traffic-------------------------------------------------------
    print("Sensor-based data NORMAL traffic:")
    sensor_normal = LightCycle(True, "Normal",5) #sensor true, traffic normal (car shows up every other tick)

