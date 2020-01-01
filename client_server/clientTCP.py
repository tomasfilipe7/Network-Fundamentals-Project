import socket
import signal
import sys
import psutil

def signal_handler(sig, frame):
    print('\nDone!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

##

ip_addr = "127.0.0.2"
tcp_port = 5006

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((ip_addr, tcp_port))

while True:
    usage = psutil.cpu_percent(interval=2,percpu=False)
    v_mem = psutil.virtual_memory()[2]

    print(usage)
    print(v_mem)
    print(psutil.cpu_count())

    message_text = "\n CPU USAGE: " + str(usage) + "%" + "\n Memory usage: " + str(v_mem) + "%"; 
    
    try: 
        message=message_text.encode()
        if len(message)>0:
            sock.send(message)
            response = sock.recv(4096).decode()
            print('Server response: {}'.format(response))
    except (socket.timeout, socket.error):
        print('Server error. Done!')
        sys.exit(0)

