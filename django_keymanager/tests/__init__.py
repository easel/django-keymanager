from django.utils import unittest

from . import agent

def suite():
    return unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(agent.AgentTestCase)
        ])
