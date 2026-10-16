class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size()-1;
        while (l < r){
            int guess = numbers[l] + numbers[r];
            if (guess == target){
                vector<int> res = {l+1, r+1};
                return res;
            }
            else if (guess < target){
                l++;
            }
            else {
                r--;
            }
        }
    }
};
