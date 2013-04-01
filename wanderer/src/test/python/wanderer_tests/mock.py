'''
Created on Feb 11, 2013

@author: dsnowdon
'''

from naoutil.naoenv import NaoEnvironment

class MockBox(object):
    def __init__(self):
        super(MockBox, self).__init__()

    def log(self, msg):
        print msg

class MockMemory(object):
    def __init__(self):
        super(MockMemory, self).__init__()
        self.values = { }

    def getData(self, name):
        try:
            return self.values[name]
        except KeyError:
            return None
    
    def insertData(self, name, value):
        self.values[name] = value

class MockMotion(object):
    def __init__(self):
        super(MockMotion, self).__init__()
    def getPosition(self, thing, frame, useSensors):
        return [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        
def make_mock_environment():
    return NaoEnvironment(MockBox(),
                          MockMemory(), 
                          MockMotion(), 
                          None)

class MockActionExecutor(object):
    def __init__(self):
        super(MockActionExecutor, self).__init__()
        self.allDoneCount = 0
        self.actions = []
    
    def do_action(self, action):
        self.actions.append(action)
        print "MockActionExecutor.do_action() : "+repr(action)
    
    def all_done(self):
        self.allDoneCount = self.allDoneCount + 1
        print "MockActionExecutor.all_done()"