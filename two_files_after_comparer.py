import time

checked_file_path = input("enter the path to file you would like checked: ")
comparison_file_path = input("enter path to base comparison file: ")

checked_file = open(checked_file_path, "r")
comparison_file = open(comparison_file_path, "r")

checked =  checked_file.read()
comparison = comparison_file.read()

before = input("what should come before in checked?")
comparison_before = input("what should come before in comparison?")
ending_sequence = input("what should be the character sequence to end it in checked? enter /endofline to indicate until end of line.")
comparison_ending_sequence = input("what should be the character sequence to end it in comparison? enter /endofline to indicate until end of line.")

if(ending_sequence == "/endofline"):
    ending_sequence = "\n"

if(comparison_ending_sequence=="/endofline"):
    comparison_ending_sequence="\n"

valid = []

comparison_len = len(comparison)
found = False
currentFound = ""
comparison_ending_sequence_len = len(comparison_ending_sequence)

for i in range(0, comparison_len):
    if(comparison[i] == comparison_before[0]):
        found = False
        for j in range (0, len(comparison_before)): #check if comparison_before is here
            if(j + i >= comparison_len):
                break #reached end of file before desired sequence ended.

            if(comparison[i + j] != comparison_before[j]):
                found = False
                break
            if(j == len(comparison_before) - 1): #reached end of comparison sequence :o
                break_out_larger = False
                k = 0
                found = True 
                currentFound = ""
                while True:
                    k += 1
                    if(j + i + k >= comparison_len):
                        found = False
                        break # out of bounds
                    #have we possibly reached ending sequence?
                    if(comparison[j + i + k] == comparison_ending_sequence[0]): 
                        for q in range(0, comparison_ending_sequence_len):
                            if (j + i + q + k >= comparison_len):
                                break_out_larger = True
                                found = False #out of bounds
                                break
                            if comparison[j + i + q + k] != comparison_ending_sequence[q]:
                                break #not the ending sequence. continue as planned.
                            if q == comparison_ending_sequence_len - 1:
                                break_out_larger = True #ok everything good
                                break
                    if break_out_larger:
                        break
                    currentFound += comparison[j + i + k]

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
            
