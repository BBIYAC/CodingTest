'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getLetter(s) {
    // Write your code here
    if ('aeiou'.includes(s[0])) return 'A';
    if ('bcdfg'.includes(s[0])) return 'B';
    if ('hjklm'.includes(s[0])) return 'C';
    if ('npqrstvwxyz'.includes(s[0])) return 'D';
}


function main() {
    const s = readLine();
    
    console.log(getLetter(s));
}