super_zombie:
    type: entity
    entity_type: zombie
    mechanisms:
        custom_name: &lSuper Zombie&r
        max_health: 200
        health: 200
        armor_bonus: 10
        custom_name_visible: true
        glowing: false
        speed: 0.3
        has_ai: false
        gravity: false
    flags:
        mm2dz.custom_damage: 14
        mm2dz.disguise: player
    data:
        drops:
            diamond: 1-3
            exp: 50
            super_zombie_sword: 1
        damagemodifiers:
            ENTITY_ATTACK: 0
            PROJECTILE: 1.25
            MAGIC: 1.75
        kill_messages:
            1: <target.name> was superbly slain by a <mob.name>
