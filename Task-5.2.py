import pyshorteners
url=input("Enter a url: ")
def urlshortener(url):
    s=pyshorteners.Shortener()
    print(s.tinyurl.short(url))
urlshortener(url)

