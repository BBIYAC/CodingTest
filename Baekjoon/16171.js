// [백준 16171] 나는 친구가 적다 Small
const inputs = require("fs").readFileSync("/dev/stdin").toString().split("\n");

const [S, K] = inputs;
let words = '';

for (const word of S) {
  if (isNaN(word)) words += word;
};

console.log((words.includes(K))? 1: 0);