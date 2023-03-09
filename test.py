import time
from pyModbusTCP.client import ModbusClient

c = ModbusClient(host='192.168.1.30', port=502, auto_open=True, debug=False)


out1 = 16
out2 = 17
out3 = 18
out4 = 19
out5 = 20
out6 = 21
out7 = 22


def reset():
    c.write_single_coil(out1, 0)
    time.sleep(0.2)
    c.write_multiple_coils(out3, [0, 0])
    time.sleep(0.5)
    c.write_single_coil(out6, 0)
    time.sleep(1)
    c.write_single_coil(out2, 0)
    time.sleep(0.8)
    c.write_single_coil(out5, 0)

def task_start():
    c.write_single_coil(out1, 1)
    time.sleep(1)
    c.write_single_coil(out3, 1)
    c.write_single_coil(out4, 1)
    time.sleep(0.5)
    c.write_single_coil(out6, 1)
    time.sleep(0.5)

    c.write_single_coil(out6, 0)
    time.sleep(0.1)
    c.write_single_coil(out2, 1)
    time.sleep(0.3)
    c.write_single_coil(out2, 0)
    time.sleep(0.1)

def task_pause():
    c.write_single_coil(out1,1)
    time.sleep(0.5)
    c.write_single_coil(out5, 0)
    time.sleep(0.4)
    c.write_single_coil(out3,0)



def task_stop():
    reset()
def task_resume():
    c.write_single_coil(out1,1)
    time.sleep(0.5)
    # c.write_single_coil(out2,0)
    c.write_single_coil(out3,1)
    time.sleep(0.5)
    c.write_single_coil(out5,1)
    time.sleep(0.5)
    c.write_single_coil(out5,0)


# reset()
# time.sleep(3)
# task_start()
# task_resume()
# task_pause()
task_stop()