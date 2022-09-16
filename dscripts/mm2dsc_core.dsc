mm2dsc_custom_damage_applier:
    type: world
    events:
        on entity damages entity:
        - determine <context.entity.flag[mm2dsc.custom_damage]> if:<context.entity.has_flag[mm2dsc.custom_damage]>

mm2dsc_kill_message:
    type: world
    events:
        on entity dies:
        - if <script[<context.entity.flag[mm2dsc.script_name]>].data_key[kill_messages].if_null[null]>:
            - announce <context.entity.flag[mm2dsc.script_name].data_key[kill_messages].random>

mm2dsc_drops_handler:
    type: world
    events:
        on entity dies:
        - if <context.entity.has_flag[mm2dsc.options.PreventOtherDrops]> && !<context.entity.flag[mm2dsc.options.PreventOtherDrops]>:
            - determine passively NOTHING
        - define config <context.entity.flag[mm2dsc.script_name].data_key[drop_chance].if_null[null]>
        - if <[config]>:
            - foreach <[config]> as:i:
                - if <util.random_chance[<[i]>]>:
                    - drop <[i]> <context.location> quantity:<script[<context.entity.name>].data_key[drops.<[i]>]>


mm2dsc_faction_manager:
    type: world
    debug: false
    events:
        on entity targets entity:
        - define entity <context.entity>
        - define target <context.target>
        - if <[entity].has_flag[mm2dsc.faction]> && <[target].has_flag[mm2dsc.faction]> && <[entity].flag[mm2dsc.faction]> == <[target].flag[mm2dsc.faction]>:
            - determine cancelled



# mm2dsc_options:
#     type: world
#     debug: false
#     events:
#         on !player picks up item:
#         - if <context.entity.has_flag[mm2dsc.options.PreventItemPickup]>:
#             - determine cancelled
