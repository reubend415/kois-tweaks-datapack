import json
from pathlib import Path

# Define amounts per item
items_and_counts = {
  "bars": 16,
  "chain": 8,
  "trapdoor": 4,
  "door": 4
}

# Define oxidation stages, file path
stages = ["", "exposed_", "weathered_", "oxidized_"]
output_dir = Path("src/data/maple/recipe/stonecutting")
output_dir.mkdir(parents=True, exist_ok=True)


# Create unwaxed recipe files
for stage in stages:
    for item, count in items_and_counts.items():
      if stage == "":
        recipe = {
          "type": "minecraft:stonecutting",
          "ingredient": f"minecraft:copper_block",
          "result": {
              "count": count,
              "id": f"minecraft:copper_{item}",
          },
        }
      else:
        recipe = {
            "type": "minecraft:stonecutting",
            "ingredient": f"minecraft:{stage}copper",
            "result": {
                "count": count,
                "id": f"minecraft:{stage}copper_{item}",
            },
        }

      path = output_dir / f"{stage}copper_{item}.json"
      path.write_text(json.dumps(recipe, indent=2) + "\n")


# Create waxed recipe files
for stage in stages:
    for item, count in items_and_counts.items():
      if stage == "":
        recipe = {
          "type": "minecraft:stonecutting",
          "ingredient": f"minecraft:waxed_copper_block",
          "result": {
              "count": count,
              "id": f"minecraft:waxed_copper_{item}",
          },
        }
      else:
        recipe = {
            "type": "minecraft:stonecutting",
            "ingredient": f"minecraft:waxed_{stage}copper",
            "result": {
                "count": count,
                "id": f"minecraft:waxed_{stage}copper_{item}",
            },
        }

      path = output_dir / f"waxed_{stage}copper_{item}.json"
      path.write_text(json.dumps(recipe, indent=2) + "\n")


# Lightning Rod Recipes

for stage in stages:
  if stage == "":
    recipe = {
      "type": "minecraft:stonecutting",
      "ingredient": f"minecraft:copper_block",
      "result": {
          "count": 3,
          "id": f"minecraft:lightning_rod",
      },
    }
  else:
    recipe = {
        "type": "minecraft:stonecutting",
        "ingredient": f"minecraft:{stage}copper",
        "result": {
            "count": 3,
            "id": f"minecraft:{stage}lightning_rod",
        },
    }

  path = output_dir / f"{stage}lightning_rod.json"
  path.write_text(json.dumps(recipe, indent=2) + "\n")
  

# Waxed lightning rod recipes
for stage in stages:
  if stage == "":
    recipe = {
      "type": "minecraft:stonecutting",
      "ingredient": f"minecraft:waxed_copper_block",
      "result": {
          "count": 3,
          "id": f"minecraft:waxed_lightning_rod",
      },
    }
  else:
    recipe = {
        "type": "minecraft:stonecutting",
        "ingredient": f"minecraft:waxed_{stage}copper",
        "result": {
            "count": 3,
            "id": f"minecraft:waxed_{stage}lightning_rod",
        },
    }

  path = output_dir / f"waxed_{stage}lightning_rod.json"
  path.write_text(json.dumps(recipe, indent=2) + "\n")