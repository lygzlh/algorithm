class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict1 = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        # dict1 = {
        #     '2': 'abc',
        #     '3': 'def',
        #     '4': 'ghi',
        #     '5': 'jkl',
        #     '6': 'mno',
        #     '7': 'pqrs',
        #     '8': 'tuv',
        #     '9': 'wxyz',
        # }

        def backtrack(conn, next_num):
            if len(next_num) == 0:
                res.append(conn)
            else:
                for i in dict1[next_num[0]]:
                    backtrack(conn + i, next_num[1:])

        res = []
        if digits:
            backtrack('', digits)
        return res

s = Solution()
print(s.letterCombinations('23'))