// [프로그래머스 42628] 이중우선순위큐

function solution(operations) {
  const heap = [];
  // 입력된 명령어를 공백(' ')을 기준으로 분할한다.
  const op = operations.map(operation => operation.split(' '));
  
  op.forEach(num => {
      if(num[0] === 'I') {	// 명령어가 I라면 데이터 삽입
          heap.push(Number(num[1]))
      }
      else {	// 그 외의 경우, 즉 명령어가 D인 경우
          const findValue = (num[1] === '1' ? Math.max : Math.min)(...heap);
          // 숫자가 1이라면 max값을, -1이라면 min값을 적용해서
          const delIdx = heap.indexOf(findValue);
          // 찾고자 하는 값의 인덱스를 찾아서
          heap.splice(delIdx, 1);
          // (이름만 heap인) 배열에서 해당 인덱스의 원소를 제거
      }
  })
  
  return heap.length ? [Math.max(...heap), Math.min(...heap)] : [0, 0];
}