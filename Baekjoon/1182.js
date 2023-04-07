// [백준 1182] 부분수열의 합

// 백준 node.js 입력값 처리
const inputs = require("fs").readFileSync("/dev/stdin").toString().split("\n");
// 정수의 개수를 N과 정수 S, N개의 정수 배열
const [[N, S], N_nums] = inputs.map(input => input.split(' ').map(num => Number(num)));

const solution = (N, S, N_nums) => {
  var answer = 0;
  const recursive = (idx, sum) => {
    if (idx === N) return;

    sum += N_nums[idx];
    if (sum === S) answer++;

    recursive(idx+1, sum);
    recursive(idx+1, sum-N_nums[idx]);
  };

  recursive(0, 0);
  return answer;
}

// 결과 출력
console.log(solution(N, S, N_nums));