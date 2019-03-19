from urllib.request import urlopen

def read_texts(target_file):
    text = open(target_file)
    contents_of_file = text.read()
    text.close()
    checkProfanity(contents_of_file)


def checkProfanity(inputText):
    response = urlopen("http://www.wdylike.appspot.com/?q="+ inputText)
    answer = response.read().decode('utf-8') #convert from byte to string
    if 'true' in answer:
        answer = True
    else: answer = False
    response.close()

    #Output is bool
    return answer
