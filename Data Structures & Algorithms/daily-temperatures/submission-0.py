class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res=[0]*len(temp)
        stack=[]
        for i,t in enumerate(temp):
            while stack and t>temp[stack[-1]]:
                prev_i=stack.pop()
                res[prev_i]=i-prev_i
            stack.append(i)  
        return res     
        