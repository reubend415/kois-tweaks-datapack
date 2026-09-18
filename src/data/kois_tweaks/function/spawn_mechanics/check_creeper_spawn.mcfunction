execute if predicate kois_tweaks:is_surface_spawn run tag @s add SpawnForbidden
execute if entity @s[tag=SpawnForbidden] at @s run tp @s ~ ~-1000 ~
execute if entity @s[tag=SpawnForbidden] run kill @s
tag @s add SpawnChecked