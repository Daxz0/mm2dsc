mm2dz_custom_damage_applier:
    type: world
    events:
        on entity damages entity:
        - determine <context.entity.flag[mm2dz.custom_damage]> if:<context.entity.has_flag[mm2dz.custom_damage]>

mm2dz_kill_message:
    type: world
    events:
        on entity dies:
        - if <script[<context.entity.flag[mm2dz.script_name]>].data_key[kill_messages].random.if_null[false]>:
            - announce <script[<context.entity.flag[script_name]>].data_key[kill_messages].random>

mm2dz_drops_handler:
    type: world
    events:
        on entity dies:
        - if <context.entity.has_flag[mm2dz.options.PreventOtherDrops]> && !<context.entity.flag[mm2dz.options.PreventOtherDrops]>:
            - determine passively NOTHING
        - define config <script[<context.entity.flag[script_name]>].data_key[drop_chance].if_null[false]>
        - if <[config]> != false:
            - foreach <[config]> as:i:
                - if <util.random_chance[<[i]>]>:
                    - drop <[i]> <context.location> quantity:<script[<context.entity>].data_key[drops.<[i]>]>


mm2dz_faction_manager:
    type: world
    debug: false
    events:
        on entity targets entity:
        - define entity <context.entity>
        - define target <context.target>
        - if <[entity].has_flag[mm2dz.faction]> && <[target].has_flag[mm2dz.faction]> && <[entity].flag[mm2dz.faction]> == <[target].flag[mm2dz.faction]>:
            - determine cancelled


mm2dz_options:
    type: world
    debug: false
    events:
        on !player picks up item:
        - if <context.entity.has_flag[mm2dz.options.PreventItemPickup]>:
            - determine cancelled
