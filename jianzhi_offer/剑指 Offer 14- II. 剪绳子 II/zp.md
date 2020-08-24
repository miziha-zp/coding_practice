```C++  // 数学推导 + 快速幂
class Solution {
public:
    long long int qick_power(int a,int b,int mod){
        long long ans = 1;
        long long aa = a;
        while(b){
            if(b%2){
                ans *= aa;
            }
            aa *= aa;
            aa %= mod;
            ans %= mod;
            b /= 2;
        }
        return ans;
    }
    int cuttingRope(int n) {
        if(n==2)return 1;
        if(n==3)return 2;
        if(n==4)return 4;
        if(n==5)return 6;
        int mod = 1e9 + 7;
        // int ans = 1;
        int l = n / 3;
        if(n % 3 == 0){
            return qick_power(3,l,mod);
        }else if(n % 3 == 1){
            long long ans = (qick_power(3,l-1,mod) * 4) % mod;
            return ans; 
        }else{
            long long ans = qick_power(3,l,mod) * 2 % mod;
            return ans;
            
        }
    }
};
```