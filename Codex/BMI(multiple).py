#BMI CALCULATOR
name_1="Aditya";
height_m1=2;
weight_kg1=90;

name_2="Kshitij";
height_m2=1.8;
weight_kg2=70;

name_3="Tejas";
height_m3=2;
weight_kg3=110;

def bmi_calculator(name,height_m,weight_kg):
    bmi=weight_kg/(height_m**2);
    print("bmi:");
    print(bmi);
    if bmi<25:
        return name + " is not overweight";
    else:
        return name + " is overweight";
result1=bmi_calculator(name_1,height_m1,weight_kg1);
result2=bmi_calculator(name_2,height_m2,weight_kg2);
result3=bmi_calculator(name_3,height_m3,weight_kg3);

print(result1);
print(result2);
print(result3);
