/* 소수찾기 */
// function solution(n) {
//     let answer = 0;
//     const arr = new Array(n+1).fill(true); // 초깃값 설정
//     const end = Math.sqrt(n) 
    
//     for(let i = 2; i <= end; ++i){
//         // 이미 소수가 아닌 인덱스는 건너뛴다.
//         if(arr[i] === false){
//             continue; 
//         }
//         // 소수가 아닌 데이터는 false로 입력한다.
//         for(let k = i * i; k <= n; k += i){
//             arr[k] = false;
//         }
//     }
//     // 소수의 갯수를 구한다.
//     for(let i = 2; i <= n; ++i){
//         if(arr[i] === true){
//             answer++;
//         }
//     }
//     return answer;
// }

// 다른 풀이
function solution(n) {
    const s = new Set();
    for(let i=1; i<=n; i+=2){
        s.add(i);
    }
    s.delete(1);
    s.add(2);
    for(let j=3; j<Math.sqrt(n); j++){
        if(s.has(j)){
             for(let k=j*2; k<=n; k+=j){    
                s.delete(k);
             }
        }
    }
    return s.size;
}