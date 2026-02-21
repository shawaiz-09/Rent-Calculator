# rent 
# food
# electricity
# charge per unit
# persons

print("Welcome to the rent calculator made by shawaiz hassan")
rent=int(input("Enter the rent of the room/house : "))
food = int(input("Enter the amount of snacks/food ordered : "))
electricity=int(input("Enter the electricity spend  : "))
charge_per_unit=int(input("Enter the charge per unit : "))
total_persons=int(input("Enter the total persons living in a room/house : "))

electricity_bill=electricity*charge_per_unit

total=(rent + food + electricity_bill) // total_persons

print(f"Total cost per head is : {total}")

# shawaiz hassan