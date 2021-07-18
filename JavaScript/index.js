const inquirer = require('inquirer');

//adds two numbers
const add = (n1, n2) => {
    return n1 + n2
}

//subtracts the second number from the first
const subtract = (n1, n2) => {
    return n1 - n2
}

//multiplies two numbers 
const multiply = (n1, n2) => {
    return n1 * n2
}

//divides the first number by the second
const divide = (n1, n2) => {
    return n1 / n2
}

const answer = (result) => {
    console.log(`The answer is ${result}`);
}

inquirer
    .prompt([{
        type: 'number',
        name: 'numOne',
        message: 'Enter a number'
    }, {
        type: 'list',
        name: 'operation',
        message: 'chose an operation to perform',
        choices: ['+', '-', '*', '/']
    }, {
        type: 'number',
        name: 'numTwo',
        message: 'Enter another number'
    }])
    .then(({
        numOne,
        operation,
        numTwo
    }) => {
        switch (operation) {
            case '+':
                answer(
                    add(numOne, numTwo)
                );
                break;
            case '-':
                answer(
                    subtract(numOne, numTwo)
                );
                break;
            case '*':
                answer(
                    multiply(numOne, numTwo)
                );
                break;
            case '/':
                answer(
                    divide(numOne, numTwo)
                );
                break;
        }
    })
    .catch((error) => {
        console.log(error);
    });