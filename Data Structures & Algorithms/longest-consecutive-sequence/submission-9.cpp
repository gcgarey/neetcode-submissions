class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> s(nums.begin(), nums.end());
        // create a result int
        int res = 0;

        // loop through each num
        for (const auto& n : nums){
            if (!s.contains(n - 1)){
                int temp_ct = n;
                int temp_sq = 0;
                while ((s.contains(temp_ct))){
                    temp_ct++;
                    temp_sq++;
                }
                if (temp_sq > res){
                    res = temp_sq;
                }
            }
        }
        return res;
    }
};
