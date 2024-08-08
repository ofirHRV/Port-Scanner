import pyfiglet
import socket
import sys
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("Port Scanner")  # banner
print(ascii_banner)

target = input("Enter a host to scan: ")  # The hosts domain name (or IP address) to scan
host = socket.gethostbyname(target)

file = open("Port-Scanner.txt", "w")  # open file to save the results to
file.write(ascii_banner)  # add banner to file

print(f"\n{'Target: ' : <10}{target : >10}")  # show chosen host name (or IP address)
file.write(f"\n{'Target: ' : <10}{target : >10}\n")  # add to file
print(f"{'Host: ' : <10}{host : >10}")  # show host name's IP address
file.write(f"{'Host: ' : <10}{host : >10}\n")  # add to file

date1 = datetime.date(datetime.now())  # start sate
t1 = datetime.now()  # start time

print(f"\n{'Start date:' : <20}{str(date1) : >20}")  # show start date
file.write(f"\n{'Start date:' : <20}{str(date1) : >20}\n")  # add to file
print(f"{'Start time:' : <20}{str(t1.strftime('%H:%M:%S')) : >20}\n\n")  # show start time
file.write(f"{'Start time:' : <20}{str(t1.strftime('%H:%M:%S')) : >20}\n\n\n")  # add to file

print(f"{'Port number' : <20}{'State' : ^20}{'Service' : >20}\n")
file.write(f"{'Port number' : <20}{'State' : ^20}{'Service' : >20}\n\n")  # add to file

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 addresses, TCP Stream
        sock.settimeout(0.001)  # time out for port state check

        result = sock.connect_ex((host, port))  # get port state
        if result == 0:  # if port is open
            try:
                print(f"{str(port) : <20}{'Open' : ^20}{socket.getservbyport(port, 'tcp') : >20}")
                # show port number, state and service type
                file.write(f"{str(port) : <20}{'Open' : ^20}{socket.getservbyport(port, 'tcp') : >20}\n")  # add to file
            except socket.error:
                print(f"{str(port) : <20}{'Open' : ^20}{'Unknown' : >20}")
                file.write(f"{str(port) : <20}{'Open' : ^20}{'Unknown' : >20}\n")  # add to file

# error handling
except socket.gaierror:
    print("Host name could not resolved. Exiting")
    file.write("Host name could not be found. Exiting..\n")  # add to file
    file.close()
    sys.exit()
except socket.error:
    print("Couldn't connect to server. Exiting..")
    file.write("Couldn't connect to server. Exiting..\n")  # add to file
    file.close()
    sys.exit()

date2 = datetime.date(datetime.now())  # start sate
t2 = datetime.now()  # end time
total_time = t2 - t1  # total time

print(f"\n\n{'End date:' : <20}{str(date2) : >20}")  # show start date
file.write(f"\n\n{'End date:' : <20}{str(date2) : >20}\n")  # add to file
print(f"{'End time:' : <20}{str(t2.strftime('%H:%M:%S')) : >20}")  # show end date
file.write(f"{'End time:' : <20}{str(t2.strftime('%H:%M:%S')) : >20}\n")  # add to file
print(f"{'Total time:' : <20}{str(total_time) : >20}")  # show total time
file.write(f"{'Total time:' : <20}{str(total_time) : >20}\n")  # add to file

file.close()
