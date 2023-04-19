// [프로그래머스 43162] 네트워크
function solution(n, computers) {
  let count = 0;
  const visited = [];
  
  for(let i = 0; i < n; i++) {
      if(!visited[i]) {
          dfs(i, visited, computers);
          count++;
      }
  }
  
  return count;
}

const dfs = (node, visited, computers) => {
  visited[node] = true;
  for(let i = 0; i < computers.length; i++) {
      if(computers[node][i] === 1 && !visited[i]) dfs(i, visited, computers);
  }
}