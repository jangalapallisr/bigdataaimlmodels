# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

@profile
# @profile(precision=4)
def my_func():
    a = [1] * (10 ** 3)
    print(a)
    b = [2] * (2 * 10 ** 2)
    print(b)
    del b
    return a

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    my_func()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
