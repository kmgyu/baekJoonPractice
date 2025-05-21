import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def tree_maker(b_l, in_idx, post_idx):
    root_val = postorder[post_idx[-1]-1]
    in_root_idx = order_dict[root_val]
    print(root_val, end=' ')
    if b_l == 1: return
    inorder_left = (in_idx[0], in_root_idx)
    inorder_right = (in_root_idx+1, in_idx[1])
    
    left_length = max(in_root_idx-in_idx[0],0)
    right_length = max(in_idx[1]-in_root_idx-1,0)
    
    postorder_left = (post_idx[0], post_idx[0]+left_length)
    postorder_right = (post_idx[0]+left_length, post_idx[-1]-1)
    
    if left_length: tree_maker(left_length, inorder_left, postorder_left)
    if right_length: tree_maker(right_length, inorder_right, postorder_right)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
order_dict = {v:i for i,v in enumerate(inorder)}

tree_maker(n, (0,n), (0,n))