# Store player's current XP into xp_levels scoreboard
execute store result score @s xp_levels run xp query @s levels

# Divide that score by 2
scoreboard players operation @s xp_levels /= #two xp_levels

# Wipe current levels
xp set @s 0 levels

# Give back halved lvls
execute store result storage maple:dummy temp int 1 run scoreboard players get @s xp_levels
function maple:death_mechanics/restore_xp with storage maple:dummy
