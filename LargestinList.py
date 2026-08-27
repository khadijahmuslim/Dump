# find the largest numbers in lists

class NumberList:
  def __init__(self):
    self.numbers = []

  def input_numbers(self):
    user_input = input("Enter your number seperate by spaces: ")
    self.numbers = [int(x) for x in user_input.split()]

  def find_largest(self):
    largest = self.numbers[0]
    for num in self.numbers:
      if num > largest:
        largest = num
    return largest

my_list = NumberList()
my_list = input_numbers()
print(f"List: {my_list.numbers}")
print(f"Largest numbers: {my_list.find_largest()}")
