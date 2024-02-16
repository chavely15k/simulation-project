import unittest


import sys
import os

sys.path.insert(0, os.getcwd() + '/src')

from event_system import *

class SimulationTest(unittest.TestCase):
    def test_simulate(self):
        sim = simulation(2, get_uniform, get_uniform)
        sim.simulate(10)

if __name__ == '__main__':
    unittest.main()