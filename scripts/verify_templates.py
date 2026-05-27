"""Verify that each template carries required artifacts and static gates."""

from __future__ import annotations

from pathlib import Path
import tomllib


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = ROOT / "templates"

REQUIRED_ROOT_FILES = [
    "README.md",
    "PROJECT_SPEC.md",
    "AGENTS.md",
    ".env.example",
    "Makefile",
    "verify.sh",
    "pyproject.toml",
]

REQUIRED_CI_FILE = ".github/workflows/verify.yml"

REQUIRED_CI_SNIPPETS = [
    "setup-python",
    'pip install -e ".[dev]"',
    "make verify",
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

REQUIRED_VERIFY_COMMANDS = [
    "compileall",
    "ruff check",
    "pytest",
]

REQUIRED_MAKE_TARGETS = [
    "verify:",
    "compile:",
    "lint:",
    "test:",
]

REQUIRED_DEV_DEPENDENCIES = [
    "pytest",
    "ruff",
]


def read_text(path: Path) -> str:
    """Read a UTF-8 file for verification."""
    return path.read_text(encoding="utf-8")


def package_dir(template_dir: Path) -> Path:
    """Return the single package directory under a template's src folder."""
    src_dir = template_dir / "src"
    if not src_dir.is_dir():
        raise AssertionError(f"{template_dir}: missing src directory")

    packages = [path for path in src_dir.iterdir() if path.is_dir()]
    if len(packages) != 1:
        raise AssertionError(f"{template_dir}: expected exactly one src package")
    return packages[0]


def has_dependency(dependencies: list[str], package_name: str) -> bool:
    """Return whether a dependency list contains a package requirement."""
    normalized_name = package_name.lower()
    return any(
        dependency.lower().startswith(normalized_name) for dependency in dependencies
    )


def verify_non_empty_files(template_dir: Path, relative_paths: list[str]) -> list[str]:
    """Return problems for required files that are empty placeholders."""
    problems: list[str] = []

    for relative_path in relative_paths:
        path = template_dir / relative_path
        if path.is_file() and not read_text(path).strip():
            problems.append(f"empty file: {relative_path}")

    return problems


def verify_docs(template_dir: Path) -> list[str]:
    """Return problems for documentation that is too thin for reuse."""
    problems: list[str] = []

    for relative_path in REQUIRED_DOCS:
        path = template_dir / relative_path
        if not path.is_file():
            continue

        text = read_text(path)
        meaningful_words = [word for word in text.split() if not word.startswith("#")]
        if len(meaningful_words) < 12:
            problems.append(f"documentation too thin: {relative_path}")

    return problems


def verify_template_verification(template_dir: Path) -> list[str]:
    """Return problems for missing per-template verification commands."""
    problems: list[str] = []

    verify_script = template_dir / "verify.sh"
    if verify_script.is_file():
        text = read_text(verify_script)
        for command in REQUIRED_VERIFY_COMMANDS:
            if command not in text:
                problems.append(f"verify.sh does not run {command}")

    makefile = template_dir / "Makefile"
    if makefile.is_file():
        text = read_text(makefile)
        for target in REQUIRED_MAKE_TARGETS:
            if target not in text:
                problems.append(f"Makefile missing target: {target.rstrip(':')}")

    return problems


def verify_ci_workflow(template_dir: Path) -> list[str]:
    """Return problems for missing copied-project CI workflow basics."""
    problems: list[str] = []
    workflow = template_dir / REQUIRED_CI_FILE
    if not workflow.is_file():
        return problems

    text = read_text(workflow)
    for snippet in REQUIRED_CI_SNIPPETS:
        if snippet not in text:
            problems.append(f"{REQUIRED_CI_FILE} missing {snippet}")
    if "branches:" in text:
        problems.append(f"{REQUIRED_CI_FILE} should not filter branches")

    return problems


def verify_pyproject(template_dir: Path) -> list[str]:
    """Return problems for pyproject development-tool configuration."""
    problems: list[str] = []
    pyproject = template_dir / "pyproject.toml"
    if not pyproject.is_file():
        return problems

    try:
        with pyproject.open("rb") as file:
            config = tomllib.load(file)
    except tomllib.TOMLDecodeError as exc:
        return [f"invalid pyproject.toml: {exc}"]

    project = config.get("project", {})
    dependencies = project.get("dependencies", [])
    if not has_dependency(dependencies, "pydantic"):
        problems.append("pyproject.toml missing pydantic dependency")

    optional_dependencies = project.get("optional-dependencies", {})
    dev_dependencies = optional_dependencies.get("dev", [])
    for dependency in REQUIRED_DEV_DEPENDENCIES:
        if not has_dependency(dev_dependencies, dependency):
            problems.append(f"pyproject.toml missing dev dependency: {dependency}")

    tool_config = config.get("tool", {})
    pytest_config = tool_config.get("pytest", {}).get("ini_options", {})
    pythonpath = pytest_config.get("pythonpath", [])
    if isinstance(pythonpath, str):
        pythonpath = [pythonpath]
    if "src" not in pythonpath:
        problems.append('pyproject.toml missing pytest pythonpath = ["src"]')

    ruff_config = tool_config.get("ruff")
    if not ruff_config:
        problems.append("pyproject.toml missing ruff configuration")

    return problems


def verify_tests(template_dir: Path) -> list[str]:
    """Return problems for missing behavioral test entry points."""
    problems: list[str] = []
    tests_dir = template_dir / "tests"

    if tests_dir.is_dir() and not list(tests_dir.glob("test_*.py")):
        problems.append("missing test file: tests/test_*.py")

    fakes_dir = tests_dir / "fakes"
    if fakes_dir.is_dir() and not list(fakes_dir.glob("*.py")):
        problems.append("tests/fakes has no Python fake clients")

    fixtures_dir = tests_dir / "fixtures"
    if fixtures_dir.is_dir():
        fixture_files = [path for path in fixtures_dir.iterdir() if path.is_file()]
        if not fixture_files:
            problems.append("tests/fixtures has no fixture files")

    return problems


def verify_prompt_files(package: Path) -> list[str]:
    """Return problems for missing or empty named prompt files."""
    problems: list[str] = []
    prompts_dir = package / "prompts"
    if not prompts_dir.is_dir():
        return problems

    prompt_files = sorted(prompts_dir.glob("*.md"))
    if not prompt_files:
        problems.append(f"missing prompt files: src/{package.name}/prompts/*.md")
        return problems

    for prompt_file in prompt_files:
        if not read_text(prompt_file).strip():
            problems.append(
                f"empty prompt file: src/{package.name}/prompts/{prompt_file.name}"
            )

    return problems


def verify_llm_boundary(package: Path) -> list[str]:
    """Return problems for missing fakeable LLM provider boundaries."""
    problems: list[str] = []
    llm_client = package / "llm_client.py"
    if not llm_client.is_file():
        return problems

    text = read_text(llm_client)
    if "Protocol" not in text:
        problems.append(
            f"llm_client.py missing Protocol boundary in src/{package.name}"
        )
    if "Fake" not in text:
        problems.append(f"llm_client.py missing fake client in src/{package.name}")

    return problems


def verify_template(template_dir: Path) -> list[str]:
    """Return structural and static acceptance problems for one template."""
    problems: list[str] = []

    for relative_path in REQUIRED_ROOT_FILES + REQUIRED_DOCS + [REQUIRED_CI_FILE]:
        if not (template_dir / relative_path).is_file():
            problems.append(f"missing file: {relative_path}")

    for relative_path in REQUIRED_TEST_DIRS:
        if not (template_dir / relative_path).is_dir():
            problems.append(f"missing directory: {relative_path}")

    required_text_files = REQUIRED_ROOT_FILES + REQUIRED_DOCS + [REQUIRED_CI_FILE]
    problems.extend(verify_non_empty_files(template_dir, required_text_files))
    problems.extend(verify_docs(template_dir))
    problems.extend(verify_template_verification(template_dir))
    problems.extend(verify_ci_workflow(template_dir))
    problems.extend(verify_pyproject(template_dir))
    problems.extend(verify_tests(template_dir))

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

    problems.extend(verify_prompt_files(package))
    problems.extend(verify_llm_boundary(package))

    return problems


def main() -> int:
    """Run fast structural and static acceptance verification for all templates."""
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
