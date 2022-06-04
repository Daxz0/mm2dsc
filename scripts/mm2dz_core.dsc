mm2dz_custom_damage_applier:
    type: world
    events:
        on entity damages entity:
        - determine <context.entity.flag[mm2dz.custom_damage]> if:<context.entity.has_flag[mm2dz.custom_damage]>

mm2dz_kill_message:
    type: world
    events:
        on entity dies:
        - determine <script[<context.entity>].data_key[kill_messages].random> if:<script[<context.entity>].data_key[kill_messages].random.if_null[false]>

mm2dz_faction_manager:
    type: world
    events:
        on entity targets entity:
        - define entity <context.entity>
        - define target <context.target>
        - if <[entity].has_flag[mm2dz.faction]> && <[target].has_flag[mm2dz.faction]> && <[entity].flag[mm2dz.faction]> == <[target].flag[mm2dz.faction]>:
            - determine cancelled
