grade_data = float(input())


def scope(grade):
    if 2 <= grade <= 2.99:
        return "Fail"
    elif 3 <= grade <= 3.49:
        return "Poor"
    elif 3.50 <= grade <= 4.49:
        return "Good"
    elif 4.50 <= grade <= 5.49:
        return "Very good"
    elif 5.50 <= grade <= 6:
        return "Excellent"


print(scope(grade_data))

