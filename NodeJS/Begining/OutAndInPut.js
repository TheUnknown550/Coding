//requirments
const ask = require('prompt-sync')();

//this is to output in console
console.log('Hello World!');

//theres many ways to input with node js

//Way1: using readline and.question()
function readline(){
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });
    //ask for input
    readline.question('name: ', name => {
        //output the input
        console.log(name);
        
        //ask for input
        readline.question('age: ', age => {
            //output the input
            console.log(age);
            
            //end readline module
            readline.close();
        });
    });
}


//Way2: using prompt-sync
function promt(){
    //giving requirements, it can be at the start of the code
    const prompt = require('prompt-sync')();
    //asking for input
    const name = prompt('name: ');
    console.log(name);
    //asking for input
    const age = prompt('age: ');
    console.log(age);
}
console.log("this shows drifferent types to out put");
console.log("\n1: using readline and.question()");
console.log("2: using prompt-sync");
const Way = ask("\npick which to learn: ");
if (Way == 1){
    readline();
}
else if (Way == 2){
    promt();
}
else{
    console.log('Invalid Syntax');
}