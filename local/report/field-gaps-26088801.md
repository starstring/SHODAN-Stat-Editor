# Field gaps — build 26088801

`✗` = the panel cannot edit this member. Offsets are in the record; values come from up to a dozen real rows of the first table that has this record.

- type library: 1208 types / 7349 members · panel: 102 table(s), 11272 field(s), 505 page(s), 10006 row(s) of stats
- records the panel reads: 51 · blocks in the game's files it never parses: 891

## 1. Candidates (not editable, scalar, and not constant)

The likeliest new stats: numeric members of records the panel already reads, which are neither edited nor the same value on every row. `?` types are members whose type the library does not name; both readings are shown.

| record | member | off | size | type | name | values |
|---|---|---:|---:|---|---|---|
| ProjectileWeaponComponentData | ProjectileWeaponComponent | +540 | 4 | u32/f32 |  | -1.433e-09, 0, 4.059e-12 …  [-1.433e-09..8.66e+05] |
| ProjectileWeaponComponentData | ProjectileWeaponComponent | +560 | 4 | u32/f32 |  | 1, 2, 3 …  [1..4] |
| ProjectileSettings | ProjectileInfo | +0 | 4 | u32/f32 | Type? | 118, 132, 133 …  [118..343] |
| ProjectileSettings | ProjectileInfo | +60 | 4 | u32/f32 | DamageInfoType? | 0, 39, 244 …  [0..261] |
| ProjectileSettings | ProjectileInfo | +136 | 4 | u32/f32 | ExplosionThresholdAngle? | 0, 1117782016, 1119092736  (f32: 0, 80)  [0..1119092736]  (f32: 0, 80) |
| ProjectileSettings | ProjectileInfo | +244 | 2 | u16 |  | 125, 188, 6168  [125..6168] |
| WeaponHeatComponentData | WeaponHeatComponent | +104 | 4 | u32/f32 | WarningTemperature | 1117126656, 1127153664, 1153138688  (f32: 75, 175)  [1117126656..1153138688]  (f32: 75, 175) |
| WeaponHeatComponentData | WeaponHeatComponent | +108 | 4 | u32/f32 | EmissionTemperature | 1112014848, 1120403456, 1148846080  (f32: 50, 100)  [1112014848..1148846080]  (f32: 50, 100) |
| WeaponHeatComponentData | WeaponHeatComponent | +148 | 4 | u32/f32 | FiringCharge | 0, 1092616192, 1120403456  (f32: 0, 10)  [0..1120403456]  (f32: 0, 10) |
| WeaponHeatComponentData | WeaponHeatComponent | +584 | 4 | u32/f32 | OverheatAbility | 0, 2882, 2884  [0..2884] |
| JumppackComponentData | JumppackComponent | +84 | 4 | u32/f32 |  | 0, 2058, 2506  [0..2506] |
| JumppackComponentData | JumppackComponent | +92 | 4 | u32/f32 |  | 0, 2059, 2508  [0..2508] |
| JumppackComponentData | JumppackComponent | +96 | 4 | u32/f32 |  | 0, 2060, 2509  [0..2509] |
| HealthComponentData | HealthComponent | +40 | 4 | u32/f32 | Size | 0, 1, 2 …  [0..3] |
| HealthComponentData | HealthComponent | +21984 | 4 | u32/f32 | OnDeathDestructionLevel | 3, 4, 5 …  [3..9] |
| ShieldComponentData | ShieldComponent | +80 | 4 | u32/f32 |  | 0, 1073741824, 1077936128 …  (f32: 0, 2)  [0..1082130432]  (f32: 0, 2) |
| ShieldComponentData | ShieldComponent | +168 | 4 | u32/f32 |  | -6.364e+04, 0, 9.15e-16  [-6.364e+04..9.15e-16] |
| ShieldComponentData | ShieldComponent | +216 | 4 | u32/f32 |  | 7, 8, 11 …  [7..12] |
| ShieldComponentData | ShieldComponent | +228 | 4 | u32/f32 |  | 0, 0.5, 0.65 …  [0..0.75] |
| ShieldComponentData | ShieldComponent | +232 | 4 | u32/f32 |  | 0, 1, 2  [0..2] |
| EagleComponentData | EagleComponent | +16 | 4 | u32/f32 |  | 1, 2, 3 …  [1..5] |
| EagleComponentData | EagleComponent | +20 | 4 | u32/f32 |  | 0, 3, 4 …  [0..7] |
| EagleComponentData | EagleComponent | +24 | 4 | u32/f32 |  | 0, 84, 117 …  [0..291] |
| EagleComponentData | EagleComponent | +48 | 4 | u32/f32 |  | 1101004800, 1114636288, 1133903872  (f32: 20, 60)  [1101004800..1133903872]  (f32: 20, 60) |
| EagleComponentData | EagleComponent | +72 | 4 | u32/f32 |  | 1145569280, 1147207680, 1148846080  (f32: 800, 900)  [1145569280..1148846080]  (f32: 800, 900) |
| EagleComponentData | EagleComponent | +76 | 4 | u32/f32 |  | 1073741824, 1086324736, 1098907648  (f32: 2, 6)  [1073741824..1098907648]  (f32: 2, 6) |
| EagleComponentData | EagleComponent | +136 | 4 | u32/f32 |  | 1133903872, 1135542272, 1142292480  (f32: 300, 350)  [1133903872..1142292480]  (f32: 300, 350) |
| ThrowableComponentData | ThrowableComponent | +0 | 4 | u32/f32 |  | -2.305e-17, 0.0006292, 16.95  [-2.305e-17..16.95] |
| ThrowableComponentData | ThrowableComponent | +12 | 4 | u32/f32 |  | 0, 0.1, 4  [0..4] |
| SeekingMissileComponentData | SeekingMissileComponent | +0 | 4 | u32/f32 | TargetingMode | 0, 1, 2 …  [0..3] |
| ExplosiveComponentData | ExplosiveComponent | +0 | 4 | u32/f32 | Mode | 0, 1, 2  [0..2] |
| ExplosiveComponentData | ExplosiveComponent | +28 | 4 | u32/f32 | ImpactDistance | 0.5, 1, 3  [0.5..3] |
| ExplosiveComponentData | ExplosiveComponent | +32 | 4 | u32/f32 | ImpactAirburstDistance | 0, 0.25, 0.5  [0..0.5] |
| ExplosiveComponentData | ExplosiveComponent | +36 | 4 | u32/f32 | ExplosionType | 73, 91, 100 …  [73..257] |
| ExplosiveComponentData | ExplosiveComponent | +312 | 4 | u32/f32 | CollisionActor | -2.305e-17, 0, 0.0006292 …  [-2.305e-17..16.95] |
| ExplosionSettings | ExplosionInfo | +0 | 4 | u32/f32 | Type? | 71, 118, 123 …  [71..408] |
| ExplosionSettings | ExplosionInfo | +4 | 4 | u32/f32 | DamageType? | 5, 298, 300 …  [5..416] |
| ExplosionSettings | ExplosionInfo | +32 | 4 | u32/f32 | CameraShakeRadius? | 1065353216, 1088421888, 1090519040 …  (f32: 1, 7)  [1065353216..1112014848]  (f32: 1, 7) |
| ExplosionSettings | ExplosionInfo | +88 | 1 | u8 |  | 0, 14, 15  [0..15] |
| BombardmentComponentData | BombardmentComponent | +16 | 4 | u32/f32 |  | 0, 1065353216, 1092616192 …  (f32: 0, 1)  [0..1097859072]  (f32: 0, 1) |
| BombardmentComponentData | BombardmentComponent | +20 | 4 | u32/f32 |  | 0, 1065353216, 1097859072 …  (f32: 0, 1)  [0..1106247680]  (f32: 0, 1) |
| BombardmentComponentData | BombardmentComponent | +40 | 4 | u32/f32 |  | 0, 1065353216, 1097859072 …  (f32: 0, 1)  [0..1106247680]  (f32: 0, 1) |
| BombardmentComponentData | BombardmentComponent | +44 | 4 | u32/f32 |  | 1132068864, 1142292480, 1148846080 …  (f32: 250, 600)  [1132068864..1161527296]  (f32: 250, 600) |
| BombardmentComponentData | BombardmentComponent | +128 | 4 | u32/f32 |  | 0, 1077936128, 1084227584 …  (f32: 0, 3)  [0..1092616192]  (f32: 0, 3) |
| BombardmentComponentData | BombardmentComponent | +176 | 4 | u32/f32 |  | 0, 1065353216, 1098907648 …  (f32: 0, 1)  [0..1112014848]  (f32: 0, 1) |
| StatusEffectSettings | StatusEffectInfo | +0 | 4 | u32/f32 |  | 1, 2, 3 …  [1..12] |
| StatusEffectSettings | StatusEffectInfo | +36 | 4 | u32/f32 |  | 0, 0.15, 0.25 …  [0..5] |
| StatusEffectSettings | StatusEffectInfo | +44 | 4 | u32/f32 |  | 0, 531, 532 …  [0..552] |
| StatusEffectSettings | StatusEffectInfo | +76 | 4 | u32/f32 |  | -0.6377, 0, 1.895e-06  [-0.6377..1.895e-06] |
| StatusEffectSettings | StatusEffectInfo | +104 | 1 | u8 |  | 0, 2, 3 …  [0..8] |
| BeamSettings | BeamInfo | +0 | 4 | u32/f32 |  | 1, 2, 7 …  [1..30] |
| BeamSettings | BeamInfo | +12 | 4 | u32/f32 |  | 512, 513, 514 …  [512..530] |
| BeamSettings | BeamInfo | +44 | 4 | u32/f32 | SurfaceImpactType? | 22, 23, 24 …  [22..25] |
| WeaponChargeComponentData | WeaponChargeComponent | +200 | 4 | u32/f32 | ExplodeType | 269, 321, 326  [269..326] |
| ArcSettings | ArcInfo | +0 | 4 | u32/f32 | Type | 1, 2, 3 …  [1..16] |
| ArcSettings | ArcInfo | +4 | 4 | u32/f32 | Speed | 1112014848, 1133903872, 1157234688  (f32: 50, 300)  [1112014848..1157234688]  (f32: 50, 300) |
| ArcSettings | ArcInfo | +12 | 4 | u32/f32 | DistanceAtMaxAngleSpread | 1065353216, 1092616192, 1109393408 …  (f32: 1, 10)  [1065353216..1120403456]  (f32: 1, 10) |
| ArcSettings | ArcInfo | +16 | 4 | u32/f32 | DistanceAtMaxAngleSpreadFirstShot | 1092616192, 1097859072, 1101004800 …  (f32: 10, 15)  [1092616192..1112014848]  (f32: 10, 15) |
| ArcSettings | ArcInfo | +20 | 4 | u32/f32 | MaxAngleSpread | 1092616192, 1114636288, 1127481344 …  (f32: 10, 60)  [1092616192..1133903872]  (f32: 10, 60) |
| ArcSettings | ArcInfo | +24 | 4 | u32/f32 | MaxAngleSpreadFirstShot | 3, 10, 22.5 …  [3..180] |
| ArcSettings | ArcInfo | +36 | 4 | u32/f32 | DamageInfoType | 49, 50, 51 …  [49..221] |
| TurretComponentData | TurretComponent | +16 | 4 | u32/f32 |  | 0, 0.95, 1  [0..1] |
| TurretComponentData | TurretComponent | +20 | 4 | u32/f32 |  | 1103626240, 1117126656, 3221225472 …  (f32: -90, -65)  [1103626240..3266576384]  (f32: -90, -65) |
| TurretComponentData | TurretComponent | +24 | 4 | u32/f32 |  | 1073741824, 1082130432, 1097859072 …  (f32: 2, 4)  [1073741824..1119092736]  (f32: 2, 4) |
| TurretComponentData | TurretComponent | +28 | 4 | u32/f32 |  | 3231711232, 3248488448, 3253731328 …  (f32: -180, -30)  [3231711232..3274964992]  (f32: -180, -30) |
| TurretComponentData | TurretComponent | +32 | 4 | u32/f32 |  | 1084227584, 1101004800, 1106247680 …  (f32: 5, 20)  [1084227584..1127481344]  (f32: 5, 20) |
| DepositComponentData | DepositComponent | +36 | 4 | u32/f32 | SelfInteractAbility | 0, 2637, 2640  [0..2640] |
| DepositComponentData | DepositComponent | +128 | 4 | u32/f32 | RefillStyle | 0, 1, 3  [0..3] |
| SensorEyeComponentData | SensorEyeComponent | +8 | 4 | u32/f32 |  | 0, 1065353216, 1133903872  (f32: 0, 1)  [0..1133903872]  (f32: 0, 1) |
| SensorEyeComponentData | SensorEyeComponent | +12 | 4 | u32/f32 |  | 1101004800, 1108082688, 1117782016 …  (f32: 20, 35)  [1101004800..1126825984]  (f32: 20, 35) |
| SensorEyeComponentData | SensorEyeComponent | +16 | 4 | u32/f32 |  | 1101004800, 1108082688, 1119092736 …  (f32: 20, 35)  [1101004800..1126825984]  (f32: 20, 35) |
| SensorEyeComponentData | SensorEyeComponent | +32 | 4 | u32/f32 |  | 1, 2, 3  [1..3] |
| ArcWeaponComponentData | ArcWeaponComponent | +0 | 4 | u32/f32 | Type | 1, 3, 4 …  [1..16] |
| MinefieldComponentData | MinefieldComponent | +24 | 4 | u32/f32 |  | 72, 230, 270 …  [72..367] |
| WeaponWindUpComponentData | WeaponWindUpComponent | +12 | 4 | u32/f32 | RpmMultiplier | 0.1667, 0.3333, 1  [0.1667..1] |
| DamageSettings | DamageInfo | +0 | 4 | u32/f32 | Damage? | 1, 2, 3 …  [1..591] |
| DamageSettings | DamageInfo | +40 | 4 | u32/f32 | ElementType? | 0, 1, 3 …  [0..9] |

Left out (identifiers and hashes, not values): ArcSettings 1; ArcWeaponComponentData 3; AvatarComponentData 3; BeamSettings 3; BombardmentComponentData 1; DepositComponentData 3; DisplacementComponentData 6; EagleComponentData 3; ExplosionSettings 1; HealthComponentData 2; JumppackComponentData 10; MinefieldComponentData 2; OrbitalAbilityComponentData 2; ProjectileSettings 5; ProjectileWeaponComponentData 3; SeekingMissileComponentData 2; SensorEyeComponentData 1; ShieldComponentData 16; StatusEffectSettings 6; ThrowableComponentData 5; TurretComponentData 8; WeaponChargeComponentData 9; WeaponDataComponentData 5; WeaponHeatComponentData 14; WeaponReloadComponentData 2; WeaponRoundsComponentData 2; WeaponWindUpComponentData 4.

## 2. Every member of every record the panel reads

### WeaponDataComponentData → WeaponDataComponent (79 members, 5 editable, 373 rows)

tables: weapon

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
|  | +0 | 60 | struct 0x30D8708A | recoil_info | recoil_dh, recoil_ch, recoil_dv |  |
| ✗ | +60 | 24 | struct 0x21368180 | recoil_modifiers |  |  |
|  | +84 | 12 | struct 0xF916ED4B | spread_info | spread_h, spread_v |  |
| ✗ | +96 | 8 | struct 0xC2161EE1 | spread_modifiers |  | 4575657222473777152 |
|  | +104 | 4 | u32/f32 | sway_multiplier | sway | 0, 1065353216  (f32: 0, 1)  [0..1065353216] |
| ✗ | +108 | 4 | u32/f32 | aim_block_length |  | 1065353216  (f32: 1) |
| ✗ | +112 | 1 | u8 | is_suppressed |  | 0 |
| ✗ | +116 | 12 | struct 0x85B82A43 | aim_zoom |  |  |
| ✗ | +128 | 4 | u32/f32 | scope_sway |  | 1065353216  (f32: 1) |
| ✗ | +132 | 1 | u8 | noise_template |  | 0, 7  [0..7] |
| ✗ | +136 | 4 | u32/f32 | visibility_modifier |  | 1065353216  (f32: 1) |
| ✗ | +140 | 4 | u32/f32 | num_burst_rounds |  | 1, 3  [1..3] |
| ✗ | +144 | 4 | u32/f32 | primary_fire_mode |  | 1 |
| ✗ | +148 | 4 | u32/f32 | secondary_fire_mode |  | 0 |
| ✗ | +152 | 4 | u32/f32 | tertiary_fire_mode |  | 0 |
| ✗ | +156 | 4 | u32/f32 | quaternary_fire_mode |  | 0 |
| ✗ | +160 | 24 | struct 0x81E38472 | UnknownMinigunStruct |  |  |
| ✗ | +184 | 8 | struct 0xDD1E521C | function_info |  | 0 |
| ✗ | +192 | 8 | u64 | crosshair |  | 0x2D4AE6FD3E95EB30, 0x2D4AE6FD3E95EB30 |
| ✗ | +200 | 1 | u8 | always_show_crosshair |  | 0 |
| ✗ | +204 | 96 | 96B | fire_nodes |  |  |
| ✗ | +300 | 4 | u32/f32 | aim_source_node |  | 0, 4.059e-12, 0.01888  [0..0.01888] |
| ✗ | +304 | 1 | u8 | simultaneous_fire |  | 0 |
| ✗ | +308 | 8 | struct 0x85B82A42 | scope_crosshair |  | 0 |
| ✗ | +316 | 12 | struct 0x85B82A43 | scope_offset |  |  |
| ✗ | +328 | 8 | struct 0x85B82A42 | scope_zoom |  | 0 |
| ✗ | +336 | 1 | u8 | UnknownMinigunBool |  | 0 |
| ✗ | +340 | 12 | struct 0x85B82A43 | ScopeZeroing |  |  |
| ✗ | +352 | 1 | u8 | scope_lens_hides_weapon |  | 0 |
|  | +356 | 4 | u32/f32 | ergonomics | ergonomics | 1115815936  (f32: 65) |
| ✗ | +360 | 4 | u32/f32 | UnknownFloat |  | 0.35 |
| ✗ | +364 | 1 | u8 | UnknownMinigunBool2 |  | 0 |
| ✗ | +368 | 8 | struct 0x85B82A42 | Unknown2dVec2 |  | 4656722017952202752 |
| ✗ | +376 | 8 | struct 0x85B82A42 | Unknown2dVec3 |  | 0 |
| ✗ | +384 | 1 | u8 | allow_fpv |  | 1 |
| ✗ | +385 | 1 | u8 | hide_weapons_in_fpv |  | 0 |
| ✗ | +386 | 1 | u8 | allow_aiming |  | 1 |
|  | +387 | 1 | u8 | prevent_movement_when_firing | stationary | 0 |
| ✗ | +388 | 4 | u32/f32 | StartFiringMinigunAnimationEvent |  | 0 |
| ✗ | +392 | 4 | u32/f32 | StopFiringMinigunAnimationEvent |  | 0 |
| ✗ | +396 | 4 | u32/f32 |  |  | 0 |
| ✗ | +400 | 1 | u8 | crosshair_type |  | 0 |
| ✗ | +404 | 4 | u32/f32 |  |  | 0 |
| ✗ | +408 | 48 | struct 0x4C18DE6F |  |  |  |
| ✗ | +456 | 4 | u32/f32 | first_person_sight_node |  | 1383898227 |
| ✗ | +460 | 4 | u32/f32 | first_person_optic_attach_node |  | 1294297178 |
| ✗ | +464 | 4 | u32/f32 | auto_drop_ability |  | 0 |
| ✗ | +468 | 1 | u8 | should_weapon_scream |  | 1 |
| ✗ | +472 | 4 | u32/f32 | enter_first_person_aim_audio_event |  | 0 |
| ✗ | +476 | 4 | u32/f32 | exit_first_person_aim_audio_event |  | 0 |
| ✗ | +480 | 4 | u32/f32 | first_person_aim_audio_event_node_id |  | 0 |
| ✗ | +484 | 4 | u32/f32 | enter_third_person_aim_audio_event |  | 0 |
| ✗ | +488 | 4 | u32/f32 | exit_third_person_aim_audio_event |  | 0 |
| ✗ | +492 | 4 | u32/f32 | third_person_aim_audio_event_node_id |  | 0 |
| ✗ | +496 | 4 | u32/f32 | fire_mode_changed_audio_event |  | 0 |
| ✗ | +500 | 4 | u32/f32 | on_fire_rounds_remaining_animation_variable |  | 0 |
| ✗ | +504 | 4 | u32/f32 |  |  | 0 |
| ✗ | +512 | 384 | struct 0x10CEE58B |  |  |  |
| ✗ | +896 | 32 | struct 0x49D0074E |  |  |  |
| ✗ | +928 | 4 | u32/f32 | on_fire_round_anim_event |  | 0, 4125806552  [0..4125806552] |
| ✗ | +932 | 4 | u32/f32 | on_fire_last_round_event |  | 0 |
| ✗ | +936 | 4 | u32/f32 | on_fire_round_wielder_anim_event |  | 0 |
| ✗ | +940 | 4 | u32/f32 | on_fire_mode_changed_anim_variable |  | 0 |
| ✗ | +944 | 4 | u32/f32 | on_fire_mode_changed_wielder_anim_event |  | 0 |
| ✗ | +948 | 4 | u32/f32 | fire_ability |  | 0 |
| ✗ | +952 | 4 | u32/f32 |  |  | 0 |
| ✗ | +956 | 4 | u32/f32 |  |  | 0 |
| ✗ | +960 | 1 | u8 | infinite_ammo |  | 0 |
| ✗ | +964 | 64 | struct 0xEE866013 |  |  |  |
| ✗ | +1032 | 8 | u64 | ammo_icon_inner |  | 0xFB6B3350A1645AA8, 0xFB6B3350A1645AA8 |
| ✗ | +1040 | 8 | u64 | ammo_icon_outer |  | 0x728B4020ADEADDF6, 0x728B4020ADEADDF6 |
| ✗ | +1048 | 160 | struct 0x2F79AD03 |  |  |  |
| ✗ | +1208 | 4 | u32/f32 | UnkHash2 |  | 0 |
| ✗ | +1212 | 4 | u32/f32 | UnkHash3 |  | 0 |
| ✗ | +1216 | 4 | u32/f32 | UnkHash4 |  | 0 |
| ✗ | +1220 | 4 | u32/f32 |  |  | 0 |
| ✗ | +1224 | 4 | u32/f32 | UnkFloat |  | 0 |
| ✗ | +1228 | 1 | u8 |  |  | 0 |
| ✗ | +1232 | 4 | u32/f32 |  |  | 1065353216  (f32: 1) |

### ProjectileWeaponComponentData → ProjectileWeaponComponent (57 members, 3 editable, 278 rows)

tables: fire mode

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
|  | +0 | 4 | u32/f32 | projectile_type | proj_fire | 7, 42, 46 …  [7..349] |
|  | +4 | 12 | struct 0x85B82A43 | rounds_per_minute | rpm_1, rpm, rpm_3 |  |
| ✗ | +16 | 12 | struct 0x85B82A43 | zeroing_slots |  |  |
| ✗ | +28 | 4 | u32/f32 | zeroing_hipfire |  | 1101004800  (f32: 20) |
| ✗ | +32 | 4 | u32/f32 | current_zeroing_slot |  | 0 |
| ✗ | +36 | 1 | u8 | infinite_ammo |  | 0, 1  [0..1] |
| ✗ | +40 | 8 | u64 | ProjectileEntity |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +48 | 4 | u32/f32 | firenode_pose_limit |  | 0, 1084227584, 1097859072 …  (f32: 0, 5)  [0..1127481344] |
| ✗ | +52 | 16 | struct 0xA981D3A1 | heat_buildup |  |  |
| ✗ | +68 | 1 | u8 | scale_down_used_fire_node |  | 0 |
| ✗ | +72 | 32 | struct 0xAEB3CFCB | on_round_fired_shakes |  |  |
| ✗ | +104 | 4 | u32/f32 | num_low_ammo_rounds |  | 4 |
| ✗ | +108 | 4 | u32/f32 | low_ammo_audio_event |  | 0 |
| ✗ | +112 | 4 | u32/f32 | last_bullet_audio_event |  | 0 |
| ✗ | +116 | 4 | u32/f32 | last_bullet_owner_vo_event |  | 2645484469 |
| ✗ | +120 | 4 | u32/f32 | wind_effect_template |  | 0 |
| ✗ | +124 | 4 | u32/f32 | speed_multiplier |  | 1065353216  (f32: 1) |
| ✗ | +128 | 8 | struct 0xDFB2C267 | damage_addends |  | 0 |
| ✗ | +136 | 8 | struct 0xDFB2C267 | ap_addends |  | 0 |
| ✗ | +144 | 4 | u32/f32 | spinup_time |  | 0 |
| ✗ | +148 | 1 | u8 | rpc_synced_fire_events |  | 0, 1  [0..1] |
| ✗ | +152 | 72 | struct 0x2EB74158 | casing_eject |  |  |
| ✗ | +224 | 8 | u64 | muzzle_flash |  | 0xCFC50B3165A6970B, 0x0000000000000000 … |
| ✗ | +232 | 4 | u32/f32 | shockwave_type |  | 38 |
| ✗ | +236 | 1 | u8 | use_faint_shockwave |  | 1 |
| ✗ | +237 | 1 | u8 | use_midi_event_system |  | 0, 1  [0..1] |
| ✗ | +240 | 8 | struct 0x85B82A42 | midi_timing_randomization |  | 0 |
| ✗ | +248 | 4 | u32/f32 | midi_stop_delay |  | 0 |
| ✗ | +252 | 4 | u32/f32 | fire_loop_start_audio_event |  | 0, 873017846  (f32: 0, 1.278e-07)  [0..873017846] |
| ✗ | +256 | 4 | u32/f32 | fire_loop_stop_audio_event |  | 0, 1645131656  [0..1645131656] |
| ✗ | +260 | 4 | u32/f32 | fire_single_audio_event |  | 0, 192313521, 1667744348 …  [0..2348066281] |
| ✗ | +264 | 4 | u32/f32 | fire_all_barrel_audio_event |  | 0 |
| ✗ | +268 | 4 | u32/f32 | fire_reflect_audio_event |  | 0 |
| ✗ | +272 | 4 | u32/f32 | silenced_fire_reflect_audio_event |  | 0 |
| ✗ | +276 | 4 | u32/f32 | haptics_fire_loop_start_audio_event |  | 0 |
| ✗ | +280 | 4 | u32/f32 | haptics_fire_loop_stop_audio_event |  | 0 |
| ✗ | +288 | 8 | u64 | FireLoopCameraShake |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +296 | 8 | struct 0x85B82A42 | fire_loop_camera_shake_radius |  | 0 |
| ✗ | +304 | 224 | struct 0x9D5EFA1C |  |  |  |
| ✗ | +528 | 4 | u32/f32 | silenced_fire_loop_start_audio_event |  | 0 |
| ✗ | +532 | 4 | u32/f32 | silenced_fire_loop_stop_audio_event |  | 0 |
| ✗ | +536 | 4 | u32/f32 | silenced_fire_single_audio_event |  | 0 |
| ✗ | +540 | 4 | u32/f32 | fire_source_node |  | -1.433e-09, 0, 4.059e-12 …  [-1.433e-09..8.66e+05] |
| ✗ | +544 | 4 | u32/f32 | dry_fire_audio_event |  | 0 |
| ✗ | +548 | 4 | u32/f32 | dry_fire_repeat_audio_event |  | 0 |
| ✗ | +552 | 4 | u32/f32 | heat_percentage_material_variable |  | 0 |
| ✗ | +556 | 1 | u8 | silenced |  | 0 |
| ✗ | +560 | 4 | u32/f32 | aim_zeroing_quality |  | 1, 2, 3 …  [1..4] |
| ✗ | +564 | 1 | u8 | casing_eject_disabled_on_fire |  | 0 |
| ✗ | +568 | 4 | u32/f32 | burst_fire_rate |  | 0 |
| ✗ | +572 | 4 | u32/f32 | weapon_function_muzzle_velocity |  | 1125515264  (f32: 150) |
|  | +576 | 4 | u32/f32 | weapon_function_projectile_type | projectile_2 | 0 |
| ✗ | +584 | 8 | u64 |  |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +592 | 1 | u8 |  |  | 0, 1  [0..1] |
| ✗ | +596 | 4 | u32/f32 |  |  | 2 |
| ✗ | +600 | 12 | 12B |  |  |  |
| ✗ | +612 | 1 | u8 |  |  | 0 |

### ProjectileSettings → ProjectileInfo (56 members, 11 editable, 355 rows)

tables: projectile

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 4 | u32/f32 | type |  | 118, 132, 133 …  [118..343] |
| ✗ | +4 | 4 | u32/f32 | name_upper |  | 0, 96621472, 1027666422 …  [0..4135288639] |
| ✗ | +8 | 4 | u32/f32 | name_cased |  | 0, 233995848, 1028168550 …  [0..3990334796] |
| ✗ | +12 | 4 | u32/f32 | short_name |  | 4056765033 |
| ✗ | +16 | 8 | u64 | hud_icon |  | 0x6A6598587D4BC8F5, 0x6A6598587D4BC8F5 |
|  | +24 | 4 | u32/f32 | calibre | calibre, m2_calibre, t_calibre | 1065353216, 1103626240, 1109393408 …  (f32: 1, 25)  [1065353216..1112014848] |
|  | +28 | 4 | u32/f32 | num_projectiles | pellets, m2_pellets, t_pellets | 1 |
|  | +32 | 4 | u32/f32 | speed | velocity, m2_velocity, p192_velocity | 1106247680, 1133903872, 1140457472  (f32: 30, 300)  [1106247680..1140457472] |
|  | +36 | 4 | u32/f32 | mass | mass, m2_mass, t_mass | 1093664768, 1112014848, 1120403456 …  (f32: 11, 50)  [1093664768..1140457472] |
|  | +40 | 4 | u32/f32 | drag | drag, m2_drag, t_drag | 0.3, 0.5  [0.3..0.5] |
|  | +44 | 4 | u32/f32 | gravity_multiplier | gravity, m2_gravity, p192_gravity | 1065353216  (f32: 1) |
| ✗ | +48 | 4 | u32/f32 | simulation_steps |  | 1 |
| ✗ | +52 | 4 | u32/f32 | life_time |  | 0, 0.35  [0..0.35] |
| ✗ | +56 | 4 | u32/f32 | life_time_randomness |  | 0 |
| ✗ | +60 | 4 | u32/f32 | damage_info_type |  | 0, 39, 244 …  [0..261] |
|  | +64 | 4 | u32/f32 | penetration_slowdown | pen_slowdown, m2_pen_slowdown, t_pen_slowdown | 0.25 |
| ✗ | +72 | 8 | u64 | ParticleThrusterEffectPath? |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +80 | 8 | u64 | LowAmmoParticleThrusterEffectPath? |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +88 | 4 | u32/f32 | particle_thruster_effect_length |  | 0 |
| ✗ | +96 | 8 | u64 | ParticleTrailEffectPath? |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +104 | 8 | u64 | DissipateParticleEffectPath? |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +112 | 8 | u64 | DisintegrationParticleEffectPath? |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +120 | 8 | u64 | HitDirectionHintEffect? |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +128 | 8 | u64 | projectile_unit_path |  | 0x71E52F800636B336, 0x4FD8795ED60F5579 … |
| ✗ | +136 | 4 | u32/f32 | explosion_threshold_angle |  | 0, 1117782016, 1119092736  (f32: 0, 80)  [0..1119092736] |
| ✗ | +140 | 1 | u8 | can_expire_after_impact |  | 1 |
|  | +144 | 4 | u32/f32 | explosion_type_on_impact | impact_explosion, m2_impact_explosion, t_impact_explosion | 0, 14, 75 …  [0..423] |
|  | +148 | 4 | u32/f32 | explosion_proximity | fuse_proximity, m2_fuse_proximity, c1_fuse_proximity | 0 |
|  | +152 | 4 | u32/f32 | explosion_delay | fuse_delay, m2_fuse_delay, c1_fuse_delay | 0, 0.5, 0.8  [0..0.8] |
|  | +156 | 4 | u32/f32 | explosion_type_expire | expiry_explosion, m2_expiry_explosion, t_expiry_explosion | 0, 277, 419  [0..419] |
| ✗ | +160 | 4 | u32/f32 | arming_distance |  | 0 |
| ✗ | +164 | 4 | u32/f32 | decal_size |  | 3212836864  (f32: -1) |
| ✗ | +168 | 4 | u32/f32 | surface_impact_type |  | 0.1 |
| ✗ | +172 | 4 | u32/f32 | ricochet_impact_type |  | 0, 3  [0..3] |
| ✗ | +176 | 4 | u32/f32 | max_ricochets |  | 0, 3  [0..3] |
| ✗ | +180 | 4 | u32/f32 | ricochet_threshold_angle |  | 1, 5  [1..5] |
| ✗ | +184 | 4 | u32/f32 | ricochet_threshold_speed |  | 1118175232, 1119092736  (f32: 83, 90)  [1118175232..1119092736] |
| ✗ | +188 | 4 | u32/f32 | ricochet_angle_loss |  | 1092616192, 1114636288  (f32: 10, 60)  [1092616192..1114636288] |
| ✗ | +192 | 4 | u32/f32 | ricochet_spread_vertical |  | 0.75 |
| ✗ | +196 | 4 | u32/f32 | ricochet_spread_horizontal |  | 0, 1084227584  (f32: 0, 5)  [0..1084227584] |
| ✗ | +200 | 4 | u32/f32 | audio_crack_event |  | 0, 1101004800  (f32: 0, 20)  [0..1101004800] |
| ✗ | +204 | 4 | u32/f32 | audio_ricochet_event |  | 0 |
| ✗ | +208 | 4 | u32/f32 | audio_trail_event_start |  | 0 |
| ✗ | +212 | 4 | u32/f32 | audio_trail_event_stop |  | 0, 223688661, 657364492 …  [0..3742797545] |
| ✗ | +216 | 4 | u32/f32 | audio_trail_event_stop |  | 0, 1041721433, 1880483028 …  [0..4071212405] |
| ✗ | +220 | 4 | u32/f32 | UnkFloat2? |  | 3212836864  (f32: -1) |
| ✗ | +224 | 4 | u32/f32 | UnkAudioEvent? |  | 0 |
| ✗ | +228 | 1 | u8 | status_effect_volume_template |  | 0 |
| ✗ | +232 | 4 | u32/f32 | effect_damage_type |  | 0 |
| ✗ | +236 | 4 | u32/f32 | fire_template |  | 1, 2, 3  [1..3] |
| ✗ | +240 | 4 | u32/f32 | projectile_flags_1 |  | 0 |
| ✗ | +244 | 2 | u16 | raycast_template |  | 125, 188, 6168  [125..6168] |
| ✗ | +248 | 4 | u32/f32 | proximity_explosion_collision_filter |  | 0 |
| ✗ | +252 | 4 | u32/f32 | projectile_flags_2 |  | 0.0001808 |
| ✗ | +256 | 1 | u8 |  |  | 0 |
| ✗ | +260 | 12 | struct 0x85B82A43 | projectile_attachment_local_offset |  |  |

### WeaponHeatComponentData → WeaponHeatComponent (54 members, 11 editable, 30 rows)

tables: weapon heat

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
|  | +0 | 72 | struct 0x8F124598 | HeatLevelSettings | heatlvl1_at, heatlvl2_at, heatlvl3_at |  |
| ✗ | +72 | 4 | u32/f32 | rpm_multiplier |  | 1065353216  (f32: 1) |
| ✗ | +76 | 4 | u32/f32 | UnknownFloat2 |  | 1065353216  (f32: 1) |
| ✗ | +80 | 1 | u8 | forbid_shoot_after_overheated |  | 1 |
|  | +84 | 4 | u32/f32 | magazines | heatsinks_start | 0, 3, 6  [0..6] |
|  | +88 | 4 | u32/f32 | magazines_refill | heatsinks_supply | 6 |
|  | +92 | 4 | u32/f32 | magazines_max | heatsinks_max | 0, 3, 12  [0..12] |
|  | +96 | 4 | u32/f32 | overheat_temperature | heat_capacity | 1120403456, 1132068864, 1157234688  (f32: 100, 250)  [1120403456..1157234688] |
| ✗ | +100 | 4 | u32/f32 | overheat_temperature_recover |  | 0 |
| ✗ | +104 | 4 | u32/f32 | warning_temperature |  | 1117126656, 1127153664, 1153138688  (f32: 75, 175)  [1117126656..1153138688] |
| ✗ | +108 | 4 | u32/f32 | emission_temperature |  | 1112014848, 1120403456, 1148846080  (f32: 50, 100)  [1112014848..1148846080] |
| ✗ | +112 | 4 | u32/f32 | rtpc_temperature |  | 0, 1148846080  (f32: 0, 1000)  [0..1148846080] |
|  | +116 | 4 | u32/f32 | temp_gain_per_shot | heat_shot | 0.5, 2, 2.15  [0.5..2.15] |
|  | +120 | 4 | u32/f32 | temp_gain_per_second | heat_second | 0, 0.1, 1 …  [0..8] |
| ✗ | +124 | 4 | u32/f32 | temp_gain_per_second_modifier |  | 1120403456  (f32: 100) |
|  | +128 | 4 | u32/f32 | temp_loss_per_second | heat_cool | 1084227584, 1090519040, 1092616192  (f32: 5, 8)  [1084227584..1092616192] |
| ✗ | +132 | 4 | u32/f32 | temp_loss_modifier_extreme_heat |  | 0.75 |
| ✗ | +136 | 4 | u32/f32 | temp_loss_modifier_extreme_cold |  | 1.5 |
|  | +140 | 4 | u32/f32 | temp_loss_per_second_overheated | heat_cool_overheated | 1137180672  (f32: 400) |
| ✗ | +144 | 1 | u8 | needs_reload_after_overheat |  | 1 |
| ✗ | +148 | 4 | u32/f32 | firing_charge |  | 0, 1092616192, 1120403456  (f32: 0, 10)  [0..1120403456] |
|  | +152 | 4 | u32/f32 | charge_gain_per_second | windup | 1120403456, 1128792064  (f32: 100, 200)  [1120403456..1128792064] |
|  | +156 | 4 | u32/f32 | charge_loss_per_second | winddown | 1117126656, 1120403456, 1140457472  (f32: 75, 100)  [1117126656..1140457472] |
| ✗ | +160 | 1 | u8 | reset_charge_after_shot |  | 0 |
| ✗ | +161 | 1 | u8 | charging_triggers_dry_fire_events |  | 0 |
| ✗ | +164 | 4 | u32/f32 | owner_warning_vo_event |  | 267052615 |
| ✗ | +168 | 4 | u32/f32 | owner_overheat_vo_event |  | -1.483e-06 |
| ✗ | +172 | 4 | u32/f32 | min_reload_temperature |  | 0, 1112014848  (f32: 0, 50)  [0..1112014848] |
| ✗ | +176 | 4 | u32/f32 | charge_mesh |  | 0, 2629263327  [0..2629263327] |
| ✗ | +180 | 4 | u32/f32 | charge_material |  | 0, 2113163872  [0..2113163872] |
| ✗ | +184 | 4 | u32/f32 | charge_variable |  | 0, 3379599616  (f32: -9.855e+05, 0)  [0..3379599616] |
| ✗ | +188 | 4 | u32/f32 | overheat_variable |  | 0, 92240865  [0..92240865] |
| ✗ | +192 | 1 | u8 | UnknownBool2 |  | 0 |
| ✗ | +196 | 288 | struct 0xA6FDE7CF | HeatMaterialSettings |  |  |
| ✗ | +484 | 4 | u32/f32 | charging_start_audio_event |  | 0, 288323536, 600843021  [0..600843021] |
| ✗ | +488 | 4 | u32/f32 | charging_complete_audio_event |  | 0, 288323536, 600843021  [0..600843021] |
| ✗ | +492 | 4 | u32/f32 | discharging_start_audio_event |  | 0, 1718037339, 2931772786  [0..2931772786] |
| ✗ | +496 | 4 | u32/f32 | discharging_complete_audio_event |  | 0, 1718037339, 2931772786  [0..2931772786] |
| ✗ | +500 | 4 | u32/f32 | charge_source_node |  | 0, 2601604451, 3886002811  [0..3886002811] |
| ✗ | +504 | 4 | u32/f32 | on_temp_yellow_start_sound_event |  | 0, 317119392, 496760146 …  [0..3089820262] |
| ✗ | +508 | 4 | u32/f32 | on_temp_yellow_stop_sound_event |  | 0, 362614256, 2539347916 …  [0..2847120394] |
| ✗ | +512 | 4 | u32/f32 | on_overheat_start_sound_event |  | 0, 471745860, 2288211034  [0..2288211034] |
| ✗ | +516 | 4 | u32/f32 | on_overheat_stop_sound_event |  | -1.743e+04, 0, 1.738e-12  [-1.743e+04..1.738e-12] |
| ✗ | +520 | 4 | u32/f32 | on_overheat_anim_event |  | 0 |
| ✗ | +524 | 4 | u32/f32 | on_overheat_alarm_start_sound_event |  | 0, 858357660, 1628302831  [0..1628302831] |
| ✗ | +528 | 4 | u32/f32 | on_overheat_alarm_stop_sound_event |  | 0, 1442842101, 3950639984  [0..3950639984] |
| ✗ | +536 | 8 | u64 | CameraShakeOnChargingStart |  | 0x0000000000000000, 0x0000000000000000 … |
| ✗ | +544 | 8 | u64 | CameraShakeOnFiringStart |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +552 | 8 | u64 | CameraShakeOnYellowTempStart |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +560 | 8 | u64 | CameraShakeOnRedTempStart |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +568 | 8 | u64 | CameraShakeOnFireStopConstant |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +576 | 8 | u64 | CameraShakeOnFireStopKick |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +584 | 4 | u32/f32 | overheat_ability |  | 0, 2882, 2884  [0..2884] |
| ✗ | +588 | 4 | u32/f32 | UnknownFloat6 |  | 1120403456  (f32: 100) |

### JumppackComponentData → JumppackComponent (53 members, 10 editable, 3 rows)

tables: jump pack

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
|  | +0 | 4 | u32/f32 |  | bp_launch | 1108082688, 1109393408  (f32: 35, 40)  [1108082688..1109393408] |
| ✗ | +4 | 4 | u32/f32 |  |  | 1101004800  (f32: 20) |
| ✗ | +8 | 12 | struct 0x85B82A43 |  |  |  |
| ✗ | +20 | 4 | u32/f32 |  |  | 1.5 |
|  | +24 | 4 | u32/f32 |  | bp_takeoff | 0.5 |
| ✗ | +28 | 4 | u32/f32 |  |  | 0.75 |
|  | +32 | 4 | u32/f32 |  | bp_forward | 0.05, 0.4  [0.05..0.4] |
| ✗ | +36 | 4 | u32/f32 |  |  | 1114636288  (f32: 60) |
|  | +40 | 4 | u32/f32 |  | bp_landing_time | 1065353216  (f32: 1) |
| ✗ | +44 | 4 | u32/f32 |  |  | 0.1, 0.3  [0.1..0.3] |
| ✗ | +48 | 4 | u32/f32 |  |  | 1065353216  (f32: 1) |
| ✗ | +52 | 4 | u32/f32 |  |  | 1077936128  (f32: 3) |
| ✗ | +56 | 4 | u32/f32 |  |  | 1065353216  (f32: 1) |
|  | +60 | 4 | u32/f32 |  | bp_steer | 1082130432  (f32: 4) |
| ✗ | +64 | 1 | u8 |  |  | 0 |
| ✗ | +68 | 4 | u32/f32 |  |  | 59 |
| ✗ | +72 | 4 | u32/f32 |  |  | 2055, 2503  [2055..2503] |
| ✗ | +76 | 4 | u32/f32 |  |  | 2056, 2504  [2056..2504] |
| ✗ | +80 | 4 | u32/f32 |  |  | 2057, 2505  [2057..2505] |
| ✗ | +84 | 4 | u32/f32 |  |  | 0, 2058, 2506  [0..2506] |
| ✗ | +88 | 4 | u32/f32 |  |  | 1288385068, 4262094111  [1288385068..4262094111] |
| ✗ | +92 | 4 | u32/f32 |  |  | 0, 2059, 2508  [0..2508] |
| ✗ | +96 | 4 | u32/f32 |  |  | 0, 2060, 2509  [0..2509] |
| ✗ | +100 | 8 | u64 |  |  | 0, 5634997093662  [0..5634997093662] |
| ✗ | +108 | 8 | u64 |  |  | 0, 5639292060959  [0..5639292060959] |
| ✗ | +116 | 4 | u32/f32 |  |  | 3778614046 |
| ✗ | +120 | 12 | struct 0x85B82A43 |  |  |  |
| ✗ | +132 | 12 | struct 0x85B82A43 |  |  |  |
| ✗ | +144 | 1 | u8 |  |  | 0, 1  [0..1] |
| ✗ | +145 | 1 | u8 |  |  | 0, 1  [0..1] |
| ✗ | +148 | 4 | u32/f32 |  |  | 0 |
| ✗ | +152 | 1 | u8 |  |  | 0, 1  [0..1] |
| ✗ | +153 | 1 | u8 |  |  | 0, 1  [0..1] |
| ✗ | +154 | 1 | u8 |  |  | 0, 1  [0..1] |
| ✗ | +155 | 1 | u8 |  |  | 0, 1  [0..1] |
|  | +156 | 4 | u32/f32 |  | bp_climb_time | 1086324736, 3212836864  (f32: -1, 6)  [1086324736..3212836864] |
|  | +160 | 16 | struct 0x85B82A42 |  | bp_agility, bp_agility_high, bp_climb_accel |  |
|  | +176 | 8 | struct 0x85B82A42 |  | bp_hover_speed, bp_climb_target | 4692750812800090112, 4740038608911073280  [4692750812800090112..4740038608911073280] |
|  | +184 | 16 | struct 0x85B82A42 |  | bp_climb_speed |  |
|  | +200 | 8 | struct 0x85B82A42 |  | bp_hover_fuel, bp_climb_fuel | 0, 1070386381  [0..1070386381] |
| ✗ | +208 | 4 | u32/f32 |  |  | 0, 0.5  [0..0.5] |
| ✗ | +212 | 4 | u32/f32 |  |  | 2.8, 10  [2.8..10] |
| ✗ | +216 | 4 | u32/f32 |  |  | 1.5, 10  [1.5..10] |
| ✗ | +220 | 12 | struct 0x85B82A43 |  |  |  |
| ✗ | +232 | 4 | u32/f32 |  |  | 0, 1430067306  [0..1430067306] |
| ✗ | +236 | 4 | u32/f32 |  |  | 0, 2242773211  [0..2242773211] |
| ✗ | +240 | 4 | u32/f32 |  |  | 0, 1454103075  [0..1454103075] |
| ✗ | +244 | 4 | u32/f32 |  |  | 0, 40722924  [0..40722924] |
| ✗ | +248 | 4 | u32/f32 |  |  | 0, 4136739262  [0..4136739262] |
| ✗ | +252 | 4 | u32/f32 |  |  | 0, 1065353216  (f32: 0, 1)  [0..1065353216] |
| ✗ | +256 | 4 | u32/f32 |  |  | 1073741824  (f32: 2) |
| ✗ | +260 | 12 | struct 0x85B82A43 |  |  |  |
| ✗ | +272 | 8 | struct 0x85B82A42 |  |  | 4575657222473777152, 4611686019501129728  [4575657222473777152..4611686019501129728] |

### HealthComponentData → HealthComponent (51 members, 6 editable, 506 rows)

tables: health

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
|  | +0 | 4 | u32/f32 | health | unit_health, health, drone_health | 11, 180, 500 …  [11..6000] |
|  | +4 | 4 | u32/f32 | health_changerate | regen, regen_2, silo_regen | 0 |
| ✗ | +8 | 1 | u8 | health_changerate_disabled |  | 0, 1  [0..1] |
|  | +12 | 4 | u32/f32 | health_changerate_cooldown | regen_delay, regen_delay_2 | 0 |
| ✗ | +16 | 4 | u32/f32 | regeneration_segments |  | 1 |
|  | +20 | 4 | u32/f32 | regeneration_changerate | regen_phase, regen_phase_2 | 0 |
| ✗ | +24 | 4 | u32/f32 | constitution |  | 0 |
| ✗ | +28 | 4 | u32/f32 | constitution_changerate |  | 0 |
| ✗ | +32 | 1 | u8 | constitution_disables_interactions |  | 0 |
| ✗ | +36 | 4 | u32/f32 | zone_bleedout_changerate |  | 0 |
| ✗ | +40 | 4 | u32/f32 | unit_size |  | 0, 1, 2 …  [0..3] |
| ✗ | +44 | 4 | u32/f32 | unit_mass |  | 0 |
| ✗ | +48 | 4 | u32/f32 | kill_score |  | 0 |
| ✗ | +52 | 8 | struct 0x4CAB1DD7 | wounded_state |  | 4557642823972683776 |
|  | +64 | 456 | struct 0x33EA64FB | default_damageable_zone_info | unit_durable, pod_durable, body1_durable |  |
|  | +520 | 20976 | struct 0xD19131CF | DamageableZones | zone3_armor, zone3_armor_2, zone4_health |  |
| ✗ | +21496 | 1 | u8 | UnknownBool1 |  | 0 |
| ✗ | +21500 | 32 | struct 0xCED49B49 | ElementDamageValues |  |  |
| ✗ | +21532 | 24 | struct 0x0B0112B7 | decay |  |  |
| ✗ | +21556 | 40 | 40B | death_sound_ids |  |  |
| ✗ | +21596 | 1 | u8 | trigger_death_sounds_on_remove |  | 0 |
| ✗ | +21600 | 48 | struct 0x10CEE58B | on_hit_effect |  |  |
| ✗ | +21648 | 112 | struct 0x2790F5BA | WhileLivingEffect |  |  |
| ✗ | +21760 | 48 | struct 0x10CEE58B | on_death_effect |  |  |
| ✗ | +21808 | 48 | struct 0x10CEE58B | bled_to_death_effect |  |  |
| ✗ | +21856 | 48 | struct 0x10CEE58B | UnknownEffect |  |  |
| ✗ | +21904 | 1 | u8 | require_demolition |  | 0 |
| ✗ | +21908 | 4 | u32/f32 | downed_anim |  | 0 |
| ✗ | +21912 | 4 | u32/f32 | dead_anim |  | 0 |
| ✗ | +21916 | 4 | u32/f32 | UnknownFloat1 |  | 0 |
| ✗ | +21920 | 4 | u32/f32 | UnknownHash1 |  | 0 |
| ✗ | +21924 | 4 | u32/f32 | UnknownHash2 |  | 0 |
| ✗ | +21928 | 4 | u32/f32 | UnknownHash3 |  | 0 |
| ✗ | +21932 | 4 | u32/f32 | on_downed_hide_visibility_group |  | 0 |
| ✗ | +21936 | 4 | u32/f32 | on_downed_show_visibility_group |  | 0 |
| ✗ | +21940 | 4 | u32/f32 | on_dead_hide_visibility_group |  | 0, 3954544245  [0..3954544245] |
| ✗ | +21944 | 4 | u32/f32 | on_dead_show_visibility_group |  | 0 |
| ✗ | +21948 | 16 | 16B | UnknownVisibilityGroupHashes |  |  |
| ✗ | +21964 | 16 | 16B | UnknownVisibilityGroupHashes2 |  |  |
| ✗ | +21980 | 4 | u32/f32 | UnknownDeathDestructionHash |  | 0 |
| ✗ | +21984 | 4 | u32/f32 | on_death_destruction_level |  | 3, 4, 5 …  [3..9] |
| ✗ | +21988 | 1 | u8 | can_die_naturally |  | 1 |
| ✗ | +21992 | 4 | u32/f32 | death_propagation |  | 0 |
| ✗ | +21996 | 16 | 16B | ui_health_strings |  |  |
| ✗ | +22012 | 1 | u8 | UnknownBool2 |  | 0 |
| ✗ | +22016 | 4 | u32/f32 | UnknownFloat2 |  | 0 |
| ✗ | +22020 | 1 | u8 | UnknownBool3 |  | 1 |
| ✗ | +22021 | 1 | u8 | UnknownBool4 |  | 0 |
| ✗ | +22024 | 64 | struct 0x3F011AEF | DeathAnimationSounds |  |  |
| ✗ | +22088 | 4 | u32/f32 | UnknownThinHash |  | 0 |
| ✗ | +22092 | 1 | u8 |  |  | 0 |

### ShieldComponentData → ShieldComponent (49 members, 6 editable, 15 rows)

tables: shield

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
|  | +0 | 4 | u32/f32 | radius | shield_radius | 0, 1.3, 1.8 …  [0..60] |
| ✗ | +4 | 4 | u32/f32 | shield_node |  | 0, 41183413, 494311543 …  [0..2420200265] |
| ✗ | +8 | 4 | u32/f32 |  |  | 0, 2748617169, 3340321277 …  [0..4037424617] |
| ✗ | +12 | 64 | 64B |  |  |  |
|  | +76 | 4 | u32/f32 | charge | shield_capacity | 1120403456, 1125515264, 1148846080 …  (f32: 100, 150)  [1120403456..1176256512] |
| ✗ | +80 | 4 | u32/f32 |  |  | 0, 1073741824, 1077936128 …  (f32: 0, 2)  [0..1082130432] |
| ✗ | +84 | 1 | u8 |  |  | 0, 1  [0..1] |
|  | +88 | 4 | u32/f32 | recharge_delay | shield_delay | 1065353216, 1077936128, 1084227584 …  (f32: 1, 3)  [1065353216..1114636288] |
|  | +92 | 4 | u32/f32 | broken_recharge_delay | shield_broken | 1086324736, 1090519040, 1094713344 …  (f32: 6, 8)  [1086324736..1123024896] |
|  | +96 | 4 | u32/f32 | recharge_rate | shield_rate | 0, 1125515264, 1128792064 …  (f32: 0, 150)  [0..1157234688] |
|  | +100 | 4 | u32/f32 | starter_charge_on_recharge | shield_restart | 1065353216, 1120403456, 1125515264 …  (f32: 1, 100)  [1065353216..1159479296] |
| ✗ | +104 | 4 | u32/f32 |  |  | 0, 1073741824  (f32: 0, 2)  [0..1073741824] |
| ✗ | +108 | 4 | u32/f32 |  |  | 0, 24  [0..24] |
| ✗ | +112 | 4 | u32/f32 |  |  | 1065353216  (f32: 1) |
| ✗ | +120 | 8 | u64 |  |  | 0x0000000000000000, 0x733A4E2DC738DBE9 … |
| ✗ | +128 | 8 | u64 | shield_break_particles |  | 0x0D26C244BCDC0AD1, 0xC333FECB6457E27D … |
| ✗ | +136 | 4 | u32/f32 | shield_break_sound |  | 0, 142715993, 192646497 …  [0..4191843541] |
| ✗ | +140 | 4 | u32/f32 | shield_unk_sound_0x008C |  | 0, 192646497  [0..192646497] |
| ✗ | +144 | 4 | u32/f32 | shield_online_sound |  | 0, 239834729, 1412411401 …  [0..3314442605] |
| ✗ | +148 | 4 | u32/f32 | shield_idle_loop_start_sound |  | 0, 297542164, 420191383 …  [0..4188928295] |
| ✗ | +152 | 4 | u32/f32 | shield_idle_loop_stop_sound |  | 0, 589174221, 1807716893 …  [0..4288704149] |
| ✗ | +156 | 4 | u32/f32 | shield_bubble_loop_start_sound |  | 0, 3942179094  [0..3942179094] |
| ✗ | +160 | 4 | u32/f32 | shield_bubble_loop_stop_sound |  | 0, 377749160  [0..377749160] |
| ✗ | +164 | 4 | u32/f32 | shield_surface_loop_start_sound |  | 0, 1404604684, 3452637299  [0..3452637299] |
| ✗ | +168 | 4 | u32/f32 | shield_surface_loop_stop_sound |  | -6.364e+04, 0, 9.15e-16  [-6.364e+04..9.15e-16] |
| ✗ | +172 | 1 | u8 |  |  | 0, 1  [0..1] |
| ✗ | +173 | 1 | u8 |  |  | 0, 1  [0..1] |
| ✗ | +174 | 1 | u8 |  |  | 0, 1  [0..1] |
| ✗ | +176 | 4 | u32/f32 | start_offline |  | 0 |
| ✗ | +180 | 4 | u32/f32 | shield_recharging_loop_start_sound |  | 0, 749920396, 1661027042 …  [0..3865076282] |
| ✗ | +184 | 4 | u32/f32 | shield_recharging_loop_stop_sound |  | 0, 570440274, 1852415162 …  [0..4141563610] |
| ✗ | +188 | 4 | u32/f32 | shield_pass_through_sound |  | 0, 99157305, 1718113561 …  [0..4063244793] |
| ✗ | +192 | 4 | u32/f32 | shield_pass_through_sound_avatar |  | 0, 874388386, 938842190 …  [0..3614750990] |
| ✗ | +196 | 4 | u32/f32 | shield_recharging_loop_event_node |  | 0.4057 |
| ✗ | +200 | 4 | u32/f32 | shield_unit_coming_online_sound |  | 0 |
| ✗ | +204 | 4 | u32/f32 | shield_unit_coming_online_node |  | 1.029e+04 |
| ✗ | +208 | 4 | u32/f32 | shield_activate_animation_event |  | 2297540503, 3470895594  [2297540503..3470895594] |
| ✗ | +212 | 4 | u32/f32 | shield_deactivate_animation_event |  | 1922100775, 3731554523  [1922100775..3731554523] |
| ✗ | +216 | 4 | u32/f32 | hit_effect_receiver_type |  | 7, 8, 11 …  [7..12] |
| ✗ | +220 | 1 | u8 | inflict_pain |  | 0 |
| ✗ | +224 | 4 | u32/f32 | block_melee_type |  | 0, 1  [0..1] |
| ✗ | +228 | 4 | u32/f32 | inside_shield_opacity |  | 0, 0.5, 0.65 …  [0..0.75] |
| ✗ | +232 | 4 | u32/f32 | shield_color_type |  | 0, 1, 2  [0..2] |
| ✗ | +236 | 1 | u8 | linked_to_status_effect_volume |  | 1 |
| ✗ | +240 | 80 | struct 0x904CF40C |  |  |  |
| ✗ | +320 | 4 | u32/f32 | charge_event_trigger_audio_node |  | 0 |
| ✗ | +324 | 4 | u32/f32 | shield_shape |  | 0, 2  [0..2] |
| ✗ | +328 | 8 | u64 |  |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +336 | 1 | u8 |  |  | 0, 1  [0..1] |

### EagleComponentData → EagleComponent (47 members, 6 editable, 11 rows)

tables: eagle

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 4 | u32/f32 | flyby_event |  | 0 |
| ✗ | +4 | 4 | u32/f32 | strafing_fire_over_event |  | 1534884119 |
| ✗ | +8 | 4 | u32/f32 | flyby_distance |  | 1142292480  (f32: 600) |
| ✗ | +12 | 4 | u32/f32 | flyby_cooldown |  | 1077936128  (f32: 3) |
| ✗ | +16 | 4 | u32/f32 | payload |  | 1, 2, 3 …  [1..5] |
| ✗ | +20 | 4 | u32/f32 | airstrike_pattern |  | 0, 3, 4 …  [0..7] |
| ✗ | +24 | 4 | u32/f32 | projectile_type |  | 0, 84, 117 …  [0..291] |
| ✗ | +32 | 8 | u64 |  |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +40 | 4 | u32/f32 | search_radius |  | 1119092736, 1127481344  (f32: 90, 180)  [1119092736..1127481344] |
| ✗ | +44 | 1 | u8 | fire_duration |  | 0, 1  [0..1] |
| ✗ | +48 | 4 | u32/f32 | bomb_interval |  | 1101004800, 1114636288, 1133903872  (f32: 20, 60)  [1101004800..1133903872] |
|  | +52 | 4 | u32/f32 | bomb_prediction_interval | eagle_fire_time | 1.5, 2  [1.5..2] |
|  | +56 | 4 | u32/f32 | approach_min_distance | eagle_bomb_gap | 0.05, 0.1, 0.2 …  [0.05..1e+04] |
| ✗ | +60 | 4 | u32/f32 | approach_max_distance |  | 0.05 |
|  | +64 | 4 | u32/f32 | approach_max_height | eagle_approach | 1145569280, 1148846080  (f32: 800, 1000)  [1145569280..1148846080] |
|  | +68 | 4 | u32/f32 |  | eagle_approach_2 | 1145569280, 1148846080  (f32: 800, 1000)  [1145569280..1148846080] |
| ✗ | +72 | 4 | u32/f32 | num_heights_to_try |  | 1145569280, 1147207680, 1148846080  (f32: 800, 900)  [1145569280..1148846080] |
| ✗ | +76 | 4 | u32/f32 | attack_movespeed |  | 1073741824, 1086324736, 1098907648  (f32: 2, 6)  [1073741824..1098907648] |
| ✗ | +80 | 4 | u32/f32 | evade_movespeed |  | 1120403456  (f32: 100) |
| ✗ | +84 | 4 | u32/f32 | damaged_movespeed |  | 1094713344  (f32: 12) |
| ✗ | +88 | 4 | u32/f32 | acceleration |  | 1135869952  (f32: 360) |
|  | +92 | 4 | u32/f32 | deceleration | eagle_speed | 1133903872  (f32: 300) |
| ✗ | +96 | 4 | u32/f32 | damage_cooldown |  | 1133903872  (f32: 300) |
| ✗ | +100 | 4 | u32/f32 | master_target_position_adjustment |  | 1120403456  (f32: 100) |
| ✗ | +104 | 4 | u32/f32 | master_target_enemy_count |  | 1106247680  (f32: 30) |
| ✗ | +108 | 4 | u32/f32 | strafing_run_length |  | 1106247680  (f32: 30) |
| ✗ | +112 | 4 | u32/f32 | strafing_run_target_adjustment |  | 1133903872  (f32: 300) |
| ✗ | +116 | 4 | u32/f32 | strafing_run_target_bias_time |  | 1103626240  (f32: 25) |
| ✗ | +120 | 4 | u32/f32 | strafing_run_fire_distance |  | 1082130432  (f32: 4) |
|  | +124 | 4 | u32/f32 |  | eagle_run_length | 0, 1092616192, 1112014848 …  (f32: 0, 10)  [0..1114636288] |
| ✗ | +128 | 4 | u32/f32 |  |  | 1088421888  (f32: 7) |
| ✗ | +132 | 4 | u32/f32 |  |  | 0.4 |
| ✗ | +136 | 4 | u32/f32 | engine_start_audio |  | 1133903872, 1135542272, 1142292480  (f32: 300, 350)  [1133903872..1142292480] |
| ✗ | +140 | 28 | struct 0x19CCA20E |  |  |  |
| ✗ | +168 | 84 | struct 0x2308DBEC |  |  |  |
| ✗ | +252 | 40 | struct 0x2C2D1CF9 |  |  |  |
| ✗ | +292 | 4 | u32/f32 | engine_stop_audio |  | 1094713344  (f32: 12) |
| ✗ | +296 | 4 | u32/f32 |  |  | 1090519040  (f32: 8) |
| ✗ | +300 | 4 | u32/f32 |  |  | 822447567, 1501143151, 2158166289 …  [822447567..3636994674] |
| ✗ | +304 | 4 | u32/f32 |  |  | 989231445, 1910392746, 2209072266 …  [989231445..4087131915] |
| ✗ | +312 | 8 | u64 | sonic_boom_effect |  | 0xC4652C812D9C2873, 0xC4652C812D9C2873 |
| ✗ | +320 | 4 | u32/f32 |  |  | 3212836864  (f32: -1) |
| ✗ | +324 | 4 | u32/f32 |  |  | 3212836864  (f32: -1) |
| ✗ | +328 | 4 | u32/f32 |  |  | 3212836864  (f32: -1) |
| ✗ | +332 | 1 | u8 |  |  | 0 |
| ✗ | +333 | 1 | u8 |  |  | 1 |
| ✗ | +334 | 1 | u8 |  |  | 0, 1  [0..1] |

### SeekingMissileComponentData → SeekingMissileComponent (42 members, 9 editable, 29 rows)

tables: seeking missile

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 4 | u32/f32 | targeting_mode |  | 0, 1, 2 …  [0..3] |
| ✗ | +4 | 4 | u32/f32 | UnknownFloat1 |  | 0.01667 |
| ✗ | +8 | 1 | u8 | autoplay_starting_effects |  | 0, 1  [0..1] |
|  | +12 | 4 | u32/f32 | time_to_enable_guidance | missile_guidance_after | -1, 0, 0.01 …  [-1..0.9] |
| ✗ | +16 | 4 | u32/f32 | time_to_disable_guidance |  | 3212836864  (f32: -1) |
| ✗ | +20 | 4 | u32/f32 | distance_to_enable_guidance |  | 3212836864  (f32: -1) |
| ✗ | +24 | 4 | u32/f32 | distance_to_disable_guidance |  | 3212836864  (f32: -1) |
|  | +28 | 4 | u32/f32 | angle_lost_guidance | missile_lost_angle | 1127481344  (f32: 180) |
| ✗ | +32 | 4 | u32/f32 | movement_prediction_accuracy |  | 0 |
| ✗ | +36 | 4 | u32/f32 |  |  | 3212836864  (f32: -1) |
| ✗ | +40 | 4 | u32/f32 |  |  | 3212836864  (f32: -1) |
| ✗ | +44 | 4 | u32/f32 |  |  | 3212836864  (f32: -1) |
| ✗ | +48 | 4 | u32/f32 |  |  | 3212836864  (f32: -1) |
| ✗ | +52 | 4 | u32/f32 |  |  | 3212836864  (f32: -1) |
| ✗ | +56 | 4 | u32/f32 | time_to_enable_movement |  | 0, 3212836864  (f32: -1, 0)  [0..3212836864] |
| ✗ | +60 | 4 | u32/f32 | time_to_enable_explosive |  | 0, 3212836864  (f32: -1, 0)  [0..3212836864] |
|  | +64 | 4 | u32/f32 | max_lifetime | missile_lifetime | 1097859072, 1106247680  (f32: 15, 30)  [1097859072..1106247680] |
|  | +68 | 4 | u32/f32 | starting_speed | missile_launch_speed | 1065353216, 1092616192, 1101004800 …  (f32: 1, 10)  [1065353216..1120403456] |
|  | +72 | 4 | u32/f32 | minimum_speed | missile_min_speed | 1065353216, 1092616192, 1101004800 …  (f32: 1, 10)  [1065353216..1119092736] |
|  | +76 | 4 | u32/f32 | preferred_speed | missile_cruise_speed | 1116471296, 1117782016, 1119092736 …  (f32: 70, 80)  [1116471296..1128792064] |
|  | +80 | 4 | u32/f32 | acceleration | missile_acceleration | 1112014848, 1128792064  (f32: 50, 200)  [1112014848..1128792064] |
| ✗ | +84 | 4 | u32/f32 | max_angle_to_target |  | 1110704128  (f32: 45) |
|  | +88 | 4 | u32/f32 | min_turn_speed | missile_turn_cruise | 1065353216, 1073741824, 1082130432 …  (f32: 1, 2)  [1065353216..1106247680] |
|  | +92 | 4 | u32/f32 | max_turn_speed | missile_turn_slow | 1086324736, 1088421888, 1090519040 …  (f32: 6, 7)  [1086324736..1108082688] |
| ✗ | +96 | 4 | u32/f32 | p_factor |  | 0.01, 0.5  [0.01..0.5] |
| ✗ | +100 | 4 | u32/f32 | i_factor |  | 1065353216  (f32: 1) |
| ✗ | +104 | 4 | u32/f32 | d_factor |  | 0.0001 |
| ✗ | +108 | 4 | u32/f32 | target_update_interval |  | 0, 0.2  [0..0.2] |
| ✗ | +112 | 48 | struct 0x10CEE58B | missile_trail |  |  |
| ✗ | +160 | 4 | u32/f32 | missile_trail_audio_event |  | 0, 281865650, 315345141 …  [0..2780259181] |
| ✗ | +164 | 4 | u32/f32 | missile_trail_audio_event_stop |  | 0, 2347017450, 2526517935  [0..2526517935] |
| ✗ | +168 | 4 | u32/f32 | target_dot_minimum |  | -1, 0.3  [-1..0.3] |
| ✗ | +172 | 1 | u8 | javelin_firing_mode |  | 0, 1  [0..1] |
| ✗ | +173 | 1 | u8 | movement_should_be_processed_by_projectile_system |  | 0, 1  [0..1] |
| ✗ | +176 | 4 | u32/f32 | projectile_type_to_process |  | 0 |
| ✗ | +180 | 68 | struct 0x0C15CCB0 | seeking_missile_deviation |  |  |
| ✗ | +248 | 4 | u32/f32 | UnknownFloat4 |  | 3212836864  (f32: -1) |
| ✗ | +252 | 4 | u32/f32 | UnknownHash |  | 0 |
| ✗ | +256 | 1 | u8 | UnknownBool |  | 0 |
| ✗ | +257 | 1 | u8 | UnknownBool2 |  | 0 |
| ✗ | +260 | 4 | u32/f32 | UnknownFloat5 |  | 0, 0.1  [0..0.1] |
| ✗ | +264 | 4 | u32/f32 | UnknownFloat6 |  | 0, 1082130432  (f32: 0, 4)  [0..1082130432] |

### ThrowableComponentData → ThrowableComponent (42 members, 4 editable, 46 rows)

tables: throwable

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 4 | u32/f32 | dynamic_actor |  | -2.305e-17, 0.0006292, 16.95  [-2.305e-17..16.95] |
| ✗ | +4 | 4 | u32/f32 | delayed_dynamic_actor |  | 0, 0.006809  [0..0.006809] |
| ✗ | +8 | 4 | u32/f32 | delayed_dynamic_actor_duration |  | 0, 0.1  [0..0.1] |
| ✗ | +12 | 4 | u32/f32 | throw_distance_min |  | 0, 0.1, 4  [0..4] |
|  | +16 | 4 | u32/f32 | throw_distance_max | throw_distance | 1065353216, 1093664768, 1101004800  (f32: 1, 11)  [1065353216..1101004800] |
| ✗ | +20 | 1 | u8 | use_angular_velocity |  | 1 |
| ✗ | +21 | 1 | u8 | angular_velocity_in_motion_space |  | 1 |
| ✗ | +24 | 12 | struct 0x85B82A43 | custom_angular_velocity_min |  |  |
| ✗ | +36 | 12 | struct 0x85B82A43 | custom_angular_velocity_max |  |  |
| ✗ | +48 | 4 | u32/f32 | vo_release |  | 0, 2853716018, 3742874205 …  [0..3951650251] |
| ✗ | +52 | 4 | u32/f32 | animation_event_arm |  | 0, 802787461, 2184765689 …  [0..3476578654] |
| ✗ | +56 | 4 | u32/f32 | animation_event |  | 780071362  (f32: 5.797e-11) |
| ✗ | +60 | 4 | u32/f32 | animation_event_short |  | 4192910305 |
| ✗ | +64 | 4 | u32/f32 |  |  | 0, 51  [0..51] |
| ✗ | +68 | 4 | u32/f32 |  |  | 0 |
| ✗ | +72 | 4 | u32/f32 | thrower_velocity_addition |  | 0.4 |
| ✗ | +76 | 4 | u32/f32 | thrower_velocity_subtraction |  | 0.2 |
| ✗ | +80 | 4 | u32/f32 | thrower_velocity_deadzone |  | 1065353216  (f32: 1) |
| ✗ | +84 | 1 | u8 | sticky |  | 0, 1  [0..1] |
| ✗ | +88 | 4 | u32/f32 | sticky_delay |  | 0 |
| ✗ | +92 | 1 | u8 | is_impact_trigger |  | 0, 1  [0..1] |
| ✗ | +93 | 1 | u8 | ignore_thrower_impact_trigger |  | 0, 1  [0..1] |
| ✗ | +94 | 1 | u8 | drop_on_cancelled |  | 1 |
| ✗ | +96 | 4 | u32/f32 | enable_interaction_delay |  | -1, 0.5  [-1..0.5] |
|  | +100 | 4 | u32/f32 | start_amount | throw_start | 2, 3, 4  [2..4] |
|  | +104 | 4 | u32/f32 | max_amount | throw_max | 2, 4, 5  [2..5] |
|  | +108 | 4 | u32/f32 | refill_amount | throw_supply | 2, 3  [2..3] |
| ✗ | +112 | 4 | u32/f32 | on_thrown_audio_event |  | 0, 1413803333, 2873350161  [0..2873350161] |
| ✗ | +116 | 4 | u32/f32 | on_deflect_audio_event |  | 0 |
| ✗ | +120 | 48 | struct 0x10CEE58B | thrown_trail_effect |  |  |
| ✗ | +168 | 1 | u8 | destroy_thrown_trail_effect_on_attach |  | 1 |
| ✗ | +172 | 4 | u32/f32 | max_spawned_amount |  | 4294967295 |
| ✗ | +176 | 8 | struct 0x62C74EDA |  |  | 0 |
| ✗ | +184 | 144 | struct 0xD8C3E99B |  |  |  |
| ✗ | +328 | 4 | u32/f32 |  |  | 0 |
| ✗ | +332 | 4 | u32/f32 |  |  | 0 |
| ✗ | +336 | 4 | u32/f32 |  |  | 0 |
| ✗ | +340 | 1 | u8 |  |  | 1 |
| ✗ | +344 | 4 | u32/f32 |  |  | 2 |
| ✗ | +348 | 4 | u32/f32 |  |  | 0 |
| ✗ | +352 | 1 | u8 |  |  | 0 |
| ✗ | +356 | 4 | u32/f32 |  |  | -932.6 |

### DisplacementComponentData → DisplacementComponent (39 members, 8 editable, 1 rows)

tables: warp pack

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 4 | u32/f32 |  |  | 0 |
| ✗ | +4 | 4 | u32/f32 |  |  | 2693893514  (f32: -2.466e-19) |
| ✗ | +8 | 4 | u32/f32 |  |  | 8.863e-06 |
| ✗ | +12 | 12 | struct 0x85B82A43 |  |  |  |
| ✗ | +24 | 8 | u64 |  |  | 0xC2997181F9602573 |
| ✗ | +32 | 4 | u32/f32 |  |  | 0 |
| ✗ | +36 | 4 | u32/f32 |  |  | 379630579 |
| ✗ | +40 | 8 | u64 |  |  | 0x98AC7FEEFEFF57F9 |
| ✗ | +48 | 4 | u32/f32 |  |  | 3212836864  (f32: -1) |
| ✗ | +52 | 4 | u32/f32 |  |  | 1.017e-06 |
| ✗ | +56 | 4 | u32/f32 | explosion_type |  | 254 |
| ✗ | +64 | 8 | u64 |  |  | 0x15CD3B1EFE881F9D |
| ✗ | +72 | 4 | u32/f32 |  |  | 1 |
| ✗ | +76 | 4 | u32/f32 | teleportation_delay |  | 0.2 |
| ✗ | +80 | 4 | u32/f32 | delay_between_uses |  | 0.2 |
| ✗ | +84 | 4 | u32/f32 |  |  | 1065353216  (f32: 1) |
| ✗ | +88 | 4 | u32/f32 |  |  | 4290361375 |
| ✗ | +92 | 12 | struct 0x85B82A43 |  |  |  |
| ✗ | +104 | 12 | struct 0x85B82A43 |  |  |  |
| ✗ | +116 | 4 | u32/f32 |  |  | 1065353216  (f32: 1) |
|  | +120 | 4 | u32/f32 | teleportation_distance  | bp_warp_range | 1092616192  (f32: 10) |
| ✗ | +124 | 4 | u32/f32 |  |  | 5 |
|  | +128 | 4 | u32/f32 | teleportation_upward_bias | bp_warp_up | 1.4 |
|  | +132 | 4 | u32/f32 | teleportation_downward_bias | bp_warp_down | 1082130432  (f32: 4) |
| ✗ | +136 | 1 | u8 |  |  | 1 |
| ✗ | +137 | 1 | u8 |  |  | 0 |
|  | +140 | 4 | u32/f32 | safe_usage_threshold | bp_warp_safe | 1097859072  (f32: 15) |
|  | +144 | 4 | u32/f32 | explosion_threshold | bp_warp_unsafe | 1110704128  (f32: 45) |
|  | +148 | 4 | u32/f32 | heat_per_use | bp_warp_heat | 1107558400  (f32: 33) |
|  | +152 | 4 | u32/f32 | heat_lose_per_second | bp_warp_cool | 1086324736  (f32: 6) |
|  | +160 | 288 | struct 0x49ECCD2F |  | bp_warp_head, bp_warp_arms, bp_warp_arms_2 |  |
| ✗ | +448 | 156 | struct 0x92F73BFB |  |  |  |
| ✗ | +604 | 4 | u32/f32 |  |  | 4244241910 |
| ✗ | +608 | 4 | u32/f32 |  |  | 3732338588 |
| ✗ | +612 | 4 | u32/f32 |  |  | 450287375 |
| ✗ | +616 | 4 | u32/f32 |  |  | 49732699 |
| ✗ | +620 | 4 | u32/f32 |  |  | 1106247680  (f32: 30) |
| ✗ | +624 | 4 | u32/f32 |  |  | 1101004800  (f32: 20) |
| ✗ | +628 | 4 | u32/f32 |  |  | 0.3 |

### ExplosiveComponentData → ExplosiveComponent (33 members, 3 editable, 71 rows)

tables: explosive

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 4 | u32/f32 | mode |  | 0, 1, 2  [0..2] |
| ✗ | +4 | 4 | u32/f32 | collision_raycast_filter |  | 0 |
| ✗ | +8 | 4 | u32/f32 | arming_delay |  | 0 |
|  | +12 | 4 | u32/f32 | explosion_delay | fuse | 0, 1065353216, 1077936128  (f32: 0, 1)  [0..1077936128] |
|  | +16 | 4 | u32/f32 | removal_delay | burn_removal | 0.1, 1  [0.1..1] |
| ✗ | +20 | 1 | u8 | start_active |  | 0, 1  [0..1] |
| ✗ | +21 | 1 | u8 | hide_on_explosion |  | 0, 1  [0..1] |
| ✗ | +22 | 1 | u8 | destroy_actor_on_explosion |  | 0, 1  [0..1] |
| ✗ | +23 | 1 | u8 | ignore_friendly_fire |  | 0, 1  [0..1] |
| ✗ | +24 | 1 | u8 | UnkBool |  | 0 |
| ✗ | +28 | 4 | u32/f32 | impact_distance |  | 0.5, 1, 3  [0.5..3] |
| ✗ | +32 | 4 | u32/f32 | impact_airburst_distance |  | 0, 0.25, 0.5  [0..0.5] |
| ✗ | +36 | 4 | u32/f32 | explosion_type |  | 73, 91, 100 …  [73..257] |
| ✗ | +40 | 4 | u32/f32 | impact_explosion_type |  | 0 |
| ✗ | +44 | 4 | u32/f32 | on_exploded_sound |  | 0 |
| ✗ | +48 | 4 | u32/f32 | on_status_effect_done_sound |  | 0 |
| ✗ | +56 | 48 | struct 0x10CEE58B | armed_effect |  |  |
| ✗ | +104 | 48 | struct 0x10CEE58B | trail_effect |  |  |
| ✗ | +152 | 48 | struct 0x10CEE58B | status_effect_particle_effect |  |  |
| ✗ | +200 | 48 | struct 0x10CEE58B | status_effect_done_particle_effect |  |  |
| ✗ | +248 | 4 | u32/f32 | armed_sound |  | 0 |
|  | +252 | 56 | struct 0xAA4F951B | status_effect_template | burn |  |
| ✗ | +308 | 4 | u32/f32 | trigger_actor |  | 0 |
| ✗ | +312 | 4 | u32/f32 | collision_actor |  | -2.305e-17, 0, 0.0006292 …  [-2.305e-17..16.95] |
| ✗ | +316 | 1 | u8 | explode_on_death |  | 0, 1  [0..1] |
| ✗ | +320 | 8 | struct 0x85B82A42 | SomeVector |  | 0 |
| ✗ | +328 | 4 | u32/f32 | on_armed_ability |  | 0 |
| ✗ | +332 | 4 | u32/f32 | UnkFloat1 |  | 0 |
| ✗ | +336 | 4 | u32/f32 | UnkFloat2 |  | 0 |
| ✗ | +340 | 4 | u32/f32 | firenode_pose_limit |  | 1127481344  (f32: 180) |
| ✗ | +344 | 1 | u8 |  |  | 0 |
| ✗ | +348 | 4 | u32/f32 | step_detection_min_unit_size |  | 0 |
| ✗ | +352 | 4 | u32/f32 |  |  | 0 |

### BombardmentComponentData → BombardmentComponent (32 members, 6 editable, 23 rows)

tables: bombardment

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 4 | u32/f32 | initial_delay |  | 0, 1077936128  (f32: 0, 3)  [0..1077936128] |
|  | +4 | 4 | u32/f32 | num_bombs | barrage_shells | 1, 3, 5 …  [1..64] |
|  | +8 | 4 | u32/f32 | bomb_interval | barrage_shell_gap | 0, 0.1, 0.15 …  [0..1.5] |
| ✗ | +12 | 4 | u32/f32 | bomb_interval_random_offset |  | 0, 0.2  [0..0.2] |
| ✗ | +16 | 4 | u32/f32 | wander_offset_radius_min |  | 0, 1065353216, 1092616192 …  (f32: 0, 1)  [0..1097859072] |
| ✗ | +20 | 4 | u32/f32 | wander_offset_radius_max |  | 0, 1065353216, 1097859072 …  (f32: 0, 1)  [0..1106247680] |
|  | +24 | 4 | u32/f32 | num_salvos | barrage_salvos | 1, 2, 4 …  [1..12] |
|  | +28 | 4 | u32/f32 | salvo_interval | barrage_salvo_gap | 0.1, 0.45, 1 …  [0.1..7.5] |
| ✗ | +32 | 4 | u32/f32 | salvo_interval_random_offset |  | 0 |
|  | +36 | 4 | u32/f32 | area_size | barrage_area | 1065353216, 1092616192, 1101004800 …  (f32: 1, 10)  [1065353216..1126170624] |
| ✗ | +40 | 4 | u32/f32 | wander_start_area_radius |  | 0, 1065353216, 1097859072 …  (f32: 0, 1)  [0..1106247680] |
| ✗ | +44 | 4 | u32/f32 | fire_height |  | 1132068864, 1142292480, 1148846080 …  (f32: 250, 600)  [1132068864..1161527296] |
| ✗ | +48 | 12 | struct 0x85B82A43 | fire_angle_offset |  |  |
| ✗ | +60 | 1 | u8 | fire_from_ship |  | 0, 1  [0..1] |
| ✗ | +64 | 32 | 32B | projectile_types |  |  |
|  | +96 | 4 | u32/f32 | speed | barrage_speed | 0, 0.1  [0..0.1] |
| ✗ | +104 | 8 | u64 | muzzle_flash |  | 0x61A844A05923DB53, 0x61A844A05923DB53 |
| ✗ | +112 | 8 | u64 |  |  | 0x74E41D7D366F5EE4, 0x74E41D7D366F5EE4 … |
| ✗ | +120 | 4 | u32/f32 |  |  | 0, 1101004800  (f32: 0, 20)  [0..1101004800] |
| ✗ | +124 | 1 | u8 |  |  | 1 |
| ✗ | +128 | 4 | u32/f32 | start_delay |  | 0, 1077936128, 1084227584 …  (f32: 0, 3)  [0..1092616192] |
| ✗ | +132 | 4 | u32/f32 | walk_angle |  | 0 |
| ✗ | +136 | 4 | u32/f32 | walk_offset_fraction |  | 0 |
| ✗ | +140 | 4 | u32/f32 | destroyer_stratagem_fire |  | 3511619768 |
| ✗ | +144 | 4 | u32/f32 | destroyer_stratagem_fire_stop |  | 6.659e-05 |
| ✗ | +148 | 4 | u32/f32 |  |  | 0 |
| ✗ | +152 | 4 | u32/f32 |  |  | 0 |
| ✗ | +160 | 16 | 16B |  |  |  |
| ✗ | +176 | 4 | u32/f32 | tag_avoidance_distance |  | 0, 1065353216, 1098907648 …  (f32: 0, 1)  [0..1112014848] |
| ✗ | +180 | 4 | u32/f32 | first_projectile_destroyed_audio_event |  | 0 |
| ✗ | +184 | 4 | u32/f32 | projectile_destroyed_audio_event |  | 0 |
| ✗ | +188 | 4 | u32/f32 | final_projectile_destroyed_audio_event |  | 0 |

### ExplosionSettings → ExplosionInfo (32 members, 5 editable, 424 rows)

tables: explosion

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 4 | u32/f32 | type |  | 71, 118, 123 …  [71..408] |
| ✗ | +4 | 4 | u32/f32 | damage_type |  | 5, 298, 300 …  [5..416] |
| ✗ | +8 | 4 | u32/f32 | UnkHash? |  | 0 |
| ✗ | +12 | 1 | u8 | fallback_damage_loc_name |  | 0 |
|  | +16 | 4 | u32/f32 | inner_radius | blast_inner, m2_blast_inner, x331_inner | 1, 1.5, 2 …  [1..10] |
|  | +20 | 4 | u32/f32 | outer_radius | blast_outer, m2_blast_outer, x343_outer | 2, 2.2, 3 …  [2..17] |
|  | +24 | 4 | u32/f32 | stagger_radius | blast_shockwave, m2_blast_shockwave, x343_shockwave | 2, 2.5, 6 …  [2..22] |
| ✗ | +28 | 4 | u32/f32 | cone_angle |  | 0 |
| ✗ | +32 | 4 | u32/f32 | camera_shake_radius |  | 1065353216, 1088421888, 1090519040 …  (f32: 1, 7)  [1065353216..1112014848] |
| ✗ | +40 | 16 | 16B | shake_assets_offset |  |  |
| ✗ | +56 | 8 | u64 | particle_effect_path |  | 0x0000000000000000, 0x0000000000000000 … |
| ✗ | +64 | 4 | u32/f32 | audio_event |  | 0, 1682101871, 1887468366 …  [0..2796635700] |
| ✗ | +68 | 1 | u8 | crater_type |  | 0 |
| ✗ | +72 | 4 | u32/f32 | surface_impact_type |  | 0, 14  [0..14] |
| ✗ | +76 | 4 | u32/f32 | hit_effect_damage_type |  | 0 |
|  | +80 | 4 | u32/f32 | num_shrapnel_projectiles | blast_shrapnel_count, m2_blast_shrapnel_count, c1_blast_shrapnel_count | 0 |
|  | +84 | 4 | u32/f32 | shrapnel_projectile_type | blast_shrapnel_projectile, m2_blast_shrapnel_projectile, c1_blast_shrapnel_projectile | 0, 353  [0..353] |
| ✗ | +88 | 1 | u8 | noise_template |  | 0, 14, 15  [0..15] |
| ✗ | +92 | 4 | u32/f32 | wind_effect_template |  | 0 |
| ✗ | +96 | 4 | u32/f32 | fire_template |  | 0 |
| ✗ | +100 | 4 | u32/f32 | persistent_status_volume |  | 0, 28  [0..28] |
| ✗ | +104 | 4 | u32/f32 | status_volume_effect_time |  | 0, 1092616192  (f32: 0, 10)  [0..1092616192] |
| ✗ | +108 | 4 | u32/f32 | status_volume_effect_audio_play |  | 0 |
| ✗ | +112 | 4 | u32/f32 | status_volume_effect_audio_stop |  | 0 |
| ✗ | +116 | 1 | u8 | explosion_flags_1 |  | 1, 4  [1..4] |
| ✗ | +120 | 4 | u32/f32 | arc_type_on_explosion |  | 0 |
| ✗ | +124 | 1 | u8 | explosion_flags_2 |  | 2 |
| ✗ | +128 | 4 | u32/f32 |  |  | 0 |
| ✗ | +132 | 1 | u8 | explosion_flags_3 |  | 0 |
| ✗ | +136 | 4 | u32/f32 |  |  | 1107296256  (f32: 32) |
| ✗ | +140 | 1 | u8 | explosion_flags_4 |  | 3 |
| ✗ | +144 | 4 | u32/f32 |  |  | 0 |

### AvatarComponentData → AvatarComponent (28 members, 1 editable, 1 rows)

tables: avatar

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 4 | struct 0xFA112620 | InputInfo |  | 1045220557 |
|  | +4 | 148 | struct 0x068EE2A3 | input_info | cost_dive, cost_jump, recover_delay |  |
| ✗ | +152 | 56 | struct 0xDBD22BBB | move_info |  |  |
| ✗ | +208 | 24 | struct 0x60BB2B26 | steep_slope_movement |  |  |
| ✗ | +232 | 60 | struct 0xB2705A13 | action_slide_movement_info |  |  |
| ✗ | +292 | 8 | struct 0x789EFE40 | climb_info |  | 4554039943422279680 |
| ✗ | +300 | 8 | struct 0x789EFE40 | short_throw_info |  | 4590068740441243648 |
| ✗ | +308 | 12 | struct 0x8FDF240B | long_throw_info |  |  |
| ✗ | +320 | 20 | struct 0x7836993E | detection_info |  |  |
| ✗ | +340 | 416 | struct 0x66ED4CF2 | weathering_settings |  |  |
| ✗ | +756 | 28 | struct 0x79F33237 | exertion_vo_params |  |  |
| ✗ | +784 | 4 | u32/f32 | heal_self_duration |  | 1090519040  (f32: 8) |
| ✗ | +788 | 4 | u32/f32 | heal_self_decay_wait_time |  | 0.5 |
| ✗ | +792 | 4 | u32/f32 | heal_self_decay_rate |  | 0.5 |
| ✗ | +796 | 4 | u32/f32 | heal_self_cancle_damage_amount |  | 1084227584  (f32: 5) |
| ✗ | +800 | 4 | u32/f32 | ragdoll_damage_velocity_lower |  | 1094713344  (f32: 12) |
| ✗ | +804 | 4 | u32/f32 | ragdoll_damage_velocity_upper |  | 1121058816  (f32: 105) |
| ✗ | +808 | 4 | u32/f32 | ragdoll_damage_min |  | 1092616192  (f32: 10) |
| ✗ | +812 | 4 | u32/f32 | ragdoll_damage_max |  | 1133903872  (f32: 300) |
| ✗ | +816 | 4 | u32/f32 | ragdoll_damage_snow_modifier |  | 0.75 |
| ✗ | +820 | 4 | u32/f32 | min_aim_duration |  | 0.09 |
| ✗ | +824 | 4 | u32/f32 | max_aim_duration |  | 0.5 |
| ✗ | +828 | 4 | u32/f32 | min_fire_ready_duration |  | 0.04 |
| ✗ | +832 | 4 | u32/f32 | max_fire_ready_duration |  | 0.12 |
| ✗ | +836 | 4 | u32/f32 | taunt_time_before_drain |  | 1092616192  (f32: 10) |
| ✗ | +840 | 4 | u32/f32 | taunt_drain_per_second |  | 0.01 |
| ✗ | +844 | 4 | u32/f32 | taunt_on_trigger_probability_mul |  | 0.5 |
| ✗ | +848 | 4 | u32/f32 | taunt_cooldown_timer |  | 1092616192  (f32: 10) |

### StatusEffectSettings → StatusEffectInfo (27 members, 1 editable, 73 rows)

tables: status effect

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 4 | u32/f32 | type |  | 1, 2, 3 …  [1..12] |
| ✗ | +8 | 8 | u64 | debug_name |  | 0x0000000000002DB0, 0x0000000000002DB6 … |
| ✗ | +16 | 4 | u32/f32 | shader_variable_preset |  | 0, 1  [0..1] |
| ✗ | +24 | 8 | u64 |  |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +32 | 4 | u32/f32 | shading_environment_fade_time |  | 0 |
| ✗ | +36 | 4 | u32/f32 | strength |  | 0, 0.15, 0.25 …  [0..5] |
|  | +40 | 4 | u32/f32 | duration | status5_duration, status44_duration, a2_status40_duration | 0.5, 1, 3 …  [0.5..9999] |
| ✗ | +44 | 4 | u32/f32 | damage_info_type |  | 0, 531, 532 …  [0..552] |
| ✗ | +48 | 1 | u8 | damage_ignore_avatar_armor |  | 0 |
| ✗ | +56 | 8 | u64 |  |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +64 | 4 | u32/f32 | script_event_start |  | 0, 1897902647  [0..1897902647] |
| ✗ | +68 | 4 | u32/f32 | script_event_stop |  | 0, 1034147453, 1912561169  [0..1912561169] |
| ✗ | +72 | 4 | u32/f32 | audio_event_start |  | 0, 1033575834, 3734442065  [0..3734442065] |
| ✗ | +76 | 4 | u32/f32 | audio_event_stop |  | -0.6377, 0, 1.895e-06  [-0.6377..1.895e-06] |
| ✗ | +80 | 4 | u32/f32 | audio_event_enter |  | 0, 1404037441, 3198568334  [0..3198568334] |
| ✗ | +84 | 4 | u32/f32 | audio_event_exit |  | 0 |
| ✗ | +88 | 4 | u32/f32 | animation_event_start |  | 0 |
| ✗ | +92 | 4 | u32/f32 | animation_event_stop |  | 0 |
| ✗ | +96 | 4 | u32/f32 | difficult_terrain_amount |  | 0 |
| ✗ | +100 | 4 | u32/f32 | status_effect_flags |  | 0, 1065353216  (f32: 0, 1)  [0..1065353216] |
| ✗ | +104 | 1 | u8 | notify_event_on_added |  | 0, 2, 3 …  [0..8] |
| ✗ | +112 | 16 | struct 0x17B9083A |  |  |  |
| ✗ | +128 | 4 | u32/f32 |  |  | 0, 2343002388, 4224911188  [0..4224911188] |
| ✗ | +132 | 4 | u32/f32 |  |  | 0, 47623951, 1086274594  [0..1086274594] |
| ✗ | +136 | 1 | u8 |  |  | 0 |
| ✗ | +140 | 4 | u32/f32 |  |  | 1 |
| ✗ | +144 | 16 | struct 0x9DDD1BE2 |  |  |  |

### BeamSettings → BeamInfo (25 members, 1 editable, 30 rows)

tables: beam

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 4 | u32/f32 | type |  | 1, 2, 7 …  [1..30] |
| ✗ | +4 | 4 | u32/f32 | radius |  | 0, 0.1  [0..0.1] |
|  | +8 | 4 | u32/f32 | length | beam_range | 9.5, 200, 1000  [9.5..1000] |
| ✗ | +12 | 4 | u32/f32 | damage_info_type |  | 512, 513, 514 …  [512..530] |
| ✗ | +16 | 4 | u32/f32 | focal_distance |  | 0 |
| ✗ | +20 | 4 | u32/f32 | focal_shoulder_width |  | 0 |
| ✗ | +24 | 4 | u32/f32 | focal_shoulder_damage_multiplier |  | 1065353216  (f32: 1) |
| ✗ | +28 | 4 | u32/f32 | focal_point_damage_multiplier |  | 1065353216  (f32: 1) |
| ✗ | +32 | 4 | u32/f32 | DamageInfoType? |  | 1065353216  (f32: 1) |
| ✗ | +36 | 4 | u32/f32 | FocalShoulderWidth? |  | 1065353216  (f32: 1) |
| ✗ | +40 | 4 | u32/f32 | decal_size |  | 0.1, 0.15  [0.1..0.15] |
| ✗ | +44 | 4 | u32/f32 | surface_impact_type |  | 22, 23, 24 …  [22..25] |
| ✗ | +48 | 8 | u64 | beam_effect_path |  | 0xDBAF8323AA29198D, 0x698B1C70167A03AE … |
| ✗ | +56 | 8 | u64 | FalloffEffectPath? |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +64 | 8 | u64 | BeamUnitPath? |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +72 | 4 | u32/f32 | audio_trail_event_start |  | 0, 13789844, 514225198 …  [0..1860773244] |
| ✗ | +76 | 4 | u32/f32 | audio_trail_event_stop |  | 810767780, 980126251, 3697901054  [810767780..3697901054] |
| ✗ | +80 | 4 | u32/f32 | raycast_template |  | 0 |
| ✗ | +84 | 4 | u32/f32 | overlap_beam_query |  | 2435390391 |
| ✗ | +88 | 4 | u32/f32 | effect_damage_type |  | 7, 8  [7..8] |
| ✗ | +92 | 4 | u32/f32 | UnkFloat? |  | 3212836864  (f32: -1) |
| ✗ | +96 | 4 | u32/f32 | impact_explosion_type |  | 0 |
| ✗ | +100 | 1 | u8 | UnkBool? |  | 1 |
| ✗ | +104 | 4 | u32/f32 | DangerLevel? |  | 5 |
| ✗ | +108 | 1 | u8 | not_dps_damage |  | 0 |

### WeaponChargeComponentData → WeaponChargeComponent (22 members, 3 editable, 10 rows)

tables: weapon charge

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
|  | +0 | 72 | struct 0x90B3FC89 | ChargeStateSettings | proj_c1, proj_c2, proj_c3 |  |
|  | +72 | 48 | struct 0x66FC58AB | projectile_multipliers | mul_range_min, mul_range_max, mul_speed_min |  |
| ✗ | +120 | 4 | u32/f32 | charge_start_sound_id |  | 0, 122845797, 1364443767 …  [0..2924963139] |
| ✗ | +124 | 4 | u32/f32 | charge_stop_sound_id |  | 0, 100308039, 444396153 …  [0..4226901298] |
| ✗ | +128 | 4 | u32/f32 | ready_to_fire_sound_id |  | 0, 217870560, 2109193558 …  [0..3911236321] |
| ✗ | +132 | 4 | u32/f32 | danger_overcharge_sound_id |  | 0, 648648688, 3312421269 …  [0..3972604218] |
| ✗ | +136 | 4 | u32/f32 | charge_mesh |  | 0, 4221645464  [0..4221645464] |
| ✗ | +140 | 4 | u32/f32 | charge_material |  | 0, 2113163872, 3939295745 …  [0..4075618851] |
| ✗ | +144 | 4 | u32/f32 | charge_variable |  | 0, 3379599616  (f32: -9.855e+05, 0)  [0..3379599616] |
| ✗ | +152 | 8 | u64 | charge_up_muzzle_flash |  | 0xC43DCFB252CF5F3E, 0xC43DCFB252CF5F3E … |
| ✗ | +160 | 8 | u64 | charge_up_muzzle_flash_loop |  | 0xD5A4446AB1455831, 0xD5A4446AB1455831 … |
| ✗ | +168 | 4 | u32/f32 | charge_anim_id |  | 0, 450287375  [0..450287375] |
| ✗ | +172 | 4 | u32/f32 | charge_end_anim_id |  | 0, 698547094  (f32: 0, 7.238e-14)  [0..698547094] |
| ✗ | +176 | 4 | u32/f32 | charge_rate_anim_id |  | 0, 450287375, 1743663529  [0..1743663529] |
| ✗ | +180 | 4 | u32/f32 | spin_speed_anim_id |  | 0, 18.63  [0..18.63] |
| ✗ | +184 | 1 | u8 | auto_fire_in_safety |  | 0, 1  [0..1] |
| ✗ | +185 | 1 | u8 | explode_at_third_charge_time |  | 0, 1  [0..1] |
| ✗ | +188 | 4 | u32/f32 | extra_projectiles |  | 0, 2  [0..2] |
| ✗ | +192 | 4 | u32/f32 | extra_projectiles_interval |  | 0, 0.12  [0..0.12] |
| ✗ | +196 | 4 | u32/f32 | dry_fire_audio_event |  | 0, 1837771762  [0..1837771762] |
| ✗ | +200 | 4 | u32/f32 | overcharge_explosion_type |  | 269, 321, 326  [269..326] |
|  | +204 | 8 | struct 0xE5073B6A | StateValue | charge_limit | 2, 4620693217682128898, 4634204016564240386  [2..4634204016564240386] |

### ArcSettings → ArcInfo (21 members, 3 editable, 16 rows)

tables: arc

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 4 | u32/f32 | type |  | 1, 2, 3 …  [1..16] |
| ✗ | +4 | 4 | u32/f32 | speed |  | 1112014848, 1133903872, 1157234688  (f32: 50, 300)  [1112014848..1157234688] |
|  | +8 | 4 | u32/f32 | distance | arc_range, blast_arc_range | 1097859072, 1101004800, 1103626240 …  (f32: 15, 20)  [1097859072..1120403456] |
| ✗ | +12 | 4 | u32/f32 | distance_at_max_angle_spread |  | 1065353216, 1092616192, 1109393408 …  (f32: 1, 10)  [1065353216..1120403456] |
| ✗ | +16 | 4 | u32/f32 | distance_at_max_angle_spread_first_shot |  | 1092616192, 1097859072, 1101004800 …  (f32: 10, 15)  [1092616192..1112014848] |
| ✗ | +20 | 4 | u32/f32 | max_angle_spread |  | 1092616192, 1114636288, 1127481344 …  (f32: 10, 60)  [1092616192..1133903872] |
| ✗ | +24 | 4 | u32/f32 | max_angle_spread_first_shot |  | 3, 10, 22.5 …  [3..180] |
|  | +28 | 4 | u32/f32 | max_chain_length | arc_chain, blast_arc_chain | 0, 1, 2 …  [0..3] |
|  | +32 | 4 | u32/f32 | max_chain_split | arc_split, blast_arc_split | 0, 1, 2 …  [0..5] |
| ✗ | +36 | 4 | u32/f32 | damage_info_type |  | 49, 50, 51 …  [49..221] |
| ✗ | +40 | 8 | u64 |  |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +48 | 8 | u64 |  |  | 0x0000000000000000, 0x0000000000000000 |
| ✗ | +56 | 4 | u32/f32 | particle_linger_time |  | 0.1, 0.25  [0.1..0.25] |
| ✗ | +64 | 8 | u64 | explosion_effect_path |  | 0x6C3208B3FAB4A0B4, 0x6C3208B3FAB4A0B4 |
| ✗ | +72 | 4 | u32/f32 | hit_effect_damage_type |  | 3, 7  [3..7] |
| ✗ | +76 | 4 | u32/f32 | hit_audio_event |  | 0, 3528384486, 4066763531  [0..4066763531] |
| ✗ | +80 | 8 | u64 | bolt_path |  | 0x69B4296484F7539A, 0x69B4296484F7539A |
| ✗ | +88 | 4 | u32/f32 | demolition_strength |  | 10 |
| ✗ | +92 | 1 | u8 |  |  | 0, 1  [0..1] |
| ✗ | +96 | 4 | u32/f32 | arc_count |  | 1 |
| ✗ | +100 | 1 | u8 | ignore_launcher |  | 1 |

### OrbitalAbilityComponentData → OrbitalAbilityComponent (20 members, 4 editable, 2 rows)

tables: orbital beam

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 4 | u32/f32 | pattern_segments |  | 0 |
| ✗ | +4 | 1 | u8 | smooth_segments |  | 1 |
| ✗ | +8 | 448 | struct 0x85B82A42 |  |  |  |
| ✗ | +456 | 4 | u32/f32 | segment_pause |  | 0 |
|  | +460 | 4 | u32/f32 | duration | beam_duration | 1073741824, 1103626240  (f32: 2, 25)  [1073741824..1103626240] |
| ✗ | +464 | 4 | u32/f32 | remove_time |  | 1065353216  (f32: 1) |
|  | +468 | 4 | u32/f32 | movement_speed | beam_speed | 1092616192, 1119092736  (f32: 10, 90)  [1092616192..1119092736] |
|  | +472 | 4 | u32/f32 | search_radius | beam_radius | 1106247680, 1112014848  (f32: 30, 50)  [1106247680..1112014848] |
|  | +476 | 28 | struct 0x491A6F07 | damage_dealer_zone | beam_tick |  |
| ✗ | +504 | 4 | u32/f32 | surface_impact |  | 0, 26  [0..26] |
| ✗ | +508 | 1 | u8 | noise_hit_template |  | 0, 18  [0..18] |
| ✗ | +512 | 8 | u64 | ship_effect |  | 0xFD2C40B16D5D4EDA, 0xBE06ACBE399020C6 |
| ✗ | +520 | 1 | u8 | ship_effect_is_laser_pointer |  | 0, 1  [0..1] |
| ✗ | +524 | 4 | u32/f32 | audio_event_start |  | 1135102613, 3732618020  [1135102613..3732618020] |
| ✗ | +528 | 4 | u32/f32 | audio_event_stop |  | 1843908931, 3597066355  [1843908931..3597066355] |
| ✗ | +532 | 4 | u32/f32 | projectile_type |  | 0, 282  [0..282] |
| ✗ | +536 | 4 | u32/f32 | projectile_spawn_height |  | 1161527296  (f32: 3000) |
| ✗ | +540 | 4 | u32/f32 | projectile_spawn_delay |  | 0, 1.7  [0..1.7] |
| ✗ | +544 | 4 | u32/f32 | target_list_update_time |  | 0, 1065353216  (f32: 0, 1)  [0..1065353216] |
| ✗ | +548 | 16 | 16B |  |  |  |

### TurretComponentData → TurretComponent (19 members, 2 editable, 74 rows)

tables: turret

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 4 | u32/f32 | vertical |  | 4238039248 |
| ✗ | +4 | 4 | u32/f32 | horizontal |  | 161490677 |
|  | +8 | 4 | u32/f32 | turn_speed_vertical | unit_turn_v | 1092616192, 1095761920, 1099956224 …  (f32: 10, 13)  [1092616192..1140457472] |
|  | +12 | 4 | u32/f32 | turn_speed_horizontal | unit_turn_h | 1092616192, 1095761920, 1097859072 …  (f32: 10, 13)  [1092616192..1140457472] |
| ✗ | +16 | 4 | u32/f32 | ratio_exponent |  | 0, 0.95, 1  [0..1] |
| ✗ | +20 | 4 | u32/f32 | vertical_limit_min |  | 1103626240, 1117126656, 3221225472 …  (f32: -90, -65)  [1103626240..3266576384] |
| ✗ | +24 | 4 | u32/f32 | vertical_limit_max |  | 1073741824, 1082130432, 1097859072 …  (f32: 2, 4)  [1073741824..1119092736] |
| ✗ | +28 | 4 | u32/f32 | horizontal_limit_min |  | 3231711232, 3248488448, 3253731328 …  (f32: -180, -30)  [3231711232..3274964992] |
| ✗ | +32 | 4 | u32/f32 | horizontal_limit_max |  | 1084227584, 1101004800, 1106247680 …  (f32: 5, 20)  [1084227584..1127481344] |
| ✗ | +36 | 4 | u32/f32 | trigger_rotation_sound_timer |  | 0.1 |
| ✗ | +40 | 4 | u32/f32 | trigger_pitch_sound_timer |  | 0.1 |
| ✗ | +44 | 4 | u32/f32 | rotation_start_event |  | 0, 130563709, 466811889 …  [0..3592179882] |
| ✗ | +48 | 4 | u32/f32 | rotation_stop_event |  | 0, 1227160923, 1306893155 …  [0..3592602702] |
| ✗ | +52 | 4 | u32/f32 |  |  | 0 |
| ✗ | +56 | 4 | u32/f32 |  |  | 0 |
| ✗ | +60 | 4 | u32/f32 | pitch_start_event |  | 0, 603788381, 649890770 …  [0..3501611644] |
| ✗ | +64 | 4 | u32/f32 | pitch_stop_event |  | 0, 868036591, 2266827806 …  [0..3949663124] |
| ✗ | +68 | 4 | u32/f32 | warning_event |  | 1305891758 |
| ✗ | +72 | 4 | u32/f32 | pivot_node |  | 161490677, 551832871, 4238039248  [161490677..4238039248] |

### WeaponRoundsComponentData → WeaponRoundsComponent (16 members, 7 editable, 25 rows)

tables: rounds

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 64 | struct 0x7A213C9B | ammo_infos |  |  |
|  | +64 | 8 | struct 0x7A2774D1 | ammo_types | proj_rounds, projectile_a2 | 63, 70, 266 …  [63..1511828488544] |
|  | +72 | 8 | struct 0x85B82A42 | magazine_capacity | rounds_capacity | 1073741824, 1082130432, 1086324736 …  [1073741824..4683743613555834880] |
|  | +80 | 4 | u32/f32 | ammo_capacity | rounds_max | 24, 32, 40 …  [24..70] |
|  | +84 | 4 | u32/f32 | ammo_refill | rounds_supply | 0, 18, 32 …  [0..70] |
|  | +88 | 4 | u32/f32 | ammo | rounds_start | 18, 22, 24 …  [18..64] |
|  | +92 | 4 | u32/f32 | reload_amount | rounds_per_reload | 1 |
|  | +96 | 8 | struct 0x85B82A42 | reload_thresholds | reload_below | 0 |
| ✗ | +104 | 1 | u8 | chambered |  | 0, 1  [0..1] |
| ✗ | +108 | 4 | u32/f32 | magazine_switch_audio |  | 0, 2751498770  (f32: -2.787e-17, 0)  [0..2751498770] |
| ✗ | +112 | 4 | u32/f32 | magazine_0_weapon_anim |  | 0, 2386575183  [0..2386575183] |
| ✗ | +116 | 4 | u32/f32 | magazine_0_wielder_anim |  | -2.555e+04, 0  [-2.555e+04..0] |
| ✗ | +120 | 4 | u32/f32 | magazine_1_weapon_anim |  | 0, 2144827903  [0..2144827903] |
| ✗ | +124 | 4 | u32/f32 | magazine_1_wielder_anim |  | 0, 1.017e+05  [0..1.017e+05] |
| ✗ | +128 | 4 | u32/f32 | magazine_anim_variable |  | 0, 1258484571  (f32: 0, 8.582e+06)  [0..1258484571] |
| ✗ | +132 | 1 | u8 |  |  | 0 |

### DepositComponentData → DepositComponent (15 members, 3 editable, 30 rows)

tables: backpack charges

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
|  | +0 | 4 | u32/f32 | capacity | bp_ammo, bp_charges | 1, 4, 5 …  [1..120] |
|  | +4 | 4 | u32/f32 | start_amount | bp_ammo_start, bp_charges_start | 1, 4, 6 …  [1..4294967295] |
|  | +8 | 4 | u32/f32 | refill_amount | bp_ammo_supply, bp_charges_supply | 0, 1, 3 …  [0..60] |
| ✗ | +12 | 4 | u32/f32 | deduct_owner_vo_event |  | 0, 195519030  [0..195519030] |
| ✗ | +16 | 4 | u32/f32 | last_deduct_owner_vo_event |  | -0.1215, 0  [-0.1215..0] |
| ✗ | +24 | 8 | u64 | DronePath |  | 0x0000000000000000, 0x0000000000000000 … |
| ✗ | +32 | 4 | u32/f32 | friendly_interact_ability |  | 0, 2636  [0..2636] |
| ✗ | +36 | 4 | u32/f32 | self_interact_ability |  | 0, 2637, 2640  [0..2640] |
| ✗ | +40 | 1 | u8 | show_self_interact |  | 0 |
| ✗ | +44 | 80 | 80B | node_hiding_order |  |  |
| ✗ | +124 | 4 | u32/f32 | node_hiding_order_post_anim_event |  | 0, 3740288220  [0..3740288220] |
| ✗ | +128 | 4 | u32/f32 | refill_style |  | 0, 1, 3  [0..3] |
| ✗ | +136 | 8 | u64 | AssistedReloadWeaponPath |  | 0x0000000000000000, 0x0000000000000000 … |
| ✗ | +144 | 4 | u32/f32 |  |  | 792497908, 1269087576  [792497908..1269087576] |
| ✗ | +148 | 1 | u8 |  |  | 0, 1  [0..1] |

### ArcWeaponComponentData → ArcWeaponComponent (11 members, 1 editable, 10 rows)

tables: arc weapon

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 4 | u32/f32 | arc_type |  | 1, 3, 4 …  [1..16] |
|  | +4 | 4 | u32/f32 | rounds_per_minute | arc_rpm | 1094713344, 1110704128, 3212836864  (f32: -1, 12)  [1094713344..3212836864] |
| ✗ | +8 | 1 | u8 | infinite_ammo |  | 1 |
| ✗ | +9 | 1 | u8 | rpc_synced_fire_events |  | 0 |
| ✗ | +12 | 4 | u32/f32 | fire_single_audio_event |  | 0, 29902759, 694574617 …  [0..4293099941] |
| ✗ | +16 | 4 | u32/f32 | fire_all_barrel_audio_event |  | 0 |
| ✗ | +20 | 4 | u32/f32 | fire_fail_audio_event |  | 0, 1078217113, 3527293210  [0..3527293210] |
| ✗ | +24 | 4 | u32/f32 | fire_source_node |  | 747556395, 1243096897, 1441931427 …  [747556395..2601604451] |
| ✗ | +32 | 32 | struct 0xAEB3CFCB | on_round_fired_shakes |  |  |
| ✗ | +64 | 8 | u64 | muzzle_flash |  | 0x913C622ADDEE1187, 0x913C622ADDEE1187 |
| ✗ | +72 | 8 | u64 | muzzle_flash_fail |  | 0xE70B762201596806, 0xE70B762201596806 |

### MinefieldComponentData → MinefieldComponent (11 members, 2 editable, 13 rows)

tables: minefield

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 4 | u32/f32 |  |  | 0, 35293833  [0..35293833] |
| ✗ | +4 | 4 | u32/f32 | on_mine_triggered_sound_event |  | 0, 73412703, 4259855754  [0..4259855754] |
|  | +8 | 4 | u32/f32 | trigger_time | mine_trigger | 0.001, 0.1  [0.001..0.1] |
|  | +12 | 4 | u32/f32 | chain_reaction_time | mine_chain | 0.2 |
| ✗ | +16 | 4 | u32/f32 | arm_time |  | 0.25 |
| ✗ | +20 | 4 | u32/f32 | trigger_actor |  | 80.3 |
| ✗ | +24 | 4 | u32/f32 | explosion_type |  | 72, 230, 270 …  [72..367] |
| ✗ | +28 | 4 | u32/f32 | ai_avoidance_radius |  | 0, 1100480512  (f32: 0, 19)  [0..1100480512] |
| ✗ | +32 | 1 | u8 | trigger_on_touch |  | 0, 1  [0..1] |
| ✗ | +36 | 4 | u32/f32 | step_detection_min_unit_size |  | 0 |
| ✗ | +40 | 1 | u8 |  |  | 0, 1  [0..1] |

### SensorEyeComponentData → SensorEyeComponent (11 members, 1 editable, 315 rows)

tables: sensor

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
|  | +0 | 4 | u32/f32 | distance | unit_sight, drone_sight, charge_sight | 1101004800, 1109393408, 1114636288 …  (f32: 20, 40)  [1101004800..1148846080] |
| ✗ | +4 | 4 | u32/f32 | peripheral_distance |  | 1065353216, 1145569280  (f32: 1, 800)  [1065353216..1145569280] |
| ✗ | +8 | 4 | u32/f32 | back_distance |  | 0, 1065353216, 1133903872  (f32: 0, 1)  [0..1133903872] |
| ✗ | +12 | 4 | u32/f32 | angle_horizontal |  | 1101004800, 1108082688, 1117782016 …  (f32: 20, 35)  [1101004800..1126825984] |
| ✗ | +16 | 4 | u32/f32 | angle_vertical |  | 1101004800, 1108082688, 1119092736 …  (f32: 20, 35)  [1101004800..1126825984] |
| ✗ | +20 | 4 | u32/f32 | sight_node |  | 747556395, 951729526, 1383898227 …  [747556395..3789292000] |
| ✗ | +24 | 1 | u8 | use_sight_node_for_direction |  | 0, 1  [0..1] |
| ✗ | +28 | 4 | u32/f32 | vision_raycast_template |  | 14, 15  [14..15] |
| ✗ | +32 | 4 | u32/f32 | eye_type |  | 1, 2, 3  [1..3] |
| ✗ | +36 | 4 | u32/f32 | ignore_inside_foliage_distance |  | 1090519040  (f32: 8) |
| ✗ | +40 | 4 | u32/f32 | inside_foliage_distance |  | 0.5 |

### WeaponReloadComponentData → WeaponReloadComponent (10 members, 2 editable, 254 rows)

tables: reload

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 1 | u8 | manual_clearing |  | 0 |
|  | +1 | 1 | u8 | reload_allow_move | reload_move | 1 |
| ✗ | +4 | 4 | u32/f32 | ability_type |  | 0 |
| ✗ | +8 | 48 | struct 0xE88D05FD | ReloadAnimEvents |  |  |
|  | +56 | 4 | u32/f32 | duration | reload_time | 0 |
| ✗ | +60 | 1 | u8 | has_shared_deposit |  | 0 |
| ✗ | +64 | 4 | u32/f32 | reload_vo_normal |  | 2501033797 |
| ✗ | +68 | 4 | u32/f32 | reload_vo_lastmag |  | 1547933619 |
| ✗ | +72 | 4 | u32/f32 | reload_vo_nomags |  | 3044503528  (f32: -9.218e-07) |
| ✗ | +76 | 4 | u32/f32 | reload_vo_nomags_no_backpack |  | 0 |

### WeaponMagazineComponentData → WeaponMagazineComponent (9 members, 5 editable, 276 rows)

tables: magazine

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 4 | u32/f32 | magazine_type |  | 0 |
|  | +4 | 132 | struct 0x174B724A | magazine_pattern | proj_mag1, proj_mag2, proj_mag3 |  |
|  | +136 | 4 | u32/f32 | magazine_capacity | capacity | 1, 30, 100 …  [1..1000] |
|  | +140 | 4 | u32/f32 | magazines | mags_start | 1, 2, 6  [1..6] |
|  | +144 | 4 | u32/f32 | magazines_refill | mags_supply | 6 |
|  | +148 | 4 | u32/f32 | magazines_max | mags_max | 1, 2, 4 …  [1..12] |
| ✗ | +152 | 4 | u32/f32 | reload_threshold |  | 0 |
| ✗ | +156 | 1 | u8 | chambered |  | 0, 1  [0..1] |
| ✗ | +157 | 1 | u8 | UnknownBool |  | 0 |

### WeaponWindUpComponentData → WeaponWindUpComponent (9 members, 2 editable, 9 rows)

tables: wind-up

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
|  | +0 | 4 | u32/f32 | WindUpTime | spin_up | 0.5, 1  [0.5..1] |
|  | +4 | 4 | u32/f32 | WindDownTime | spin_down | 0.5, 1  [0.5..1] |
| ✗ | +8 | 4 | u32/f32 | RpmAnimId |  | 1.728e+05 |
| ✗ | +12 | 4 | u32/f32 | RpmMultiplier |  | 0.1667, 0.3333, 1  [0.1667..1] |
| ✗ | +16 | 4 | u32/f32 | WindUpSound |  | 0, 946816232, 2939539185 …  [0..4155509744] |
| ✗ | +20 | 4 | u32/f32 | WindDownSound |  | 0, 1170769191, 1399724180 …  [0..3296420459] |
| ✗ | +24 | 4 | u32/f32 | WindUpAnim |  | 858471599, 992368565, 4125806552  [858471599..4125806552] |
| ✗ | +28 | 4 | u32/f32 | WindDownAnim |  | 0, 2394913884, 4125806552  [0..4125806552] |
| ✗ | +32 | 1 | u8 | UnknownBool |  | 0, 1  [0..1] |

### DamageSettings → DamageInfo (8 members, 6 editable, 661 rows)

tables: damage

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
| ✗ | +0 | 4 | u32/f32 | type |  | 1, 2, 3 …  [1..591] |
|  | +4 | 8 | u64 | damage | damage, blast_damage, d458_damage | 0x0000003200000032, 0x0000000F0000000A … |
|  | +12 | 16 | 16B | armor_penetration_per_angle | ap_direct, blast_ap_direct, d458_ap_direct |  |
|  | +28 | 4 | u32/f32 | demolition_strength | demolition, blast_demolition, d402_demolition | 0, 10, 20 …  [0..30] |
|  | +32 | 4 | u32/f32 | force_strength | stagger, blast_stagger, d402_stagger | 0, 5, 20 …  [0..50] |
|  | +36 | 4 | u32/f32 | force_impulse | push, blast_push, d402_push | 0, 5, 10 …  [0..40] |
| ✗ | +40 | 4 | u32/f32 | element_type |  | 0, 1, 3 …  [0..9] |
|  | +44 | 32 | struct 0xB99AE45C |  | slot1, blast_slot1, mine_x_slot1 |  |

### DestructionSettings → DestructionEventLevel (5 members, 1 editable, 0 rows) ⚠ the panel reads 1 B a row, the record is 48 B

tables: destruction

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
|  | +0 | 16 | struct 0x363E10E3 |  | unit_demolition, pod_demolition |  |
| ✗ | +16 | 8 | struct 0xB247DB30 |  |  |  |
| ✗ | +24 | 4 | u32/f32 |  |  |  |
| ✗ | +32 | 8 | struct 0xB247DB30 |  |  |  |
| ✗ | +40 | 4 | u32/f32 |  |  |  |

### ComponentEntityDeltaStorage → EntityDeltaTypeData (2 members, 1 editable, 572 rows) ⚠ the panel reads 1 B a row, the record is 16 B

tables: attachment deltas

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
|  | +0 | 8 | u64 | ResourceID | spread_h, spread_v, recoil_h |  |
| ✗ | +8 | 4 | u32/f32 | Index |  |  |

### DetectorComponentData → ComponentIndexData (2 members, 1 editable, 321 rows) ⚠ the panel reads 24 B a row, the record is 16 B

tables: detector

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
|  | +0 | 8 | u64 | package | unit_search_min, drone_search_min, unit_search_max | 0x0000000000000000, 0x3F0000003ECCCCCD |
| ✗ | +8 | 4 | u32/f32 | danger_sphere_radius |  | 1065353216, 1101004800  (f32: 1, 20)  [1065353216..1101004800] |

### RechargeComponentData → ComponentIndexData (2 members, 1 editable, 3 rows) ⚠ the panel reads 4 B a row, the record is 16 B

tables: recharge

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
|  | +0 | 8 | u64 | package | bp_recharge |  |
| ✗ | +8 | 4 | u32/f32 | danger_sphere_radius |  |  |

### ThrowerComponentData → ThrowerComponent (1 members, 1 editable, 5 rows)

tables: mine thrower

| | off | size | type | name | panel rows | values |
|---:|---:|---:|---|---|---|---|
|  | +0 | 752 | struct 0xAB75A020 |  | mine_panels, mine_per_panel, mine_arming |  |

## 3. Tables the panel never parses (891)

| file | block | container | record | record B | rows |
|---|---|---|---|---:|---:|
| generated_add_resource_dependencies.dl_bin | 0x06F9ABD0 | 0x06F9ABD0 | 0x1F0B6202 | 16 | ~3 |
| generated_add_resource_dependencies.dl_bin | 0x06F9ABD0 | 0x06F9ABD0 | 0x1F0B6202 | 16 | ~5 |
| generated_planet_color_set_settings.dl_bin | 0x9E5B02C2 | 0x9E5B02C2 | 0x80EB67CF | 64 | ~30 |
| generated_animation_event_trigger_settings.dl_bin | 0x40ECAA07 | AnimationEventTriggerSettings | AnimationEventTriggerSetting | 24 | ~6876 |
| generated_arc_settings.dl_bin | 0xAFDF0267 | ArcSettings | ArcInfo | 104 | ~16 |
| generated_beam_settings.dl_bin | 0xC5085606 | BeamSettings | BeamInfo | 112 | ~30 |
| generated_candidate_descs.dl_bin | 0x47BD3634 | CandidateDescriptions | CandidateDescription | 40 | ~19 |
| generated_collision_event_settings.dl_bin | 0x3C29C0FF | CollisionEventSettings | CollisionEventSetting | 80 | ~180 |
| generated_corporation_logos.dl_bin | 0x12C32914 | CorporationLogos | CorporationLogo | 40 | ~8 |
| generated_credits_settings.dl_bin | 0x9B490117 | CreditsRowSettings | CreditsRowData | 64 | ~5753 |
| generated_damage_settings.dl_bin | 0xEB1433DA | DamageArmorAngles | ? | ? |  |
| generated_damage_settings.dl_bin | 0xE0A72CF0 | DamageSettings | DamageInfo | 76 | ~661 |
| generated_distant_war_effect_settings.dl_bin | 0x63E1DBE8 | DistantWarEffectPool | DistantWarEffect | 24 | ~12 |
| generated_distant_war_effect_settings.dl_bin | 0x63E1DBE8 | DistantWarEffectPool | DistantWarEffect | 24 | ~7 |
| generated_distant_war_effect_settings.dl_bin | 0x63E1DBE8 | DistantWarEffectPool | DistantWarEffect | 24 | ~4 |
| generated_distant_war_effect_settings.dl_bin | 0x63E1DBE8 | DistantWarEffectPool | DistantWarEffect | 24 | ~8 |
| generated_distant_war_effect_settings.dl_bin | 0x63E1DBE8 | DistantWarEffectPool | DistantWarEffect | 24 | ~8 |
| generated_distant_war_effect_settings.dl_bin | 0x63E1DBE8 | DistantWarEffectPool | DistantWarEffect | 24 | ~7 |
| generated_distant_war_effect_settings.dl_bin | 0x63E1DBE8 | DistantWarEffectPool | DistantWarEffect | 24 | ~8 |
| generated_environment_settings.dl_bin | 0x68E17506 | EnvironmentSettings | LevelGenerationPathSettings | 72 | ~8 |
| generated_environment_settings.dl_bin | 0x68E17506 | EnvironmentSettings | LevelGenerationPathSettings | 72 | ~8 |
| generated_environment_settings.dl_bin | 0x68E17506 | EnvironmentSettings | LevelGenerationPathSettings | 72 | ~8 |
| generated_environment_settings.dl_bin | 0x68E17506 | EnvironmentSettings | LevelGenerationPathSettings | 72 | ~8 |
| generated_environment_settings.dl_bin | 0x68E17506 | EnvironmentSettings | LevelGenerationPathSettings | 72 | ~8 |
| generated_environment_settings.dl_bin | 0x68E17506 | EnvironmentSettings | LevelGenerationPathSettings | 72 | ~8 |
| generated_environment_settings.dl_bin | 0x68E17506 | EnvironmentSettings | LevelGenerationPathSettings | 72 | ~8 |
| generated_environment_settings.dl_bin | 0x68E17506 | EnvironmentSettings | LevelGenerationPathSettings | 72 | ~8 |
| generated_environment_settings.dl_bin | 0x68E17506 | EnvironmentSettings | LevelGenerationPathSettings | 72 | ~8 |
| generated_environment_settings.dl_bin | 0x68E17506 | EnvironmentSettings | LevelGenerationPathSettings | 72 | ~8 |
| generated_environment_settings.dl_bin | 0x68E17506 | EnvironmentSettings | LevelGenerationPathSettings | 72 | ~8 |
| generated_environment_settings.dl_bin | 0x68E17506 | EnvironmentSettings | LevelGenerationPathSettings | 72 | ~8 |
| generated_environment_settings.dl_bin | 0x68E17506 | EnvironmentSettings | LevelGenerationPathSettings | 72 | ~8 |
| generated_environment_settings.dl_bin | 0x68E17506 | EnvironmentSettings | LevelGenerationPathSettings | 72 | ~8 |
| generated_environment_settings.dl_bin | 0x68E17506 | EnvironmentSettings | LevelGenerationPathSettings | 72 | ~8 |
| generated_environment_settings.dl_bin | 0x68E17506 | EnvironmentSettings | LevelGenerationPathSettings | 72 | ~8 |
| generated_environment_settings.dl_bin | 0x68E17506 | EnvironmentSettings | LevelGenerationPathSettings | 72 | ~8 |
| generated_explosion_settings.dl_bin | 0x2AEA2592 | ExplosionSettings | ExplosionInfo | 152 | ~448 |
| generated_font_lookup.dl_bin | 0xF192DD51 | FontLookup | FontLookupEntry | 24 | ~3 |
| generated_font_lookup.dl_bin | 0xF192DD51 | FontLookup | FontLookupEntry | 24 | ~3 |
| generated_font_lookup.dl_bin | 0xF192DD51 | FontLookup | FontLookupEntry | 24 | ~4 |
| generated_font_lookup.dl_bin | 0xF192DD51 | FontLookup | FontLookupEntry | 24 | ~3 |
| generated_font_lookup.dl_bin | 0xF192DD51 | FontLookup | FontLookupEntry | 24 | ~3 |
| generated_font_lookup.dl_bin | 0xF192DD51 | FontLookup | FontLookupEntry | 24 | ~3 |
| generated_font_settings.dl_bin | 0x226555C8 | FontSettings | ? | ? |  |
| generated_font_settings.dl_bin | 0x226555C8 | FontSettings | ? | ? |  |
| generated_font_settings.dl_bin | 0x226555C8 | FontSettings | ? | ? |  |
| generated_font_settings.dl_bin | 0x226555C8 | FontSettings | ? | ? |  |
| generated_font_settings.dl_bin | 0x226555C8 | FontSettings | ? | ? |  |
| generated_font_settings.dl_bin | 0x226555C8 | FontSettings | ? | ? |  |
| generated_body_settings.dl_bin | 0xDE0DF22D | HelldiverBody | ? | ? |  |
| generated_body_settings.dl_bin | 0xDE0DF22D | HelldiverBody | ? | ? |  |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~122 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~122 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~122 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~13 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~117 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~122 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~103 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~117 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~122 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~141 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~131 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~131 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~122 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~94 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~122 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~131 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~131 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~141 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~141 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~94 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~136 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~94 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~131 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~103 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~141 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~131 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~117 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~122 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~117 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~13 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~127 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~131 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~131 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~122 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~120 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~11 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~103 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~127 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~94 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~131 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~94 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~108 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~122 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~99 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~94 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~127 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~131 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~75 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~117 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~122 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~131 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~131 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~122 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~136 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~122 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~94 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~122 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~131 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~108 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~131 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~103 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~85 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~85 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~117 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~13 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~13 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~186 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~11 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~171 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~11 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~108 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~122 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~99 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~113 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~11 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~11 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~11 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_armor_sets.dl_bin | 0xD9A55AA0 | HelldiverCustomizationKit | HelldiverBodyTypePieces | 24 | ~8 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~4 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~5 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~5 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~5 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~7 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~6 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~6 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~5 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~5 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~4 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~5 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~4 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~5 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~7 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~6 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~6 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~6 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~6 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~6 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~5 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~8 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~7 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~6 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~5 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~8 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~5 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~7 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~5 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~6 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~5 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~7 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~5 |
| generated_customization_passive_bonuses.dl_bin | 0x63CE0FEB | HelldiverCustomizationPassiveBonusSettings | HelldiverCustomizationPassiveBonusModifier | 16 | ~4 |
| generated_hit_effect_settings.dl_bin | 0xE0F572E3 | HitEffectSettings | HitEffectInfo | 48 | ~1512 |
| generated_language_settings.dl_bin | 0x248CC2D1 | LanguageListSettings | LanguageListEntry | 208 | ~18 |
| generated_location_groups.dl_bin | 0x9BF3BB9D | LevelGenerationLocation | LevelGenerationLocationGroup | 24 | ~41 |
| generated_location_groups.dl_bin | 0x9BF3BB9D | LevelGenerationLocation | LevelGenerationLocationGroup | 24 | ~669 |
| generated_location_groups.dl_bin | 0x9BF3BB9D | LevelGenerationLocation | LevelGenerationLocationGroup | 24 | ~2 |
| generated_location_groups.dl_bin | 0x9BF3BB9D | LevelGenerationLocation | LevelGenerationLocationGroup | 24 | ~22 |
| generated_location_groups.dl_bin | 0x9BF3BB9D | LevelGenerationLocation | LevelGenerationLocationGroup | 24 | ~98 |
| generated_location_groups.dl_bin | 0x9BF3BB9D | LevelGenerationLocation | LevelGenerationLocationGroup | 24 | ~3 |
| generated_location_groups.dl_bin | 0x9BF3BB9D | LevelGenerationLocation | LevelGenerationLocationGroup | 24 | ~60 |
| generated_location_groups.dl_bin | 0x9BF3BB9D | LevelGenerationLocation | LevelGenerationLocationGroup | 24 | ~1218 |
| generated_location_groups.dl_bin | 0x9BF3BB9D | LevelGenerationLocation | LevelGenerationLocationGroup | 24 | ~894 |
| generated_location_groups.dl_bin | 0x9BF3BB9D | LevelGenerationLocation | LevelGenerationLocationGroup | 24 | ~98 |
| generated_location_groups.dl_bin | 0x9BF3BB9D | LevelGenerationLocation | LevelGenerationLocationGroup | 24 | ~10670 |
| generated_location_groups.dl_bin | 0x9BF3BB9D | LevelGenerationLocation | LevelGenerationLocationGroup | 24 | ~2730 |
| generated_location_groups.dl_bin | 0x9BF3BB9D | LevelGenerationLocation | LevelGenerationLocationGroup | 24 | ~22 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~3 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~1 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~2 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~2 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~15 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~1 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~2 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~1 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~0 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~0 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~1 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~11 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~0 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~0 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~0 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~0 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~18 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~2 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~0 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~7 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~33 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~0 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~0 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~0 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~0 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~1 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~0 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~16 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~12 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~26 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~4 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~0 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~0 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~3 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~5 |
| generated_satellite_groups.dl_bin | 0x9D66BB58 | LevelGenerationSatelliteGroup | LevelGenerationSatellite | 488 | ~1 |
| generated_generation_settings.dl_bin | 0x38F3BE95 | LevelGenerationSettings | LocationFlagSettings | 16 | ~648 |
| generated_layer_package_indirection_settings.dl_bin | 0xD0D94E9D | PackageLayerTagIndirection | PackageLayerTagIndirectionPair | 8 | ~10 |
| generated_planet_override_settings.dl_bin | 0x003BA515 | PlanetOverrideSettings | PlanetOverrides | 40 | ~8 |
| generated_planet_override_settings.dl_bin | 0x003BA515 | PlanetOverrideSettings | PlanetOverrides | 40 | ~99 |
| generated_planet_override_settings.dl_bin | 0x003BA515 | PlanetOverrideSettings | PlanetOverrides | 40 | ~41 |
| generated_planet_override_settings.dl_bin | 0x003BA515 | PlanetOverrideSettings | PlanetOverrides | 40 | ~43 |
| generated_planet_override_settings.dl_bin | 0x003BA515 | PlanetOverrideSettings | PlanetOverrides | 40 | ~6 |
| generated_planet_override_settings.dl_bin | 0x003BA515 | PlanetOverrideSettings | PlanetOverrides | 40 | ~89 |
| generated_planet_override_settings.dl_bin | 0x003BA515 | PlanetOverrideSettings | PlanetOverrides | 40 | ~29 |
| generated_planet_override_settings.dl_bin | 0x003BA515 | PlanetOverrideSettings | PlanetOverrides | 40 | ~0 |
| generated_planet_override_settings.dl_bin | 0x003BA515 | PlanetOverrideSettings | PlanetOverrides | 40 | ~41 |
| generated_planet_override_settings.dl_bin | 0x003BA515 | PlanetOverrideSettings | PlanetOverrides | 40 | ~82 |
| generated_planet_override_settings.dl_bin | 0x003BA515 | PlanetOverrideSettings | PlanetOverrides | 40 | ~115 |
| generated_planet_override_settings.dl_bin | 0x003BA515 | PlanetOverrideSettings | PlanetOverrides | 40 | ~60 |
| generated_planet_override_settings.dl_bin | 0x003BA515 | PlanetOverrideSettings | PlanetOverrides | 40 | ~261 |
| generated_policy_settings.dl_bin | 0x025D41C1 | PolicySettings | PolicySetting | 16 | ~28 |
| generated_projectile_settings.dl_bin | 0xBD4042C2 | ProjectileSettings | ProjectileInfo | 272 | ~355 |
| generated_planet_territory_graphs.dl_bin | 0xE5A620DD | SavedPlanetTerritoryGraph | TerritoryCell | 136 | ~1052 |
| generated_planet_territory_graphs.dl_bin | 0xE5A620DD | SavedPlanetTerritoryGraph | TerritoryCell | 136 | ~1052 |
| generated_planet_territory_graphs.dl_bin | 0xE5A620DD | SavedPlanetTerritoryGraph | TerritoryCell | 136 | ~1052 |
| generated_planet_territory_graphs.dl_bin | 0xE5A620DD | SavedPlanetTerritoryGraph | TerritoryCell | 136 | ~1052 |
| generated_planet_territory_graphs.dl_bin | 0xE5A620DD | SavedPlanetTerritoryGraph | TerritoryCell | 136 | ~1052 |
| generated_planet_territory_graphs.dl_bin | 0xE5A620DD | SavedPlanetTerritoryGraph | TerritoryCell | 136 | ~1052 |
| generated_planet_territory_graphs.dl_bin | 0xE5A620DD | SavedPlanetTerritoryGraph | TerritoryCell | 136 | ~1052 |
| generated_planet_territory_graphs.dl_bin | 0xE5A620DD | SavedPlanetTerritoryGraph | TerritoryCell | 136 | ~1052 |
| generated_planet_territory_graphs.dl_bin | 0xE5A620DD | SavedPlanetTerritoryGraph | TerritoryCell | 136 | ~1052 |
| generated_planet_territory_graphs.dl_bin | 0xE5A620DD | SavedPlanetTerritoryGraph | TerritoryCell | 136 | ~1052 |
| generated_planet_territory_graphs.dl_bin | 0xE5A620DD | SavedPlanetTerritoryGraph | TerritoryCell | 136 | ~1052 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~2 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~2 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~2 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~5 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~3 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~4 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~4 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~3 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~2 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~5 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~5 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~7 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~4 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~5 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~2 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~2 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~2 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~4 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~2 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~2 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~8 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~6 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~8 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~4 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~7 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~4 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~3 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~5 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~2 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~4 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~2 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~2 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~2 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~3 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~2 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~6 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~4 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~2 |
| generated_scenario_settings.dl_bin | 0x7BB38A25 | ScenarioSettings | ScenarioSetting | 48 | ~8 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_sky_settings.dl_bin | 0xF6CB7F28 | SkySettings | SkySetting | 264 | ~1 |
| generated_planet_types_settings.dl_bin | 0x857AC132 | SolarSystemObjectTypes | SolarSystemObjectType | 24 | ~700 |
| generated_solar_system_settings.dl_bin | 0x7528E477 | SolarSystemSettings | SolarSystemSetting | 280 | ~327 |
| generated_status_effect_settings.dl_bin | 0xC63E0B22 | StatusEffectSettings | StatusEffectInfo | 160 | ~79 |
| generated_status_effect_settings.dl_bin | 0xDE8193C0 | StatusEffectTemplates | StatusEffectTemplate | 40 | ~29 |
| generated_stratagem_upgrade_settings.dl_bin | 0x56E1C594 | StratagemCustomizations | StratagemCustomizationInfo | 64 | ~1 |
| generated_stratagem_settings.dl_bin | 0x30EB6399 | StratagemSettings | StratagemInfo | 400 | ~17 |
| generated_stratagem_settings.dl_bin | 0x30EB6399 | StratagemSettings | StratagemInfo | 400 | ~2 |
| generated_stratagem_settings.dl_bin | 0x30EB6399 | StratagemSettings | StratagemInfo | 400 | ~14 |
| generated_stratagem_settings.dl_bin | 0x30EB6399 | StratagemSettings | StratagemInfo | 400 | ~13 |
| generated_stratagem_settings.dl_bin | 0x30EB6399 | StratagemSettings | StratagemInfo | 400 | ~2 |
| generated_stratagem_settings.dl_bin | 0x30EB6399 | StratagemSettings | StratagemInfo | 400 | ~47 |
| generated_stratagem_settings.dl_bin | 0x30EB6399 | StratagemSettings | StratagemInfo | 400 | ~17 |
| generated_stratagem_settings.dl_bin | 0x30EB6399 | StratagemSettings | StratagemInfo | 400 | ~9 |
| generated_stratagem_settings.dl_bin | 0x30EB6399 | StratagemSettings | StratagemInfo | 400 | ~48 |
| generated_stratagem_settings.dl_bin | 0x30EB6399 | StratagemSettings | StratagemInfo | 400 | ~12 |
| generated_stratagem_settings.dl_bin | 0x30EB6399 | StratagemSettings | StratagemInfo | 400 | ~2 |
| generated_stratagem_settings.dl_bin | 0x30EB6399 | StratagemSettings | StratagemInfo | 400 | ~16 |
| generated_surface_effect_settings.dl_bin | 0x79400A27 | SurfaceEffectSettings | SurfaceEffectInfo | 40 | ~7644 |
| generated_unit_customization_settings.dl_bin | 0xA2BA274A | UnitCustomizationSettings | UnitCustomizationSetting | 64 | ~39 |
| generated_unit_customization_settings.dl_bin | 0xA2BA274A | UnitCustomizationSettings | UnitCustomizationSetting | 64 | ~32 |
| generated_unit_customization_settings.dl_bin | 0xA2BA274A | UnitCustomizationSettings | UnitCustomizationSetting | 64 | ~39 |
| generated_unit_customization_settings.dl_bin | 0xA2BA274A | UnitCustomizationSettings | UnitCustomizationSetting | 64 | ~32 |
| generated_unit_customization_settings.dl_bin | 0xA2BA274A | UnitCustomizationSettings | UnitCustomizationSetting | 64 | ~38 |
| generated_unit_customization_settings.dl_bin | 0xA2BA274A | UnitCustomizationSettings | UnitCustomizationSetting | 64 | ~32 |
| generated_unit_customization_settings.dl_bin | 0xA2BA274A | UnitCustomizationSettings | UnitCustomizationSetting | 64 | ~32 |
| generated_unit_customization_settings.dl_bin | 0xA2BA274A | UnitCustomizationSettings | UnitCustomizationSetting | 64 | ~38 |
| generated_unit_customization_settings.dl_bin | 0xA2BA274A | UnitCustomizationSettings | UnitCustomizationSetting | 64 | ~17 |
| generated_unit_customization_settings.dl_bin | 0xA2BA274A | UnitCustomizationSettings | UnitCustomizationSetting | 64 | ~38 |
| generated_unit_customization_settings.dl_bin | 0xA2BA274A | UnitCustomizationSettings | UnitCustomizationSetting | 64 | ~41 |
| generated_unit_customization_settings.dl_bin | 0xA2BA274A | UnitCustomizationSettings | UnitCustomizationSetting | 64 | ~44 |
| generated_unit_effect_settings.dl_bin | 0xA212489E | UnitEffectSettings | UnitEffectSetting | 112 | ~562 |
| generated_video_flow_settings.dl_bin | 0xFBD8E5C0 | VideoFlowSettings | VideoSegment | 112 | ~18 |
| generated_video_ui_settings.dl_bin | 0x82E72346 | VideoUISettings | VideoUIElement | 120 | ~9 |
| generated_weapon_customization_settings.dl_bin | 0x1E604234 | WeaponCustomizationSettings | WeaponCustomizableItem | 88 | ~134 |
| generated_weapon_customization_settings.dl_bin | 0x1E604234 | WeaponCustomizationSettings | WeaponCustomizableItem | 88 | ~3 |
| generated_weapon_customization_settings.dl_bin | 0x1E604234 | WeaponCustomizationSettings | WeaponCustomizableItem | 88 | ~5 |
| generated_weapon_customization_settings.dl_bin | 0x1E604234 | WeaponCustomizationSettings | WeaponCustomizableItem | 88 | ~80 |
| generated_weapon_customization_settings.dl_bin | 0x1E604234 | WeaponCustomizationSettings | WeaponCustomizableItem | 88 | ~47 |
| generated_weapon_customization_settings.dl_bin | 0x1E604234 | WeaponCustomizationSettings | WeaponCustomizableItem | 88 | ~26 |
| generated_weapon_customization_settings.dl_bin | 0x1E604234 | WeaponCustomizationSettings | WeaponCustomizableItem | 88 | ~20 |
| generated_weapon_customization_settings.dl_bin | 0x1E604234 | WeaponCustomizationSettings | WeaponCustomizableItem | 88 | ~3 |
| generated_weapon_customization_settings.dl_bin | 0x1E604234 | WeaponCustomizationSettings | WeaponCustomizableItem | 88 | ~24 |
| generated_weather_color_set_settings.dl_bin | 0x786F17CE | WeatherColorSets | WeatherColorSet | 196 | ~132 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~8 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~8 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~8 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~8 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~7 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~7 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~5 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~5 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~5 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~5 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~5 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~5 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~5 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~6 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~6 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~5 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~5 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~3 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
| generated_weather_settings.dl_bin | 0x6C613D21 | WeatherSettings | WeatherColorSet | 196 | ~4 |
