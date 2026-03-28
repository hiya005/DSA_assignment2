def check_parenthesis(expr):
    stack = []

    for ch in expr:
        if ch in "{[(":
            stack.append(ch)

        elif ch in "}])":
            if not stack:
                return False

            top = stack[-1]

            if ch == "}":
                if top != "{":
                    return False
            elif ch == "]":
                if top != "[":
                    return False
            elif ch == ")":
                if top != "(":
                    return False

            stack.pop()

    return len(stack) == 0


def main():
    expression = "({[]})"
    print(check_parenthesis(expression))


if __name__ == "__main__":
    main()