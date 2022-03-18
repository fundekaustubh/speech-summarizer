const summaryLength = document.getElementById('summary_length');
const summaryText = document.getElementById('summary_text');
summaryText.addEventListener('input', (e) => {
    summaryLength.value = parseInt(summaryText.value.count(' ') / 2);
})

console.log('Hey');