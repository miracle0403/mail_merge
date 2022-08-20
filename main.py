#TODO: Create a letter using starting_letter.txt
with open("./input/letters/starting_letter.txt") as letter:
    lett = letter.read()

with open("./input/Names/invited_names.txt", "r") as gett:
    invited_names = gett.readlines()

#for each name in invited_names.txt
for names in invited_names:
    x = names.strip("\n")
    #Replace the [name] placeholder with the actual name.
    txt = lett.replace("[name]", x)
    #Save the letters in the folder "ReadyToSend".
    with open(f"./output/readytosend/letterto{x}.txt", mode="w") as writer:
        writer.write(txt)
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp