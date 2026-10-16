class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m; // {num : idx}
        for (int i = 0; i < nums.size(); i++){
            int temp = target - nums[i];
            if (m.count(temp)) {
                vector<int> res = {m[temp], i};
                return res;
            }
            m[nums[i]] = i;
        }
    }
};
