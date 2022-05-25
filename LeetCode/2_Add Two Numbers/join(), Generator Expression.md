제너레이터 표현식은 이터러블(Iterable)이고 괄호를 묶어서 표현할 수 있다.

```py
a = (x for x in [1, 2, 3, 4])
```

print 함수로 호출하면 제너레이터 객체라는 것을 확인할 수 있다.

```py
<generator object <genexpr> at 0x10246b900>
```

isinstance(object, classinfo) 함수로 호출하면 Iterable 클래스에 등록되어 있다는 의미이므로

True가 나오는 것을 확인할 수 있다.

```py
from collections.abc import Iterable
a = (x for x in [1, 2, 3, 4])
isinstance(a, Iterable)
```

```py
True
```

만약 괄호로 묶지 않는다면 SyntaxError: invalid syntax가 발생한다.

```py
a = x for x in [1, 2, 3, 4]
```

```py
    a = x for x in [1, 2, 3, 4]
          ^
SyntaxError: invalid syntax
```

str.join(iterable) 함수를 호출할 때 함수의 호출이 단일 위치의 인수(single positional argument)로 되어 있다면 추가 괄호 없이 제너레이터 표현식을 쓸 수 있다. 하지만 다른 모든 경우에는 괄호로 묶어줘야 한다.

이터러블의 문자열을 연결한 문자열을 리턴하므로 문자열로 형변환해주면 문자열 '1234'가 된다.

```py
''.join(str(x) for x in a)
```

```py
'1234'
```

참고:

[https://www.python.org/dev/peps/pep-0289/](https://www.python.org/dev/peps/pep-0289/)
[https://docs.python.org/3.8/library/stdtypes.html?#str.join](https://docs.python.org/3.8/library/stdtypes.html?#str.join)
[https://docs.python.org/3.8/library/functions.html#isinstance](https://docs.python.org/3.8/library/functions.html#isinstance)
[https://docs.python.org/3.8/library/collections.abc.html?#collections.abc.Iterable](https://docs.python.org/3.8/library/collections.abc.html?#collections.abc.Iterable)
