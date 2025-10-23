import os
from math import cos, sin, pi, floor
import pygame
from adafruit_rplidar import RPLidar

pygame.init()
lcd = pygame.display.set_mode((1280,720))
pygame.mouse.set_visible(False)
lcd.fill((0,0,0))
pygame.display.update()

PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME)

max_d = 0

def process_data(data):
    global max_d
    lcd.fill((0,0,0))
    for angle in range(360):
        dist = data[angle]
        if dist > 0:
            max_d = max([min([5000, dist]), max_d])
            rads = angle * pi / 180.0
            x = dist * cos(rads)
            y = dist * sin(rads)
            point = (640 + int(x / max_d * 239), 360 + int(y / max_d * 239))
            lcd.set_at(point,pygame.Color(255,255,255))
    pygame.display.update()

scan_data = [0]*360
try:
    print(lidar.info)
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            scan_data[min([359,floor(angle)])] = distance
        process_data(scan_data)
except KeyboardInterrupt:
    print('Stopping.')
lidar.stop()
lidar.disconnect()
