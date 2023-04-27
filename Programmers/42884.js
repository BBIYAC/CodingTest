// [프로그래머스 42884] 단속카메라
function solution(routes) {
  routes.sort((a, b) => a[1] - b[1]);
  let camera = -1e9;
  let answer = 0;
  for (let i = 0; i < routes.length; i++) {
    if (camera < routes[i][0]) {
      camera = routes[i][1];
      answer++;
    }
  }
  return answer;
}