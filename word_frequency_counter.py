#counting each word appeared
def count_words(text):
  text = text.lower()
  for ch in [",",".","!","?",";",":"]: #removing punctuations
    text = text.replace(ch,"")
  words = text.split()
  word_map = {}
  
  for w in words: #counting words
      if w in word_map:
        word_map[w]+=1
      else:
        word_map[w]=1
  #sorting 
  sort= sorted(word_map.items(), key=lambda x: x[1],reverse= True)
  for word,count in sort:
    print(f"{word}-{count}")
if __name__=="__main__":
  text= "Hello world, hello Spyyda"
  count_words(text)
