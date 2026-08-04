class Solution {
public:
    vector<int> findMissingElements(vector<int>& a) 
    {
        int smallest = INT_MAX ;
        int largest = INT_MIN ;
        vector<int>ans;
        for(int i : a)
        {
            if (i < smallest) smallest = i ;
            if (i > largest) largest = i;
        }

        for(int i =smallest ; i <= largest; i++)
        {
            ans.push_back(i);
            for(int j : a)
            {
                if (j==i)ans.pop_back();
            }

        }
        
        return ans;
    }
};