class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def checker(string1, string2):
            s = set(string1)
            for i in string2:
                if(i in s):
                    return False
            return True
        @cache
        def f(i, string):
            if(i<0):
                return len(string)
            choose = 0
            notchoose = 0
            if(checker(string, arr[i]) and len(set(arr[i]))==len(arr[i])):
                choose = f(i-1, arr[i]+string)
            notchoose = f(i-1, string)
            return max(choose, notchoose)
        return f(len(arr)-1, "")