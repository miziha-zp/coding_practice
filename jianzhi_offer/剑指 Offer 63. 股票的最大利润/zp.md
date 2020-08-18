```C++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxValue = 0;
        int curMinValue = 1e9;
        for(int price:prices){
            curMinValue = min(curMinValue,price);
            maxValue = max(maxValue,price - curMinValue);
        }
        return maxValue;
    }
};
```