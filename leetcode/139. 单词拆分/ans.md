```C++
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> dp(s.size()+1);
        dp[0] = true;
        auto wordset = unordered_set<string>();
        for (auto str:wordDict){
            wordset.insert(str);
        }
        for(int i=1;i<=s.size();i++){
            for(int j=0;j<i;j++){
                if(dp[j]&&wordset.find(s.substr(j,i-j))!=wordset.end()){
                    dp[i]=true;
                }
            }
        }
        return dp[s.size()];
    }
};
```