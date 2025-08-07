function startDictation() {
    if (window.hasOwnProperty('webkitSpeechRecognition')) {
        var recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = "en-IN";
        recognition.start();
        recognition.onresult = function (e) {
            document.querySelector("input[type='text']").value = e.results[0][0].transcript;
            document.querySelector("input[type='text']").dispatchEvent(new Event('input', { bubbles: true }));
            recognition.stop();
        };
        recognition.onerror = function (e) {
            recognition.stop();
        }
    }
}
