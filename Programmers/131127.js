// [프로그래머스 131127] 할인행사
function solution(want, number, discount) {
  let answer = 0;
  
  // 할인 품목과 원하는 제품이 일치하는지 확인하는 함수
  const isMatch = (arr) => { 
      let map = new Map();
      arr.forEach(v=>map.set(v, (map.get(v)||0)+1)); // 할인 품목들을 map에 셋팅한다.
      for(let i = 0; i < want.length; i++){
          // 원하는 품목의 수량과 할인 품목이 일치하지 않으면 false
          if(map.get(want[i]) !== number[i]) return false;
      }             
      return true;  // 일치하면 true를 리턴한다
  }
  
  for(let j = 0; j <= discount.length - 10; j++){
      // 10일동안 할인이 되므로 10개씩 배열을 잘라 확인
      if(isMatch(discount.slice(j, j+10))) answer++; 
  }
    return answer;
}