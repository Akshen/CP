
int Solution::lPalin(ListNode* A) {
    /// 1 2 3 4 3 2 1
    ///find mid
    // create secondlist by going from mid+1 till null 
    // compare first list to first of secondList till mid
    // if != return 0 else return 1
    
    ListNode *slow = A;
    ListNode *fast = A;
    ListNode *slowp = NULL;
    
    
    while(fast!=NULL and fast->next!=NULL){
        slowp = slow;
        slow = slow->next;
        fast = fast->next->next;
    }
    
    ListNode *secondL = slow;
    if(fast!=NULL){
        secondL = slow ->next;
        slow->next = NULL;
    } else {
        slowp->next = NULL;
        secondL = slow;
    }
    
    
   // ListNode *dummy = new ListNode(0);
    ListNode *prev = NULL;
    ListNode *now = secondL;
    ListNode *next;
    
    while(now!=NULL){
        next = now->next;
        now->next = prev;
        prev = now; 
        now = next;
    }
    
    
    ListNode *fp = A;
    ListNode *sp = prev;
    
    while(fp!= NULL and sp!=NULL){
        if(fp->val != sp->val){
            return false;
        }
        fp = fp->next;
        sp = sp->next;
    }
        
    return 1;
    
}
