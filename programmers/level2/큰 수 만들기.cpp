#include <string>
#include <vector>
#include <stack>

using namespace std;

string solution(string number, int k) {
    stack<char> Stack;

    for (int i = 0; i < number.size(); i++) {
        while (k > 0 && !Stack.empty() && Stack.top() < number[i]) {
            Stack.pop();
            k--;
        }
        Stack.push(number[i]);
    }

    string str = "";
    while (!Stack.empty()) {
      str.insert(0, 1, Stack.top());
      Stack.pop();
    }

    return str.substr(0, str.size() - k);
}