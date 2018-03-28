from serial import *
from multiprocessing import Pool


def single_port_is_available(port_name):
    s = Serial()
    try:
        s.port = port_name
        s.baudrate = 115200
        s.open()
        return True
    except SerialException:
        return False

    finally:
        s.close()


if __name__ == '__main__':
    while True:
        p = Pool(processes=4)
        table = []
        req = ['COM{i}'.format(i=i)for i in range(1, 30)]
        table.append(req)

        res = p.map(single_port_is_available, req)

        table = [[req[i], res[i]] for i in range(len(req))]
        output = list(map(lambda x:x[0], list(filter(lambda item: item[1] is True, table))))
        print(output)