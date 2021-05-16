import socket



client = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM, 
)

client.connect(

    ("192.168.1.80", 1234)
)



while True:

    data = client.recv(2048)
    
    command = data.decode("utf-8")
    print (data.decode("utf-8"))

G = input ("")




    
    
