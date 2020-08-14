```C++ 
//栈
class Solution {
public:
    bool isValid(string s) {
        stack<char> left;
        for(int i=0;i<s.size();i++){
            if (s[i]=='('||s[i]=='{'||s[i]=='['){
                left.push(s[i]);
            }else{
                if(s[i]==')'){
                    if (left.empty()){
                        return false;
                    }
                    char t = left.top();
                    left.pop();
                    if (t!='('){
                        return false;
                    }
                }else if (s[i]==']'){
                    if (left.empty()){
                        return false;
                    }
                    char t = left.top();
                    left.pop();
                    if(t!='['){
                        return false;
                    }
                }else {
                    if (left.empty()){
                        return false;
                    }
                    char t = left.top();
                    left.pop();
                    if(t!='{'){
                        return false;
                    }
                }
            }
        }
        return left.empty();       
    }
};
```
