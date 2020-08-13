## 实现了三个方案

### 递归的实现

```C++
class Solution {
public:
    int hammingDistance(int x, int y) {
        if (x == 0 && y == 0)
            return 0;
        else return
        (x%2 ^ y%2) + hammingDistance(x / 2, y / 2); 
    }
};
```

### 迭代的实现

```C++
class Solution {//迭代实现
// 执行用时：
// 4 ms
// , 在所有 C++ 提交中击败了
// 25.19%
// 的用户
// 内存消耗：
// 6 MB
// , 在所有 C++ 提交中击败了
// 26.22%
// 的用户
public:
    int hammingDistance(int x, int y) {
        int ans = 0;
        while(x != 0 || y != 0){
            if(x % 2 ^ y % 2)ans++;
            x /= 2;
            y /= 2;
        }
        return ans;
    }
};
```

### 位运算

x 与 y按位异或运算得到n,然后再找出n中1的个数（这个是一个快速实现的模板问题）
```C++
class Solution {
// 执行用时：
// 0 ms
// , 在所有 C++ 提交中击败了
// 100.00%
// 的用户
// 内存消耗：
// 5.8 MB
// , 在所有 C++ 提交中击败了
// 73.09%
// 的用户
public:
    int hammingDistance(int x, int y) {
       int n = x ^ y;
       int cnt = 0;
       while (n){
           n = n & (n-1);
           cnt ++;
       }
       return cnt;
    }
};
```

