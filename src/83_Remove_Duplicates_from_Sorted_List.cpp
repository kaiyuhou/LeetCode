class Solution {
public:
    ListNode *deleteDuplicates(ListNode *head) {
        ListNode *p = head, *q = head;
        while(p){
            if(!q) {
                p->next = NULL;
                break;
            }
            else if(p-> val != q-> val){
                p->next = q;
                p = p->next;
            }
            q = q->next;
        }
        return head;
    }
};