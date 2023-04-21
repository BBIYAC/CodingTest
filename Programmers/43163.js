// [프로그래머스 43163] 단어 변환
function solution(begin, target, words) {
  const visited = { [begin] : 0 };
  const queue = [begin];

  while(queue.length) {
    const current = queue.shift();
    
    if(current === target) break;
    
    for(const word of words) {
      if(isConnected(word, current) && !visited[word]) {
        visited[word] = visited[current] + 1;
        queue.push(word);
      }
    }
  }
  return visited[target] ? visited[target] : 0;
}

const isConnected = (word, current) => {
  let count = 0;
  const len = word.length;
  
  for(let i = 0; i < len; i++) {
    if(word[i] !== current[i]) count++;
  }
  
  return count === 1;
}