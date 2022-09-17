

from collections import deque
from math import sqrt


class Animator:
    
    def __init__(self, framerate):
        self.framerate = framerate
        self.transformQueue = deque()# (object, transformRequest, doneCheck)

    
    def lerp(self, object, destination, time):
        x_step,y_step = self.getLerpValues(object.coordinates,destination, time)
        #print(f"x:{x_step},y:{y_step}")
        self.transformQueue.append((object, lambda: object.translatePosition(x_step,y_step), \
                                            lambda: abs(object.coordinates[1] - destination[1])<1 and abs(object.coordinates[0] - destination[0])<1,\
                                            lambda: object.updatePosition(destination)))

    def getLerpValues(self, pointA, pointB, time):
        
        x_delta = pointB[0]-pointA[0]
        y_delta = pointB[1]-pointA[1]

        x_speed = x_delta / time / self.framerate
        y_speed = y_delta / time / self.framerate

        return (x_speed, y_speed)

    def update(self):
        cleanup=[]
        for i,transformInstructions in enumerate(self.transformQueue):
            object,transform,completionCriteria,postOP = transformInstructions
            if not completionCriteria():
                transform()
            else:
                postOP()
                cleanup.append(i)
        
        for i in cleanup:
            del self.transformQueue[i]
            

        
