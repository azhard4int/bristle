import requests
import gc
from time import time
from memory_profiler import profile
from threading import Thread, current_thread
from bristle._internal import get_queue, get_process_memory


def initiate_requests(queue):
    item = queue.get()
    # print(current_thread())
    print(requests.get(item).status_code)
    gc.collect()
    # print(get_process_memory() / 1024)


def run_with_join_threads():
    start_time = time()
    queue = get_queue()
    while queue.qsize() > 5:
        thread_list = []
        for i in range(1, 15):
            worker = Thread(target=initiate_requests, args=(queue,))
            thread_list.append(worker)

        print('Memory before start is {0}'.format(get_process_memory()/1024))

        for worker in thread_list:
            worker.start()

        print('Memory after start is {0}'.format(get_process_memory() / 1024))

        for worker in thread_list:
            worker.join()

        print('Memory after join is {0}'.format(get_process_memory() / 1024))
        # print('workers joined again...')
    completed_time = time() - start_time
    print('The completion time is {0}'.format(completed_time))


def initiate_direct_requests(queue):
    while queue.qsize() > 5:
        item = queue.get()
        print(current_thread())
        print(requests.get(item).status_code)
        print(get_process_memory() / 1024)


def run_directly():
    start_time = time()
    queue = get_queue()
    thread_list = []
    for i in range(1, 15):
        worker = Thread(target=initiate_direct_requests, args=(queue,))
        thread_list.append(worker)

    for worker in thread_list:
        worker.start()
    completed_time = time() - start_time
    print('The completion time is {0}'.format(completed_time))
