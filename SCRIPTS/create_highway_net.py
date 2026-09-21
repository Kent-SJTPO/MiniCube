# create_highway_net.py
# Creates a minimal placeholder highway.net file.

content = """; Minimal Highway Network
NODES:
; id, x, y
1, 0.0, 0.0
2, 1.0, 1.0

LINKS:
; a, b, distance, time
1, 2, 1.0, 2.0
END
"""

with open("highway.net", "w") as f:
    f.write(content)

print("highway.net created successfully.")