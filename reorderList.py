#143. Reorder List

import unittest

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # For easy test output
    def __repr__(self):
        result = []
        node = self
        while node:
            result.append(str(node.val))
            node = node.next
        return "->".join(result)
