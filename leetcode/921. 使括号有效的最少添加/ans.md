```C++
class Solution {
public:
    int minAddToMakeValid(string S) {
        int count0 = 0;
        int ans = 0;
        for(auto s:S){
            if(s=='('){
                count0 ++;
            }else{
                if (count0){
                    count0 --;
                }else{
                    ans ++;
                }
            }
        }
        ans += count0;
        return ans;
    }
};
```