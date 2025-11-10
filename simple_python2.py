# simple_python2.py
# Cookie demo: variables, arithmetic operators, input(), type(), and print()

def safe_int(s, default=0):
	"""Convert s to int, return default on failure."""
	try:
		return int(s)
	except (ValueError, TypeError):
		return default

print("Cookie calculator — tell me about your cookies")

cookies = safe_int(input("How many cookies do you have? "))
cal_per = safe_int(input("Estimated calories per cookie (default 120): "), 120)

# arithmetic operators: multiplication and addition used to compute totals
total_calories = cookies * cal_per
bonus = 10  # extra snack calories to add
total_with_bonus = total_calories + bonus

people = safe_int(input("Share among how many people? (enter 1 if none): "), 1)
per_person_cal = total_with_bonus / people  # division yields float
remainder_cookies = cookies % people  # modulus operator

print()
print("Summary:")
print("Cookies:", cookies, "->", type(cookies))
print("Calories per cookie:", cal_per, "->", type(cal_per))
print("Total calories:", total_with_bonus, "->", type(total_with_bonus))
print("Each person gets approx:", per_person_cal, "calories")
print("Remainder cookies after sharing:", remainder_cookies)

