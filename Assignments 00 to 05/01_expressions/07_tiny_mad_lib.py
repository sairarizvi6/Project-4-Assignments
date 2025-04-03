#Write a program which prompts the user for an adjective, then a noun, then a verb, 
#and then prints a fun sentence with those words!
#Mad Libs is a word game where players are prompted for one word at a time, 
#and the words are eventually filled into the blanks of a word template to make an entertaining
#story! We've provided you with the beginning of a sentence (the SENTENCE_START constant) 
#which will end in a user-inputted adjective, noun, and then verb.
#Please type an adjective and press enter. tiny
#Please type a noun and press enter. plant
#Please type a verb and press enter. fly
#Code in Place is fun. I learned to program and used Python to make my tiny plant fly!

# Sentence starter constant to form the final sentence
SENTENCE_START: str = "Code in Place is fun. I learned to program and used Python to make my "

def main():
    # Prompt the user for an adjective
    adjective: str = input("Please type an adjective and press enter: ")
    
    # Prompt the user for a noun
    noun: str = input("Please type a noun and press enter: ")
    
    # Prompt the user for a verb
    verb: str = input("Please type a verb and press enter: ")

    # Print the final sentence by combining user input with the sentence starter
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

# Call the main function to execute the program
main()
