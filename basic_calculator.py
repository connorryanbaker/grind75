def calculate(s: str) -> int:
    s = s.replace(" ", "")
    values, operators = [], []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            values.append(int(s[i:j]))
            i = j
        elif s[i] == '+':
            operators.append(s[i])
            i += 1
        elif s[i] == '-':
            if len(operators) == 0 and len(values) == 0:
                j = i + 1
                if s[j] == '(':
                    k = close_parens_idx(s, j)
                    values.append(-1 * calculate(s[j+i:k]))
                    i = k
                else:
                    while j < len(s) and s[j].isdigit():
                        j += 1
                    values.append(-1 * int(s[i+1:j]))
                    i = j
            else:
                operators.append(s[i])
                i += 1
        elif s[i] == '(':
            j = close_parens_idx(s, i)
            values.append(calculate(s[i+1:j]))
            i = j
        else:
            i += 1
    while operators:
        operator = operators.pop(0)
        if operator == '+': 
            x, y = values.pop(0), values.pop(0)
            values = [x + y] + values
        else:
            if len(values) == 1:
                return - 1 * values[0]
            x, y = values.pop(0), values.pop(0)
            values = [x - y] + values
    return values[0]

def close_parens_idx(s: str, i: int) -> int:
    open_paren = 1
    j = i + 1
    while j < len(s):
        if s[j] == ')':
            open_paren -= 1
            if open_paren == 0:
                break
        elif s[j] == '(':
            open_paren += 1

        j += 1
    return j

print(calculate("- (3 + (4 + 5))"))