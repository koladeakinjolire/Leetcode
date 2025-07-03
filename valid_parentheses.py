def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        #Stack to store opening brackets
        stack = []
        #Dictionary to map closing to opening brackets
        brackets_map = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        #Set of opening brackets
        opening_brackets = set(['(','[','{'])

        #Iterate thrpugh each character in the string
        for char in s:
            if char in opening_brackets:
                #If its the opening bracket, push it to the stack
                stack.append(char)
            elif char in brackets_map:
                #If its a closing bracket, check if the stack is empty or mismatched
                if not stack:
                    return False
                #Pop the last opening bracket and check if it matches
                last_opening = stack.pop()
                if brackets_map[char] != last_opening:
                    return False
        #Check if  at least one pair was formed 
        return len(stack) == 0 and len(s) >= 2