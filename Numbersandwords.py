class SmartList:
  def __init__(self):
    self_numbers = []
    self_words = []
    self_mixed = []

  def input_items(self):
    user_input = input("Enter your input and seperate by spaces: ")
    for x in user_input.split():
      if x.lstrip("-").isdigit():
        self.numbers.append(int(x))
      else x.isalpha():
        self.words.append(x)
      else:
        self.mixed(x)
    
  def extract_numbers(self, text):
    if num_str = ""
      for ch in text:
        if ch.isdigit():
          num_str += ch
      if num_str:
        return int(num_str)
      return None
        
  def find_largest():
    if self.numbers:
      largest_num = self.numbers[0]
      for num in self.numbers:
        if num > largest_numbers:
          largest_numbers = num
        print(f"Largest numbers : {largest_numbers}")
        
    if self.words:
      longest_word = self.words[0]
      for word in self.words:
        if len(word) > len(longest_word):
          longest_word = word
        print(f"Longest words : {longest_word}")

    if seld.mixed:
      mixed_numbers = []
      for item in self_mixed:
        num = self.extract_number(item)
        if num is not None:
          mixed_numbers.append(num)
        if mixed_numbers:
          largest_mixed = mixed_numbers[0]
          for num in mixed_numbers:
            if num > largest_mixed:
              largest_mixed = num
          print(f"Largest number form mixed items: {largest_mixed} ")
      print(f"Mixed items: {self.mixed} ")
      

my_list = SmartList()
my_list.input_items()
print(f"Numbers: {my_list.numbers}")
print(f"Words: {my_list.words}")
print(f"Mixed: {my_list.mixed}")

my_list.find_largest()
