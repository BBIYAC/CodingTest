// [프로그래머스 17679] 프렌즈 4블록
function solution(m, n, board) {
  let gameBoard = board.map(row => row.split(''));

  while (true) {
      let blocksToPop = new Set(); // 제거할 블록의 위치를 저장하는 Set

      // 2x2 블록 탐색
      for (let i = 0; i < m - 1; i++) {
          for (let j = 0; j < n - 1; j++) {
              const currBlock = gameBoard[i][j];
              if (currBlock === '') continue; // 이미 제거된 블록은 스킵

              // 현재 블록의 우하단, 우상단, 좌하단 블록들과 같은지 비교
              if (currBlock === gameBoard[i][j + 1] &&
                  currBlock === gameBoard[i + 1][j] &&
                  currBlock === gameBoard[i + 1][j + 1]) {
                  // 2x2 블록의 위치를 Set에 저장
                  blocksToPop.add(`${i},${j}`);
                  blocksToPop.add(`${i},${j + 1}`);
                  blocksToPop.add(`${i + 1},${j}`);
                  blocksToPop.add(`${i + 1},${j + 1}`);
              }
          }
      }

      if (blocksToPop.size === 0) break; // 제거할 블록이 없으면 반복문 종료

      // 제거할 블록을 빈 문자열로 표시
      for (const block of blocksToPop) {
          const [i, j] = block.split(',').map(Number);
          gameBoard[i][j] = '';
      }

      // 빈 문자열이 아닌 블록들을 아래에서 위로 끌어올림
      for (let j = 0; j < n; j++) {
          for (let i = m - 1; i >= 0; i--) {
              if (gameBoard[i][j] === '') {
                  for (let k = i - 1; k >= 0; k--) {
                      if (gameBoard[k][j] !== '') {
                          gameBoard[i][j] = gameBoard[k][j];
                          gameBoard[k][j] = '';
                          break;
                      }
                  }
              }
          }
      }
  }

  // 제거된 블록의 개수 반환
  return gameBoard.flat().filter(block => block === '').length;
}
