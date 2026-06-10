import os
import matplotlib.pyplot as plt

os.makedirs("images", exist_ok=True)

# =====================================================
# Architecture Diagram
# =====================================================

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis("off")

components = [
    ("GPS Module", 10),
    ("ESP32", 8),
    ("Cloud Dashboard", 6),
    ("Geofence Engine", 4),
    ("Alert System", 2),
]

for text, y in components:
    ax.text(
        5, y, text,
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.5")
    )

for y in [9.3, 7.3, 5.3, 3.3]:
    ax.arrow(
        5, y,
        0, -0.8,
        head_width=0.2,
        head_length=0.2,
        length_includes_head=True
    )

ax.set_title(
    "IoT Vehicle Tracking Architecture",
    fontsize=16
)

plt.savefig(
    "images/architecture_diagram.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# =====================================================
# Circuit Diagram
# =====================================================

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

ax.text(5, 8, "ESP32",
        ha="center",
        bbox=dict(boxstyle="round"))

ax.text(2, 5, "GPS",
        ha="center",
        bbox=dict(boxstyle="round"))

ax.text(5, 5, "Relay",
        ha="center",
        bbox=dict(boxstyle="round"))

ax.text(8, 5, "Buzzer",
        ha="center",
        bbox=dict(boxstyle="round"))

ax.text(5, 2, "LED",
        ha="center",
        bbox=dict(boxstyle="round"))

ax.plot([5, 2], [7.7, 5.3])
ax.plot([5, 5], [7.7, 5.3])
ax.plot([5, 8], [7.7, 5.3])
ax.plot([5, 5], [4.7, 2.3])

ax.set_title("ESP32 Circuit Connections")

plt.savefig(
    "images/circuit_diagram.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# =====================================================
# Dashboard Preview
# =====================================================

fig, ax = plt.subplots(figsize=(9, 5))
ax.axis("off")

dashboard_text = """
Vehicle Status : SAFE

Latitude  : 28.6139
Longitude : 77.2090

Speed : 45 km/h

Current Location:
https://maps.google.com

Alert Status : NORMAL
"""

ax.text(
    0.5,
    0.5,
    dashboard_text,
    fontsize=14,
    ha="center",
    va="center",
    bbox=dict(boxstyle="round,pad=1")
)

ax.set_title("Dashboard Preview")

plt.savefig(
    "images/dashboard_preview.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# =====================================================
# Geofence Alert
# =====================================================

fig, ax = plt.subplots(figsize=(9, 5))
ax.axis("off")

alert_text = """
⚠ VEHICLE THEFT ALERT ⚠

Vehicle Left Safe Zone

Time : 14:22:15

Location:
28.6200 , 77.2300

Action:
Remote Lock Recommended
"""

ax.text(
    0.5,
    0.5,
    alert_text,
    fontsize=14,
    ha="center",
    va="center",
    bbox=dict(boxstyle="round,pad=1")
)

ax.set_title("Theft Detection Alert")

plt.savefig(
    "images/geofence_alert.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

print("\nImages Generated Successfully!\n")
print("Created:")
print("1. architecture_diagram.png")
print("2. circuit_diagram.png")
print("3. dashboard_preview.png")
print("4. geofence_alert.png")