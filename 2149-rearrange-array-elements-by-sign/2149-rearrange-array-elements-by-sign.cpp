class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> positives;
        vector<int> negatives;

        for (int num : nums) {
            if (num > 0)
                positives.push_back(num);
            else
                negatives.push_back(num);
        }

        int j = 0;
        for (int i = 0; i < positives.size(); i++) {
            nums[j] = positives[i];
            nums[j + 1] = negatives[i];
            j += 2;
        }

        return nums;
    }
};