// [프로그래머스 12938] 최고의 집합

function solution(n, s) {
  const best = parseInt(s / n);
  if(!best) return [-1];
  
  const rest = s % n;
  const answer = new Array(n).fill(best);
  
  for(let i = 0; i < rest; i++) {
      answer[answer.length - 1 - i]++;
  };

  return answer;
}