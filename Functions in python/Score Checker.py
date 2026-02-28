def evaluate_model(accuracy):
    if accuracy >= 0.80:
       return "pass"
    else:
       return "fail"
print(evaluate_model(0.80))
