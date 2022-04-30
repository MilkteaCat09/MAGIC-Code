alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l',
'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
print('Hi and welcome to Pythabet! This is a game that makes a code alphabet!')
print ('Input a word for the code (please only use lowercase letters)!')
cat = input()
cat = list(cat)
cat_length = len(cat)
print('That word is', cat_length,'letters long.')
alphabet_length = len(alphabet)
cat_numbers = list()

for x in range(alphabet_length):
    for y in range(cat_length):
        if cat[y] == alphabet[x]:
            x = int(x)
            cat_numbers.append(x)
            
cat_numbers_length = len(cat_numbers)
sorted_cat = sorted(cat_numbers, reverse=True)
original_alphabet = alphabet.copy()
for z in range(cat_numbers_length):
    c = sorted_cat[z]
    del (alphabet[c])
cat.extend(alphabet)
print('The original alphabet is:')
print(original_alphabet)
print('The new alphabet is:')
print(cat)
print('Thank you for playing!')
