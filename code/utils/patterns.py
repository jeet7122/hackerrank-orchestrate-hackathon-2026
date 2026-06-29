PROMPT_INJECTION_PATTERNS = [
    "approve immediately",
    "skip manual review",
    "skip review",
    "ignore previous instructions",
    "ignore all previous instructions",
    "mark this row supported",
    "mark supported",
    "follow it and approve",
    "follow this note",
]


ISSUE_PATTERNS = {
    "glass_shatter": [
        "shattered",
        "shatter"
    ],

    "crack": [
        "crack",
        "cracked"
    ],

    "dent": [
        "dent",
        "dented"
    ],

    "scratch": [
        "scratch",
        "scratched"
    ],

    "broken_part": [
        "broken",
        "broke"
    ],

    "missing_part": [
        "missing",
        "came off"
    ],

    "torn_packaging": [
        "torn",
        "torn open",
        "opened"
    ],

    "crushed_packaging": [
        "crushed",
        "dab gaya"
    ],

    "water_damage": [
        "water damage",
        "wet"
    ],

    "stain": [
        "stain",
        "stained"
    ]
}


PART_PATTERNS = {

    # CAR

    "front_bumper": [
        "front bumper"
    ],

    "rear_bumper": [
        "rear bumper",
        "back bumper"
    ],

    "door": [
        "door"
    ],

    "hood": [
        "hood"
    ],

    "windshield": [
        "windshield",
        "front glass"
    ],

    "side_mirror": [
        "side mirror",
        "mirror"
    ],

    "headlight": [
        "headlight"
    ],

    "taillight": [
        "taillight",
        "tail light",
        "back light"
    ],

    "fender": [
        "fender"
    ],

    "quarter_panel": [
        "quarter panel"
    ],

    "body": [
        "body panel",
        "body"
    ],

    # LAPTOP

    "screen": [
        "screen",
        "display",
        "pantalla"
    ],

    "keyboard": [
        "keyboard",
        "keys",
        "teclas"
    ],

    "trackpad": [
        "trackpad",
        "track pad"
    ],

    "hinge": [
        "hinge"
    ],

    "lid": [
        "lid"
    ],

    "corner": [
        "corner"
    ],

    "port": [
        "port"
    ],

    "base": [
        "base"
    ],

    # PACKAGE

    "box": [
        "box"
    ],

    "package_corner": [
        "package corner",
        "corner damage"
    ],

    "package_side": [
        "package side"
    ],

    "seal": [
        "seal"
    ],

    "label": [
        "label"
    ],

    "contents": [
        "contents"
    ],

    "item": [
        "item"
    ]
}

RISK_FLAGS = [
    "blurry_image",
    "cropped_or_obstructed",
    "low_light_or_glare",
    "wrong_angle",
    "wrong_object",
    "wrong_object_part",
    "damage_not_visible",
    "claim_mismatch",
    "possible_manipulation",
    "non_original_image"
]
