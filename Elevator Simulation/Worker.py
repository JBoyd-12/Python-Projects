import random as rd

class Worker():
    def __init__(self):
        super().__init__()
        self.chosen_floor = rd.randint(2,4)
        self.arrival_time = 0
        self.wait_time = 0
        
    def chance_of_walking(self):
        if(self.chosen_floor == 2):
            return rd.randint(1,2)
        if(self.chosen_floor == 3):
            return rd.randint(1,3)
        if(self.chosen_floor == 4):
            return rd.randint(1,10)
        