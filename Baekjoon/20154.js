// [백준 20154] 이 구역의 승자는 누구야?!
const inputs = require("fs").readFileSync("/dev/stdin").toString().split("\n");

const words = {
  'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3,
  'G': 3, 'H': 3, 'I': 1, 'J': 1, 'K': 3, 'L': 1,
  'N': 3, 'M': 3, 'O': 1, 'P': 2, 'Q': 2, 'R': 2,
  'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 2, 'X': 2,
  'Y': 2, 'Z': 1,
}

const input = inputs[0].split('');

const count = [];
for (const word of input) {
  count.push(words[word]);
}

const sum = count.reduce((a, b) => a + b, 0);
console.log((sum%10)%2? "I'm a winner!": "You're the winner?");