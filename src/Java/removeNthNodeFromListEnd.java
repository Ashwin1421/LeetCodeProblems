/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int i = 1, length=1;
        ListNode currentNode = head;
        ListNode previousNode = null;
        
        while(currentNode != null){
            length++;
            currentNode = currentNode.next;
        }
        currentNode = head;
        while(currentNode != null){
            if((length-i) == n){
                break;
            }else{
                previousNode = currentNode;
                currentNode = currentNode.next;
                i++;
            }
        }
        
        if(currentNode == null){
            return null;
        }else if(previousNode == null){
            head = currentNode.next;
        }else {
            previousNode.next = currentNode.next;
        }
        return head;
    }
}