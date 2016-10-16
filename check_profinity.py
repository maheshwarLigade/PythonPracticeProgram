import urllib
def read_text():
    quotes = open("/Users/maheshwarligade/Documents/PythonPractice/movie_quotes.txt")
    content_of_file = quotes.read()
    print(content_of_file)
    quotes.close()
    check_profinity(content_of_file)

def check_profinity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q"+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
read_text()
