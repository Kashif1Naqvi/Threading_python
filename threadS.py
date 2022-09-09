import time 
import threading
import concurrent.futures

img_urls = [
    "https://images.unsplash.com/photo-1662578108849-6f75d4f8c280",
    "https://images.unsplash.com/photo-1657664049378-c8aadfe323f1",
    "https://images.unsplash.com/photo-1662622194548-f50b20179287"
]

threads = []

def do_something(seconds):
    print(f"sleeping start {seconds}.....second(s)")
    time.sleep(seconds)
    return f"sleeping Done {seconds}.....second(s)"


# execute thread more easily 
with concurrent.futures.ProcessPoolExecutor() as executor:
    
    # executor with submit method

    # f1 = executor.submit(do_something, 1)
    # print(f1.result())
    
    secs = [5, 4, 3, 2, 1]
    
    # retrun the start time of thread after some seconds return done thread.
    
    results = executor.map(do_something, secs)

    for result in results:
        print(result)
    
    # diffrent ways of itterations 

    # results = [executor.submit(do_something, 1) for _ in range(10)]
    # results = [executor.submit(do_something, sec) for sec in secs]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

# for _ in range(10):
#     t1 = threading.Thread(target=do_something, args=[1.5])

#     t1.start()
#     threads.append(t1)

# for thread in threads:
#     thread.join()


# do_something()


finish = time.perf_counter()
print("Task is done in {0} second(s)".format(round(finish, 2)))
