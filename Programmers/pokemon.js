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

// BEST ANSWER
function answer_solution(nums){
    const pokemon = new Set(nums);
    const pokemonVarietyCount = pokemon.size;
    const pokemonCounts = nums.length;
    return pokemonVarietyCount > pokemonCounts/2 ? pokemonCounts/2 : pokemonVarietyCount;
}