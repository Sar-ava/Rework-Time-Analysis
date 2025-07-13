import pandas as pd

tasks = {
    "Battery Replacement": [
        ("Fetch tools and safety gear", "ENVA", 1.5),
        ("Load bike onto ramp", "ENVA", 2.0),
        ("Lift ramp to working height", "ENVA", 1.0),
        ("Remove seat bolts", "VA", 1.2),
        ("Remove seat panel", "VA", 1.0),
        ("Disconnect battery terminals", "VA", 1.5),
        ("Unfasten battery mount", "VA", 1.0),
        ("Remove old battery", "VA", 1.0),
        ("Walk to battery storage area", "NVA", 2.5),
        ("Search for correct battery", "NVA", 1.5),
        ("Carry new battery to workstation", "ENVA", 1.5),
        ("Place and fasten new battery", "VA", 1.5),
        ("Connect terminals", "VA", 1.0),
        ("Perform voltage test", "ENVA", 1.2),
        ("Reattach seat panel", "VA", 1.0),
        ("Tighten seat bolts", "VA", 1.2),
        ("Lower ramp", "ENVA", 1.0),
        ("Unload vehicle", "ENVA", 1.5),
        ("Clean and return tools", "ENVA", 1.2),
    ],
    "Headlight Replacement": [
        ("Fetch tools and headlight unit", "ENVA", 1.5),
        ("Position bike on ramp", "ENVA", 2.0),
        ("Lift ramp", "ENVA", 1.0),
        ("Remove front panel screws", "VA", 1.5),
        ("Remove front panel", "VA", 1.0),
        ("Disconnect old headlight wiring", "VA", 1.2),
        ("Uninstall old headlight", "VA", 1.0),
        ("Walk to parts room", "NVA", 2.0),
        ("Search for correct headlight unit", "NVA", 1.2),
        ("Install new headlight", "VA", 1.2),
        ("Connect wiring", "VA", 1.0),
        ("Test new headlight", "ENVA", 1.2),
        ("Reattach front panel", "VA", 1.0),
        ("Tighten panel screws", "VA", 1.2),
        ("Lower ramp", "ENVA", 1.0),
        ("Unload bike", "ENVA", 1.5),
        ("Clean and return tools", "ENVA", 1.0),
    ],
    "Front Panel Repair": [
        ("Fetch tools", "ENVA", 1.0),
        ("Position vehicle", "ENVA", 2.0),
        ("Lift ramp", "ENVA", 1.0),
        ("Inspect damage", "ENVA", 1.0),
        ("Remove screws", "VA", 1.5),
        ("Remove front panel", "VA", 1.0),
        ("Walk to parts area", "NVA", 2.0),
        ("Search replacement part", "NVA", 1.2),
        ("Install new panel", "VA", 1.5),
        ("Tighten screws", "VA", 1.2),
        ("Lower ramp", "ENVA", 1.0),
        ("Unload bike", "ENVA", 1.5),
        ("Return tools", "ENVA", 1.0),
    ],
    "Rear Panel Repair": [
        ("Get safety equipment and tools", "ENVA", 1.0),
        ("Position and secure bike", "ENVA", 2.0),
        ("Lift ramp", "ENVA", 1.0),
        ("Remove seat and rear frame bolts", "VA", 1.5),
        ("Detach rear panel", "VA", 1.0),
        ("Walk to inventory room", "NVA", 2.0),
        ("Look for correct rear panel", "NVA", 1.2),
        ("Install new rear panel", "VA", 1.5),
        ("Reattach bolts", "VA", 1.2),
        ("Lower ramp", "ENVA", 1.0),
        ("Unload vehicle", "ENVA", 1.5),
        ("Return tools", "ENVA", 1.0),
    ],
    "Side Panel Repair": [
        ("Get tools and materials", "ENVA", 1.0),
        ("Position vehicle on ramp", "ENVA", 2.0),
        ("Lift ramp", "ENVA", 1.0),
        ("Unscrew and remove side panel", "VA", 1.5),
        ("Walk to side panel storage", "NVA", 2.0),
        ("Find correct panel", "NVA", 1.0),
        ("Install new side panel", "VA", 1.2),
        ("Tighten screws", "VA", 1.2),
        ("Lower ramp", "ENVA", 1.0),
        ("Unload vehicle", "ENVA", 1.5),
        ("Return tools", "ENVA", 1.0),
    ],
}

all_dfs = []
for task, steps in tasks.items():
    df = pd.DataFrame(steps, columns=["Step Description", "Category", "Time (min)"])
    df["Task Name"] = task
    df["Step No."] = df.index + 1
    df = df[["Task Name", "Step No.", "Step Description", "Category", "Time (min)"]]
    all_dfs.append(df)

final_df = pd.concat(all_dfs, ignore_index=True)

output_path = "1Rework_Task_Modules.xlsx"
final_df.to_excel(output_path, index=False)
