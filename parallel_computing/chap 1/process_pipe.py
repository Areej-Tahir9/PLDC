from multiprocessing import Process, Queue

def producer(queue):
    for i in range(5):
        queue.put(i)

if __name__ == "__main__":
    queue = Queue()
    process = Process(target=producer, args=(queue,))
    process.start()
    process.join()

    while not queue.empty():
        print(queue.get())