import socket

server = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM, 

)

server.bind (


    ("localhost", 5555)

)

server.listen()


while True:
    user_socket, address = server.accept()
    
    
    def massage_():
        massage = input ("::: ")
            
        user_socket.send(massage.encode("utf-8"))
        massage_()


    massage_()

massage()

    
    
