// [프로그래머스 12987] 숫자 게임
function solution(A, B) {
  A.sort((a, b) => a - b); // A를 오름차순으로 정렬
  B.sort((a, b) => a - b); // B를 오름차순으로 정렬

  let answer = 0;
  let idxA = 0;
  let idxB = 0;

  while (idxB < B.length) {
      if (A[idxA] < B[idxB]) { // A의 수가 B의 수보다 작은 경우
          answer++; // 승점 획득
          idxA++; // 다음 A의 수를 검사
      }
      idxB++; // 다음 B의 수를 검사
  }

  return answer;
}
