
"""
The following formula is used to calculate the fixed monthly payment (P)
required to fully amortize a loan of L dollars over a term of n months at a
monthly interest rate of c. [If the quoted rate is 6%, for example, c is .06/12
or .005].

P = L[c(1 + c)n]/[(1 + c)n - 1]

"""

class LoanCalculator():
    @staticmethod
    def getMortgagePayment(loanAmount, numYears, interestRate):
        interestRate = interestRate/12
        numMonths = numYears*12
        numerator = loanAmount * (interestRate * (1 + interestRate) ** numMonths)
        denominator = ((1 + interestRate) ** numMonths - 1)
        return numerator/denominator

    @staticmethod
    def getPITI(mortgagePayment, annualTaxes, annualInsurance):
        return mortgagePayment + annualTaxes/12 + annualInsurance/12
