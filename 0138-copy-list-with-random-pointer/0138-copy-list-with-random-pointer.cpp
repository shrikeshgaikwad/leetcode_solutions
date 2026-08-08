class Solution {
public:
    Node* copyRandomList(Node* head) {

        if (head == NULL)
            return NULL;

        unordered_map<Node*, Node*> mp;

        // Step 1: Create copies of all nodes
        Node* current = head;

        while (current != NULL) {
            mp[current] = new Node(current->val);
            current = current->next;
        }

        // Step 2: Connect next and random pointers
        current = head;

        while (current != NULL) {

            mp[current]->next = mp[current->next];
            mp[current]->random = mp[current->random];

            current = current->next;
        }

        return mp[head];
    }
};