import socket

def run_client():
    # 1. Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Connect to the server's address and port
    client.connect(('localhost', 8080))
    
    print("Successfully connected to the server!")
    
    # 3. Close the connection
    client.close()

if __name__ == "__main__":
    run_client()
