class Solution {
public:
    ListNode *deleteDuplicates(ListNode *head) {
        ListNode *dummy =new ListNode(-1);
        dummy->next = head;
        ListNode *p = dummy, *q = dummy->next;
        while(p){
            if(!q) {
                p->next = NULL;
                break;
            }
            int current = q->val;
            bool isDuplicate = false;
            while(q->next && q->next->val == current){
                q = q->next;
                isDuplicate = true;
            }
            if(isDuplicate){
                p->next = q->next;
            }else{
                p = p->next;

            }
            q = q->next;
        }
        return dummy->next;
    }
};