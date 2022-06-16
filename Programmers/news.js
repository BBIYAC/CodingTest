/* [1차] 뉴스 클러스터링 */
function solution(str1, str2) {
    const arr1 = strCheck(str1);
    const arr2 = strCheck(str2);

    //교집합과 합집합을 구하는 과정
    const intersection = [];
    const union = [];
    for (let i = 0; i < arr2.length; i++) {
      if (arr1.indexOf(arr2[i]) >= 0) {
        intersection.push(arr1.splice(arr1.indexOf(arr2[i]), 1));
      }
      union.push(arr2[i]);
    }

    for (let i = 0; i < arr1.length; i++) {
      union.push(arr1[i]);
    }
    if (intersection.length === 0 && union.length === 0) {
      return 65536;
    }
    return parseInt(65536 * (intersection.length / union.length));
}

function strCheck(text){
    let arr = [];
    for (let i = 0; i < text.length - 1; i++) {
      const str = text.toUpperCase().substr(i, 2);
      if (str.match(/[A-Z]{2}/)) {
        arr.push(str);
      }
    }
    return arr;
}