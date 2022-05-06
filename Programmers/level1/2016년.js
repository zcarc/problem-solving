function solution(a, b) {
  const days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"];
  const months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  const total =
    months
      .slice(0, a - 1)
      .reduce((prev_val, cur_val) => prev_val + cur_val, 0) + b;

  return days[(total - 1) % 7];
}

console.log(solution(5, 24));