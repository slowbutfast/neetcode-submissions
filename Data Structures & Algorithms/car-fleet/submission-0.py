from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        input:
            position[i] - position of the ith car, its position in miles
            speed[i] - speed of the ith car, how how much its position moves
                every hour
        output:
            Given a car can't pass another car ahead of it, how many different
            car fleets will arrive at the same destination?

        notes:
            when two cars intersect, they will drive at the same speed, i.e.
            drive the speed of the slower car

            create third array of cars, with position and speed linked,
            then sort the array based on positions
             
        """
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        cars.sort(reverse=True)

        time = []

        for c_pos, c_speed in cars:
            time.append((target-c_pos)/c_speed)

        # now we have times. we can now iterate descending the list
        # of car positions. if the car has a time greater than the 
        # previous car farther back, we add the time to the stack, since they intersect
        # else maintain that time.

        fleets = deque()
    
        for i in range(len(cars)):
            if not fleets:
                fleets.append(time[i])
            else:
                last_time = fleets[-1]
                if time[i] <= last_time: # check if can reach the next car
                    continue
                else:
                    # create a new fleet
                    fleets.append(time[i])

        return len(fleets)