# drills_day2.py — Day 2 drills

# ---------- Drill 1: swap two variables ----------
a = 5
b = 10
a, b = b, a
print("Drill 1:", a, b)   # expect: 10 5

# ---------- Drill 2: str + number (gotcha) ----------
year = 2026
print("Drill 2a:", "Year " + str(year))   # works — str() converts
print("Drill 2b:", f"Year {year}")        # works — f-string

# ---------- Drill 3: math + formatting ----------
budget = 50000
spent = 32500
remaining = budget - spent
percent_left = (remaining / budget) * 100
print(f"Drill 3: Remaining ₹{remaining}, {percent_left:.1f}%")

# ---------- Drill 4: boolean logic ----------
mrr = 0
paying_users = 0
has_pmf = mrr > 1000 and paying_users >= 10
print(f"Drill 4: PMF? {has_pmf}")

# ---------- Drill 5: input from user ----------
city = input("Drill 5: Where you live? ")
print(f"You said: {city}")