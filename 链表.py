# 定义节点
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
# 遍历
def itera(root):
    p = root
    while(p):
        print(p.data,end=' ')
        p = p.next

if __name__ == '__main__':
    # 初始化链表
    root = Node(1)
    root1 = Node(2)
    root2 = Node(3)
    root.next = root1
    root1.next = root2
    #print(root.next.data)
    itera(root)
