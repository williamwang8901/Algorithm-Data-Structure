import pdb
class Solution(object):

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if input is None or len(input) == 0:
            return 0
        map = dict()
        map[0] = 0
        res = 0
        for str in input.split('\n'):
            level = str.rfind('\t') + 1 if str.rfind('\t') is not -1 else 0
            length = len(str[level:])
            if '.' in str:
                res = max(res, map.get(level) + length)
            else:
                map[level + 1] = map.get(level) + length + 1

        return res

    def lengthLongestPath(self, input):
        if input is None or len(input ):
            return 0
        res = 0
        map = {0 : 0}
        level = 0
        for i, item in enumerate(input):
            start = i
            while (i)



if __name__ == '__main__':
    str = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
    solution = Solution()
    print solution.lengthLongestPath(str)

class Solution {
public:
    int lengthLongestPath(string input) {
        int res = 0, n = input.size(), level = 0;
        unordered_map<int, int> m {{0, 0}};
        for (int i = 0; i < n; ++i) {
            int start = i;
            while (i < n && input[i] != '\n' && input[i] != '\t') ++i;
            if (i >= n || input[i] == '\n') {
                string t = input.substr(start, i - start);
                if (t.find('.') != string::npos) {
                    res = max(res, m[level] + (int)t.size());
                } else {
                    ++level;
                    m[level] = m[level - 1] + (int)t.size() + 1;
                }
                level = 0;
            } else {
                ++level;
            }
        }
        return res;
    }
};