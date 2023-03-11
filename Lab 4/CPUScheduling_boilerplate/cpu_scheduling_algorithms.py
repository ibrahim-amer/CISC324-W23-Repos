
class Process:
    def __init__(self, arrival_time, burst_time, priority) -> None:
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority
        self.turn_around_time = 0 #Initially, has a value of zero but you should update it
        self.waiting_time = 0 #Initially, has a value of zero but you should update it

class CPUScheduler:
    def __init__(self, processes, time_quantum) -> None:
        self.processes = processes
        self.time_quantum = time_quantum
    
    def first_come_first_served(self):
        #TODO: implement FCFS algorithm here and print the average waiting time
        pass

    def shortest_job_first(self):
        #TODO: implement SJF here and print the average waiting time
        pass

    def round_robin(self):
        #TODO: implement Round Robin algorithm here and print the average waiting time and the average turn around time
        pass
    
    def priority_based(self):
        #TODO: implement priority based process scheduling algorithm
        pass

