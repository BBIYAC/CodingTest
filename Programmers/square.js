/*
멀쩡한 사각형
가로의 길이 W와 세로의 길이 H가 주어질 때, 
사용할 수 있는 정사각형의 개수를 구하는 solution 함수를 완성해 주세요.
*/

// 유클리드 호제법을 이용한 최대 공약수 구하기
function gcd(w, h){
    // w 나누기 h의 나머지 구하기
    const mod = w % h;
    // 나머지가 0이면 h 리턴
    if(mod==0){
        return h;
    }else{ // 나머지가 0이 아니면 재귀호출
        return gcd(h, mod);
    }
}

function solution(w, h) {
    // 최대 공약수 구하기
    const gcdValue = gcd(w, h);
    
    // 공식
    return w*h - (w+h-gcdValue);
}