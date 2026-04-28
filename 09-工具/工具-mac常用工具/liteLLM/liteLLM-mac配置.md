---
aliases: []
tags: []
description:
type:
ref-url:
create-date: 2026-04-26 18:48
---

# LiteLLM Mac 配置要点

> [!summary]
> 推荐把 LiteLLM 作为本机统一大模型网关：LiteLLM 监听 `http://localhost:4000`，Claude Code 走 Anthropic-compatible [[endpoint]]，Aider / OpenCode / 其他 OpenAI SDK 工具走 OpenAI-compatible endpoint。

## 推荐结构

```text
agent 编程工具
├─ Claude Code  -> http://localhost:4000        # Anthropic Messages API
├─ Aider        -> http://localhost:4000/v1     # OpenAI-compatible API
└─ OpenCode     -> http://localhost:4000/v1     # OpenAI-compatible API

LiteLLM
└─ 上游模型供应商
   ├─ DeepSeek Anthropic endpoint
   └─ OpenAI-compatible 中转商
```

核心原则：

- LiteLLM 配置文件只写模型路由，不写真实 API Key。
- API Key 放在 `~/.litellm/.env`。
- Claude Code 和 OpenAI-compatible 工具要分开配置 endpoint。
- 每个模型先用最小请求验证，再接入 agent 工具。

## 文件位置

```text
~/.litellm/config.yaml              # LiteLLM 模型路由
~/.litellm/.env                     # API Key / master key
~/.litellm/start_proxy.sh           # 启动脚本
~/.claude/settings.json             # Claude Code 设置
~/.config/opencode/opencode.json    # OpenCode provider
~/.local/share/opencode/auth.json   # OpenCode provider key
```

## LiteLLM 配置要点

`~/.litellm/config.yaml` 示例：

```yaml
model_list:
  - model_name: deepseek-v4-pro
    litellm_params:
      model: anthropic/deepseek-v4-pro
      api_key: os.environ/DEEPSEEK_ANTHROPIC_API_KEY
      api_base: https://api.deepseek.com/anthropic

  - model_name: sonnet-4-6
    litellm_params:
      model: openai/claude-sonnet-4-6
      api_base: os.environ/OHMYGPT_API_BASE
      api_key: os.environ/OHMYGPT_API_KEY

litellm_settings:
  drop_params: true
  add_streaming_chunk_size: true

general_settings:
  master_key: os.environ/LITELLM_MASTER_KEY
  disable_ui_auth: true
```

`~/.litellm/.env` 示例：

```bash
LITELLM_MASTER_KEY='<local-master-key>'
OHMYGPT_API_BASE='https://api.ohmygpt.com/v1'
OHMYGPT_API_KEY='...'
DEEPSEEK_ANTHROPIC_API_KEY='...'
```

注意：`.env` 权限建议设为 `600`。

```bash
chmod 600 ~/.litellm/.env
```

## 启动脚本

```bash
#!/usr/bin/env zsh
set -a
source "$HOME/.litellm/.env"
set +a
export LITELLM_LOCAL_MODEL_COST_MAP=true
export PATH="/Users/haoxc/Library/Application Support/uv/tools/litellm/bin:$PATH"
exec "/Users/haoxc/Library/Application Support/uv/tools/litellm/bin/litellm" \
  --config "$HOME/.litellm/config.yaml" \
  --host 127.0.0.1 \
  --port 4000 \
  --num_workers 4 \
  --use_prisma_db_push
```

推荐在 `~/.zshrc` 中封装：

```bash
function proxy-on() {
    if command -v docker >/dev/null 2>&1; then
        if docker ps -a --format '{{.Names}}' | grep -qx 'litellm-postgres'; then
            docker start litellm-postgres >/dev/null 2>&1 || true
        fi
    fi

    if lsof -iTCP:4000 -sTCP:LISTEN -P -n > /dev/null; then
        echo "LiteLLM Proxy already running on http://localhost:4000"
    else
        echo "Starting LiteLLM Proxy on http://localhost:4000 ..."
        nohup "$HOME/.litellm/start_proxy.sh" > "$HOME/.litellm/proxy.log" 2>&1 &
        disown
        sleep 8
        if lsof -iTCP:4000 -sTCP:LISTEN -P -n > /dev/null; then
            echo "LiteLLM Proxy is ready"
        else
            echo "LiteLLM Proxy failed to start. See ~/.litellm/proxy.log"
        fi
    fi
}

alias proxy-off='pkill -f "litellm --config" && echo "LiteLLM Proxy stopped"'
```

## Admin UI 数据库配置

LiteLLM Admin UI 登录不只需要 `LITELLM_MASTER_KEY`，还需要数据库。否则会出现：

```text
Authentication Error, Not connected to DB!
```

本机使用 Docker Postgres：

```bash
docker run -d \
  --name litellm-postgres \
  -e POSTGRES_USER=litellm \
  -e POSTGRES_PASSWORD="<db-password>" \
  -e POSTGRES_DB=litellm \
  -p 127.0.0.1:5432:5432 \
  -v litellm-postgres-data:/var/lib/postgresql/data \
  postgres:16-alpine
```

`.env` 需要包含：

```bash
DATABASE_URL='postgresql://litellm:<db-password>@127.0.0.1:5432/litellm'
LITELLM_SALT_KEY='<stable-random-salt>'
```

首次使用数据库版 LiteLLM 时，需要生成 Prisma client：

```bash
"/Users/haoxc/Library/Application Support/uv/tools/litellm/bin/python" -m prisma py fetch

source ~/.litellm/.env
export PATH="/Users/haoxc/Library/Application Support/uv/tools/litellm/bin:$PATH"
prisma generate --schema "/Users/haoxc/Library/Application Support/uv/tools/litellm/lib/python3.12/site-packages/litellm/proxy/schema.prisma"
```

Admin UI 登录：

```text
Username: admin
Password: LITELLM_MASTER_KEY 的值
```

## Claude Code 配置

Claude Code 使用 Anthropic Messages API，不是 OpenAI `/v1/chat/completions`。

`~/.claude/settings.json` 示例：

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://localhost:4000",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "deepseek-v4-pro",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "deepseek-v4-pro",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-flash"
  },
  "model": "deepseek-v4-pro",
  "apiKeyHelper": "/Users/haoxc/.litellm/claude_api_key_helper.sh"
}
```

`apiKeyHelper` 示例：

```bash
#!/usr/bin/env zsh
source "$HOME/.litellm/.env"
printf '%s' "$LITELLM_MASTER_KEY"
```

启动：

```bash
proxy-on
claude --model deepseek-v4-pro
```

## Aider 配置

Aider 走 OpenAI-compatible endpoint：

```bash
proxy-on
source ~/.litellm/.env
OPENAI_API_BASE="http://localhost:4000/v1" \
OPENAI_API_KEY="$LITELLM_MASTER_KEY" \
aider --model openai/sonnet-4-6
```

## OpenCode 配置

`~/.config/opencode/opencode.json` 示例：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "litellm/sonnet-4-6",
  "provider": {
    "litellm": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "LiteLLM Local Gateway",
      "options": {
        "baseURL": "http://localhost:4000/v1"
      },
      "models": {
        "sonnet-4-6": {
          "name": "Sonnet 4.6 via LiteLLM"
        },
        "deepseek-v4-pro": {
          "name": "DeepSeek V4 Pro via LiteLLM"
        }
      }
    }
  }
}
```

## 验证顺序

先验证 LiteLLM 本身：

```bash
source ~/.litellm/.env
curl -sS \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  http://127.0.0.1:4000/v1/models
```

再验证 OpenAI-compatible 路由：

```bash
curl -sS http://127.0.0.1:4000/v1/chat/completions \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonnet-4-6",
    "messages": [{"role": "user", "content": "Reply with only: OK"}],
    "max_tokens": 8
  }'
```

最后验证 Claude Code：

```bash
claude -p "Reply with only: OK" --model deepseek-v4-pro
```

## 易错点与误区

### 误区 1：把 Claude Code 当成 OpenAI-compatible 客户端

Claude Code 访问的是 Anthropic Messages API。它会请求类似 `/v1/messages` 的接口，不是 `/v1/chat/completions`。

因此：

- Claude Code 用 `ANTHROPIC_BASE_URL=http://localhost:4000`
- Aider / OpenCode 用 `http://localhost:4000/v1`

不要把 Claude Code 配成：

```bash
ANTHROPIC_BASE_URL=http://localhost:4000/v1
```

这类配置很容易造成路径错位。

### 误区 2：中转商的 base URL 少写 `/v1`

OpenAI-compatible 上游通常要求 base URL 包含 `/v1`。

例如：

```bash
OHMYGPT_API_BASE='https://api.ohmygpt.com/v1'
```

如果写成：

```bash
OHMYGPT_API_BASE='https://api.ohmygpt.com'
```

常见现象是 LiteLLM 本地 `/v1/models` 正常，但真实调用上游时报 `404 Not Found`。

### 误区 3：LiteLLM `/v1/models` 正常，不等于模型真实可用

`/v1/models` 只说明 LiteLLM 读到了本地 `model_list`。它不会证明：

- 上游 API Key 有效；
- 上游 base URL 正确；
- 上游支持该模型名；
- 当前协议适配正确。

必须再做一次最小真实调用，例如要求模型只返回 `OK`。

### 误区 4：同一个模型别名不能无脑给所有 agent 用

Claude Code 与 Aider/OpenCode 的协议不同。

实测中：

- Claude Code 走 `deepseek-v4-pro` 的 Anthropic-compatible 路由稳定。
- OpenAI-compatible 客户端可走 `sonnet-4-6`、`claude-haiku-4-5` 等路由。

如果把 OpenAI-compatible 的 Claude 模型直接给 Claude Code，可能触发上游 `400` 参数校验错误。

### 误区 5：后台启动命令看似成功，但进程已经退出

在非交互 shell 中直接：

```bash
litellm --config ~/.litellm/config.yaml --port 4000 &
```

可能出现“显示 ready，但 shell 退出后进程也没了”的情况。

更稳的写法：

```bash
nohup "$HOME/.litellm/start_proxy.sh" > "$HOME/.litellm/proxy.log" 2>&1 &
disown
```

然后用下面命令确认端口真的在监听：

```bash
lsof -iTCP:4000 -sTCP:LISTEN -P -n
```

### 误区 6：把真实 API Key 写进 `config.yaml` 或 shell 配置

不要在以下文件中明文写 provider key：

```text
~/.litellm/config.yaml
~/.zshrc
项目仓库里的 markdown / yaml / json
```

推荐：

- provider key 放 `~/.litellm/.env`
- `config.yaml` 使用 `os.environ/XXX`
- Claude Code 使用 `apiKeyHelper`
- OpenCode auth 放 `~/.local/share/opencode/auth.json`

### 误区 7：`ANTHROPIC_API_KEY` 和 `ANTHROPIC_AUTH_TOKEN` 混用

通过 LiteLLM 本地网关时，Claude Code 不需要上游 Anthropic 官方 key。

推荐做法：

- `ANTHROPIC_BASE_URL=http://localhost:4000`
- token 使用 LiteLLM 的 `LITELLM_MASTER_KEY`
- 用 `apiKeyHelper` 从 `~/.litellm/.env` 读取

避免在 shell 中残留旧变量：

```bash
unset ANTHROPIC_API_KEY ANTHROPIC_AUTH_TOKEN
```

### 误区 8：模型名写成“看起来像”的名字

LiteLLM 的 `model_name` 是本地别名，`litellm_params.model` 是上游实际模型名。两者可以不同，但必须明确区分。

例如：

```yaml
- model_name: sonnet-4-6
  litellm_params:
    model: openai/claude-sonnet-4-6
```

如果上游实际模型名写错，LiteLLM 不一定在启动时报错，通常会在真实请求时报 `400` 或 `404`。

## 当前推荐命令

```bash
proxy-on
claude --model deepseek-v4-pro
```

```bash
proxy-on
aider-litellm
```

```bash
proxy-on
opencode
```

> [!warning]
> 如果 `.zshrc` 曾经明文保存过 GitHub token 或模型 API Key，建议轮换这些 key。迁移到 `.env` 只能避免以后继续扩散，不能撤销已经暴露过的历史风险。
