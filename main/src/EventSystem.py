from collections import deque

class Event:

    def __init__(self, action, postOP=None, finishFlag=lambda: True):
        '''if finish flag is true, this event is a single event. else action runs until finished. postOP func happens on exit'''
        self.action = action
        self.finishFlag = finishFlag
        self.postOP = postOP

    def run(self):
        '''runs an action and returns whether it has been completed or not'''
        self.action()
        return self.finishFlag()
    

class EventSystem:

    def __init__(self):
        self.event_queue = deque()

    def push(self, event):
        self.event_queue.append(event)

    def update(self):

        cleanup = []
        for i in range(len(self.event_queue)):
            event = self.event_queue[i]
            flag = event.run()
            if flag:
                if event.postOP:
                    event.postOP()

                cleanup.append(event)

        
        for e in cleanup:
            self.event_queue.remove(e)