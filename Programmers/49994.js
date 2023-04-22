// [프로그래머스 49994] 방문 길이
function solution(dirs) {
  // 동, 서, 남, 북으로의 이동 방향
  const dx = [0, 0, 1, -1]; 
  const dy = [1, -1, 0, 0];
  const visited = new Set(); // 방문한 경로를 저장할 Set
  let x = 0; // 현재 위치의 x 좌표
  let y = 0; // 현재 위치의 y 좌표
  let count = 0; // 방문한 경로의 개수

  for (let i = 0; i < dirs.length; i++) {
    const dir = dirs[i]; // 현재 이동 방향
    let nx, ny; // 다음 위치의 x, y 좌표
    const idx = {'R': 0, 'L': 1, 'D': 2, 'U': 3}; // 인덱스

    // 이동 방향에 따라 다음 위치를 계산
    nx = x + dx[idx[dir]];
    ny = y + dy[idx[dir]];

    // 다음 위치가 범위를 벗어나지 않는지 확인
    if (nx >= -5 && nx <= 5 && ny >= -5 && ny <= 5) {
      const path = `${x}${y}${nx}${ny}`; // 현재 위치와 다음 위치를 경로 문자열로 표현
      const reversePath = `${nx}${ny}${x}${y}`; // 역방향 경로도 함께 저장하기 위해 문자열 순서를 뒤집은 문자열 생성
      
      // 경로가 처음 방문한 것이라면 Set에 추가하고 count 증가
      if (!visited.has(path)) {
        visited.add(path);
        visited.add(reversePath);
        count++;
      }
      
      // 현재 위치를 다음 위치로 갱신
      x = nx;
      y = ny;
    }
  }

  return count;
}
