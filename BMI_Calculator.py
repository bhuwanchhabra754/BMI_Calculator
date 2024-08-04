def BMI_Cal(Height,weight):
    result=weight/(Height*Height)
    return result

def classification(BMI_Cal):
    if BMI_Cal<16:
        return("Severe Thinness")
    elif 16<=BMI_Cal<17:
        return("Moderate Thinness")
    elif 17<=BMI_Cal<18.5:
        return("Mild Thinness")
    elif 18.5<=BMI_Cal<25:
        return("Normal")
    elif 25<=BMI_Cal<30:
        return("Overweight")
    elif 30<=BMI_Cal<35:
        return("Obese Class I")
    elif 35<=BMI_Cal<40:
        return("Obese Class II")
    else:
        return("Obese Class III")

if __name__=="__main__":
    height = float(input("Enter your Height in meters (or cm): "))
    if 1 < height < 4:
        height = height  # Assuming height is entered in meters
    elif 100 < height < 250:
        height = height / 100  # Converting height from cm to meters
    else:
        print("Please enter a realistic height in meters or centimeters.")
        exit()

    weight = float(input("Enter your weight in kg: "))
    if weight > 150:
        print("Please enter your weight in kg.")
        weight = float(input("Enter your weight again in kg: "))
        if weight > 150:
            print("Please enter a realistic weight.")
            exit()

    BM_index=BMI_Cal(height,weight)
    Category=classification(BM_index)
    print("Your BM_Index is ",BM_index ,"and Your Category is",Category)
    

