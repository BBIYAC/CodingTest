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
// function solution(n) {
//     const s = new Set();
//     for(let i=1; i<=n; i+=2){
//         s.add(i);
//     }
//     s.delete(1);
//     s.add(2);
//     for(let j=3; j<Math.sqrt(n); j++){
//         if(s.has(j)){
//              for(let k=j*2; k<=n; k+=j){    
//                 s.delete(k);
//              }
//         }
//     }
//     return s.size;
// }

// 소수 찾기 Level2
function isPrime(n) {
	if (n < 2) return false;
	for (let i = 2; i <= Math.sqrt(n); i++) {
		if (n % i === 0) return false;
	}
	return true;
}

function dfs(set, arr, fixed) {
	if (arr.length >= 1) {
		for (let i = 0; i < arr.length; i++) {
			let newFixed = fixed + arr[i];
			let copyArr = [...arr];
			copyArr.splice(i, 1);

			if (isPrime(parseInt(newFixed))) {
				set.add(parseInt(newFixed));
			}

			dfs(set, copyArr, newFixed);
		}
	}
}

function solution(numbers) {
	let nums = numbers.split("");
	let set = new Set();

	dfs(set, nums, '');
	
	console.log(set);

	return set.size;
}