# A cookiecutter template for software projects

## Pre-requisite

You need to have the cli `cookiecutter` available in your Python environment. Please see its
installation instructions [here](https://cookiecutter.readthedocs.io/en/latest/installation.html).

## Usage

To generate a directory structure for a new project, you can run the following commands in your
Python environment.

```bash
cookiecutter https://github.com/verdimrc/simple-project-template
```

Alternatively, you can also clone this repository to use a local template:

```bash
# Clone to a local repository in the current directory.
git clone https://github.com/verdimrc/simple-project-template

# The above command creates simple-project-template/ in the current dir.

# Use the local repo to generate project structure
cookiecutter simple-project-template
```

## Project Structure

By using this template, your project is auto-generated as follows:

```text
.
|-- .editorconfig                # Sample editor config (for IDE / editor that supports this)
|-- .gitattributes               # Sample .gitattributes
|-- .gitleaks.toml               # Sample Gitleaks config (if pre_commit is advanced)
|-- .gitignore                   # Sample .gitignore
|-- .pre-commit-config.yaml      # Sample precommit hooks
|-- LICENSE                      # Boilperplate (auto-generated)
`-- README.md                    # Template for you to customize
```

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
