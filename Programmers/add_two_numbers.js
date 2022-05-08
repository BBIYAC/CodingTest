/*두 개 뽑아서 더하기 */
function solution(numbers) {
    var answer = [];
    for(var i=0; i<numbers.length-1; i++){
        for(var j=i+1; j<numbers.length; j++){
            var number = numbers[i]+numbers[j];
            if(!answer.includes(number)){
                answer.push(number); 
            }
        }
    }
    
    return answer.sort((a,b)=>a-b);
}