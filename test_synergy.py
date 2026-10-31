from boss_build_engine import generate_boss_build
from synergy_engine import analyze_synergy

result = generate_boss_build("King Hrolf Kraki")

synergy = analyze_synergy({
    **result["equipment"],
    "relic": result["equipment"]["relic_options"][0]
})

print("\n========== EQUIPMENT SYNERGY ==========")

for name, items in synergy["synergies"].items():
    print("\nSynergy:", name)

    for item in items:
        print(item["slot"], ":", item["item"])

print("\nSynergy Score:", synergy["synergy_score"])