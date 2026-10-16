class Solution {
public:
    int maxArea(vector<int>& heights) {
        int max_water = 0;
        int l = 0;
        int r = heights.size()-1;
        while (l < r){
            int w = (r - l) * min(heights[l], heights[r]);
            max_water = max(max_water, w);
            if (heights[l] < heights[r]){
                l++;
            }
            else {
                r--;
            };
        }
        return max_water;
    }
};
