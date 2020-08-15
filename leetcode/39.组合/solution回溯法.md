class Solution(object):
    def helper(self,candidates,target,level,tmp,res):
        for i in range(level,len(candidates)):
            tmp.append(candidates[i])
            if candidates[i]<target:
                self.helper(candidates,target-candidates[i],i,tmp,res)
            elif candidates[i]==target:
                res.append(tmp[:])
            tmp.pop()


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        self.helper(candidates,target,0,[],res)
        return res
        
#组合1,2,3都是一样的思路，对level进行循环，不同的是，下一个level的取值问题，如果要去重的话，
下一个level就要从i+1取，如果是取子集的话，就从level+1取。
#子集也是一样的思路。
