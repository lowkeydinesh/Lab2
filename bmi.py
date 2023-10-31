def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Display calculated BMI
    print("BMI = " + str(bmi))

    # Classify weight based on BMI range
    if bmi < 18.5:
        print("Weight Classification: Under Weight")
        return -1
    elif 18.5 <= bmi <= 25.0:
        print("Weight Classification: Normal Weight")
        return 0
    else:
        print("Weight Classification: Over Weight")
        return 1

# Example usage
classification_result = calculate_bmi(weight=57, height=1.73)
print("Weight Classification Result:", classification_result)
