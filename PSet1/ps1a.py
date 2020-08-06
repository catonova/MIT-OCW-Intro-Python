#!/usr/bin/env python3

def get_months(current_savings, r, annual_salary, portion_saved, total_cost, portion_down_payment):
    num_months = 0
    while current_savings < portion_down_payment*total_cost:
        num_months += 1
        current_savings += portion_saved*annual_salary/12.0 + current_savings*r/12.0
    return num_months

if __name__ == '__main__':
    annual_salary = float(input("What is your starting annual salary?\n"))
    portion_saved = float(input("What portion of your salary will you save?\n"))
    total_cost = float(input("What is the cost of your dream home?\n"))
    portion_down_payment = 0.25
    r = 0.04
    current_savings = 0
    months_to_save = get_months(current_savings, r, annual_salary, portion_saved, total_cost, portion_down_payment)
    print("It will take", months_to_save, "months to buy your dream home.")
