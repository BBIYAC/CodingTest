// [프로그래머스] 우박수열 정적분
function solution(k, ranges) {
    
    const sequence = [k];
    let recentValue = sequence[sequence.length - 1];
    while (recentValue > 1) {
        if (recentValue % 2) recentValue = recentValue * 3 + 1;
        else recentValue = recentValue / 2;
        sequence.push(recentValue);
    }
    
    const areas = [];
    for (let i = 0; i < sequence.length - 1; i++) {
        areas.push((sequence[i] + sequence[i + 1]) / 2);
    }

	const prefixSum = [0];
	for (let i = 0; i <= areas.length; i++) {
    	prefixSum[i + 1] = prefixSum[i] + areas[i];
	}
    
    return ranges.map(([a, b]) => {
        b = areas.length + b;
        if(a > b) return -1;
        return prefixSum[b] - prefixSum[a]
    })
}