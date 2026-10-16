class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0;
        set<int> hash;
        int res = 0;

        for (int r=0; r<s.length(); r++){
            if (!hash.contains(s[r])){
                hash.insert(s[r]);
            } else {
                while (hash.contains(s[r])){
                    hash.erase(s[l]);
                    l++;
                }
                hash.insert(s[r]);
            }
            res = max(res, (r-l)+1);
        }
        return res;
    }
};
