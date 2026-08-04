class Solution {
public:
    vector<vector<int>> generate(int n) 
    {
        vector<vector<int>>a(n);
        for (int i = 0; i < n ; i++)
        {
            a[i].resize(i+1,0);
        }

        for(int i = 0 ; i < n; i++)
        {
            for(int j = 0 ; j < i +1 ; j++)
            {
                if (j == 0 or j == i)a[i][j] = 1 ;
                else
                {
                    a[i][j] = a[i-1][j-1] + a[i-1][j];
                } 
                    cout<<a[i][j]<<endl;
            }
        }   
        return a ;  
    }
};