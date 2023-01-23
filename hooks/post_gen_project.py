import sys
from pathlib import Path

# missing_ok available only since python-3.8
# https://docs.python.org/3/library/pathlib.html#pathlib.Path.unlink
if sys.version_info[0:2] >= (3, 8):

    def rm(s: Path) -> None:
        Path(s).unlink(missing_ok=True)

else:

    def rm(s: Path) -> None:
        try:
            Path(s).unlink()
        except FileNotFoundError:
            pass


license = "{{cookiecutter.open_source_license}}"
if license == "No license file":
    rm("LICENSE")

# fmt: off
pre_commit = "{{cookiecutter.pre_commit}}"
if pre_commit != "advanced":
    rm(".gitleaks.toml")

# Display next steps.
cwd = Path().resolve()
message = [
    "#" * 80,
    "# Congratulations, your project has been initialized!",
    "#",
    f"# The generated project is located at {cwd}",
    "#",
    "# Recommended next steps:",
    f"# - cd {cwd}",
    "# - git init",
    "# - pre-commit autoupdate",
    "# - pre-commit install",
    "# - review README.md",
]
if license != "No license file":
    message.append("# - review LICENSE")
message += [
    "# - git add .",
    "# - git commit",
    "#" * 80,
]
print(*message, sep="\n")
