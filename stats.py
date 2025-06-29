
def getBookText(filepath):
    with open(filepath) as f:
        contents = f.read()
        return(contents)

def countWords(book):
    return len(book.split())

def characterCount(book):
    
