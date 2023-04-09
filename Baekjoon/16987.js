// [백준 16987] 계란으로 계란치기

// 백준 node.js 입력값 처리
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let n = 0;
let eggs = [];
let answer = 0;
const S = 0;
const W = 1;

rl.on('line', function (line) {
  if (n === 0) {
    n = parseInt(line);
  } else {
    const egg = line.split(' ').map(str => parseInt(str));
    eggs.push(egg);
  }
}).on('close', function () {
  function crash(nowIndex) {
    // 종료조건
    if (nowIndex === n) {
      let breakEggs = 0;
      for (let i = 0; i < n; i++) {
        if (eggs[i][S] <= 0) {
          breakEggs += 1;
        }
      }
      answer = Math.max(answer, breakEggs);
      return;
    }

    // 자기가 깨져있는 경우 다음 계란으로
    if (eggs[nowIndex][S] <= 0) {
      crash(nowIndex + 1);
      return;
    }

    // 자기말고 다 깨져있는 상황인 경우
    let isAllBroken = true;
    for (let targetIndex = 0; targetIndex < n; targetIndex++) {
      if (targetIndex === nowIndex) continue;
      if (eggs[targetIndex][S] > 0) {
        isAllBroken = false;
        break;
      }
    }
    if (isAllBroken) {
      answer = Math.max(answer, n - 1);
      return;
    }

    // 때려보기
    for (let targetIndex = 0; targetIndex < n; targetIndex++) {
      if (targetIndex === nowIndex) continue;
      if (eggs[targetIndex][S] <= 0) continue;
      // 때리기
      eggs[nowIndex][S] -= eggs[targetIndex][W];
      eggs[targetIndex][S] -= eggs[nowIndex][W];
      crash(nowIndex + 1);
      // 복구
      eggs[nowIndex][S] += eggs[targetIndex][W];
      eggs[targetIndex][S] += eggs[nowIndex][W];
    }
  }
  
  crash(0);
  console.log(answer);
});