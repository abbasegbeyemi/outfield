from psolv_ch_4.psolv_ch_4_ADT import Stack

# Infix to postfix algo
# 1. Modify the algorithm to handle errors
prec = {
    "^": 4,
    "/": 3,
    "*": 3,
    "-": 2,
    "+": 3,
    "(": 1
}
permittedOperators = list(prec.keys())
permittedOperators.append(")")


def infixToPostfix(expression: str) -> str:
    if not expression.strip():
        raise ValueError("Enter something bitch.")

    inputExpression = []

    for c in expression.split(" "):
        if not checkTokenType(c):
            raise ValueError("What you have entered is nonsense. Add a space between tokens and operators."
                             "Also you might be using an unpermitted operator.")

        inputExpression.append(c)

    # Quick check to make sure no error in the expression
    c = 0
    while c < len(inputExpression) - 1:
        if checkTokenType(inputExpression[c]) == "n":
            if checkTokenType(inputExpression[c + 1]) != "o":
                raise ArithmeticError("Invalid Expression operator should follow token.")

        elif checkTokenType(inputExpression[c]) == "o":
            if checkTokenType(inputExpression[c + 1]) != "n" \
                    and inputExpression[c + 1] not in "()" \
                    and inputExpression[c] not in "()":
                raise ArithmeticError("Invalid Expression token should follow operator.")
        else:
            raise ArithmeticError("You are dumb")
        c += 1

    operatorStrack = Stack()
    outputList = []

    for e in inputExpression:
        if checkTokenType(e) == "n":
            outputList.append(e)
        elif e == "(":
            operatorStrack.push(e)
        elif e == ")":
            try:
                topOperator = operatorStrack.pop()
            except IndexError:
                raise IndexError(f"Unblanced parenthesis in {expression}")

            while topOperator != "(":
                outputList.append(topOperator)
                topOperator = operatorStrack.pop()
        else:
            while (not operatorStrack.isEmpty()) and prec[operatorStrack.peek()] >= prec[e]:
                outputList.append(operatorStrack.pop())
            operatorStrack.push(e)

    while not operatorStrack.isEmpty() and operatorStrack.peek() not in "()":
        outputList.append(operatorStrack.pop())

    return " ".join(outputList)


def checkTokenType(token):
    if token in permittedOperators:
        return "o"
    elif type(float(token)) is float:
        return "n"
    else:
        return None


def postfixEvaluation(expression: str) -> float:
    operandStack = Stack()
    inputExpression = expression.split(" ")

    for token in inputExpression:
        if checkTokenType(token) == "n":
            operandStack.push(float(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()

            result = evaluateMath(token, operand1, operand2)
            operandStack.push(result)

    return operandStack.pop()


def calculator(expression: str) -> float:
    postfixExpr = infixToPostfix(expression)
    return postfixEvaluation(postfixExpr)


def evaluateMath(operator: str, operand1: float, operand2: float) -> float:
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "^":
        return operand1 ** operand2
    else:
        return operand1 / operand2


if __name__ == '__main__':
    print(calculator("( 1 + 2 ) - 3 / ( 4 ^ 2 )"))
