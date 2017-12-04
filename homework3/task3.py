import psutil
from datetime import datetime

cpu = psutil.cpu_percent(interval=1)
vm = psutil.virtual_memory()
disk = psutil.disk_io_counters(perdisk=False)
net = psutil.net_io_counters(pernic=False)
memory = psutil.swap_memory()
time = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
with open('/opt/log.txt', "a") as log:
    log.write(time + " | " + "CPU load: " + str(cpu) + "%" + '\n')
    log.write(time + " | " + "Memory usage: " + str(memory.percent) + "%" + '\n')
    log.write(time + " | " + "VM usage: " + str(vm.percent) + "%" + '\n')
    log.write(time+" | "+"I/O info: "+"Read count: "+str(disk.read_count)+" Write count: "+str(disk.write_count)+'\n')
    log.write(time + " | " + "Net (bytes sent/recv): " + str(net.bytes_sent) +"/" + str(net.bytes_recv) + '\n')
    log.write("---------------------------------------------" + '\n')