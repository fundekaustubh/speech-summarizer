from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
# from transformers import pipeline
import nltk.data
import spacy
import en_core_web_sm
from string import punctuation
from collections import Counter

nlp = en_core_web_sm.load()
sentenceTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# summarizer = pipeline("summarization", model="t5-base")

config = {
    "DEBUG": True
}

app = Flask(__name__)
app.config.from_mapping(config)

def punctuate(text):
    sentences = sentenceTokenizer.tokenize(text)
    sentences = [sent.capitalize() for sent in sentences]
    text = ' '.join(sentences)
    return text

# def abstractive(text, limit):
#     summarizedText = summarizer(text, max_length=limit, do_sample=False)[0]['summary_text'].replace(' .', '. ').replace(' . ', '. ')
#     return summarizedText

def extractive(text, limit):
    keyword = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
    doc = nlp(text.lower())
    for token in doc:
        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            keyword.append(token.text)
    
    freq_word = Counter(keyword)
    max_freq = Counter(keyword).most_common(1)[0][1]
    for w in freq_word:
        freq_word[w] = (freq_word[w]/max_freq)
        
    sent_strength={}
    for sent in doc.sents:
        for word in sent:
            if word.text in freq_word.keys():
                if sent in sent_strength.keys():
                    sent_strength[sent]+=freq_word[word.text]
                else:
                    sent_strength[sent]=freq_word[word.text]
    
    summary = []
    
    sorted_x = sorted(sent_strength.items(), key=lambda kv: kv[1], reverse=True)
    
    counter = 0
    for i in range(len(sorted_x)):
        summary.append(str(sorted_x[i][0]).capitalize())

        counter += 1
        if(counter >= limit):
            break
            
    return ' '.join(summary)

@app.route('/summarize', methods=["POST"])
def summarize():
    text = request.form.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    extractiveText = punctuate(extractive(text, int(request.form.get('summary_length'))))
    # abstractiveText = punctuate(abstractive(text, int(request.form.get('summary_length'))))
    # return jsonify({"Abstractive": abstractiveText, "Extractive": extractiveText})
    return extractiveText

@app.route('/', methods=["GET"])
def createApplication():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()