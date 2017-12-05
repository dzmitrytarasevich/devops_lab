import psutil
from datetime import datetime
import configparser
import time


def get_params():
    config = configparser.ConfigParser()
    config.read('settings.ini')

    interval_min = config['common']['interval']
    data_type = config['common']['output']

    return [int(interval_min), str(data_type)]


if __name__ == '__main__':

    interval = get_params()[0]
    type_data = get_params()[1]

    i = 0
    while True:
        i += 1
        time.sleep(interval * 60)

        cpu = psutil.cpu_percent()
        vm = psutil.virtual_memory()
        disk = psutil.disk_io_counters(perdisk=False)
        net = psutil.net_io_counters(pernic=False)
        memory = psutil.swap_memory()
        time_format = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")

        with open('snapshot.log', "a+") as log:
            log.write("| SNAPSHOT " + str(i) + ": " + time_format + '\n')
            log.write("| " + "CPU load: " + str(cpu) + "%" + '\n')
            log.write("| " + "Memory usage: " + str(memory.percent) + "%" + '\n')
            log.write("| " + "VM usage: " + str(vm.percent) + "%" + '\n')
            log.write("| " + "I/O (read/write): " + str(disk.read_count) + " / " + str(disk.write_count) + '\n')
            log.write("| " + "Net (bytes sent/recv): " + str(net.bytes_sent) + " / " + str(net.bytes_recv))
            log.write("\n---------------------------------------------\n")
            log.close()
