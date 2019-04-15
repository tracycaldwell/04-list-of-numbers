#Assume you have a list of numbers ``nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]``
nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]

def print_each_number():
    # Write a loop that prints each of the numbers on a new line, like this:
    # 12
    # 10
    # ...etc
    # TODO - Write your code below this line.  (Keep the indentation)
    for nums1 in (12, 10, 32, 3, 66, 17, 42, 99, 20):
        print(nums1)

    

def print_each_number_and_its_square():
    # Write a second loop that prints each number and its square on a new line
    # precisely like this:
    #
    # The square of 12 is 144
    # The square of 10 is 100
    # ...etc
    # TODO - Write your code below this line.  (Keep the indentation)
    for nums2 in (12, 10, 32, 3, 66, 17, 42, 99, 20):
        x = int(nums2)
        y = (int(nums2))**2
        print("The square of", x, "is", y)
