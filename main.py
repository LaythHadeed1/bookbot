import sys
import string
def readFile(filename):
    with open(filename) as f:
        return f.read()

def countWords(text:str) -> int:
    return len(text.split(" "))  

def countCharacters(text:str):    
    dic = {c:0 for c in list(string.ascii_lowercase) }
    for x in text:
        if not x.isalpha():
            continue
        ax = x.lower()
        dic[ax] = dic[ax]+1  
    return dic    
def main() ->int:
    filepath = 'books/frankenstein.txt'
    fileContents = readFile(filepath)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{countWords(fileContents)} words found in the document")
    charsDict = countCharacters(fileContents)
    
    for sortedList in sorted(charsDict.items(),key= lambda item:item[1], reverse=True):
        print (f"The '{sortedList[0]}' character was found {sortedList[1]} times")
    return 0


if __name__ == '__main__':
    sys.exit(main())
    