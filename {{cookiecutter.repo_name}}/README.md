# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Project Structure

```text
{{cookiecutter.repo_name}}
|-- .editorconfig                # Editor config (for IDE / editor that support this)
|-- .gitattributes               # Files that Git must give special treatments
{% if cookiecutter.pre_commit == "advanced" -%}
|-- .gitleaks.toml               # Configuration for Gitleaks tool
{% endif -%}
|-- .gitignore                   # Git ignore list
|-- .pre-commit-config.yaml      # Precommit hooks
|-- LICENSE                      # License
`-- README.md                    # Template document
```

## Credits

This project was initialized by {{cookiecutter.author_name}} using:

```bash
cookiecutter https://github.com/verdimrc/simple-project-template
```

## License

This library is licensed under the {{cookiecutter.open_source_license}}.{% if cookiecutter.open_source_license != "No license file" %} See the [LICENSE](LICENSE) file.{%- endif %}
