// [프로그래머스 77885] 2개 이하로 다른 비트
function solution(numbers) {
  var answer = [];
  for (var i = 0; i < numbers.length; i++) {
      var num = numbers[i];
      if (num % 2 == 0) {
          answer.push(num + 1);
      } else {
          var binary = num.toString(2);
          var idx = binary.lastIndexOf('0');
          if (idx == -1) {
              binary = '10' + binary.substr(1);
          } else {
              binary = binary.substr(0, idx) + '10' + binary.substr(idx + 2);
          }
          answer.push(parseInt(binary, 2));
      }
  }
  return answer;
}
