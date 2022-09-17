

from collections import deque
from math import sqrt
from src.EventSystem import Event, EventSystem

class Animator:
    
    def __init__(self, framerate):
        self.framerate = framerate
        #self.transformQueue = deque()# (object, transformRequest, doneCheck)
        self.transformQueue = EventSystem()
    
    def lerp(self, object, destination, time):
        x_step,y_step = self.getLerpValues(object.coordinates,destination, time)
        lerpEvent = Event(
            action=lambda: object.translatePosition(x_step,y_step), \
            finishFlag=lambda: abs(object.coordinates[1] - destination[1])<1 and abs(object.coordinates[0] - destination[0])<1,\
            postOP=lambda: object.updatePosition(destination))
        # lerpEvent = Event(
        #     action=lambda: object.translatePosition(x_step,y_step), \
        #     finishFlag=lambda: abs(object.coordinates[1] - destination[1])<1 and abs(object.coordinates[0] - destination[0])<1)
        self.transformQueue.push(lerpEvent)

    def getLerpValues(self, pointA, pointB, time):
        
        x_delta = pointB[0]-pointA[0]
        y_delta = pointB[1]-pointA[1]

        x_speed = x_delta / time / self.framerate
        y_speed = y_delta / time / self.framerate

        return (x_speed, y_speed)

    def update(self):
        self.transformQueue.update()
            

        
