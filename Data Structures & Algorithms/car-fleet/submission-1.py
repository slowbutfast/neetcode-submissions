from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        we have n cars with a position and speed travelling to 
        location target, all in miles, or miles per second. cars
        cannot pass other cars, and if a car reaches a car ahead
        of it, it joins the fleet. return how many different
        car fleets will arrive at the destination.

        we want to know when a car will reach a car ahead of it.
        we can sort the cars by position, and then track how 
        much time it'll take for the car to reach the target.
        then before any cars move, we can compare the car closest 
        to the destination to the car behind it. if the car farther
        away takes more time than the car ahead, it'll never reach
        it. if it takes less time, it'll join the fleet.

        we can use a stack to track this. append the first car to the
        stack. check if previous car is faster than the car on the stack.
        if it is, it'll join the fleet and travel with the same time.
        if it isn't, we append the car's new time as its own fleet.
        len of stack is # of fleets
        """
        cars = []
        for pos, c_speed in zip(position, speed):
            time = (target - pos) / c_speed
            cars.append((pos, time))

        fleets = deque()
        cars.sort(reverse=True)
        # print(cars)        
        for _, c_time in cars:
            if not fleets:
                fleets.append(c_time)
            else:
                prev_time = fleets[-1]
                if c_time <= prev_time: # car will catch up and join the fleet
                    continue
                else: # car is won't catch up and start its own fleet
                    fleets.append(c_time)
        # print(fleets)
        return len(fleets)

