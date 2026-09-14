# 2130. Maximum Twin Sum of a Linked List


class Solution:
    def pairSum(self, head):
        arr = []

        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        n = len(arr)
        ans = 0

        for i in range(n // 2):
            ans = max(ans, arr[i] + arr[n - 1 - i])

        return ans 
