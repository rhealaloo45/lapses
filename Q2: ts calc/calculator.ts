function calculate(){
    const input1 = parseFloat((document.getElementById("input1") as HTMLInputElement).value);
    const input2 = parseFloat((document.getElementById("input2") as HTMLInputElement).value);
    const operation = (document.getElementById("operation") as HTMLSelectElement).value;

    let result = 0;

    switch(operation){
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
        default :
            break;
    }

    displayResult(result);
}

function displayResult(result: number){
    const resultInput = document.getElementById("result") as HTMLInputElement;
    resultInput.value = `Result: ${result}`;
}