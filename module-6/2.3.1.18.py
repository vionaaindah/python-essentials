def mysplit(strng):
    # put your code here
    word = ""
    list_string = []

    for phrase in strng:
      if phrase != " ":
         word += phrase
      elif word:
         list_string.append(word)
         word = ""
    
    if word:
      list_string.append(word)
    return list_string

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
