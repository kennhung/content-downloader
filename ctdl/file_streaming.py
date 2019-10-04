from downloader import download
import socket,os
import threading
import pickle

class socketHandler(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket

    def run(self):
        socket = self.socket
        data_dict = pickle.loads(socket.recv(1024))
        url = data_dict["url"]
        download(url, wirter=socket)
        socket.close()


class socketListener(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port


    def run(self):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.bind(('', self.port))
        soc.listen(10)
        while True:
            client, addr = soc.accept()        
            print('{} connected.'.format(addr))
            sh = socketHandler(client)
            sh.start()


def main():
    pid = os.getpid()
    port = 8080
    sl = socketListener(port)
    sl.start()
    input('Socket is listening, press any key to abort...')
    os.kill(pid,9)


if __name__ == "__main__":
    main()