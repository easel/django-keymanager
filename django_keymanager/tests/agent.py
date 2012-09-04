from django.utils import unittest
from ..agent import Agent

class AgentTestCase(unittest.TestCase):
    def setUp(self):
        self.agent = Agent()

    def tearDown(self):
        print "tearDown"

    def test_agent_can_start_stop(self):
        "ensure the agent can be started"
        if self.agent.is_running():
            self.assertTrue(self.agent.stop())
        self.assertTrue(self.agent.start())
        self.assertTrue(self.agent.is_running())
        self.assertTrue(self.agent.stop())
        self.assertFalse(self.agent.is_running())
