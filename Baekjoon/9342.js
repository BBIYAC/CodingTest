// [백준 9342] 염색체
const inputs = require("fs").readFileSync("/dev/stdin").toString().split("\n");

/*
^: 정규표현식 시작
[A-F]: A, B, C, D, E, F
?: 0번 또는 1번
+: 이전 문자가 1개 이상
$: 정규표현식 끝
*/
const T = parseInt(inputs.shift());

const check = (string) => {
  return string.match("^[A-F]?A+F+C+[A-F]?$");
};

for (let i=1; i<=T; i++) {
  console.log(check(inputs[i])? "Infected!": "Good");
}