# text-summarizer
### A Flask-based application that allows users to create extractive summaries of large texts and to translate them to other languages if needed.
#### Initially, the user submits a text which is to be summarized, along with the number of sentences he wishes to cut down the summary to. The system then selects that number of the most important sentences in the paragraph and displays it (aka extractive text summary). I will also implement abstractive summarization later on.

<img width="960" alt="image" src="https://user-images.githubusercontent.com/69348639/162585021-b9f9a553-0ca2-4154-baba-98de64971031.png">

#### After clicking on "summarize", the user is then redirected to '/summarize', where a summary of his / her text is displayed on the left, along with a list of languages he might wish to translate his / her summary to, on the right side.

<img width="960" alt="image" src="https://user-images.githubusercontent.com/69348639/162585032-3b6cde2d-ec69-42c9-b1d1-2c4277480891.png">

#### In case we want to translate the summary to another language, we can do that as well.
 
<img width="960" alt="image" src="https://user-images.githubusercontent.com/69348639/162585072-6b64199d-3813-46de-9b9f-e0606ba35261.png">
<img width="960" alt="image" src="https://user-images.githubusercontent.com/69348639/162585126-172fa676-0780-4140-a89b-8f33a3cec3cc.png">
<img width="960" alt="image" src="https://user-images.githubusercontent.com/69348639/162585114-f5dcc367-0d64-445f-ba01-90b32616beb0.png">
