```c++ //DFS模板提
class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        int oralcolor = image[sr][sc];
        if (oralcolor == newColor)return image;
        help(image,sr,sc,newColor,oralcolor);
        return image;
    }
    void help(vector<vector<int>>& image, int sr, int sc, int newColor,int oralcolor){
        if(sr >= image.size() || sc >= image[0].size() || sr < 0||sc < 0 || image[sr][sc]!=oralcolor)
        return ;
        image[sr][sc] = newColor;
        help(image,sr+1,sc,newColor,oralcolor);
        help(image,sr,sc+1,newColor,oralcolor);
        help(image,sr-1,sc,newColor,oralcolor);
        help(image,sr,sc-1,newColor,oralcolor);   
    }
};
```