def kebabToCamelCase(s: str) -> str:
    parts = s.split("-")
    return parts[0].capitalize() + "".join(p.capitalize() for p in parts[1:])
