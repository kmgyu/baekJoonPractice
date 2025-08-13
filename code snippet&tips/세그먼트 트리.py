'''
https://book.acmicpc.net/ds/segment-tree
리프 노드를 제외한 다른 모든 노드는 항상 2개의 자식을 가집니다.
따라서, 세그먼트 트리는 Full Binary Tree의 형태를 가집니다.
만약, N이 2의 제곱꼴인 경우에는 Perfect Binary Tree가 됩니다.

리프 노드가  N개인 Full Binary Tree에는 리프 노드가 아닌 노드가 N-1개 있습니다.
따라서, 필요한 노드의 수는 2N-1개 있습니다. 
N이 2의 제곱꼴이 아닌 경우에 높이 H=ceil(logN)입니다.

세그먼트 트리의 정보를 저장하기 위해서 배열을 사용하겠습니다.
깊이가 가장 깊은 리프 노드와 가장 깊지 않은 리프 노드의 깊이 차이는 1보다 작거나 같습니다.
따라서, 배열을 이용해도 공간을 크게 낭비하지 않습니다.
tree[x]에 노드 x의 정보를 저장하겠습니다.

높이가 H인 Perfect Binary Tree에 있는 노드의 개수가 배열의 크기가 되고, 이 값은 2**(H+1)-1와 같습니다.
'''

# a: 배열 A
# tree: 세그먼트 트리
# node: 노드 번호
# node에 저장되어 있는 합의 범위가 start - end
def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]

'''
start == end인 경우는 리프 노드인 경우입니다.
리프 노드는 배열의 그 수를 저장해야 하기 때문에, tree[node] = a[start]가 됩니다.

node의 왼쪽 자식은 node*2이고, 오른쪽 자식은 node*2+1입니다.
또, node에 저장된 구간이 [start,end]라면, 왼쪽 자식은 [start,(start+end)/2], 오른쪽 자식은 [(start+end)/2+1,end]가 저장된 구간입니다.

tree[node]에 저장될 값을 구하려면 왼쪽 자식에 저장된 값 tree[node*2], 오른쪽 자식에 저장된 값 tree[node*2+1]을 먼저 구해야 합니다.
따라서, 재귀 함수를 이용해 각각의 값을 먼저 구했습니다.
'''

'''
구간의 합 구하기
구간 left, right가 주어졌을 때, 합을 구하려면 트리를 루트부터 순회하면서 각 노드에 저장된 구간의 정보와 left, right와의 관계를 살펴봐야 합니다.

node에 저장된 구간이 [start,end] 이고, 합을 구해야하는 구간이 [left,right]라면 다음과 같이 4가지 경우로 나누어질 수 있습니다.

[left,right]와 [start,end]가 겹치지 않는 경우
[left,right]가 [start,end]를 완전히 포함하는 경우
[start,end]가 [left,right]를 완전히 포함하는 경우
[left,right]와 [start,end]가 겹쳐져 있는 경우 (1, 2, 3 제외한 나머지 경우)
1번 경우는 if (left > end || right < start)로 나타낼 수 있습니다.
left > end는 [start,end] 뒤에 [left,right]가 있는 경우이고, right < start는 [start,end] 앞에 [left,right]가 있는 경우입니다.
이 경우에는 겹치지 않기 때문에, 더 이상 탐색을 이어나갈 필요가 없습니다.
따라서 0을 리턴해 탐색을 종료합니다.

2번 경우는 if (left <= start && end <= right)로 나타낼 수 있습니다. 이 경우도 더 이상 탐색을 이어나갈 필요가 없습니다.
구해야하는 합의 범위는 [left,right]인데, [start,end]는 그 범위에 모두 포함되고,
그 node의 자식도 모두 포함되기 때문에 더 이상 호출을 하는 것은 비효율적입니다.
따라서, tree[node]를 리턴해 탐색을 종료합니다.

3번과 4번의 경우에는 왼쪽 자식과 오른쪽 자식을 루트로 하는 트리에서 다시 탐색을 시작해야 합니다.

소스 3의 query는 세그먼트 트리에서 [left,right]의 합을 구하는 소스입니다.
'''

# 세그먼트 트리에서 [left, right] 구간 합 구하기
def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    lsum = query(tree, node*2, start, (start+end)//2, left, right)
    rsum = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return lsum + rsum



'''
수 변경하기
index번째 수를 val로 변경하는 경우, index번째를 포함하는 노드에 들어있는 합만 변경해주면 됩니다.

원래 index번째 수가 a[index]였고, 바뀐 수가 val이라면, 합은 val - a[index]만큼 변합니다.

수 변경은 다음과 같이 2가지 경우가 있습니다.

[start,end]에 index가 포함되는 경우
[start,end]에 index가 포함되지 않는 경우
1번 경우에만 재귀 호출을 진행하고, 2번 경우는 그 노드의 모든 자식도 index번째를 포함하지 않으니 재귀 호출을 중단하면 됩니다.

소스 4의 update(a, tree, index, val)은 index번째를 val로 변경하는 코드이고,
이 함수는 index번째를 포함하는 모든 노드의 합에 diff를 더해서 수를 변경하는 update_tree(tree, node, start, end, index, diff)를 호출하는 소스입니다.
'''
def update_tree(tree, node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] = tree[node] + diff
    if start != end:
        update_tree(tree, node*2, start, (start+end)//2, index, diff)
        update_tree(tree, node*2+1, (start+end)//2+1, end, index, diff)

def update(a, tree, n, index, val):
    diff = val - a[index]
    a[index] = val
    update_tree(tree, 1, 0, n-1, index, diff)

'''
수 변경하기 2
위에서 설명한 차이를 이용한 방법 이외에 다른 방법도 있습니다.
먼저, 리프 노드를 찾을때 까지 계속 재귀 호출을 이어나갑니다.
리프 노드를 찾으면 그 노드의 합을 변경해줍니다.
이후 리턴될때마다 각 노드의 합을 자식에 저장된 합을 이용해 다시 구하는 방법도 있습니다.

소스 5의 update(a, tree, node, start, end, index, val)은 이 방식을 구현한 소스입니다.
'''
def update(a, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        a[index] = val
        tree[node] = val
        return
    update(a, tree, node*2, start, (start+end)//2, index, val)
    update(a, tree, node*2+1, (start+end)//2+1, end, index, val)
    tree[node] = tree[node*2] + tree[node*2+1]
