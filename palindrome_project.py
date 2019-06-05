user_string = input("enter your sentence")

def is_palindrome(user_string):
    new_string = ""
    user_string = user_string.lower()
    for letter in user_string:
        if letter.isalpha():
            new_string = new_string + letter
    return new_string        

cleanned_sentence = is_palindrome(user_string)
reverse_sentence = cleanned_sentence[::-1]

if cleanned_sentence == reverse_sentence:
    print ("It is a palindrome")

elif cleanned_sentence != reverse_sentence:
    print ("This is not a palindrome")


