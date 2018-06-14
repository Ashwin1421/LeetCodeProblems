/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode sum = new ListNode(0);
        ListNode a = l1, b = l2, currentNode = sum;
        int carry = 0;
        while(a!=null || b!=null){
            int sum1 = a!=null ? a.val : 0;
            int sum2 = b!=null ? b.val : 0;
            int total_sum = sum1+sum2+carry;
            carry = total_sum / 10;
            
            
            currentNode.next = new ListNode(total_sum % 10);
            currentNode = currentNode.next;
            if(a!=null){
                a = a.next;
            }
            if(b!=null){
                b = b.next;
            }
        }
        if(carry > 0){
            currentNode.next = new ListNode(carry);
        }
        return sum.next;
    }
}