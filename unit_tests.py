import pytest
from playwright.sync_api import expect

from TrafficLightSim import *

"""
MethodName_StateUnderTest_ExpectedBehavior

    Method Name = The name of the method being tested. For example, Add.
    State Under Test = The state of the method you are testing. For example, TwoFloatingPointValues.
    Expected Behavior = What you expect to happen. For example, ReturnsSumOfValues.

"""
def test_TrafficLightChangeState_LightIsRed():
    # Arrange
    Light = TrafficLight("GREEN")
    expected = "RED"

    # Act
    Light.change_state()

    # Assert
    assert expected == Light.state

def test_TrafficLightChangeState_LightIsGreen():
    # Arrange
    Light = TrafficLight("RED")
    expected = "GREEN"

    # Act
    Light.change_state()

    # Assert
    assert expected == Light.state

def test_SensorCheckLimitBelow_PassTimeris5():
    # Arrange
    wait_que = []
    sensor_target = 5
    expected = 5
    for i in range(4):
        wait_que.append(Car())

    # Act
    if len(wait_que) <= sensor_target:
        timer = 5
    else:
        timer = 25

    # Assert
    assert expected == timer

def test_SensorCheckLimitOn_Timeris5():
    # Arrange
    wait_que = []
    sensor_target = 5
    expected = 5
    for i in range(5):
        wait_que.append(Car())

    # Act
    if len(wait_que) <= sensor_target:
        timer = 5
    else:
        timer = 25

    # Assert
    assert expected == timer

def test_SensorCheckLimitAbove_Timeris25():
    # Arrange
    wait_que = []
    sensor_target = 5
    expected = 25
    for i in range(6):
        wait_que.append(Car())

    # Act
    if len(wait_que) <= sensor_target:
        timer = 5
    else:
        timer = 25

    # Assert
    assert expected == timer

def test_AddCar_QueueSize1():
    # Arrange
    wait_que = []
    expected = 1

    # Act - add car to list
    wait_que.append(Car())

    # Assert - check size
    assert expected == len(wait_que)

def test_CarWait_WaitTime10():
    # Arrange - add car to queue and wait 10 times
    wait_que = []
    expected = 10
    wait_que.append(Car())
    for i in range(0, 10):
        for x in wait_que:
            x.wait()

    # Act - remove car from queue
    car_in_queue = wait_que.pop(0)

    # Assert - call wait time
    assert expected == car_in_queue.get_time()

def test_CarRemove_QueueSize3():
    # Arrange - add 4 cars to queue
    wait_que = []
    expected = 3
    for i in range(0, 4):
        wait_que.append(Car())

    # Act  - remove car from queue
    wait_que.pop(0)

    # Assert
    assert expected == len(wait_que)

def test_WaitTimeLargeQueue_WaitTime4():
    # Arrange - add 4 cars to queue
    wait_que = []
    expected = 4
    for i in range(0, 4):
        wait_que.append(Car())
        for x in wait_que:
            x.wait()

    # Act - remove car from queue
    car_in_queue = wait_que.pop(0)

    # Assert - call wait time
    assert expected == car_in_queue.get_time()

def test_WaitTimeList_WaitTimes4():
    # Arrange - add 4 cars to queue
    wait_que = []
    wait_times = []
    expected = [4,3,2,1]
    for i in range(0, 4):
        wait_que.append(Car())
        for x in wait_que:
            x.wait()

    # Act - removes all cars from queue and records wait times
    while wait_que:
        car_in_queue = wait_que.pop(0)
        wait_times.append(car_in_queue.get_time())

    # Assert - call wait time
    assert expected == wait_times

def test_averageList_Mean10():
    # Arrange
    def average_tester(input_list):
        return sum(input_list) / len(input_list)
    input_data = [10,5,15,5,5,15,15,10,10]
    expected = 10

    # Act
    result = average_tester(input_data)

    # Assert
    assert expected == result