def my_function():
    print("Hi")


my_function()


def another_function(a):
    print(f"1: {a}")
    a += 5
    print(f"2: {a}")


a = 12
another_function(a)
print(a)


def next_function(a):
    print(f"1: {a}")
    a[0] = 99
    print(f"2: {a}")


a = [0, 1, 2, 3, 4]
next_function(a)
print(a)

# integers are not mutable
