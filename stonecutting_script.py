import json

print("Generating wood stonecutting recipes...")

woods = ["oak", "spruce", "dark_oak", "birch", "jungle", "acacia", "mangrove", "cherry", "pale_oak", "crimson", "warped", "bamboo"]
furnitures = {
    "planks": 4,
    "trapdoor": 4,
    "stairs": 4,
    "slab": 8,
    "shelf": 1,
    "fence": 4,
    "fence_gate": 4,
    "button": 4,
    "pressure_plate": 2
}

# Time to design loop

for wood in woods:
    for furniture in furnitures:

        

        if (wood == "crimson" or wood == "warped"):
            wood_descriptor = "stems"
        elif (wood == "bamboo"):
            wood_descriptor = "blocks"
        else:
            wood_descriptor = "logs"
        

        data = {
            "type": "minecraft:stonecutting",
            "ingredient": f"#minecraft:{wood}_{wood_descriptor}",
            "result": {
                "id": f"minecraft:{wood}_{furniture}",
                "count": furnitures.get(furniture)
            }
        }

        with open(f"./src/data/beet_test/recipe/stonecutting/{wood}_{furniture}_from_{wood}_{wood_descriptor}_stonecutting.json", "w") as f:
            json.dump(data, f, indent=2)