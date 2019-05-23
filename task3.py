f= open("book1.txt","w+")
f1= open("book2.txt","w+")
f2= open("book3.txt","w+")
f3= open("20k.txt","w+")
import sys
import collections

def find_most_common_words("book1.txt"):
	    
    """ Return the most common words in a text file. """

    textfile = open(book1.txt)
    text = textfile.read().lower()
    textfile.close()
    words = collections.Counter(text.split())

    return dict(words.most_common(top))

filename= sys.argv[1]
words = find_most_common_words(filename)


