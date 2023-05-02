// [프로그래머스 12979] 기지국 설치
function solution(n, stations, w) {
  const range = w * 2 + 1; // 기지국이 커버하는 범위
  let answer = 0;
  let start = 1; // 시작 지점

  for (let i = 0; i < stations.length; i++) {
    const end = stations[i] - w - 1; // 현재 기지국의 전파가 닿지 않는 구간의 끝 지점
    const length = end - start + 1; // 현재 기지국의 전파가 닿지 않는 구간의 길이

    if (length > 0) {
      answer += Math.ceil(length / range); // 필요한 기지국의 개수를 계산하여 정답에 더함
    }

    start = stations[i] + w + 1; // 다음 구간의 시작 지점 갱신
  }

  // 마지막 기지국에서 끝까지 처리
  if (start <= n) {
    const length = n - start + 1;
    answer += Math.ceil(length / range);
  }

  return answer;
}
