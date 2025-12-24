from time import sleep


def out_red(text):
    print("\033[31m {}".format(text))


def out_yellow(text):
    print("\033[33m {}".format(text))


def out_green(text):
    print("\033[32m {}".format(text))


class TrafficLight:
    __color = ['red', 'green', 'yellow']

    def running (self):
        while True:
            out_red('RED')
            sleep(7)
            out_yellow('YELLOW')
            sleep(2)
            out_green('GREEN')
            sleep(7)
            out_yellow('YELLOW')
            sleep(2)


TrafficLight = TrafficLight()
TrafficLight.running()