def q(n):
    print(f"\n--- Q{n} ---")


# 1. Given a voltage reading, print "Under Voltage", "Nominal", or "Over Voltage".
# (Nominal is between 3.0V and 3.3V inclusive.)
# Input: 3.35
# Output: Over Voltage
q(1)
voltage = 3.35
if voltage < 3.0:
    print("Under Voltage")
elif voltage <= 3.3:
    print("Nominal")
else:
    print("Over Voltage")


# 2. Take an 8-bit register value and print if the MSB (most significant bit) is set or not.
# Input: 0b10010010
# Output: MSB set
q(2)
reg = 0b10010010
if reg & 0b10000000:
    print("MSB set")
else:
    print("MSB not set")


# 3. Enter a temperature and print "Overheat" (>75°C), "Normal" (25-75°C), or "Low Temp" (<25°C).
# Input: 18
# Output: Low Temp
q(3)
temp = 18
if temp > 75:
    print("Overheat")
elif temp >= 25:
    print("Normal")
else:
    print("Low Temp")


# 4. Given two pin logic levels (0 or 1), print the output if these were inputs to an AND, OR, and XOR gate.
# Input: 1, 0
# Output: AND: 0, OR: 1, XOR: 1
q(4)
a, b = 1, 0
print(f"AND: {a & b}, OR: {a | b}, XOR: {a ^ b}")


# 5. If a sensor value is outside the range 100-900, print "Sensor Fault". If within, print "Sensor OK".
# Input: 950
# Output: Sensor Fault
q(5)
sensor = 950
if sensor < 100 or sensor > 900:
    print("Sensor Fault")
else:
    print("Sensor OK")


# 6. Take an error code (integer). Print "Critical" if code >= 1000, "Warning" if 100-999, and "Info" if < 100.
# Input: 230
# Output: Warning
q(6)
code = 230
if code >= 1000:
    print("Critical")
elif code >= 100:
    print("Warning")
else:
    print("Info")


# 7. Given three boolean flags: power_on, overcurrent, overvoltage, print:
# - "System Safe" if only power_on is True.
# - "Shut Down: Overcurrent" if overcurrent is True.
# - "Shut Down: Overvoltage" if overvoltage is True.
# - "Critical Failure" if both faults are True.
# Input: True, True, False
# Output: Shut Down: Overcurrent
