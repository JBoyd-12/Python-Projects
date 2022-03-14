from Worker import Worker

class Elevator():
    total_workers = 0
    total_wait_time = 0 #used to calculate average wait time
    workers_who_walk = 0 #used to keep track of number of workers who walk
    walk_2 = 0
    walk_3 = 0
    walk_4 = 0

    def __init__(self):
        super().__init__()
        self.max_capacity = 12
        self.current_capacity = 0
        self.time = 0
        self.new_arrival_time = 0
        self.current_floor = 'G'
        self.still_waiting = []

    def loading_elevator(self,waiting):
        workers = [0] * self.max_capacity
        length = len(self.still_waiting)
        print(f'This is how many are currently waiting {waiting}')
        if(length > 0):
            for i in range(length):
                if(self.current_capacity == self.max_capacity):
                    break
                self.still_waiting[0].wait_time = self.time - self.still_waiting[0].arrival_time
                Elevator.total_wait_time += self.still_waiting[0].wait_time 
                workers[self.current_capacity] = self.still_waiting[0]
                Elevator.total_workers +=1
                self.still_waiting.pop(0)
                self.current_capacity += 1
                waiting -=1
        count = waiting
        if(waiting > self.max_capacity):
            print("More than maximum capactiy, some will have to wait or walk")
            for i in range(count):
                worker = Worker()
                if((i % 6) == 0):
                    self.new_arrival_time+=1
                    
                worker.arrival_time = self.new_arrival_time
                if(worker.chance_of_walking() == 1):
                    #Chose to take the stairs
                    # print("Person decided to walk")
                    if(worker.chosen_floor == 2):
                        Elevator.walk_2 +=1
                    elif(worker.chosen_floor == 3):
                        Elevator.walk_3 +=1
                    elif(worker.chosen_floor == 4):
                        Elevator.walk_4 +=1
                    waiting -=1
                    Elevator.workers_who_walk += 1
                    continue
    
                if(self.current_capacity == self.max_capacity):
                    #Decide to wait
                    self.still_waiting.append(worker)
                    # print("worker decided to wait")
                    continue
                worker.wait_time = self.time - worker.arrival_time
                Elevator.total_wait_time += worker.wait_time
                # print("Worker got on the elevator")
                workers[self.current_capacity] = worker
                Elevator.total_workers +=1
                self.current_capacity += 1
                waiting -=1
        else:               
            for i in range(count):
                worker = Worker()
                if(self.time > 0):
                    if((i % 6) == 0):
                        self.new_arrival_time+=1
                worker.arrival_time = self.new_arrival_time
                worker.wait_time = self.time - worker.arrival_time
                Elevator.total_wait_time += worker.wait_time
                workers[i] = worker
                Elevator.total_workers +=1
                self.current_capacity += 1
                waiting -=1
        print(f'This is how many are waiting after loading the elevator {waiting}\n')
        return workers, waiting
    
    def executing_elevator(self, workers):
        workers = [i for i in workers if i != 0]
        workers.sort(key=lambda x: x.chosen_floor)

        for i in workers:
            print(f"Visiting floor {i.chosen_floor}, the arrival time was {i.arrival_time}, and the waiting time was {i.wait_time}")
            self.traveling_to_floor(i.chosen_floor)
        self.current_floor = 'G'

    def traveling_to_floor(self, floor):
        if(self.current_floor == 'G'):
            if(floor == 2):
                self.current_floor = 2
                self.current_capacity -= 1
                #travelling time
                self.time += 1
                #open door time
                self.time += .5
            elif(floor == 3):
                self.current_floor = 3
                self.current_capacity -= 1
                #travelling time
                self.time += 1.5
                #open door time
                self.time += .5
            elif(floor == 4):
                self.current_floor = 4
                self.current_capacity -= 1
                #travelling time
                self.time += 1.75
                #open door time
                self.time += .5
        elif(self.current_floor == 2):
            if(floor == 2):
                self.current_floor = 2
                self.current_capacity -= 1
            elif(floor == 3):
                self.current_floor = 3
                self.current_capacity -= 1
                #travelling time
                self.time += .5
                #open door time
                self.time += .5
            elif(floor == 4):
                self.current_floor = 4
                self.current_capacity -= 1
                #travelling time
                self.time += .75
                #open door time
                self.time += .5
        elif(self.current_floor == 3):
            if(floor == 3):
                self.current_floor = 3
                self.current_capacity -= 1
            elif(floor == 4):
                self.current_floor = 4
                self.current_capacity -= 1
                #travelling time
                self.time += .5
                #open door time
                self.time += .5
        elif(self.current_floor == 4):
            if(floor == 4):
                self.current_floor = 4
                self.current_capacity -= 1
