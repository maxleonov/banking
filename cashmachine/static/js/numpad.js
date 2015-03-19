var NUMPAD_INPUT_ID = "IdOfInputElement"
var NUMPAD_INPUT_MAX_LEN = 0
var NUMPAD_SEPARATOR = "-"
var NUMPAD_SEPARATOR_INTERVAL = 0

var dashCounter = 0;

function writeNumber(x) {
    var textField = document.getElementById(NUMPAD_INPUT_ID);
    if (NUMPAD_INPUT_MAX_LEN !=0 && textField.value.length == NUMPAD_INPUT_MAX_LEN) return;
    textField.value = textField.value + x;

    if (!NUMPAD_SEPARATOR_INTERVAL) return;
    if (NUMPAD_INPUT_MAX_LEN !=0 && textField.value.length == NUMPAD_INPUT_MAX_LEN) return;

    dashCounter += 1;
    if (dashCounter == NUMPAD_SEPARATOR_INTERVAL) {
        textField.value = textField.value + NUMPAD_SEPARATOR
        dashCounter = 0;
    }
}

function clearNumbers() {
    dashCounter = 0;
    document.getElementById(NUMPAD_INPUT_ID).value = "";
}