/*포켓몬 */
function solution(nums) {
    var selected = [];
    for(var num of nums){
        if(!selected.includes(num) && selected.length<parseInt(nums.length/2)){
            selected.push(num);
        }
    }

    return selected.length;
}
