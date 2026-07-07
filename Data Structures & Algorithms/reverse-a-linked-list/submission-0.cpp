// /**
//  * Definition for singly-linked list.
//  * struct ListNode {
//  *     int val;
//  *     ListNode *next;
//  *     ListNode() : val(0), next(nullptr) {}
//  *     ListNode(int x) : val(x), next(nullptr) {}
//  *     ListNode(int x, ListNode *next) : val(x), next(next) {}
//  * };
//  */

// class Solution {
// public:
//     ListNode* reverseList(ListNode* head) {
        
//         ListNode* prev = nullptr;
//         ListNode* current = head;
//         ListNode* next = nullptr;

//         while(current->next!=nullptr){

//             next = current->next;

//             current->next=prev;

//             prev = current;
//             current=next;

//         }

//         return prev;
    
//     }
// };

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* current = head;
        ListNode* next = nullptr;
        
        while (current != nullptr) {
            // 1. Store the next node
            next = current->next;
            
            // 2. Reverse the link
            current->next = prev;
            
            // 3. Advance pointers
            prev = current;
            current = next;
        }
        
        // After the loop, prev will be the new head
        return prev;
    }
};