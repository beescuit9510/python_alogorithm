def isAnagram(s, t):
    return sorted(list(s)) == sorted(list(t))


print(isAnagram("ate", "tae"))


def groupAnagrams(strs):
    str_dict = {}

    for str in strs:
        str_list = sorted(list(str))
        key = ''.join(str_list)

        if str_dict.get(key) == None:
            str_dict.update({key: []})

        str_dict[key].append(str)

    return str_dict.values()


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


def isValid(s):
    s_list = list(s)

    if (len(s_list) % 2 != 0):
        return False

    stack = []
    parentheses = {'(': ')', '{': '}', '[': ']'}
    open_parentheses = parentheses.keys()

    for parenthes in s_list:

        if parenthes in open_parentheses:
            stack.append(parenthes)

        elif len(stack) > 0 and parentheses[stack[-1]] == parenthes:
            stack.pop()

        else:
            return False

    return len(stack) == 0


print(isValid("()[]{}{}}"))


def isPalindrome(s):
    filtered = [char.lower() for char in filter(str.isalnum, s)]
    reversed_filtered = [char for char in reversed(filtered)]
    return filtered == reversed_filtered


print(isPalindrome("A man, a plan, a canal: Panama"))
