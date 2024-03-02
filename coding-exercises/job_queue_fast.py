# python3
import random
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
JobThread = namedtuple("JobThread", ["id", "next_free_time"])

class Heap(object):
    def __init__(self, heap_capacity):
        self.heap = [None] * heap_capacity
        self.size = 0

    def extract_min(self):
        if self.size:
            next_min = self.heap[0]
            self.heap[0] = self.heap[self.size - 1]
            self.size -= 1

            self._sift_down(0)

            return next_min

    def insert(self, job_thread):
        self.heap[self.size] = job_thread
        self.size += 1
        self._sift_up(self.size - 1)

    def _sift_up(self, index):
        parent = (index - 1) // 2 
        # if next_free time is the same promote the one with the smallest ID
        while index > 0 and parent >= 0 and (self.heap[parent].next_free_time > self.heap[index].next_free_time or 
            (self.heap[parent].next_free_time == self.heap[index].next_free_time and self.heap[parent].id > self.heap[index].id)):
            parent = (index - 1) // 2
            temp = self.heap[index]
            self.heap[index] = self.heap[parent]
            self.heap[parent] = temp

            index = parent
            parent = (index - 1) // 2 

    def _sift_down(self, index):
        # if next free time is the same, demote the one with the largest ID
        min_index = index
        left_child = 2 * index + 1
        if left_child < self.size:
            if self.heap[left_child].next_free_time < self.heap[min_index].next_free_time:
                min_index = left_child
            if self.heap[left_child].next_free_time == self.heap[min_index].next_free_time and self.heap[left_child].id < self.heap[min_index].id:
                min_index = left_child

        right_child = 2 * index + 2
        if right_child < self.size:
            if self.heap[right_child].next_free_time < self.heap[min_index].next_free_time:
                min_index = right_child
            if self.heap[right_child].next_free_time == self.heap[min_index].next_free_time and self.heap[right_child].id < self.heap[min_index].id:
                min_index = right_child

        if min_index != index:

            temp = self.heap[index]
            self.heap[index] = self.heap[min_index]
            self.heap[min_index] = temp

            self._sift_down(min_index)

def assign_jobs(n_workers, jobs):
    # Make the heap
    thread_heap = Heap(n_workers)
    for worker in range(n_workers):
        thread_heap.insert(JobThread(worker, 0))

    result = []
    for job in jobs:
        next_worker = thread_heap.extract_min()
        result.append(AssignedJob(next_worker.id, next_worker.next_free_time))
        thread_heap.insert(JobThread(next_worker.id,  next_worker.next_free_time + job))

    return result

def assign_jobs_slow(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    #assigned_jobs_slow = assign_jobs_slow(n_workers, jobs)
    assigned_jobs = assign_jobs(n_workers, jobs)

    #for i in range(n_jobs):
    #    if assigned_jobs_slow[i] != assigned_jobs[i]:
    #        print("stop")
    #        print(n_workers)
    #        print(n_jobs)
    #        print(jobs)

    #        print(assigned_jobs_slow[i], assigned_jobs[i])
    #        for job in assigned_jobs_slow:
    #           print(job.worker, job.started_at)

    #        print("XXX")
    #        for job in assigned_jobs:
    #           print(job.worker, job.started_at)

    #        break

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
