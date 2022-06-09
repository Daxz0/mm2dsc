super_zombie:
    type: entity
    entity_type: zombie
    mechanisms:
        custom_name: <&l>Super Zombie<&r>
        max_health: 200
        health: 200
        armor_bonus: 10
        custom_name_visible: true
        speed: 0.25
    flags:
        mm2dz.script_name: super_zombie
        mm2dz.custom_damage: 14
        mm2dz.disguise: player
        mm2dz.faction: superb_zombies
        mm2dz.options.PreventItemPickup: true
        mm2dz.options.PreventOtherDrops: true
    data:
        drops:
            diamond: 1-3
            exp: 50
            super_zombie_sword: 1
        drops_chance:
            diamond: 1
            exp: 1
            super_zombie_sword: 1
        damage_modifiers:
            ENTITY_ATTACK: 0
            PROJECTILE: 1.25
            MAGIC: 1.75
        kill_messages:
            1: <target.name> was superbly slain by a <mob.name>
