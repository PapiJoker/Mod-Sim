# Mod-Sim Traffic Simulation
## Josh Early

### Goal
The goal of this model is to simulate an intersection between a northbound
road and an eastbound road. To better understand the differences in wait times for
timer based and sensor based light controls.


### Implementation
The plans for how the intersection is to be simulated. Is to have two different traffic
flow types. One busy and one more normalized. In a study done on traffic flow during 
busy times cars would arrive to the intersection every second. While in a more normal
traffic setting cars would arrive every 2 seconds to the intersection. Once cars arrive
at a light they are added into a queue and once it is their time to go their wait time
is recorded for data collection.

The two traffic control types being tested is a timer controlled and
sensor controlled model. With the timer no matter how many cars are waiting to go the
light will cycle with 25 ticks for red/green. Cars in the green light queue will be
popped one at a time for every tick. Every tick the cars in the queue will also increase
their wait time by one. Upon being removed from the queue the wait time for the car
will be recorded into a list.

For the sensor based light control, the green light queue will be tested for size.
If the queue has *INSERT AMOUNT* of cars in the queue the light will cycle as normal
with 25 ticks for the green cycle. If there are fewer cars in the queue then the light
will cycle green for only *INSERT TIME* ticks. This should show a wait time decrease
for other lights.


### Limitations
The limitations of the model is it only implements two directions with two lanes. 
This simplifies the model as having a west or southbound lane would be
the same as having another north/east lane as this model does not implement turning
traffic. Other limitations is cars reaction time to a light turning green could change
the flow of traffic through the light. Along with acceleration times of the cars to 
pass through the light.

### Current Implementations
2 traffic lights, East and North <br\>
Cars moving in and out of Queues <br\>
Wait time averages for the lights <br\>
Timer-based control at 25 tick cycles <br\>

### To-be Implemented
Sensor based control <br\>
Heavy and normal traffic flows <br\>
