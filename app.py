import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, json
# from transformers import pipeline
import nltk.data
# import spacy
# import translators as tl
import en_core_web_sm
from iso639 import languages
from decouple import config

import googletrans
from string import punctuation
from collections import Counter

nlp = en_core_web_sm.load()
sentenceTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
translator = googletrans.Translator()

# summarizer = pipeline("summarization", model="t5-base")

configuration = {
    "DEBUG": True
}
# SECRET_KEY = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.config.from_mapping(configuration)
# app.secret_key = config(SECRET_KEY)
# print(app.secret_key)

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
    if request.method == 'POST':
        text = request.form.get("text")
        if not text:
            flash("Please enter text to summarize!")
        print(request.form.get('summary_length'))
        numberOfSentences = 0
        languages = [lang.capitalize() for lang in googletrans.LANGUAGES.values()]
        numberOfSentences = request.form.get('summary_length')
        if numberOfSentences == None or numberOfSentences == 0 :
            print('Checking number of sentences! Number: ', numberOfSentences)
            return render_template('summary.html', summarizedText = text, languages = languages) 
        extractiveText = punctuate(extractive(text, numberOfSentences))
        return render_template('summary.html', summarizedText = extractiveText, languages = languages)

@app.route('/translate', methods=["POST"])
def translate():
    if request.method == 'POST':
        req = request.get_json()
        print('Original summary: ', req["originalSummary"])
        newSummary = translator.translate('' + req["originalSummary"], dest=req["to"]).text
        # newSummary = tl.google(req["originalSummary"], to_language=req["to"])
        return jsonify({"translatedSummary": newSummary, "to": req["to"]}), 200

@app.route('/', methods=["GET"])
def createApplication():
    if request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run()