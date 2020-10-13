#import par
#import pmath

import sys
import time

class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I'm going {} kph!".format(self.speed))

    def accelerate(self):
        self.speed += 5


    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass


if __name__ == '__main__':

    my_car = Car()
    print("I'm a car!")
    print("Python version")
    print(sys.version)
    time.sleep(1)
    #sleep(120)
    f = open("myfile.txt", "w")
    f.write("Woops!!")
    f.close()
    msg = "##teamcity[publishArtifacts 'myfile.txt']"
    print(msg)
    print("I am a loooooooooooooooooooooooooong loooooooooooooooooooooooooong loooooooooooooooooooooooooong loooooooooooooooooooooooooong python line")
    if (1 > 1) or (1 > 1) or (1 > 1) or (1 > 1) or (1 > 1) or (1 > 1) or (1 > 1) or (1 > 1) or (1 > 1) or (1 > 1):
        print("a")
