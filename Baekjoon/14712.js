// [백준 14712] 넴모넴모 (Easy)

// 백준 node.js 입력값 처리
const inputs = require("fs").readFileSync("/dev/stdin").toString().split("\n");

// 격자판의 행의 개수 N, 열의 개수 M
const [N, M] = inputs[0].split(' ').map(num => Number(num));

const solution = (N, M) => {
  var answer = 0;
  // 격자판 N+1 * M+1 크기로 배열 초기화
  const board = Array.from({length: N+1}, 
    () => Array.from({length: M+1}, () => 0));

  const dfs = (V) => {
    if (V === N*M) {
      answer++;
      return;
    };
    const [y, x] = [Math.floor(V/M)+1, (V % M)+1];

    // 넴모 안놓는 경우
    dfs(V+1);

    // 넴모 놓은 칸이 2*2를 구성해 터지지 않는 경우만 놓기
    if (!(board[y-1][x] * board[y][x-1] * board[y-1][x-1])) {
      board[y][x] = 1
      dfs(V+1);
      board[y][x] = 0
    }
  };

  dfs(0);
  return answer;
}

// 결과 출력
console.log(solution(N, M));