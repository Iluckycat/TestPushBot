from pytest import main
from tests.test_mock_server import TestMockServer
import os
import time

def start_run():
    main(['{}::{}'.format(__file__, TestMockServer.__name__)])
    # os.remove(".pytest_cache/v/cache/lastfailed")

