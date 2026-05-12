#!/usr/bin/env python3

"""Render a Markdown/Jinja file using conference YAML data."""

from __future__ import annotations

import argparse
from pathlib import Path
import re

import yaml
from jinja2 import Environment, StrictUndefined


def load_yaml_config(config_path: Path) -> dict:
    """Load conference YAML config as a dictionary."""
    with config_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Expected a mapping in config YAML: {config_path}")
    return data


def render_markdown(template_path: Path, context: dict) -> str:
    """Render a Markdown template with Jinja variables from context."""
    template_text = template_path.read_text(encoding="utf-8")
    env = Environment(
        autoescape=False,
        keep_trailing_newline=True,
        undefined=StrictUndefined,
    )
    template = env.from_string(template_text)
    return template.render(**context)


def post_process_markdown(markdown: str) -> str:
    """Convert selected MyST directives to plain Markdown output."""
    lines = markdown.splitlines()
    out_lines: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i]

        if line.startswith("```{"):
            directive_header = line.strip()
            directive_name = ""
            if directive_header.startswith("```{") and "}" in directive_header:
                directive_name = directive_header[4:directive_header.index("}")].strip()

            if directive_name == "button-link":
                url = directive_header.replace("```{button-link}", "", 1).strip()
                i += 1

                label_lines: list[str] = []
                while i < len(lines) and lines[i].strip() != "```":
                    label_lines.append(lines[i])
                    i += 1

                # Skip closing fence if present.
                if i < len(lines) and lines[i].strip() == "```":
                    i += 1

                label = " ".join(part.strip() for part in label_lines if part.strip())
                out_lines.append(f"[{label}]({url})")
                continue

            # Strip all other fenced directives.
            i += 1
            while i < len(lines) and lines[i].strip() != "```":
                i += 1
            # Skip closing fence if present.
            if i < len(lines) and lines[i].strip() == "```":
                i += 1
            continue

        out_lines.append(line)
        i += 1

    markdown = "\n".join(out_lines)

    # Clean up excessive blank lines introduced by stripping blocks.
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown


def strip_frontmatter(markdown: str) -> str:
    """Remove YAML frontmatter at the top of the file if present."""
    if not markdown.startswith("---\n"):
        return markdown

    lines = markdown.splitlines()
    if not lines or lines[0].strip() != "---":
        return markdown

    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            remainder = lines[i + 1 :]
            output = "\n".join(remainder)
            if markdown.endswith("\n"):
                output += "\n"
            return output

    return markdown


def parse_args() -> argparse.Namespace:
    """Parse command-line options."""
    docs_dir = Path(__file__).resolve().parents[1]
    default_input = docs_dir / "conf/portland/2026/news/welcome-portland-2026.md"
    default_config = docs_dir / "_data/portland-2026-config.yaml"

    parser = argparse.ArgumentParser(
        description="Render Markdown containing Jinja variables with conference YAML context."
    )
    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        default=default_input,
        help="Path to Markdown file with Jinja variables.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=default_config,
        help="Path to conference YAML config file.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Optional output path. If omitted, prints to stdout.",
    )
    parser.add_argument(
        "--strip-frontmatter",
        action="store_true",
        help="Remove YAML frontmatter from the rendered output.",
    )
    return parser.parse_args()


def main() -> int:
    """Entrypoint for script execution."""
    args = parse_args()

    config_data = load_yaml_config(args.config)
    rendered = render_markdown(args.input, config_data)
    rendered = post_process_markdown(rendered)
    if args.strip_frontmatter:
        rendered = strip_frontmatter(rendered)

    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())