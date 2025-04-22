from waitress import serve
from CAMS.wsgi import application
import socket

def get_local_ip():
    return socket.gethostbyname(socket.gethostname())
if __name__ == '__main__':
    if get_local_ip()!=None:
        print("This project is already accessible on "+get_local_ip()+":8000.")
    serve(application, host='0.0.0.0', port=8000, threads=4)
