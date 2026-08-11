/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) 
    {
        if(head == NULL || head->next == NULL)return head; 
        ListNode * temp = head; 
        ListNode* current = NULL;

        while(temp->next != NULL)
        {
            current = temp->next ; 

            while(current != NULL)
            {
                if(temp->val > current->val)
                {
                    int i = temp->val ;
                    temp->val = current->val ;
                    current->val = i ; 
                }
                current = current->next;
            }
            temp = temp->next ;
        }

        
        return head;
    }
};