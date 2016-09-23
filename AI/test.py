def anti_vowel(text):
    vowel = ['a','e','i','o','u']
    rev = ''
    for i in text:
	print i
        if i not in "aeiouAEIOU":
            rev += i
    return rev
        
print anti_vowel("Hey You!")
