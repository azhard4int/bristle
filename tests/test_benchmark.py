import unittest
import cProfile
from time import time

from memory_profiler import profile
from bristle.threads import run_with_join_threads, run_directly


class TestThreads(unittest.TestCase):
    def test_thread_benchmark(self):
        run_with_join_threads()

        # start_time = time()
        # run_directly()
        # completed_time = time() - start_time
        # print('The completion time is {0}'.format(completed_time))
