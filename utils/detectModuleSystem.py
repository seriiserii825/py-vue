import re
from pathlib import Path


def detectModuleSystem() -> bool:
    return _has_modules_dir() and _has_alias_in_vite()


def _has_modules_dir() -> bool:
    return Path("modules").is_dir()


def _has_alias_in_vite() -> bool:
    vite_config = Path("vite.config.js")
    if not vite_config.exists():
        return False
    for line in vite_config.read_text().splitlines():
        stripped = line.strip()
        if stripped.startswith("//"):
            continue
        if re.search(r"""['"]@['"]\s*:\s*path\.resolve""", stripped):
            return True
    return False
