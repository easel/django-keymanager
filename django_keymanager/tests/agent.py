from django.utils import unittest

class AgentTestCase(unittest.TestCase):
    def setUp(self):
        print "setUp"

    def tearDown(self):
        print "tearDown"

    def test_agent_started(self):
        "ensure the agent can be started"
        print "test can be started"
