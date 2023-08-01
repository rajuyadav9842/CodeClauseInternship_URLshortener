# pip install pyshorteners
# pip install pyperclip
import pyshorteners
url = input('Enter the url: ')    # input from the user


def  shortenur1(url):              # define a function shortenur1 which will take longer URL
    s = pyshorteners.Shortener()   # define s variable  create object as  pyshorteners where small the url
    print(s.tinyurl.short(url))    # print it


shortenur1(url)                     # call the function

