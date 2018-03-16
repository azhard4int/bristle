import os
import psutil
from redis import Redis
from queue import Queue


def get_queue():
    """Generic queue method that will be used in all the workers."""
    queue_item = Queue(1000)
    for i in range(0, 1000):
        queue_item.put('https://bing.com')

    return queue_item


def get_process_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss
