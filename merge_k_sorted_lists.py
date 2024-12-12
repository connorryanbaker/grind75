from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None
    dummy = ListNode()
    curr = dummy
    while True:
        minv = float('inf')
        minn = None
        minidx = None
        for i in range(len(lists)):
            if lists[i] and lists[i].val < minv:
                minv = lists[i].val
                minn = lists[i]
                minidx = i
        if not minn:
            break
        curr.next = minn
        lists[minidx] = lists[minidx].next
        curr = curr.next
    return dummy.next
