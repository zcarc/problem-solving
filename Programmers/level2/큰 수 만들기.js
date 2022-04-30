function solution(number, k) {
  const stack = [];

  for (let i = 0; i < number.length; i++) {
    while (k > 0 && stack.length > 0 && stack[stack.length - 1] < number[i]) {
      stack.pop();
      k--;
    }

    stack.push(number[i]);

    if (k === 0) {
      for (let j = i + 1; j < number.length; j++) {
        stack.push(number[j]);
      }
      break;
    }
  }

  const string = stack.join("");

  return string.slice(0, string.length - k);
}

console.log(solution("1924", 2));
console.log(solution("1231234", 3));
console.log(solution("4177252841", 4));
console.log(solution("4321", 2));
