import signal
import sys
import time


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
    # print('Press Ctrl+C')
    time.sleep(1)
    # signal.pause()
