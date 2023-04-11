// [백준 10798] 세로 읽기
const inputs = require("fs").readFileSync("/dev/stdin").toString().split("\n");

const words = Array.from(Array(5), () => Array(15).fill(''));
for (var i=0; i<5; i++) {
  for (var j=0; j<inputs[i].length; j++) {
    words[i][j] = inputs[i][j];
  }
};

for (var i=0; i<15; i++) {
  for (var j=0; j<5; j++) {
    process.stdout.write(words[j][i]);
  }
}