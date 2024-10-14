# # Alternative way to set up.
# import tkinter
# window = tkinter.Tk()

# ----------------------------------------------
def say_something(thing):
    print(thing)

window.after(1000, say_something, "Hello")

# ----------------------------------------------
def say_something(a,b,c):
    print(a)
    print(b)
    print(c)

window.after(1000, say_something, 3,5,8)

# ----------------------------------------------
def count_down(count):
    # After 1000ms, call the function count_down and pass in count - 1.
    window.after(1000, count_down, count - 1)
count_down(5)

# ----------------------------------------------
