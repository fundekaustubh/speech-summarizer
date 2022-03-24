const summaryLength = document.getElementById('summaryLength');
const summaryTextBox = document.getElementById('summaryText');

summaryTextBox.addEventListener('input', (e) => {
    let heightLimit = '200px';
    console.dir(summaryLength);
    summaryLength.max = e.target.value.trim().match(/[\w|\)][.?!](\s|$)/g).length;
    if (summaryLength.value > summaryLength.max) {
        summaryLength.value = summaryLength.max;
    }
    summaryTextBox.style.height = ""; /* Reset the height*/
    summaryTextBox.style.height = Math.min(summaryTextBox.scrollHeight, heightLimit) + "px";
})

console.log('Hey');