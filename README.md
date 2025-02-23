
# Exploring PydanticAI with LiteLLM Proxy Server (LiteLLM Gateway) and OpenAI-compatible Models

* using [uv](https://github.com/astral-sh/uv) extremely fast Python package and project manager
* using [Free LLM Providers](https://github.com/cheahjs/free-llm-api-resources?tab=readme-ov-file#free-providers)
* using [OpenRouter to access many FREE models](https://openrouter.ai/models?order=pricing-low-to-high)
* using [PydanticAI Agent with OpenAIModel](https://ai.pydantic.dev/models/#openrouter) to access OpenRouter and LiteLLM models
* using [LiteLLM Proxy Server (LiteLLM Gateway)](https://docs.litellm.ai/docs/simple_proxy) to easily switch between  models - API or local (Ollama)

# Prerequisites

## uv - An extremely fast Python package and project manager, written in Rust

[uv docs](https://docs.astral.sh/uv/)

* Highlights:
	* A single tool to replace pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, and more.
	* 10-100x faster than pip.
	* Installs and manages Python versions.
	* Runs and installs Python applications.
	* Runs scripts, with support for inline dependency metadata.
	* Provides comprehensive project management, with a universal lockfile.
	* Includes a pip-compatible interface for a performance boost with a familiar CLI.
	* Supports Cargo-style workspaces for scalable projects.
	* Disk-space efficient, with a global cache for dependency deduplication.
	* Installable without Rust or Python via curl or pip.
	* Supports macOS, Linux, and Windows.

### [Installing uv](https://docs.astral.sh/uv/getting-started/installation/#installing-uv)

>On macOS and Linux.
`curl -LsSf https://astral.sh/uv/install.sh | sh`

```
$ curl -LsSf https://astral.sh/uv/install.sh | sh
downloading uv 0.5.26 x86_64-unknown-linux-gnu
no checksums to verify
installing to ~/.local/bin
  uv
  uvx
everything's installed!
$ uv --version
uv 0.5.26
$
```

### [Upgrading uv](https://docs.astral.sh/uv/getting-started/installation/#upgrading-uv)

`uv self update`

```
$ uv version
uv 0.5.29
$ uv self update
info: Checking for updates...
success: Upgraded uv from v0.5.29 to v0.6.2! https://github.com/astral-sh/uv/releases/tag/0.6.2
$ uv version
uv 0.6.2
$
```

# The Project

## Setup

Clone the repository and change directory to the cloned repo:

```
git clone https://github.com/LeonidShamis/litellm-proxy-server-pydanticai-ollama-openrouter.git
cd litellm-proxy-server-pydanticai-ollama-openrouter
```

## Creating virtual environment and install dependencies

Run `uv sync` command

## Configure the LiteLLM Proxy Server (LiteLLM Gateway) and the environment variables (.env)

Copy the example environment variables file to `.env` and populate the relevant values:

```
$ cp example.env .env
```

* OLLAMA_MODEL_NAME - local LLM name to be used with Ollama
* LITELLM_PROXY_API_KEY - API key to protect your (local) LiteLLM Proxy Server
* OPENROUTER_API_KEY - OpenRouter API key
* OPENROUTER_MODEL_NAME - LLM name to be used through OpenRouter
* LITELLM_PROXY_MODEL_NAME - LLM name to be used with the LiteLLM examples

Configure models using `config.yaml` file

## Start LiteLLM Proxy Server (LiteLLM Gateway)

>NOTE: `host` and `port` values must correspond to the values configured in the `.env` file

```
$ uv run litellm --config ./config.yaml --host localhost --port 4000
INFO:     Started server process [1141441]
INFO:     Waiting for application startup.

#------------------------------------------------------------#
#                                                            #
#           'I get frustrated when the product...'            #
#        https://github.com/BerriAI/litellm/issues/new        #
#                                                            #
#------------------------------------------------------------#

 Thank you for using LiteLLM! - Krrish & Ishaan

Give Feedback / Get Help: https://github.com/BerriAI/litellm/issues/new

LiteLLM: Proxy initialized with Config, Set models:
    llama3.2:3b-instruct-q8_0
    qwen2.5-coder:32b-instruct-q8_0
    gemini-2.0-flash-lite-preview-02-05:free
INFO:     Application startup complete.
INFO:     Uvicorn running on http://localhost:4000 (Press CTRL+C to quit)
```

## Uncomment the desired model in trhe `.env` file and execute the relevant Python programs **in a separate terminal/command window**:

`uv run python <python_program_name.py>`

>Using local Ollama model

```
$ grep LITELLM_PROXY_MODEL_NAME .env | grep -v "#"
LITELLM_PROXY_MODEL_NAME="llama3.2:3b-instruct-q8_0"
$
$ uv run python litellm_proxy_example_usage_non_streaming.py
...
$
$ uv run python litellm_proxy_example_usage_streaming.py
...
$
```

>Using LLM model available through OpenRouter

```
$ grep LITELLM_PROXY_MODEL_NAME .env | grep -v "#"
LITELLM_PROXY_MODEL_NAME="gemini-2.0-flash-lite-preview-02-05:free"
$
$ uv run python litellm_proxy_example_usage_non_streaming.py
...
$ uv run python litellm_proxy_example_usage_streaming.py
...
$
```

## Basic PytdanticAI Agent demonstration using Ollama and OpenRouter

```
$ uv run python ollama_example.py
city='London' country='United Kingdom'
Usage(requests=1, request_tokens=176, response_tokens=24, total_tokens=200, details=None)
$
$ uv run python openrouter_example.py
city='London' country='UK'
Usage(requests=1, request_tokens=64, response_tokens=20, total_tokens=84, details=None)
$
```
