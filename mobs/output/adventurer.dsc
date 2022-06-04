Adventurer:
    type: entity
    entity_type: zombie
    mechanisms:
        custom_name: Adventurer
        max_health: 65
        health: 65
        armor_bonus: 0
        custom_name_visible: true
        glowing: false
        speed: 0.3
        has_ai: false
        gravity: false
    flags:
        mm2dz.custom_damage: 6
        mm2dz.disguise: Player
    data:
        drops: null
        drops_chance: null
        damagemodifiers:
            ENTITY_ATTACK: 0.75
            PROJECTILE: 0.75
            MAGIC: 1.25
        kill_messages:
            1: <target.name> had their soul completely devoured
