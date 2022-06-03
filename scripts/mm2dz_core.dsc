custom_damage_applier:
    type: world
    events:
        on entity damages entity:
        - if <context.entity.has_flag[custom_damage]>:
            - determine <context.entity.flag[custom_damage]>