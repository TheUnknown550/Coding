//Imports
const print = require('prompt-sync')();

//Variable
let ans;

//Ask for input
let num1 = print("Please enter your first number: ");
let num2 = print("please enter your 2nd number: ");

//Ask for process type
console.log("1: Addition \n2: Subtraction \n3: Multiplication \n4: Divistion");
let cal = print("Pick how to proceed: ");

//Process types
if (cal == 1){
    ans = num1+num2;
}
else if(cal == 2){
    ans = num1-num2;
}
else if(cal == 3){
    ans = num1*num2;
}
else if(cal == 4){
    ans = num1/num2;
}
else{
    ans = "Invalid Input";
}

//Output
console.log(ans);