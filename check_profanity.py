from urllib.request import urlopen

def read_texts():
    text = open("example_Email.txt")
    contents_of_file = text.read()
    text.close()
    checkProfanity(contents_of_file)


def checkProfanity(inputText):
    print(inputText)
    response = urlopen("http://www.wdylike.appspot.com/?q="+ inputText)
    print(response.read())
    response.close()

read_texts()
