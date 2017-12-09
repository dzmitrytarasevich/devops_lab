import psutil
from datetime import datetime
import configparser
import time


class Mon(object):
    def __init__(self, name):
        self.name = name
        self.cpu = Mon(psutil.cpu_percent())
        self.vm = Mon(psutil.virtual_memory())
        self.disk = Mon(psutil.disk_io_counters(perdisk=False))
        self.net = Mon(psutil.net_io_counters(pernic=False))
        self.memory = Mon(psutil.swap_memory())
        self.time_format = Mon((datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")))


def get_set():
    config = configparser.ConfigParser()
    config.read('settings.ini')

    interval_min = config['common']['interval']
    data_type = config['common']['output']

    return [int(interval_min), str(data_type)]


if __name__ == '__main__':
    interval = get_set()[0]
    type_data = get_set()[1]
    i = 0
    while True:
        i += 1
        time.sleep(interval)
        with open('snapshot.log', "a+") as log:
            log.write("| SNAPSHOT " + str(i) + ": " + str(time_format) + '\n')
            log.write("| " + "CPU load: " + str(cpu) + "%" + '\n')
            log.write("| " + "Memory usage: " + str(memory) + "%" + '\n')
            log.write("| " + "VM usage: " + str(vm) + "%" + '\n')
            log.write("| " + "I/O (read/write): " + str(disk) + '\n')
            log.write("| " + "Net (bytes sent/recv): " + str(net))
            log.write("\n---------------------------------------------\n")
            log.close()
