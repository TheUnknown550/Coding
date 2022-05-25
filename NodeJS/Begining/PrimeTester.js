//Imports
const print = require('prompt-sync')();

// Ask for input
let num = print("Enter your number: ");

//Process
let rem = num%2;

if (rem == 0){
    console.log("YOur number is a Even number.");
}
else if(rem == 1){
    console.log("your number is an Odd number.");
}