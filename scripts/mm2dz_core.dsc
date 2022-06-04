mm2dz_custom_damage_applier:
    type: world
    events:
        on entity damages entity:
        - determine <context.entity.flag[mm2dz.custom_damage]> if:<context.entity.has_flag[mm2dz.custom_damage]>

mm2dz_faction_manager:
    type: world
    events:
        on entity targets entity:
        - define entity <context.entity>
        - define target <context.target>
        - if <[entity].has_flag[mm2dz.faction]> && <[target].has_flag[mm2dz.faction]> && <[entity].flag[mm2dz.faction]> == <[target].flag[mm2dz.faction]>:
            - determine cancelled
