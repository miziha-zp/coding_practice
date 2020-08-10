class Solution {
public:
    int countBinarySubstrings(string s) {
        if (s.size() <= 1)
            return 0;
        char before_state = s[0];
        int before_count = 1;
        int cnt = 0;
        int index = 1;
        while(s[index] == s[index-1]){
                index ++;
                before_count ++;
        }
        
        while(index < s.size()){
            int cur_count = 1;
            index ++;
            while(s[index] == s[index-1] && index < s.size()){
                index ++;
                cur_count ++;
            }
            cnt += min(cur_count,before_count);
            before_count = cur_count;
        }

        return  cnt;
    }
};