from time import sleep
from pySerialTransfer import pySerialTransfer as txfer

if __name__ == '__main__':
    try:
        link = txfer.SerialTransfer('COM1')

        link.open()
        sleep(2)  # allow some time for the Arduino to completely reset



        while not link.available():
            if link.status < 0:
                print('ERROR: {}'.format(link.status))

        print('Response received:')

        response = ''
        for i in range(200):
            for index in range(link.bytesRead):
                response += chr(link.rxBuff[index])

        print(response)
        link.close()

    except KeyboardInterrupt:
        link.close()