# mm2dsc

A Python program to convert MythicMob files to Denizen Scripts (dScript).

## Usage

Simply drop your [MythicMob](https://mythiccraft.io/index.php?resources/mythicmobs.1/) yaml files into the `input` folder, double click the program and voilà! The brand new [Denizen Script](https://github.com/DenizenScript/Denizen) file will appear in the `output` folder!

**Make sure to install Pyyaml before you run the program in order for it to work properly. Run `python setup.py install` in your shell, or read their GitHub page [here](https://github.com/yaml/pyyaml)!**

## Examples

```yml
AngrySludge:
  Type: SLIME
  Display: Angry Sludge
  Health: 40
  Damage: 2
```

```denizenscript
AngrySludge:
    type: entity
    entity_type: slime
    mechanisms:
        custom_name: Angry Sludge
        max_health: 40
        health: 40
        custom_name_visible: true
    flags:
        mm2dz.script_name: AngrySludge
        custom_damage: 2
    data:
        mm2dz: true
        damage_modifiers: null

```

A more complex example:

```yml
super_zombie:
  Type: zombie
  Display: '&lSuper Zombie&r'
  Health: 200
  Damage: 14
  Armor: 10
  Faction: superb_zombies
  Mount: super_zombie_undead_horse
  Options:
    PreventOtherDrops: true
    PreventItemPickup: true
    Despawn: false
    KnockbackResistance: 0.25
    MovementSpeed: 0.25
    Modules:
    ThreatTable: false
    ImmunityTable: true
  AIGoalSelectors:
  - clear
  - meleeattack
  - randomstroll
  AITargetSelectors:
  - clear
  - attacker
  - players
  Drops:
  - diamond 1-3 1
  - exp 50 1
  - super_zombie_sword 1 1
  DamageModifiers:
  - ENTITY_ATTACK 0
  - PROJECTILE 1.25
  - MAGIC 1.75
  Equipment:
  - super_zombie_helmet:4
  - super_zombie_sword:0
  KillMessages:
  - '<target.name> was superbly slain by a <mob.name>'
  LevelModifiers:
    MovementSpeed: 0.01
    KnockbackResistance: 0.05
    Health: 2
    Damage: 1
  Disguise: player ashijin setDisguiseName &6MythicMobs<&sq>s<&spGod
  Skills:
  - throw{v=5;vy=5} @rigger ~onAttack 0.5
  - sound{s=entity.zombie.hurt;v=1;p=0} ~onDamaged
  - e:particles{p=cloud;a=50;s=0.05} ~onDeath
```

```denizenscript
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
        custom_damage: 14
        disguise: player
        faction: superb_zombies
        PreventItemPickup: false
        PreventOtherDrops: true
    data:
        mm2dz: true
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


```

## >> Most features are still in the works <<

**Report bugs to issues.**

Created by Daxz0 & funkychicken493
