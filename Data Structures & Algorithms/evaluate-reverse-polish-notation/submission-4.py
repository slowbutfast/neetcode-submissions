from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        use stack to maintain list of last seen numbers. we then push
        the total the stack to become the next operand

        we apply the selected operation to the last two numbers
        """
        operators = {"+","-","*","/"}
        token_stack = deque()

        for token in tokens:
            if token not in operators:
                token_stack.append(token)
            else:
                # print(token_stack)
                num1 = int(token_stack.pop())
                num2 = int(token_stack.pop())
                total = 0

                match token:
                    case "+":
                        total = num1 + num2
                    case "-":
                        total = num2 - num1
                    case "*":
                        total = num1 * num2
                    case "/":
                        total = num2 / num1

                # print(total)
                token_stack.append(total)


        # final total will be the remaining value on the stack
        return int(token_stack[0])