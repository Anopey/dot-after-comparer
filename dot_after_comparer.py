checked_file_path = input("ener the path to file you would like checked: ")
comparison_file_path = input("enter path to base comparison file: ")

checked_file = open(checked_file_path, "r")
comparison_file = open(comparison_file_path, "r")

checked =  checked_file.read()
comparison = comparison_file.read()

before_dot = input("what should come before dot?")
ending_character = input("what should be the character sequence to end it? enter /endofline to indicate until end of line.")


if(ending_character == "/endofline"):
    ending_character = "\n"

valid = []

for i in range(0, len(comparison)):
    
