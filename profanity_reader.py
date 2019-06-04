import urllib

def read_text():
    quotes = open("/Users/ARouse/udacity_python_course/Profanity Reader/movie_quotes.txt")
    contents = quotes.read()

    print(contents)

    quotes.close()
    check_text(contents)

def check_text(text):

    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=shot" +text)
    output = connection.read()
    print(output)
    connection.close()

    if "true" in output:
        print("This document has a curse word")
    elif "false" in output:
              print("This document has no curse words")


read_text()



