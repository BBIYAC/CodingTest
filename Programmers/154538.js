// [프로그래머스 154538] 숫자 변환하기
function solution(x, y, n) {
  const d = new Array(y + 1).fill(Infinity);
  d[x] = 0;

  for (let i = x; i <= y; i++) {
    if (d[i] === Infinity) continue;

    if (i - 1 >= x) d[i - 1] = Math.min(d[i - 1], d[i] + 1);
    if (i + n <= y) d[i + n] = Math.min(d[i + n], d[i] + 1);
    if (i * 2 <= y) d[i * 2] = Math.min(d[i * 2], d[i] + 1);
    if (i * 3 <= y) d[i * 3] = Math.min(d[i * 3], d[i] + 1);
  }

  return d[y] === Infinity ? -1 : d[y];
}