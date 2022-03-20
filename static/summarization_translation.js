const translateButton = document.getElementById('translateButton');
console.dir(translateButton);

const originalSummary = document.getElementById('originalSummary');
const translatedSummary = document.getElementById('translatedContentText');

const optionsCard = document.querySelector('.translation-options');
console.dir(optionsCard);
const translationContainer = document.querySelector('.translated-content');
const loaderContainer = document.querySelector('.loader-container');
const languageSelected = document.querySelector('#languageSelect');
const newLanguage = document.getElementById('newLanguage');
const translateMoreButton = document.getElementById('translateMoreButton');
const backButton = document.getElementById('backButton');
translateButton.addEventListener('click', (e) => {
    e.preventDefault();
    optionsCard.classList.toggle('d-none');
    optionsCard.classList.toggle('d-flex');
    loaderContainer.classList.toggle('d-flex');
    loaderContainer.classList.toggle('d-none');
    // console.dir(originalSummary.innerText);
    fetch('/translate', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "originalSummary": originalSummary.innerText,
            "to": languageSelected.value
        })
    })
        .then(r => r.json())
        .then((response) => {
            console.dir(response);
            loaderContainer.classList.toggle('d-flex');
            loaderContainer.classList.toggle('d-none');
            translationContainer.classList.toggle('d-none');
            translationContainer.classList.toggle('d-flex');
            translatedSummary.textContent = response.translatedSummary;
            newLanguage.innerText = response.to;
        })
        .catch((error) => {
            console.dir(error);
        });
})

translateMoreButton.addEventListener('click', (e) => {
    e.preventDefault();
    optionsCard.classList.toggle('d-none');
    optionsCard.classList.toggle('d-flex');
    translationContainer.classList.toggle('d-flex');
    translationContainer.classList.toggle('d-none');
})

backButton.addEventListener('click', (e) => {
    e.preventDefault();
    history.go(-1);
})