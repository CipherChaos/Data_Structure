# def test(total):
#     total += 1
#     return total
#
# total = 0
#
# result = test(total)
#
# print(result)
# print(result)
# print(result)


# class Counter:
#     def __init__(self):
#         self.total = 0
#     def increment(self):
#         self.total += 1
#         return self.total
#
#
# counter = Counter()
#
# print(counter.increment())
# print(counter.increment())
# print(counter.increment())


def outer(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return inner

@outer
def test(n):
    n += 1
    return n

f = test(2)

counter = outer(f)

# print(counter())
# print(counter())
# print(counter())



print(test(1))

