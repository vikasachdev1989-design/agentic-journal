# day5_functions.py — Day 5: functions

def route_lead(amount):
    if amount >= 100000:
        return "Senior Sales"
    elif amount >= 50000:
        return "Sales team"
    else:
        return "Nurture list"
    
# call it directly a few times
print(route_lead(120000))
print(route_lead(60000))
print(route_lead(5000))

# now call it INSIDE a loop — this is the payoff
leads = [120000, 60000, 30000, 95000, 5000]
print("\nAll leads:")
for amount in leads:
    print(f"  Rs {amount:,} -> {route_lead(amount)}")

# a second function that returns True/False
def is_hot(amount):
    return amount >= 50000

print("\nHot check:")
print("120000 hot?", is_hot(120000))
print("30000 hot?", is_hot(30000))



