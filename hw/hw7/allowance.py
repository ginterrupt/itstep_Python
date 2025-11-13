
from functools import reduce

def get_weekly_allowances(num_weeks):
    allowances = []
    for i in range(1, num_weeks + 1):
        while True:
            
            amount = float(input(f"Week {i} allowance: "))
            if amount <= 0:
                print("Amount must be greater than 0. Try again.")
                continue
            else:
                break
        allowances.append(amount)
           
    return allowances


def add_bonuses(allowances, bonus):
    return list(map(lambda x: x + bonus, allowances))


def calculate_total(amounts):
    return reduce(lambda a, b: a + b, amounts)


def calculate_average(amounts):
    total = reduce(lambda a, b: a + b, amounts)
    return total / len(amounts)


def find_good_weeks(amounts, threshold):
    good = list(filter(lambda x: x > threshold, amounts))
    weeks = range(1, len(amounts) + 1)
    return [(week, amount) for week, amount in zip(weeks, amounts) if amount in good]


def display_results(original, with_bonus, bonus, total, average, good_weeks, best_week):
    print("\n--- ALLOWANCE SUMMARY ---\n")
    print("Weekly Earnings:")
    for i, (orig, final) in enumerate(zip(original, with_bonus), start=1):
        if bonus > 0:
            print(f"  Week {i}: ${orig:.2f} + ${bonus:.2f} bonus = ${final:.2f}")
        else:
            print(f"  Week {i}: ${final:.2f}")

    print(f"\nTotal Earned: ${total:.2f}")
    print(f"Average Per Week: ${average:.2f}\n")

    threshold = 12
    print(f"Good Weeks (above ${threshold}): ")
    if good_weeks:
        for week, amount in good_weeks:
            print(f"  Week {week}: ${amount:.2f}")
    else:
        print("  None")

    print(f"\nBest Week: Week {best_week[0]} with ${best_week[1]:.2f}!")


def main():
    print("ALLOWANCE TRACKER\n")
    while True:
        num_weeks = int(input("How many weeks to track? "))
        if num_weeks <= 0:
            print("Enter a number greater than 0.")
            continue
        else:
            break

    allowances = get_weekly_allowances(num_weeks)
    add_bonus = input("\nAdd bonus? (yes/no): ").strip().lower()
    bonus = 0.0
    if add_bonus == "yes":
        while True:
            
            bonus = float(input("Bonus amount per week: "))
            if bonus < 0:
                print("Bonus cannot be negative.")
                continue
            else:
                break   
    with_bonus = add_bonuses(allowances, bonus)
    total = calculate_total(with_bonus)
    average = calculate_average(with_bonus)

    threshold = 12
    good_weeks = find_good_weeks(with_bonus, threshold)

    best_index = with_bonus.index(max(with_bonus)) + 1
    best_week = (best_index, max(with_bonus))

    display_results(allowances, with_bonus, bonus, total, average, good_weeks, best_week)


if __name__ == "__main__":
    main()
