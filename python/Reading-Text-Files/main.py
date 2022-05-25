# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    content=""
    try:
        with open(filename) as file:
            for line in file:
                content+=line.strip()
        return content
    except:
        print("{} cannot be opened!".format(filename))


def count_words():
    text = read_file_content("./story.txt").lower()
    # [assignment] Add your code here
    bad=".,?!" #remove punctuations
    count=dict() #to store word frequency data
    new_text="" #text void of punctuations

    for word in text:
        for letter in word:
            if letter==".":
                new_text+=" "
            elif letter in bad:
                pass
            else:
                new_text+=letter
                
    new_text=new_text.split()
                
    for word in new_text:
        if word not in count:
            count[word]=1
        else:
            count[word]+=1

    return count
            
    
