# my_name = "abc"

def print_name():
    my_name = "abc"
    # global my_name = "abc"        # this will make the scope GLOBAL
    print(my_name)

print_name()

# print("outside", my_name)  # this will give an error because of scope