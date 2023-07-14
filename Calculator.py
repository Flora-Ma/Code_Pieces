
def calculate(input: list):
    stack = []
    num, operator = 0, '+'

    def update(op, number):
        if op == '*':
            stack.append(stack.pop() * number)
        elif op == '/':
            stack.append(stack.pop() / number)
        elif op == '-':
            stack.append(-number)
        else:
            stack.append(number)

    for s in input:
        if s.isdigit():
            num = int(s)
        elif s in '+-*/':
            update(operator, num)
            operator = s
        elif s == '(':
            stack.append(operator)
            operator = '+'
        elif s == ')':
            update(operator, num)
            ssum = 0
            while stack:
                item = stack.pop()
                if isinstance(item, str):
                    operator = item
                    num = ssum
                    break
                else:
                    ssum += item
    update(operator, num)
    return sum(stack)

        
print(calculate(['(', '4', '+', '5', ')', '*', '6'])) # 54
print(calculate(['6', '/', '2', '+', '4', '*', '3'])) # 15
print(calculate(['6', '/', '(', '2', '+', '4', ')', '*', '3'])) # 3