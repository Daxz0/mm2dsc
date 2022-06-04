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