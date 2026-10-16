class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int p = 0;
        int b = 0;
        for (int s; s < prices.size(); s++){
            int temp = prices[s] - prices[b];
            p = max(p, temp);
            if (prices[s] < prices[b]){
                b = s;
            }
        }
        return p;
    }
};
