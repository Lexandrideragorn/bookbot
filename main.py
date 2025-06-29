from stats import countWords
from stats import getBookText


def main():
    num_words = countWords(bookFrankenstein)
    print( f"{num_words} words found in the document") 


bookFrankenstein = getBookText("./books/frankenstein.txt")          

main()
