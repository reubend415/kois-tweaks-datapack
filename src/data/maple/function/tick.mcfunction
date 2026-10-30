execute as @e[type=minecraft:creeper,tag=!SpawnChecked] at @s run function maple:spawn_mechanics/check_creeper_spawn

# Check if a player has died
execute as @a[scores={deaths=1..}] run function maple:death_mechanics/halve_xp

# Reset death score after halving
scoreboard players set @a[scores={deaths=1..}] deaths 0