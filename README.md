# mm2dz
A python program to convert MythicMob files to Denizen Scripts (dScript).

For example:

```
AngrySludge:
  Type: SLIME
  Display: Angry Sludge
  Health: 40
  Damage: 2
```

Turns into,

```
AngrySludge:
    entity_type: SLIME
    mechanisms:
        custom_name: Angry Sludge
        health: 40
        max_health: 40
    type: entity
```

**Report bugs to issues.**

Created by Daxz0 & funkychicken493
