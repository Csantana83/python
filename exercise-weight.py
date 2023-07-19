weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")

#formula para converter Lbs to Kg
# Lbs * 0.45359237
# Kgs * 2.20462

if unit.upper() == "K":
  converted = weight / 0.45
  print ("Weight in Lbs: " + str(converted))
elif unit.upper() == "L":
  converted = weight * 0.45
  print ("Weight in Kg: " + str(converted))
else:
  print("invalid letter")