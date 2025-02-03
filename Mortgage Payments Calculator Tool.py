# Defining the object and inputting values in the private attributes.
# self allows object to remember 
class Mortgage:
    def __init__(self, principal, rate, amortization):
        
        # Inputting the key Mortgage factors which are principal, interest rate, and amortization period.
        
        self.__principal = principal
        self.__rate = rate / 100  # Convert percentage to decimal to make it simpler.
        self.__amortization = amortization
# This is the main function that helps calculate these payments for the periodic interest rates. 
    def calculate_payments(self):
            
        # These are the formulas for the different payments/frequencies.
        r_monthly = (1 + self.__rate / 2) ** (2 / 12) - 1
        r_semi_monthly = (1 + self.__rate / 2) ** (2 / 24) - 1
        r_bi_weekly = (1 + self.__rate / 2) ** (2 / 26) - 1
        r_weekly = (1 + self.__rate / 2) ** (2 / 52) - 1

        # Number of payment periods are written down to aid with the annuity formula where n=number of payments.
        n_monthly = self.__amortization * 12
        n_semi_monthly = self.__amortization * 24
        n_bi_weekly = self.__amortization * 26
        n_weekly = self.__amortization * 52

        # Function to calculate annuity payment. this is the formula to find the mortgage ammount due.
        # It has been rearranged to solve for the mortgage ammount as we have the principal.
        def annuity_payment(principal, r, n):
            return principal * (r / (1 - (1 + r) ** -n))

        # Compute payments correctly using the annuity formula after completing calculation for the rates.
        # It finds current mortgage.
        monthly_payment = annuity_payment(self.__principal, r_monthly, n_monthly)
        semi_monthly_payment = annuity_payment(self.__principal, r_semi_monthly, n_semi_monthly)
        bi_weekly_payment = annuity_payment(self.__principal, r_bi_weekly, n_bi_weekly)
        weekly_payment = annuity_payment(self.__principal, r_weekly, n_weekly)

        # Correct formulas for Rapid Payments. 
        # These rather than being coded can simply be divided into 2 & 4 from the monthly payment formula.
        rapid_bi_weekly_payment = monthly_payment / 2
        rapid_weekly_payment = monthly_payment / 4

        return monthly_payment, semi_monthly_payment, bi_weekly_payment, weekly_payment, rapid_bi_weekly_payment, rapid_weekly_payment

if __name__ == "__main__":
    # Get user input, ensures that the input is asked for when the command is ran.
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    amortization = int(input("Enter the amortization period (in years): "))

# When the input is given the mortgage class is created.
    # Create an instance of the Mortgage class using those inputted values to identify them. Tied to the init Mortgage function.
    mortgage = Mortgage(principal, rate, amortization)

    # Calculate payments when the input is given and ensures calculation is performed.
    monthly, semi_monthly, bi_weekly, weekly, rapid_bi_weekly, rapid_weekly = mortgage.calculate_payments()

    # This function simply prints the output and ensures it is rounded to 2 decimal places. 
    # It also makes sure all 6 payment frequencies are provided.
    print(f"Monthly Payment: ${monthly:.2f}")
    print(f"Semi-monthly Payment: ${semi_monthly:.2f}")
    print(f"Bi-weekly Payment: ${bi_weekly:.2f}")
    print(f"Weekly Payment: ${weekly:.2f}")
    print(f"Rapid Bi-weekly Payment: ${rapid_bi_weekly:.2f}")
    print(f"Rapid Weekly Payment: ${rapid_weekly:.2f}")
