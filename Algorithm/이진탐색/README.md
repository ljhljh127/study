# 이진탐색

리스트 내에서 데이터를 매우 빠르게 탐색하는 알고리즘

# 트리
- 트리는 부모노드와 자식 노드의 관계로 표현된다.
- 트리의 최상단 노드를 루트 노드라고 한다.
- 트리의 최하단 노드를 단말 노드라고 한다.
- 트리에서 일부를 떼어내도 트리 구조이며 이를 서브 트리라고 한다.
- 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다.

# 이진탐색 트리
- 부모노드보다 왼쪽 자식노드가 작다.
- 부모 노드보다 오른쪽 자식 노드가 크다.

# 빠르게 입력 받는 방법
sys라이브러리의 readline()을 이용하여 시간초과를 피할 수 있다.
```python
import sys
input_data = sys.stdin.readline().rstrip()
print(input_data)
```
enter키가 줄바꿈으로 입력되므로 이 공백 문자를 제거하기 위하여 rtsrip사용