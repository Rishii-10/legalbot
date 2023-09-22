import spacy
nlp=spacy.load("en_core_web_sm")
def preprocess_text(text):
    doc=nlp(text)
    return [token.text.lower() for token in doc if not token.is_punct and not token.is_stop]
def find_most_important_word(text):
    words=preprocess_text(text)
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    most_important_word=max(word_count,key=word_count.get)
    return most_important_word
with open("legal_document2.txt","r") as file:
    legal_text=file.read()
most_important_word=find_most_important_word(legal_text)
print("Most Important Word:",most_important_word)
with open("summ.txt","w") as file:
    file.write(most_important_word)
