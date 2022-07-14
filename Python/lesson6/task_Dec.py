from time import time

def timeit(n):
    

    def wrapper(*args, **kwargs):
        t1 = time()
        result = n (*args, **kwargs)
        end = time()-t1
        return result, end
    return wrapper

@timeit
def sum(n = 5):            
    return 1
print(time())
print()


def myrange():
    for i in range(1, 10, 2):
        yield i
gen = myrange()
for i in gen:
    print(i)
    print(i)
print()





    




