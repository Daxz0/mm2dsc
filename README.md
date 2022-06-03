## mm2dz
A Python program to convert MythicMob files to Denizen Scripts (dScript).


# Usage:

Simply drop a MythicMob file into the `Input` folder, run the code and voila! The brand new dScript file will appear in the `Output` folder!





# Examples:

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
    entity_type: SLIME
    mechanisms:
        custom_name: Angry Sludge
        health: 40
        max_health: 40
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
    flags:
        custom_damage: 14
        disguise: player
    mechanisms:
        armor_bonus: 10
        custom_name: '&lSuper Zombie&r'
        health: 200
        max_health: 200
```


# >> Most features are still in the works <<


**Report bugs to issues.**

Created by Daxz0 & funkychicken493
