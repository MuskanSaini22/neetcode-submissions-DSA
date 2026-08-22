class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # empty string input
        if not digits:
            return []
        #digit to letter mapping
        digit_map={
            "2":"abc", "3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }
        res=[]
        path=[]

        def dfs(i):
            if i==len(digits):
                res.append("".join(path))
                return

            #find letters of current digit
            letters=digit_map[digits[i]]

            # har letter pe branch explore krna hai
            for char in letters:
                path.append(char)

                dfs(i+1)

                path.pop()
        
        dfs(0)
        return res