import math
from Elevator import Elevator
from Worker import Worker

def main():
    #Initial values
    elevator = Elevator()
    currentTime = 0
    timeDifference = 0
    waiting = 6

    workers_at_830 = 0
    workers_at_845 = 0
    workers_at_9 = 0
    time_of_final_boarding = 0
    while(currentTime < 60):
        print("Loading the elevator")
        workers, stillWaiting = elevator.loading_elevator(waiting)
        waiting = stillWaiting

        print("Taking people to their floors")
        elevator.executing_elevator(workers)
        time_of_final_boarding = currentTime
        timeDifference = elevator.time - currentTime
        currentTime = elevator.time
        print(f"\nThis is the current time: {currentTime}, this is how much time has passed: {timeDifference}")
        print("----------------------------------------------------------------------------------------------")
        for i in range(math.floor(timeDifference)):
            waiting += 6

        if(currentTime >= 30 and workers_at_830 == 0):
            workers_at_830 = waiting
        if(currentTime >= 45 and workers_at_845 == 0):
            workers_at_845 = waiting
        if(currentTime >= 60 and workers_at_9 == 0):
            workers_at_9 = waiting
        
    
    print(f'Average wait time for a worker: {Elevator.total_wait_time} / {Elevator.total_workers} = {(Elevator.total_wait_time/Elevator.total_workers):.2f}')
    print(f'Number of workers who walk: {Elevator.workers_who_walk}')
    print(f'Number of workers who walk to the 2nd Floor: {Elevator.walk_2}')
    print(f'Number of workers who walk to the 3rd Floor: {Elevator.walk_3}')
    print(f'Number of workers who walk to the 4th Floor: {Elevator.walk_4}')
    print(f'The time the last worker boards the elevator: {time_of_final_boarding}')
    print(f'Number of workers in line at 8:30: {workers_at_830}')
    print(f'Number of workers in line at 8:45: {workers_at_845}')
    print(f'Number of workers in line at 9:00: {workers_at_9}')
main()



