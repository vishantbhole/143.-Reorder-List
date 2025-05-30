

class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None. Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        # Step 1: Find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Step 3: Merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
# ---------- Test Cases Below ----------

def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head



class TestReorderList(unittest.TestCase):
    def test_example1(self):
        head = list_to_linkedlist([1, 2, 3, 4])
        Solution().reorderList(head)
        self.assertEqual(linkedlist_to_list(head), [1, 4, 2, 3])

    def test_example2(self):
        head = list_to_linkedlist([1, 2, 3, 4, 5])
        Solution().reorderList(head)
        self.assertEqual(linkedlist_to_list(head), [1, 5, 2, 4, 3])

    def test_single_node(self):
        head = list_to_linkedlist([1])
        Solution().reorderList(head)
        self.assertEqual(linkedlist_to_list(head), [1])

    def test_two_nodes(self):
        head = list_to_linkedlist([1, 2])
        Solution().reorderList(head)
        self.assertEqual(linkedlist_to_list(head), [1, 2])

    def test_empty(self):
        head = list_to_linkedlist([])
        Solution().reorderList(head)
        self.assertEqual(linkedlist_to_list(head), [])

# Run tests when the script is executed
if __name__ == "__main__":
    unittest.main()

