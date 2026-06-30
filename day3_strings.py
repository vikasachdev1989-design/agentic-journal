#day3_string.py - Day 3: strings + numbers  (CRM data cleaning)

# --- A: clea a messy lead name ---
raw = "   vikas SACHDEV   "
name = raw.strip().title()
print("A1:", name)            #predict?
print("A2:", name.upper())    #predict?
print("A3:", len(name))       #predict (count the letters+space)

# --- B: Slice an email ---
email = "vikas@acme.in"
at = email.find("@")
user=email[:at]
domain = email[at+1:]
print("B1:", user)            # predict?
print("B2:", domain)          # predict?
print("B3:", email[-2:])      # predict?

# --- C: split a CSV row ---
full = "John Smith,Acme Corp,50000"
parts = full.split(",")
print("C1:", parts)           # predict? (it's a list)
print("C2:", parts[0])        # predict?
print("C3:", parts[1])        # predict?

# --- D: numbers + money ---
deal = int(parts[2])          # text "50000" -> number 50000
gst = deal * 0.18
total = deal + gst
print("D1:", deal)            # predict?
print("D2:", round(gst))      # predict?
print(f"D3: Total ₹{total:,.2f}")   # predict?

# --- E: build an agent-style summary line ---
summary = f"{parts[0]} from {parts[1]} — deal ₹{deal:,}"
print("E1:", summary)         # predict?