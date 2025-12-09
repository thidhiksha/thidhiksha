#import neccessary libraries
import random
import string

class UrlShortner:
    def __init__(self):
        self.data={}
    def shorten(self,url):
      #generating random 6 char code
        code="".join(random.choices(string.ascii_letters+string.digits,k=6))
      #storing 
        self.data[code]=url
        return code
    def redirect(self,code):
        if code in self.data:
            return self.data[code]
        return "Invalid code"
if __name__=="__main__":
    obj=UrlShortner()
    short=obj.shorten("https://google.com")
    print("Short Code:",short)
    print("Original:",obj.redirect(short))
      


