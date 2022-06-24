/* 튜플 */
function solution(s) {
    var answer = [];
    // 문자열 분리
    // 맨 앞 {{, 맨 뒤 }} 삭제하고 },{ 기준으로 잘라 배열에 넣는다
    let strList = s.replace('{{','').replace('}}','').split('},{');
    let setList = [];
    for (let i=0; i<strList.length; i++){
        setList.push(strList[i].split(','));
    }
    // 크기 순으로 배열을 정렬
    setList.sort((a,b)=>{
        if (a.length>b.length){
            return 1;
        }else{
            return -1;
        }
    })
    // 첫 번째 요소 answer에 저장
    answer.push(parseInt(setList[0][0]));
    // 각 배열의 요소중에 answer에 없는 요소를 찾고 answer에 저장
    for (let i=1; i<setList.length; i++){
        let ele = getEle(setList[i],answer);
        answer.push(ele);
    }
    //console.log(answer,setList);
    return answer;
}
function getEle(set, answer){
    //set과 answer의 모든 요소를 배교해서 answer에 없는 set요소를 찾기
    for (let i=0; i<set.length; i++){
        for (let j=0; j<answer.length; j++){
            set = set.filter(ele=>ele!=answer[j]);
        }
    }
    return parseInt(set[0]);
}