ALLOWED_OBJECTS = {
    "car",
    "laptop",
    "package",
    "unknown"
}

ALLOWED_ISSUES = {
    "dent",
    "scratch",
    "crack",
    "glass_shatter",
    "broken_part",
    "missing_part",
    "torn_packaging",
    "crushed_packaging",
    "water_damage",
    "stain",
    "none",
    "unknown"
}

ALLOWED_SEVERITIES = {
    "none",
    "low",
    "medium",
    "high",
    "unknown"
}

ALLOWED_PARTS = {
    # car
    "front_bumper",
    "rear_bumper",
    "door",
    "hood",
    "windshield",
    "side_mirror",
    "headlight",
    "taillight",
    "fender",
    "quarter_panel",
    "body",

    # laptop
    "screen",
    "keyboard",
    "trackpad",
    "hinge",
    "lid",
    "corner",
    "port",
    "base",

    # package
    "box",
    "package_corner",
    "package_side",
    "seal",
    "label",
    "contents",
    "item",

    "unknown"
}

PART_NORMALIZATION = {
    "": "unknown",

    # bumpers
    "bumper": "front_bumper",
    "front bumper": "front_bumper",
    "rear bumper": "rear_bumper",
    "back bumper": "rear_bumper",

    # lights
    "tail light": "taillight",
    "tailight": "taillight",
    "back light": "taillight",

    # mirrors
    "mirror": "side_mirror",
    "side mirror": "side_mirror",

    # windshield
    "front glass": "windshield",

    # package
    "corner": "package_corner",
    "side": "package_side"
}

ISSUE_NORMALIZATION = {
    "": "unknown",

    "broken": "broken_part",
    "missing": "missing_part",

    "shattered": "glass_shatter",
    "shatter": "glass_shatter",

    "water": "water_damage"
}

SEVERITY_NORMALIZATION = {
    "": "unknown",
    "minor": "low",
    "moderate": "medium",
    "severe": "high"
}


class ObservationNormalizer:

    @staticmethod
    def normalize(response: dict) -> dict:

        visible_object = (
            str(response.get("visible_object", "unknown"))
            .strip()
            .lower()
        )

        visible_part = (
            str(response.get("visible_part", "unknown"))
            .strip()
            .lower()
        )

        visible_issue = (
            str(response.get("visible_issue", "unknown"))
            .strip()
            .lower()
        )

        severity = (
            str(response.get("severity", "unknown"))
            .strip()
            .lower()
        )

        risk_flags = response.get(
            "risk_flags",
            []
        )

        visible_part = PART_NORMALIZATION.get(
            visible_part,
            visible_part
        )

        visible_issue = ISSUE_NORMALIZATION.get(
            visible_issue,
            visible_issue
        )

        severity = SEVERITY_NORMALIZATION.get(
            severity,
            severity
        )

        if visible_object not in ALLOWED_OBJECTS:
            visible_object = "unknown"

        if visible_part not in ALLOWED_PARTS:
            visible_part = "unknown"

        if visible_issue not in ALLOWED_ISSUES:
            visible_issue = "unknown"

        if severity not in ALLOWED_SEVERITIES:
            severity = "unknown"

        return {
            "visible_object": visible_object,
            "visible_part": visible_part,
            "visible_issue": visible_issue,
            "severity": severity,
            "valid_image": bool(
                response.get("valid_image", True)
            ),
            "risk_flags": risk_flags
        }