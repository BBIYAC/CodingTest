/*

/^ : 문자열의 시작 부분을 나타냅니다.
([aeiou]) : 첫 번째 그룹으로 모음(a, e, i, o, u) 중 하나를 나타냅니다.
.* : 임의의 문자열(모든 문자와 일치)을 나타냅니다.
\1 : 첫 번째 그룹과 동일한 값을 나타냅니다. 여기서는 첫 번째 그룹이 어떤 모음이었는지를 의미합니다.
$/ : 문자열의 끝 부분을 나타냅니다.

*/

function regexVar() {
  /*
   * Declare a RegExp object variable named 're'
   * It must match a string that starts and ends with the same vowel (i.e., {a, e, i, o, u})
   */
  const re = /^([aeiou]).*\1$/g;

  /*
   * Do not remove the return statement
   */
  return re;
}


function main() {
  const re = regexVar();
  const s = readLine();
  
  console.log(re.test(s));
}