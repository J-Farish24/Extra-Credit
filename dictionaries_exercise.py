FILE = 'book of John text.txt'
book_of_john_words = []
book_of_john_word_count = {'Father': 0, 'God': 0, 'Christ': 0
,'Spirit': 0, 'spirit': 0, 'life': 0, 'man': 0}

#Open file and store content
infile = open(FILE, 'r')
word = ""
for rec in infile:
    for letter in rec:
       if letter != " ":
           word += letter 
       else:
            book_of_john_words.append(word)
            word = ""
infile.close()
for key in book_of_john_word_count:
    for word in book_of_john_words:
        if word == key:
            book_of_john_word_count[key] += 1
for key in book_of_john_word_count:
    print(key, ': ', book_of_john_word_count[key], sep ='')

