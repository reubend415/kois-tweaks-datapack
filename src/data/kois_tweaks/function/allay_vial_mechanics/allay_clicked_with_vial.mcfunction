advancement revoke @s only kois_tweaks:allay_vial/allay_clicked

execute as @s run playsound block.amethyst_block.resonate player

execute as @e[type=minecraft:allay,distance=..4.5,sort=nearest,limit=1] run function kois_tweaks:allay_vial_mechanics/remove_allay

execute as @s run function kois_tweaks:allay_vial_mechanics/capture_allay
