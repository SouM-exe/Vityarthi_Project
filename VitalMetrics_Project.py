def calculate_body_mass_index(height_m, weight_kg):
    index_value = weight_kg / (height_m * height_m)
    return index_value


def basal_rate_man(weight_kg, height_cm, age_years):
    rate = (10 * weight_kg) + (6.25 * height_cm) - (5 * age_years) + 5
    return rate


def basal_rate_woman(weight_kg, height_cm, age_years):
    rate = (10 * weight_kg) + (6.25 * height_cm) - (5 * age_years) - 161
    return rate


print("=========================================\n   NutriFit: An Algorithmic Health & Nutrition Analytics Engine\n   Analytics Engine - Main Menu")

while True:
    print("=========================================\n1. BMI(Body Mass Calculator)\n2. BMR(Basal Metabolic Rate)\n3. TDEE(Total Daily Energy Expenditure)\n4. Bodyfat\n0. Exit\n=========================================")
    menu_option = int(input("Enter a choice:"))

    if menu_option == 1:
        user_height = float(input("Enter height in metre:"))
        user_weight = float(input("Enter weight:"))
        bmi_result = calculate_body_mass_index(user_height, user_weight)
        if bmi_result <= 18.5:
            print("BMI is", bmi_result, "kg/m² and the person is underweight")
        elif bmi_result <= 24.9:
            print("BMI is", bmi_result, "kg/m² and the person is healthy weight")
        elif bmi_result <= 29.9:
            print("BMI is", bmi_result, "kg/m² and the person is overweight")
        else:
            print("BMI is", bmi_result, "kg/m² and the person is Obese")

    elif menu_option == 2:
        sex = input("Person is male or female:")
        user_height = float(input("Enter height:"))
        user_weight = float(input("Enter weight:"))
        user_age = int(input("Enter age "))
        if sex == "male":
            energy_at_rest = basal_rate_man(user_weight, user_height, user_age)
            print("basal metabolic rate is:", energy_at_rest, "kilocalories per day")
        if sex == "female":
            energy_at_rest = basal_rate_woman(user_weight, user_height, user_age)
            print("basal metabolic rate is:", energy_at_rest, "kilocalories per day")

    elif menu_option == 3:
        sex = input("Person is male or female")
        user_height = float(input("Enter height:"))
        user_weight = float(input("Enter weight:"))
        user_age = int(input("Enter age "))
        if sex == "male":
            energy_at_rest = basal_rate_man(user_weight, user_height, user_age)
            print("basal metabolic rate is", energy_at_rest, "kilocalories per day")
        elif sex == "female":
            energy_at_rest = basal_rate_woman(user_weight, user_height, user_age)
            print("basal metabolic rate is", energy_at_rest, "kilocalories per day")
        activity = input("Activity level is Sedentary or Lightly Active or Moderately Active or Very Active or Extra Active:")
        if activity == "Sedentary":
            daily_energy = energy_at_rest * 1.2
            print("Total Daily Energy Expenditure of Body is", daily_energy, "kilocalories per day")
        elif activity == "Lightly Active":
            daily_energy = energy_at_rest * 1.375
            print("Total Daily Energy Expenditure of Body is", daily_energy, "kilocalories per day")
        elif activity == "Moderately Active":
            daily_energy = energy_at_rest * 1.55
            print("Total Daily Energy Expenditure of Body is", daily_energy, "kilocalories per day")
        elif activity == "Very Active":
            daily_energy = energy_at_rest * 1.725
            print("Total Daily Energy Expenditure of Body is", daily_energy, "kilocalories per day")
        elif activity == "Extra Active":
            daily_energy = energy_at_rest * 1.9
            print("Total Daily Energy Expenditure of Body is", daily_energy, "kilocalories per day")
        else:
            print("Enter a valid input")

    elif menu_option == 4:
        category = input("Person is Adult male or Adult female or Boy or Girl:")
        user_height = float(input("Enter height: "))
        user_weight = float(input("Enter weight: "))
        user_age = float(input("Enter age: "))
        bmi_result = calculate_body_mass_index(user_height, user_weight)
        if category == "Adult male":
            fat_percent = 1.2 * bmi_result + 0.23 * user_age - 16.2
            print("Body fat is", fat_percent, "%")
        if category == "Adult female":
            fat_percent = 1.2 * bmi_result + 0.23 * user_age - 5.2
            print("Body fat is", fat_percent, "%")
        if category == "Boy":
            fat_percent = 1.51 * bmi_result + 0.70 * user_age - 2.2
            print("Body fat is", fat_percent, "%")
        if category == "Girl":
            fat_percent = 1.51 * bmi_result + 0.70 * user_age - 1.4
            print("Body fat is", fat_percent, "%")

    elif menu_option == 0:
        print("Thank you")
        break

    else:
        print("Enter a valid choice")
