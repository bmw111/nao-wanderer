'''
Created on Feb 18, 2013

@author: dsnowdon
'''

import unittest

from naoutil.general import object_to_name
from naoutil.jsonobj import to_json_string, from_json_string
from wanderer.event import *

class Test(unittest.TestCase):
    def test_start_json(self):
        ev = Start()
        self.json_serialisation(ev)

    def test_obstacle_detected_json(self):
        sensors = Sensors({'LeftBumper' : True, 
                           'RightBumper' : False, 
                           'LeftSonar' : 0.25, 
                           'RightSonar' : 0.8})
        ev = ObstacleDetected('LeftBumper', sensors)
        self.json_serialisation(ev)

    def json_serialisation(self, ev):
        json = to_json_string(ev)
        print "Serialisation of "+object_to_name(ev)+" = \n"+json
        self.assertIsNotNone(json, "Serialised object should not be None")
        rev = from_json_string(json)
        self.assertTrue(isinstance(rev, ev.__class__))
        self.assertEqual(ev, rev, "Reconstituted object "+repr(rev)+" must equal original "+repr(ev))

if __name__ == '__main__':
    unittest.main()
