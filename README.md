# text-summarizer
### A Flask-based application that allows users to create extractive summaries of large texts and to translate them to other languages if needed.
#### Initially, the user submits a text which is to be summarized, along with the number of sentences he wishes to cut down the summary to. The system then selects that number of the most important sentences in the paragraph and displays it (aka extractive text summary). I will also implement abstractive summarization later on.
<img width="960" alt="image" src="https://user-images.githubusercontent.com/69348639/159164330-465b1cc8-156b-4bd8-9cdb-340bd8c023f2.png">

#### After clicking on "summarize", the user is then redirected to '/summarize', where a summary of his / her text is displayed on the left, along with a list of languages he might wish to translate his / her summary to, on the right side.
