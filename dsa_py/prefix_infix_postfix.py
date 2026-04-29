# #infix to postfix conversion

# def prec(c):
#     if c == 'A':
#         return 3
    
#     elif c == '/' or c == '*':
#         return 2
    
#     elif c == '+' or c == '-':
#         return 1
    
#     else:
#         return -1
    
# def infixToPostfix(s):
#     stack = []
#     result = ""

#     for c in s:
#         if c.isalnum():
#             result += c

#         elif c == '(':
#             stack.append('(')

#         elif c == ')':
#             while stack and stack[-1] != '(':
#                 result += stack.pop()
#                 stack.pop()

#         else:
#             while stack and prec(c) <= prec(stack[-1]):
#                 result += stack.pop()
#                 stack.append(c)

#         while stack:
#             result += stack.pop()

#         print(f"postfix expression: {result}")

# if __name__ == "__main__":
#     exp = "(p+q)*(m-n)"   # infix expression

#     print(f"Infix expression: {exp}")
#     infixToPostfix(exp)
#time complexity O(N)
#space complexity O(N)

# prefix to infix conversion

# def prefix_to_infix(prefix):
#     stack = []

#     for c in reversed(prefix):
#         if c.isalnum():
#             stack.append(c)

#         else:
#             op1 = stack.pop()
#             op2 = stack.pop()

#             stack.append(f"({op1}{c}{op2})")

#         return stack[-1]
    
# def main():
#     prefix = "*-A/BC-/AKL"
#     print("Infix Expression:", prefix_to_infix(prefix))

# if __name__ == "__main__":
#     main()
# # time complexity O(N)
# # space compesity O(N)


# # prefix to postfix conversion

# # prefix to postfix conversion

# def prefix_to_postfix(prefix):
#     stack = []

#     for c in reversed(prefix):
#         if c.isalnum():
#             stack.append(c)

#         else:
#             op1 = stack.pop()
#             op2 = stack.pop()

#             stack.append(op1 + op2 + c)

#         return stack[-1]
    
# def main():
#     prefix = "*-A/BC-/AKL"
#     print("Postfix Expression:", prefix_to_postfix(prefix))

# if __name__ == "__main__":
#     main()

# postfix to prefix conversion

# def postfix_to_prefix(postfix):
#     stack = []

#     for c in postfix:
#         if c.isalnum():
#             stack.append(c)

#         else:

#             op2 = stack.pop()
#             op1 = stack.pop()

#             stack.append(c + op1 + op2)

#         return stack[-1]
    
# def main():
#     postfix = "ABC/-AKL-*"
#     print("Prefix Expression:", postfix_to_prefix(postfix))

# if __name__ == "__main__":
#     main()

#TIME COMPLEXITY O(N)
#SPACE COMPEXITY O(N)

# postfix to infix

def postfix_to_infix(postfix):
    stack = []

    for c in postfix:

        if c.isalnum():
            stack.append(c)

        else:
            op2 = stack.pop()
            op1 = stack.pop()

            stack.append(f"{op1}{op2}{c}")

    return stack[-1]

def main():
    postfix = "AB*C+"
    print("Infix Expression:", postfix_to_infix(postfix))

if __name__ == "__main__":
    main()

#time comlexity O(N)
#space compexity O(N)

# infix to prefix 

#What is an Infix Expression?
#The traditional method of writing mathematical expressions is called infix expressions.
#It is written as . The operator is placed between two operands (e.g., A+B or (A*B)/Q).
#Infix expressions are easy to understand and evaluate for humans but hard for computers to parse due to operator precedence, associativity rules, and parentheses.
#To make parsing easier for computers, we use postfix and prefix notations.
#What is a Prefix Expression?
#In a prefix expression, the operator is placed before the operands.
#The expression is in the form .
#Prefix expressions work similarly to postfix expressions. While evaluating, operators are applied immediately to the operands on the right of the operator.
#Prefix expressions are also called Polish notation.
#Approach to Convert Infix Expression to Prefix:
#Reverse the given infix expression.
#Scan the expression from left to right.
#When an operand is encountered, print it directly.
#If the operator is encountered and the stack is empty, push the operator into the stack.
#If the incoming operator has higher precedence than the top of the stack, push it into the stack.
#If the incoming operator has the same precedence as the top of the stack, push it into the stack.
#If the incoming operator has lower precedence than the top of the stack, pop and print the top of the stack. Then, test the incoming operator against the top of the stack again and continue popping operators from the stack until it finds an operator with lower or the same precedence.
#If the incoming operator has the same precedence as the top of the stack and the incoming operator is '^', pop the top of the stack until the condition is met. If not, push the '^' operator.
#If the operator is ')', push it into the stack.
#If the operator is '(', pop all operators from the stack until a ')' is encountered.
#If the top of the stack is ')', push the operator onto the stack.
#At the end of the expression, pop and print all remaining operators from the stack.
#Finally, reverse the output and print it as the prefix expression.

def getPriority(C):
    if C == '^':
        return 3
    
    elif C == '*' or C == '/':
        return 2
    
    elif C == '+' or C == '-':
        return 1
    
    return 0

def infixToPostfix(infix):
    infix = '(' + infix + ')'
    stack = []
    result = ""

    for c in infix:
        if c.isalnum():
            result += c
        
        elif c == '(':
            stack.append('(')

        elif c == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

        else:
            while stack and getPriority(c) <= getPriority(stack[-1]):
                result += stack.pop()
            stack.append(c)
    
    while stack:
        result += stack.pop()

    return result 

def infixToPrefix(infix):
    infix = infix[::-1]

    infix = infix.replace('(', 'temp').replace(')', '(').replace('temp', ')')

    prefix = infixToPostfix(infix)

    return prefix[::-1]

if __name__ == "__main__":
    exp = "(p+q)*(c-d)"   # infix expression
    print(f"Infix expression: {exp}")
    print(f"Prefix Expression: {infixToPrefix(exp)}")   # output the prefix expression

#time complexity O(n)
#space complexity O(n)