/* 최대 공약수와 최소 공배수 */
function solution(n, m) {
    // 최대 공약수: gcd, 최소 공배수: lcm
    let GCDLCM = (num1, num2) => {
        let gcd = 1;

        for(let i=2; i<=Math.min(num1, num2); i++){
            if(num1 % i === 0 && num2 % i === 0){
                gcd = i;
            }
        }

        let lcm = (num1 * num2) / gcd;

        return [gcd, lcm];
    }
    return GCDLCM(n, m);
}