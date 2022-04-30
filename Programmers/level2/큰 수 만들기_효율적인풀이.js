function solution(number, k) {
  const stack = [];

  for (let i = 0; i < number.length; i++) {
    while (k > 0 && stack.length > 0 && stack[stack.length - 1] < number[i]) {
      stack.pop();
      k--;
    }

    stack.push(number[i]);

    // k === 0 이라면 순회 시 number[i]를 stack에 push만 할 것이니 아래 코드를 작성하지 않아도 된다.
    // if (k === 0) {
    //   for (let j = i + 1; j < number.length; j++) {
    //     stack.push(number[j]);
    //   }
    //   break;
    // }
  }

  const string = stack.join("");

  return string.slice(0, string.length - k);
}

console.log(solution("1924", 2));
console.log(solution("1231234", 3));
console.log(solution("4177252841", 4));
console.log(solution("4321", 2));
