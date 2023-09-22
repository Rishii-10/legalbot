import spacy
nlp=spacy.load("en_core_web_sm")
def preprocess_text(text):
    doc=nlp(text)
    sentences= [sent.text for sent in doc.sents]
    return sentences
def custom_extractive_summary(text, num_sentences=3):
    sentences=preprocess_text(text)
    sentence_scores={}
    for sentence in sentences:
        doc=nlp(sentence)
        sentence_scores[sentence]=sum([token.vector_norm for token in doc])
    sorted_sentences=sorted(sentence_scores,key=sentence_scores.get,reverse=True)[:num_sentences]
    summary=" ".join(sorted_sentences)
    return summary
with open("legal_document.txt","r") as file:
    legal_text=file.read()
summary=custom_extractive_summary(legal_text)
print(summary)
with open("summary.txt","w") as file:
    file.write(summary)
