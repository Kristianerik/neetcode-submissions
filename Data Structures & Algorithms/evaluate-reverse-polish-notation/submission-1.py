class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Input list str = ["1","2","+","3","*","4","-"]
        stack = []
        
        for element in tokens:
            if element not in "+-*/":
                stack.append(int(element))
            else:
                b = stack.pop()
                a = stack.pop()
                if element == "+":
                    stack.append(a+b)
                elif element == "-":
                    stack.append(a-b)
                elif element == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        
        return stack[0]
        #Output answer = Int Result of given expression