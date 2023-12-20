javascript
document.addEventListener("DOMContentLoaded", function() {
    fetch("names.json")
        .then(response => response.json())
        .then(data => {
            let names = data.names;
            let randomNameElement = document.getElementById("randomName");
            
            function generateRandomName() {
                let randomIndex = Math.floor(Math.random() * names.length);
                let randomName = names[randomIndex];
                randomNameElement.innerText = randomName;
            }

            function copyToClipboard() {
                let range = document.createRange();
                range.selectNode(randomNameElement);
                window.getSelection().removeAllRanges();
                window.getSelection().addRange(range);
                document.execCommand("copy");
                window.getSelection().removeAllRanges();
            }

            generateRandomName();
        });
});
