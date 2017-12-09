import psutil
from datetime import datetime
import configparser
import time


def get_params():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    interval_min = config['common']['interval']
    data_type = config['common']['output']
    counter = config['common']['counter']
    return [int(interval_min), str(data_type), int(counter)]


class Mon(object):
    def __init__(self):
        self.cpu = psutil.cpu_percent()
        self.memory = psutil.virtual_memory()[3] / 1024
        self.swap = psutil.swap_memory()[1] / 1024
        self.disk_r = psutil.disk_io_counters(perdisk=False)[2] / 1024
        self.disk_w = psutil.disk_io_counters(perdisk=False)[3] / 1024
        self.net_sent = psutil.net_io_counters(pernic=False)[0] / 1024
        self.net_recv = psutil.net_io_counters(pernic=False)[1] / 1024
        self.time_format = (datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"))
        self.counter = counter

    def text(self):
        result = (
               '| SNAPSHOT {0} - {1} \n'
               '| CPU load: {2}% \n'
               '| Memory usage: {3}kb \n'
               '| Swap usage: {4}kb \n'
               '| Disk read: {5}kb \n'
               '| Disk write: {6}kb \n'
               '| Net in: {7}kb \n'
               '| Net out: {8}kb \n'
               '----------------------------\n'.format(self.counter, self.time_format, self.cpu,
                                                       self.memory, self.swap, self.disk_r,
                                                       self.disk_w, self.net_sent, self.net_recv))

        with open('snapshot.log', "a+") as log:
            log.write(result)
            log.close()


if __name__ == '__main__':

    interval = get_params()[0]
    type_data = get_params()[1]
    counter = get_params()[2]

    counter = 0
    while True:
        counter += 1
        time.sleep(interval * 60)
        writer = Mon()
        writer.text()
