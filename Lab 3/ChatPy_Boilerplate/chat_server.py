import socket
import threading

# TODO: create an empty list that will store 
# new clients connections

# TODO: Complete the implementation of the class named ClientThread that will
# contain the logic of each client. Each client should
# be able to exchange messages with the server. 
class ClassThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr
    
    #The function will contain the logic of each client
    #connected to the server. "run()" function will be called after you create 
    #a new instance of the ClientThread and calling the "start()" function.
    def run():
        while True:
            # TODO: remove the "pass" keyword before modifiying this function
            pass
            # TODO: receive data stream from client. 
            # it won't accept data packet greater than 1024 bytes

            # TODO: if no data is received from the client, break this loop

            # TODO: print the data received from the client

            # TODO: now it's the server's turn to reply to the client's message.
            # take input from the console screen using "input()" function then, send
            # the message to the client using "self.conn.send()" function. 
        
        # TODO: close the connection "self.conn" and remove it from the list
        #that stores all the client's connections. 





def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(100)

    # TODO: this line should be written somewhere else. Try to figure it out!
    conn, address = server_socket.accept()  # accept new connection
    # TODO: this line should be written somewhere else. Try to figure it out!
    print("Connection from: " + str(address))
    while True:
        # TODO: this line shouldn't be here!
        data = conn.recv(1024).decode()
        # TODO: this if condition shouldn't be here!
        if not data:
            # if data is not received break
            break
        # TODO: these lines shouldn't be here
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

        # TODO: create a new instance of ClientThread

        # TODO: add the newly created instance to the client's list

        # TODO: start the thread of the newly created instance of 
        # ClientThread using "start()" function. 

    # TODO: this line shouldn't be here!
    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()


