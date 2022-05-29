// 이상한 문자 만들기
function solution(s) {
    var answer = [];
    var strings = s.split(" ")
    for(var str of strings){
        var temp = "";
        for(var i=0; i<str.length; i++){
            if(i%2 == 0){
                temp += str[i].toUpperCase();
            }else{
                temp += str[i].toLowerCase();
            }
        }
        answer.push(temp);
    }
    return answer.join(" ");
}