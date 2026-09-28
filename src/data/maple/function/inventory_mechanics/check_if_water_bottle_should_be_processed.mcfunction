execute at @a run advancement revoke @p only maple:inventory_checks/water_bottle
execute if entity @p[gamemode=!creative] run function maple:inventory_mechanics/process_water_bottle

# In creative, items are refilled by the game. This can cause serious issues, corrupting worlds.
# This is a band-aid fix for that issue. If you have a better idea, lmk
