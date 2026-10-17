# Student Identity
LAST_NAME = "CABILES"
STUDENT_ID = "TUPM-26-1094"

# Derive computational parameters
seed_digit = int(STUDENT_ID[-1])
id_checksum = sum(int(d) for d in STUDENT_ID if d.isdigit())
vector_dim = len(LAST_NAME)

# Encapsulate state into a Dictionary (Associative Map)
sys_config = {
    "operator": LAST_NAME,
    "auth_id": STUDENT_ID,
    "base_seed": seed_digit,
    "checksum": id_checksum,
    "vector_dim": vector_dim,
    "status": "INITIALIZED"
}

# Display system state
print("=== SYSTEM CONFIGURATION ===")
for key, value in sys_config.items():
    print(f"{key.upper()}: {value}")

    # Task 5: Dynamic List Operations
base_val = sys_config["base_seed"]
number_sequence = [base_val, base_val + 15, sys_config["checksum"]]

print(f"Initial Sequence: {number_sequence}")

# Append a new value to the sequence
number_sequence.append(base_val + 20)
print(f"After Append: {number_sequence}")

# Task 6: Sequential Operations
number_sequence.extend([4, 10, 4, 35])
occ_base = number_sequence.count(base_val)
print(f"Occurrences of base_val ({base_val}): {occ_base}")

number_sequence.sort()
print(f"Final Sorted Sequence: {number_sequence}")

# Task 7: Immutable Records
system_coordinates = (14.4445, 120.9939, sys_config["base_seed"])
x, y, z = system_coordinates
print(f"Tuple Unpacked Variables (X, Y, Z): X={x}, Y={y}, Z={z}")

try:
    system_coordinates[2] = 99
except TypeError as e:
    print(f"Modification Error Message: {e}")

    # Task 8: Key-Value Mappings
device_registry = {"device_id": STUDENT_ID, "operator": LAST_NAME}
print(f"Initial Identifier Value: {device_registry['device_id']}")

device_registry.update({"status": "ACTIVE", "mode": "Telemetry"})
print(f"Updated Payload Output: {device_registry}")

# Task 9: Data De-duplication
raw_list = [4, 19, 22, 4, 24, 19, 22, 10]
print(f"Raw List (with duplicates): {raw_list}")
unique_set = set(raw_list)
print(f"Unique Set Generated: {unique_set}")

# Task 10: Mathematical Set Operations
set_a = {4, 19, 22, 24}
set_b = {22, 24, 35, 50}
intersection_res = set_a.intersection(set_b)
union_res = set_a.union(set_b)
print(f"Intersection Result: {intersection_res}")
print(f"Union Result: {union_res}")

import array as arr

# Task 11: Homogeneous Arrays
int_array = arr.array('i', [4, 19, 22, 24])
print(f"Integer Array Created: {int_array}")

try:
    int_array.append("CABILES")
except TypeError as e:
    print(f"Type Error Message Printed: {e}")

    # Task 12: List Comprehensions
gen_comp = [x * 2 for x in range(1, 6)]
print(f"Generated Comprehension Output: {gen_comp}")

filtered_comp = [x for x in number_sequence if x > 10]
print(f"Filtered Comprehension Output: {filtered_comp}")

from collections import deque

# Task 13: Double-Ended Queues
q = deque([4, 19, 22])
q.appendleft(1)
q.append(24)
print(f"After Appends (Left and Right): {q}")

popped_val = q.popleft()
print(f"Final Deque (After Popleft, removed {popped_val}): {q}")

