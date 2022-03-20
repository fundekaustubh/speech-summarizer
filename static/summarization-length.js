const summaryLength = document.getElementById('summary_length');
const summaryText = document.getElementById('summary_text');
summaryText.addEventListener('input', (e) => {
    console.dir(summaryLength);
    summaryLength.max = e.target.value.trim().match(/[\w|\)][.?!](\s|$)/g).length;
    if (summaryLength.value > summaryLength.max) {
        summaryLength.value = summaryLength.max;
    }
})

console.log('Hey');