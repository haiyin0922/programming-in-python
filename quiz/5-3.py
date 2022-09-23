class Polynomial:
    def __init__(self, *coeff):
        # your code here to remember the coefficients
        self._coeff = list(coeff)

    def evaluate(self, xvalue):
        # return the sum of coefficienti * xvaluei
        sum = 0
        for i, v in enumerate(self._coeff):
            sum += v * (xvalue ** i)

        return sum

    def change_coefficient(self, i, coeff):
        # change the coefficient of the i-th term
        self._coeff[i] = coeff

 # MUST add the 6 lines below
instantiate_statement = input()
exec(instantiate_statement)
change_coeff_call = input()
exec(change_coeff_call)
print_evaluate = input()
exec(print_evaluate)
