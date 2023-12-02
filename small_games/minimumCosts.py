import time

# Given a list array of plans, where each group consists of four values: the first value represents the starting day, the second value represents the ending day, the third value represents the available inventory per day, and the last value represents the unit price. The task is to calculate the minimum cost given a specific number of days and the daily demand. Optimization tests should be taken into account.
# For example, consider the plans: {{1, 3, 5, 2}, {1, 4, 5, 3}, {2, 5, 10, 1}}, with a daily demand of 7 for 5 days. The calculation process is as follows:
# On day one, with a demand of 7, only plans 1 and 2 have availability. Since plan 1 has a lower price than plan 2, we obtain all 5 units from plan 1, incurring a cost of 2*5. The remaining demand is then fulfilled from plan 2, incurring a cost of (7-5)*3. Therefore, the cost for day one is 16. For the remaining days (2, 3, 4, 5), we obtain 7 units from plan 3, which has the lowest price among all plans. The cost for each day is 7, resulting in a total cost of 16 + 4 * 7, equal to 44
def calculate_min_cost(plans, total_days, everyday_demands):
    total_cost = 0

    # Sort available plans based on their unit price
    plans.sort(key=lambda p: p[3])

    # Loop through each day
    for day in range(1, total_days + 1):
        daily_demands = everyday_demands

        # Find available plans for the day using list comprehension and filters
        available_plans = [plan for plan in plans if plan[0] <= day <= plan[1] and plan[2] > 0]

        # Check if there are no available plans for the day
        if not available_plans:
            print(f"No available plans for day {day}")
            return -1  # Indicate an error

        # Iterate over available plans until the remaining demands for the day become zero
        for chosen_plan in available_plans:
            # Calculate the quantity to be taken from the chosen plan
            quantity_taken = min(chosen_plan[2], daily_demands)

            # Update remaining demands and chosen plan availability
            daily_demands -= quantity_taken
            chosen_plan[2] -= quantity_taken  # Update plan availability

            # Update total cost
            total_cost += quantity_taken * chosen_plan[3]

            # Break the loop if remaining demands for the day become zero
            if everyday_demands == 0:
                break

    return total_cost

# Example usage
plans = [[1, 3, 5, 2], [1, 4, 5, 3], [2, 5, 10, 1]]
everyday_demands = 7
total_days = 5

# Measure execution time
start_time = time.time()
result = calculate_min_cost(plans, total_days, everyday_demands)
end_time = time.time()
execution_time = end_time - start_time

# Display results
print("Minimum cost:", result)
print("Execution time:", execution_time)