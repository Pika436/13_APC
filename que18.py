# 18.	Accept a sentence from the user and use a set to display all unique words.
sentence=input("enetr a sentence :")
sent=set(sentence.split())
for word in sent:
    print(word)
