from time import time;

two_minute = time() + 20;

while True:
    timeout = time() + 5;
    while time() < timeout:
        pass;

    print('out');

    if time() > two_minute:
        break;

