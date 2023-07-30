import os
from pytest import main
from tests.test_mock_server import TestMockServer
import sys
import importlib
import time
def start_run():
    #TestMockServer = importlib.reload(sys.modules['tests.test_mock_server']).TestMockServer
    main = importlib.reload(sys.modules['pytest']).main
    main(['{}::{}'.format(__file__, TestMockServer.__name__)])

