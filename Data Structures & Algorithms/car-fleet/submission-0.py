class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # I need to create a structure to store the position and speed to represent the car

        stack = []
        # the one closer to the target first

        cars = sorted(zip(position, speed), reverse=True)

        for p, s in cars:
            time = (target - p) / s

            # it means it will x min for the car to travel from starting point to
            # the target; when t1 > to mean the car will not meet it at the target, 
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)