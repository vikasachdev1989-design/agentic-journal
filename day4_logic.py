# day4_logic.py — Day 4: control flow (if/elif/else + loops)

# --- One lead, one decision ---
deal = 75000
if deal >= 100000:
    route = "Senior Sales"
elif deal >= 50000:
    route = "Sales team"
else:
    route = "Nurture list"

print("Single lead:", deal, "->", route)

# --- Many leads: same decision, looped over a list ---
leads = [120000, 60000, 30000, 95000, 5000]

print("\nRouting all leads:")
for amount in leads:
    if amount >= 100000:
        route = "Senior Sales"
    elif amount >= 50000:
        route = "Sales team"
    else:
        route = "Nurture list"
    print(f"  Rs {amount:,} -> {route}")

# --- Count the hot leads ---
hot = 0
for amount in leads:
     if amount >= 50000:
         hot = hot + 1
print(f"\nHot leads (>= Rs 50,000): {hot} out of {len(leads)}")
