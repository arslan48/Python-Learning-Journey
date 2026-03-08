def workout_status(steps_walked,goal= 4000):
    if steps_walked >= goal:
        return "Target Achieved! You are a champion."
    else:
        step_needed = goal - steps_walked
        return f"keep going you need {step_needed} more steps"
steps = int(input("Enter the steps you walked: "))
steps2 = int(input("Enter the steps you walked: "))
steps3 = int(input("Enter the steps you walked: "))

result = workout_status(steps)
result2 = workout_status(steps2)
result3 = workout_status(steps3,5000)
print(result)
print(f"{result2} on day 2")
print(f"{result3}")