// [프로그래머스 12927] 야근 지수
function solution(n, works) {
  if(works.reduce((a, b) => a + b) <= n) return 0;
  
  let sorted = works.sort((a, b) => a - b);
  const len = works.length - 1;
  
  while(n) {
    const max = sorted[len];
    
    for(let i=len; i >= 0; i--) {
      if(sorted[i] >= max) {
        sorted[i]--;
        n--;
      }
      if(!n) break;
    }
  }
  
  return sorted.reduce((a, b) => a + b**2, 0);
}