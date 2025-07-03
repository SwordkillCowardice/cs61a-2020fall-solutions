def calc_eval(exp):
    if isinstance(exp, Pair):
        if exp.first == 'and': # and expressions
            return eval_and(exp.rest)
        else: # Call expressions
            return calc_apply(calc_eval(exp.first), list(exp.rest.map(calc_eval)))
    elif exp in OPERATORS: # Names
        return OPERATORS[exp]
    else: # Numbers
        return exp
    
    
def eval_and(operands):
    if operands == nil:
         return True
    elif operands.rest == nil:
        return calc_eval(operands.first)
    elif calc_eval(operands.first):
        return eval_and(operands.rest)
    return False