#A) Write a function that takes in a string and returns the number of unique consonants [10 marks]

def unique_consonants(string):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    unique_consonants = []
    duplicate_consonants = []
    
    
    for letter in string:  # Convert to lowercase to handle case-insensitivity
        if letter in consonants:
            if letter in unique_consonants:
                unique_consonants.remove(letter)
                duplicate_consonants.append(letter)
            elif letter not in duplicate_consonants:
                unique_consonants.append(letter)

    return len(unique_consonants)




#B) What is the time and space complexity of your solution?
""" I'm assuming its O(n) where n is the length of the string the lenght of the english alphabet is 21/ fixed. """