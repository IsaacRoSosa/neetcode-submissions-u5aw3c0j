class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars= []
        #(position,speed)
        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        cars.sort(key=lambda item: item[0])
        print(cars)

        fleet = []
        for car in cars:
            time = (target-car[0])/car[1]
            
            while fleet and time >= fleet[-1]:
                fleet.pop()
            fleet.append(time)
        return(len(fleet))
        #time = (target-position) / speed

        