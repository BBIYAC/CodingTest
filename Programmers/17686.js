// [프로그래머스 17686] 파일명 정렬
function solution(files) {
  return files.sort((a, b) => {
      // 정규표현식을 이용하여 파일명을 문자, 숫자, 나머지 부분으로 분리
      const regex = /(\D+)(\d*)(.*)/;
      const fileA = a.match(regex);
      const fileB = b.match(regex);

      // 파일명의 첫 번째 부분을 비교하고, 대소문자 구분 없이 사전 순으로 정렬
      const headComparison = fileA[1].toLowerCase().localeCompare(fileB[1].toLowerCase());

      if (headComparison !== 0) {
          return headComparison;
      } else {
          // 파일명의 두 번째 부분(숫자 부분)을 비교하고, 숫자 순으로 정렬
          const numA = parseInt(fileA[2]);
          const numB = parseInt(fileB[2]);

          if (numA !== numB) {
              return numA - numB;
          } else {
              // 파일명이 숫자로만 이루어져 있다면, 원래 입력에 주어진 순서 유지
              return files.indexOf(a) - files.indexOf(b);
          }
      }
  });
}
