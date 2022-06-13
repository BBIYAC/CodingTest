/* 짝지어 제거하기 */
function solution(s){
    const strArr = s.split("");

      for(let i = 0 ; i < strArr.length-1 ; i++){
        if(strArr[i] === strArr[i+1]){
            strArr.splice( i, 2 );
              i = -1;
        }
    }

  return strArr.length === 0 ? 1 : 0;
}