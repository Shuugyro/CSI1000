# simple_time.py
# Demonstrates variables, operators, casting, input(), type(), and print() (time-focused)

def safe_int(s, default=0):
    """Convert s to int, return default on failure."""
    try:
        return int(s)
    except (ValueError, TypeError):
        return default

print("Time helper — enter a time and optionally add seconds")

h = safe_int(input("Hours: "))
m = safe_int(input("Minutes: "))
s = safe_int(input("Seconds: "))

# arithmetic: compute total seconds
total_seconds = h * 3600 + m * 60 + s
print("Total seconds:", total_seconds, "->", type(total_seconds))

# demonstrate casting and float arithmetic
add_input = input("Add how many seconds? (you can enter decimals, e.g. 2.5): ")
add_seconds = float(add_input) if add_input.strip() != "" else 0.0
print("Added seconds (float):", add_seconds, "->", type(add_seconds))

new_total = total_seconds + add_seconds
print("New total seconds:", new_total, "->", type(new_total))

# convert back to hours, minutes, seconds (using operators and casting)
new_h = int(new_total // 3600)
new_m = int((new_total % 3600) // 60)
new_s = new_total % 60  # may be fractional

print("New time ->", f"{new_h}h {new_m}m {new_s:.2f}s")

# examples of casting
as_string = str(new_total)
as_int = int(new_total)  # truncates fractional seconds
print("As string:", as_string, "->", type(as_string))
print("As int (truncated):", as_int, "->", type(as_int))
