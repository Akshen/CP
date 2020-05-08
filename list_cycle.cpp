
ListNode* Solution::detectCycle(ListNode* A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    
    ListNode *slow = A;
    ListNode *fast = A;
    bool cycle=false;
    while(fast!=NULL and fast->next!=NULL){
        slow = slow->next;
        fast=fast->next->next;        
        if(fast==slow){
            cycle=true;
            break;
        }
     }
        if(cycle){
            slow = A;
            while(slow!=fast){
                slow = slow->next;
                fast = fast->next;
            }
            return slow;
        }
        else {
            return NULL;
        }
}
