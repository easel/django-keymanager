import os 
from subprocess import call, PIPE, Popen

from . import logger

class Agent(object):
    "simple gpg key agent wrapper"

    def __init__(self):
        "set up the agent properties"
        self.HOME_DIR=os.path.join(os.environ['HOME'], ".gnupg")
        self.AGENT_ENV_FILE=os.path.join(self.HOME_DIR, "env.sh")
        self.AGENT_BINARY="gpg-agent"

    def start(self):
        "start the agent"
        cmd = (self.AGENT_BINARY, '--homedir', self.HOME_DIR,
               '--daemon', '--write-env-file', self.AGENT_ENV_FILE)
        logger.debug("starting agent with %s" %(" ". join(cmd)))
        return call(cmd) == 0 and self.is_running()

    def stop(self):
        "stop the agent"
        if self.is_running() and self.pid:
            logger.debug('pid %d is running, attempting to stop' %(self.pid))
            os.kill(self.pid, 15)
            os.unlink(self.AGENT_ENV_FILE)
        return not self.is_running()

    def is_running(self):
        "check if the agent is running"
        if not os.path.exists(self.AGENT_ENV_FILE):
            logger.debug('env file %s missing, gpg-agent not running'%(
                self.AGENT_ENV_FILE))
            return False
        agent_env = file(self.AGENT_ENV_FILE).read()
        logger.debug('env file %s exists, containing %s'%(
            self.AGENT_ENV_FILE, agent_env))
        self.pid = int(agent_env.split(':')[1])
        cmd = 'ps -ax | grep "^\s*%d"' %(self.pid)
        logger.debug('checking for pid %d by running %s' %(self.pid, cmd))
        is_running = call(cmd, shell=True) == 0
        logger.debug('checked for pid %d, is_running=%s' %(self.pid, is_running))
        return is_running
