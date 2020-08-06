#!/usr/bin/env python3

def get_best_savings_rate(starting_annual_salary, r=0.04, total_cost=1000000, portion_down_payment=0.25, semi_annual_raise=0.07):
    months = 36
    threshold = 100
    amount_to_save = total_cost*portion_down_payment
    savings = 0
    num_guesses = 0
    low = 0
    high = 10000
    guess = (high + low)/2
    while abs(amount_to_save - savings) > 100:
        if low == high:
            return []
        savings = 0
        annual_salary = starting_annual_salary
        portion_saved = guess/10000.0
        for i in range(1, months+1):
            if i % 6 == 0:
                annual_salary += annual_salary * semi_annual_raise
            savings += portion_saved*annual_salary/12.0 + savings*r/12.0
        if savings < amount_to_save:
            low = round(guess)
        else:
            high = round(guess)
        guess = (high + low)/2
        num_guesses += 1
        print("Guesses:",num_guesses,"Low:",low,"High:",high,"Portion saved:",portion_saved,"Savings:",savings)
    return [portion_saved, num_guesses]

if __name__ == '__main__':
    annual_salary = float(input("What is your starting annual salary?\n"))
    search_data = get_best_savings_rate(annual_salary)
    if len(search_data) > 0:
        print("Best savings rate:", search_data[0])
        print("Number of guesses:", search_data[1])
    else:
        print("It is not possible to pay the down payment in three years.")
