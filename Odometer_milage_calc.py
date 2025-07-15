#SOV = Start Odometer value
#EOV = End Odometer Value
#FC = Fuel Consumption
#DT = Distance Travelled
SOV = int(input("Enter the starting odometer vale:"))
EOV = int(input("Enter the ending odometer value:"))
FC = int(input("Fuel Filled before travel:"))
DT = EOV-SOV
print(f"Total Distance Travelled:", DT, "KMs")
Milage = DT/FC
print(f"Milage of your vechile is:", Milage,"KMs")
