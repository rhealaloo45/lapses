function calculate() {
    var input1 = parseFloat(document.getElementById("input1").value);
    var input2 = parseFloat(document.getElementById("input2").value);
    var operation = document.getElementById("operation").value;
    var result = 0;
    switch (operation) {
        case "+":
            result = input1 + input2;
            break;
        case "-":
            result = input1 - input2;
            break;
        case "*":
            result = input1 * input2;
            break;
        case "/":
            result = input1 / input2;
            break;
        default:
            break;
    }
    displayResult(result);
}
function displayResult(result) {
    var resultInput = document.getElementById("result");
    resultInput.value = "Result: ".concat(result);
}
