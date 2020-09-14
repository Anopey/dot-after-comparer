checked_file_path = input("enter the path to file you would like checked: ")
comparison_file_path = input("enter path to base comparison file: ")

checked_file = open(checked_file_path, "r")
comparison_file = open(comparison_file_path, "r")

checked =  checked_file.read()
comparison = comparison_file.read()

before = input("what should come before?")
ending_sequence = input("what should be the character sequence to end it? enter /endofline to indicate until end of line.")


if(ending_sequence == "/endofline"):
    ending_sequence = "\n"

valid = []

comparison_len = len(comparison)
found = False
currentFound = ""

for i in range(0, comparison_len):
    if(comparison[i] == before[0]):
        found = False
        for j in range (1, len(before)): #check if before is here
            if(j + i > comparison_len):
                break #reached end of file before desired sequence ended.
            if(comparison[i + j] == ending_sequence[0]): #doing it this way also makes it so that those without ending sequences dont work.
                ending_sequence_len = len(ending_sequence)
                for q in range(1, ending_sequence_len):
                    if (j + i + q > comparison_len):
                        found = False
                        break
                    if comparison[i + j + q] != ending_sequence[q]:
                        break
                    if q == ending_sequence_len - 1:
                        found = True
                        break
                if found:
                    break #Break out of second one.

            if(comparison[i + j] != before[j]):
                found = False
                break

            currentFound += comparison[i+j]
        if found: #found :o
            valid.append(currentFound)
        else: #not found :/
            currentFound = ""

checked_len = len(checked)
current_line = 0

for i in range(0, checked_len):
    if checked[i] == '\n':
        current_line += 1
    if(checked[i] == before[0]):
        found = False
        for j in range (1, len(before)): #check if before is here
            if(j + i > checked_len):
                break #reached end of file before desired sequence ended.
            if(checked[i + j] == ending_sequence[0]): #doing it this way also makes it so that those without ending sequences dont work.
                ending_sequence_len = len(ending_sequence)
                for q in range(1, ending_sequence_len):
                    if (j + i + q > checked_len):
                        found = False
                        break
                    if checked[i + j + q] != ending_sequence[q]:
                        break
                    if q == ending_sequence_len - 1:
                        found = True
                        break
                if found:
                    break #Break out of second one.

            if(checked[i + j] != before[j]):
                found = False
                break

            currentFound += checked[i+j]
        if found: #found :o
            if currentFound not in valid:
                #found an invalid!
                print("Invalid line found at: " + str(current_line) + "\n")
        else: #not found :/
            currentFound = ""
            
