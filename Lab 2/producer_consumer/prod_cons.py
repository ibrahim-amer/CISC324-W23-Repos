import threading
import time

# Shared Memory variables
CAPACITY = 10
finished = False
buffer = [-1 for i in range(CAPACITY)]
in_index = 0
out_index = 0
n_producers = 5
n_consumers = 5

barrier = threading.Barrier(n_producers)# This barrier is used to make sure that all producers finish at the same time. You don't need to worry about it. 

# TODO: Declare the required semaphores here (mutex, empty, full) and initialize them with the proper values.
#  You will need to add mark these semaphores as global in both the Producer and Consumer classes (see the code below)

# Producer Thread Class
class Producer(threading.Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id

    def run(self, id=0):

        global CAPACITY, buffer, in_index, out_index, barrier, finished
        #TODO: mark the semaphores as global here

        items_produced = 0
        counter = 0

        while items_produced < 20:
            # TODO: acquire one of the declared semaphores here
            # TODO: acquire one of the declared semaphores here

            counter += 1
            buffer[in_index] = counter
            in_index = (in_index + 1) % CAPACITY
            print(f"Producer {self.id} produced : ", counter)

            # TODO: don't forget to release the semaphores here accordingly
            time.sleep(0.1)

            items_produced += 1

        print(f"Producer {self.id}: Done")
        # wait for all producers to finish
        barrier.wait()
        # signal that there are no further items
        if self.id == 0:
            print("ALL PRODUCERS FINISHED")
            finished = True


# Consumer Thread Class
class Consumer(threading.Thread):
  def __init__(self, id):
    super().__init__()
    self.id = id

  def run(self):
    global CAPACITY, buffer, in_index, out_index, counter
    #TODO: mark the semaphores as global here

    items_consumed = 0
    while True:
      if finished == True:# if all producers are done, then we can stop consuming
        break;
      # TODO: use one of the declared semaphores here
      # TODO: use one of the declared semaphores here

      item = buffer[out_index]
      out_index = (out_index + 1) % CAPACITY

      print(f"Consumer {self.id} consumed item : ", item)

      # TODO: don't forget to release the semaphores here accordingly
      time.sleep(0.5)

      items_consumed += 1
    print(f"Consumer {self.id}: Done")
    
      


# Creating Threads

producers = [] # TODO: Modify this line accordingly to create n_producers threads
consumers = [] # TODO: Modify this line accordingly to create n_consumers threads


# start the producers
# Starting Threads
# TODO: Loop through the producers and start them

# TODO: Loop through the consumers and start them

# Waiting for threads to complete
#TODO: loop through the producers and join them using join() function
#TODO: loop through the consumers and join them using join() function

print("Simulation Done")
