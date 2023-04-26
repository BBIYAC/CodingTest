// [프로그래머스 12900] 2xn 타일링
function solution(n) {
  const MOD = 1000000007; // 나누는 수
  const dp = [0, 1, 2]; // dp 배열 초기화

  // 다이나믹 프로그래밍으로 구하기
  for (let i = 3; i <= n; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
  }

  return dp[n];
}