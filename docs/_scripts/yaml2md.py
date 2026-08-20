from pathlib import Path

from ruamel.yaml import YAML


def yaml_to_markdown(yaml_path: str | Path) -> str:
    yaml = YAML()

    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.load(f)

    sections = []

    sections.append(f"# Speaker info")

    for session in data:
        title = (session.get("title") or "").strip()
        lines = [f"## {title}", ""]

        for speaker in session.get("speakers", []):
            name = (speaker.get("name") or "").strip()
            lines.append(f"### {name}")

            fields = [
                ("Email", "email"),
                ("Pronouns", "pronouns"),
                ("Pronunciation", "pronounce"),
                ("Bio", "bio"),
            ]

            for label, key in fields:
                value = speaker.get(key)
                if value:
                    lines.append(f"- **{label}:** {str(value).strip()}")

            lines.append("")

        sections.append("\n".join(lines).rstrip())

    return "\n\n".join(sections)


yaml_path = Path("../_data/mc-info.yaml")

markdown = yaml_to_markdown(yaml_path)

print(markdown)