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
q(7)
power_on, overcurrent, overvoltage = True, True, False
if overcurrent and overvoltage:
    print("Critical Failure")
elif overcurrent:
    print("Shut Down: Overcurrent")
elif overvoltage:
    print("Shut Down: Overvoltage")
elif power_on:
    print("System Safe")
else:
    print("Power Off")

# 8. Given a digital input value (0-255), determine and print which of 4 quadrants it falls into:
# 0-63, 64-127, 128-191, 192-255
q(8)
value = 150
if value <= 63:
    print("Quadrant 1 (0-63)")
elif value <= 127:
    print("Quadrant 2 (64-127)")
elif value <= 191:
    print("Quadrant 3 (128-191)")
else:
    print("Quadrant 4 (192-255)")


# 9. Enter a signal frequency (Hz). Print "Low Band" (<1000), "Mid Band" (1000-9999),
# "High Band" (10000-99999), or "Out of Range".
# Input: 8000
# Output: Mid Band
q(9)
freq = 8000
if freq < 1000:
    print("Low Band")
elif freq <= 9999:
    print("Mid Band")
elif freq <= 99999:
    print("High Band")
else:
    print("Out of Range")


# 10. Given three sensor readings, print "Majority High" if at least two readings are above a threshold
# (e.g., 50), otherwise "Majority Low".
# Input: 40, 65, 70
# Output: Majority High
q(10)
r1, r2, r3 = 40, 65, 70
threshold = 50
high_count = (r1 > threshold) + (r2 > threshold) + (r3 > threshold)
if high_count >= 2:
    print("Majority High")
else:
    print("Majority Low")


# 11. Enter a 16-bit value and print if parity (number of 1s) is even or odd.
# Input: 0xAAAA
# Output: Parity: Even
q(11)
value = 0xAAAA
ones = bin(value).count("1")
if ones % 2 == 0:
    print("Parity: Even")
else:
    print("Parity: Odd")


# 12. Given a voltage and current reading, print "Power OK" if both are in safe ranges,
# otherwise print specific error:
# - Voltage out of 3.0-3.3V: "Voltage Error"
# - Current out of 10-500mA: "Current Error"
# - Both out: "Power Error"
q(12)
voltage = 3.1
current = 200
v_bad = not (3.0 <= voltage <= 3.3)
c_bad = not (10 <= current <= 500)
if v_bad and c_bad:
    print("Power Error")
elif v_bad:
    print("Voltage Error")
elif c_bad:
    print("Current Error")
else:
    print("Power OK")


# 13. Given the status of three LEDs (on/off as 1/0), print which LEDs are ON.
# If all are off, print "All LEDs off".
# Input: 0, 1, 0
# Output: LED2 ON
q(13)
led1, led2, led3 = 0, 1, 0
if led1:
    print("LED1 ON")
if led2:
    print("LED2 ON")
if led3:
    print("LED3 ON")
if not (led1 or led2 or led3):
    print("All LEDs off")


# 14. Accept a device mode value:
# - 0: "Standby"
# - 1: "Active"
# - 2: "Fault"
# - Any other: "Unknown mode"
q(14)
mode = 1
if mode == 0:
    print("Standby")
elif mode == 1:
    print("Active")
elif mode == 2:
    print("Fault")
else:
    print("Unknown mode")


# 15. Enter two analog readings. Print "Match" if they are within 5 units of each other, "No Match" otherwise.
# Input: 98, 101
# Output: Match
q(15)
a, b = 98, 101
if abs(a - b) <= 5:
    print("Match")
else:
    print("No Match")