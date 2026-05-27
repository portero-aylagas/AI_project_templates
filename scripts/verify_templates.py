"""Verify that each template carries the required quality artifacts."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = ROOT / "templates"

REQUIRED_ROOT_FILES = [
    "README.md",
    "PROJECT_SPEC.md",
    ".env.example",
    "Makefile",
    "verify.sh",
    "pyproject.toml",
]

REQUIRED_DOCS = [
    "docs/architecture.md",
    "docs/runbook.md",
    "docs/limitations.md",
    "docs/evaluation.md",
]

REQUIRED_TEST_DIRS = [
    "tests/fakes",
    "tests/fixtures",
]

REQUIRED_SOURCE_FILES = [
    "config.py",
    "schemas.py",
    "llm_client.py",
    "storage.py",
]


def package_dir(template_dir: Path) -> Path:
    """Return the single package directory under a template's src folder."""
    packages = [path for path in (template_dir / "src").iterdir() if path.is_dir()]
    if len(packages) != 1:
        raise AssertionError(f"{template_dir}: expected exactly one src package")
    return packages[0]


def verify_template(template_dir: Path) -> list[str]:
    """Return structural problems for one template."""
    problems: list[str] = []

    for relative_path in REQUIRED_ROOT_FILES + REQUIRED_DOCS:
        if not (template_dir / relative_path).is_file():
            problems.append(f"missing file: {relative_path}")

    for relative_path in REQUIRED_TEST_DIRS:
        if not (template_dir / relative_path).is_dir():
            problems.append(f"missing directory: {relative_path}")

    try:
        package = package_dir(template_dir)
    except AssertionError as exc:
        problems.append(str(exc))
        return problems

    for filename in REQUIRED_SOURCE_FILES:
        if not (package / filename).is_file():
            problems.append(f"missing source file: src/{package.name}/{filename}")

    if not (package / "prompts").is_dir():
        problems.append(f"missing prompt directory: src/{package.name}/prompts")

    if not (package / "web").is_dir():
        problems.append(f"missing web directory: src/{package.name}/web")

    return problems


def main() -> int:
    """Run structural verification for all templates."""
    template_dirs = sorted(path for path in TEMPLATE_ROOT.iterdir() if path.is_dir())
    if not template_dirs:
        print("No templates found.")
        return 1

    all_problems: list[str] = []
    for template_dir in template_dirs:
        problems = verify_template(template_dir)
        for problem in problems:
            all_problems.append(f"{template_dir.name}: {problem}")

    if all_problems:
        print("Template verification failed:")
        for problem in all_problems:
            print(f"- {problem}")
        return 1

    print(f"Verified {len(template_dirs)} templates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
