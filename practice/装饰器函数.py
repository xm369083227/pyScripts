import time

def timmer(func):
    def deco():
        start_time = time.time()
        time.sleep(1)
        func()
        stop_time = time.time()
        total_time = stop_time - start_time
        print("the function has used time",total_time)
    return deco

@timmer
def test(): #test=timmer(test)--->return deco   test()== deco()
    print("this is a test")

test()



