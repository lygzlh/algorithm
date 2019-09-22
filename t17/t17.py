class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        使用字典来进行初始化值，res来作为保存数组。
        backtrack递归函数，当next_num为空结束，把conn加进res中。不为空时，字符串拼接和取next_num之后的数作为参数传入backtrack中。
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

'''
测试结果
s = Solution()
print(s.letterCombinations('23'))
'''
