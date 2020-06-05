# Standard imports
import sys


class SuppressStdout(object):
    
    def __init__(self, suppress=True):
        self.suppress = suppress
        self.sys_stdout_ref = None

    def __enter__(self):
        self.sys_stdout_ref = sys.stdout
        if self.suppress:
            sys.stdout = self
        return sys.stdout

    def __exit__(self, type, value, traceback):
        sys.stdout = self.sys_stdout_ref

    def write(self):
        pass
