
from boss_build_engine import generate_boss_build

BERSERKERS = [
    "Fraekni the Zealous",
    "Bodvar the Fierce",
    "Starolfr the Troublesome",
    "Hjalti the Stolid",
    "Haklangr the Bearded",
    "Beigadr the Feared",
    "Svipdagr the Cold",
    "Skjothendi the Unerring",
    "Hvitserkr the Bold",
    "Skarde the Hateful",
    "Frakki the Arrogant",
    "King Hrolf Kraki"
]

PLAYSTYLES = [
    "balanced",
    "aggressive",
    "defensive",
    "runic",
    "cooldown",
    "survival"
]

SLOTS = [
    "Chest", "Wrist", "Waist",
    "Grip", "Knob", "Maul",
    "Handles", "Pommels",
    "Hind", "Sauroter",
    "shield", "rond", "relic"
]

total_tests = 0
passed_tests = 0
failed_tests = 0

print("\n========== FULL BUILD VALIDATION ==========")

for boss in BERSERKERS:

    print(f"\n{'=' * 55}")
    print("BERSERKER:", boss)
    print("=" * 55)

    for style in PLAYSTYLES:

        total_tests += 1

        try:
            result = generate_boss_build(
                boss,
                playstyle=style
            )

            if "error" in result:
                failed_tests += 1
                print(f"❌ {style.upper()}: {result['error']}")
                continue

            equipment = result.get("equipment", {})

            missing_slots = [
                slot for slot in SLOTS
                if not equipment.get(slot)
            ]

            if missing_slots:
                failed_tests += 1
                print(
                    f"❌ {style.upper()}: Missing {missing_slots}"
                )
                continue

            if not isinstance(result.get("final_score"), (int, float)):
                failed_tests += 1
                print(f"❌ {style.upper()}: Invalid final score")
                continue

            passed_tests += 1

            print(
                f"✅ {style.upper()} | "
                f"Equipment: {result['build_score']} | "
                f"Final: {result['final_score']}"
            )

        except Exception as error:
            failed_tests += 1
            print(f"❌ {style.upper()}: {error}")

print("\n========== FINAL TEST REPORT ==========")
print("Total Tests:", total_tests)
print("Passed:", passed_tests)
print("Failed:", failed_tests)

if failed_tests == 0:
    print("STATUS: ALL TESTS PASSED")
else:
    print("STATUS: SOME TESTS FAILED")

print("=======================================")
