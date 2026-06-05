# glone

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://pydantic.dev)

A CLI to back up all your [GitHub](https://github.com/) repositories.

- [Source code](https://github.com/joaopalmeiro/glone)
- [PyPI package](https://pypi.org/project/glone/)
- [ClickPy](https://clickpy.clickhouse.com/dashboard/glone)
- [ecosyte.ms](https://packages.ecosyste.ms/registries/pypi.org/packages/glone)
- [Libraries.io](https://libraries.io/pypi/glone)
- [Open Source Insights](https://deps.dev/pypi/glone)
- [OSV](https://osv.dev/list?q=glone&ecosystem=PyPI)
- [PePy](https://pepy.tech/projects/glone)
- [PyPack Trends](https://pypacktrends.com/?packages=glone&time_range=allTime)
- [PyPI Stats](https://pypistats.org/search/glone)
- [Snyk](https://security.snyk.io/package/pip/glone)
- [Socket](https://socket.dev/pypi/package/glone)

## Usage

### Via [uv](https://docs.astral.sh/uv/) and [1Password CLI](https://www.1password.dev/cli/reference/commands/run)

```bash
uvx glone --help
```

```bash
GITHUB_ACCESS_TOKEN="op://Development/glone/GITHUB_ACCESS_TOKEN" op run -- uvx glone
```

## Development

Install [zizmor](https://docs.zizmor.sh/installation/), [pinact](https://github.com/suzuki-shunsuke/pinact/blob/main/INSTALL.md), [1Password](https://1password.com/downloads/), and [1Password CLI](https://developer.1password.com/docs/cli/get-started/) (if necessary).

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) (if necessary):

```bash
curl -LsSf https://astral.sh/uv/0.11.6/install.sh | sh
```

```bash
uv python install
```

```bash
uv audit --verbose
```

```bash
uv run glone --help
```

```bash
GITHUB_ACCESS_TOKEN="op://Development/glone/GITHUB_ACCESS_TOKEN" op run -- uv run glone
```

```bash
uv run mypy
```

```bash
uv run ruff format
```

```bash
uv run ruff check --fix
```

```bash
uv build
```

### GitHub Actions

```bash
zizmor .
```

```bash
pinact run -u --min-age 7
```

### Get a GitHub token

1. Go to https://github.com/settings/personal-access-tokens
2. _Generate new token_
3. _Token name_: `glone`
4. _Repository access_ > _All repositories_
5. _Add permissions_ > `Contents` (_Access:_ `Read-only`)

## Deployment

- Create the `release` [GitHub Actions environment](https://github.com/joaopalmeiro/glone/settings/environments) (if necessary).
- [Add a trusted publisher to an existing PyPI project](https://docs.pypi.org/trusted-publishers/adding-a-publisher/) or [create a new one with a trusted publisher](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/) (if necessary).

```bash
uv version --bump patch
```

```bash
uv version --bump minor
```

```bash
uv version --bump major
```

```bash
echo "v$(uv version --short)" | pbcopy
```

- Commit and push changes.
- Create a tag on [GitHub Desktop](https://github.blog/2020-05-12-create-and-push-tags-in-the-latest-github-desktop-2-5-release/).
- Check GitHub: [Tags](https://github.com/joaopalmeiro/glone/tags) and [Actions](https://github.com/joaopalmeiro/glone/actions).
- Check [PyPI](https://pypi.org/project/glone/).
