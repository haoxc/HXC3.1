# 推进后端项目搭建 - 实施计划

根据您的要求推进后端的项目搭建，我已经完成了对 `twin-platform` 代码结构的梳理。目前后端基座（Spring Boot 3 + MyBatis Plus）的代码骨架已初步形成，但项目中的配置仍是默认值，并且缺失部分基础设施，无法直接成功启动连接到我们刚刚部署好的数据库。

为此，我制定了以下后端配置和启动的实施计划：

## User Review Required
	
> [!CAUTION]  
> 目前在项目根目录 `zs-datahub/docker-compose.yml` 下，仅启动了 PostgreSQL 和 MinIO 服务。然而 Spring Boot 启动强制依赖了 Redis 缓存和 EMQX (MQTT消息队列) 组件，没有它们后端服务会启动报错。**我计划补充这两个组件到根目录的由您统一管理的 `docker-compose.yml` 中，并沿用平台文档内定义的轻量级配置**。请确认此集成方案。

## Proposed Changes

### Infrastructure (基础设施层)

#### [MODIFY] [docker-compose.yml](file:///Users/haoxc/Workspace-AntiGravity/zs-datahub/docker-compose.yml)
- **补充依赖服务**：根据 `twin-platform` 的需求，向根目录的 `docker-compose.yml` 追加 `redis` (缓存) 和 `emqx` (物联网数据接入通信) 两个必需的容器服务。

---

### Backend Configuration (后端配置层)

#### [NEW] [application-local.yml](file:///Users/haoxc/Workspace-AntiGravity/zs-datahub/twin-platform/src/main/resources/application-local.yml)
- **创建本地环境配置文件**：为了避免硬编码及直接修改主配置，新建一份 `local` 环境配置，用于适配刚刚成功创建好的各类中间件账号密码：
  - **Datasource**: 指向 `localhost:5432/twin_platform` (账号: `zsdatahub` / `zsdatahub_password`)
  - **MinIO**: 指向 `http://localhost:9000` (账号: `zsdatahub_admin` / `zsdatahub_minio_password`)
  - **Redis**: 指向本地 6379 端口，配置启动密码。
  - **MQTT**: 开启并指向本地 EMQX broker 服务。

---

### Backend Environment (环境构建)

#### [MODIFY] [pom.xml](file:///Users/haoxc/Workspace-AntiGravity/zs-datahub/twin-platform/pom.xml)
- 检查是否存在依赖冲突或未闭合的问题。由于项目已经结构化良好，我们会直接执行 `mvn clean install -DskipTests` 对框架底层实体类、Mapper、Controller 与配置层进行编译打包验证。

## Open Questions

> [!IMPORTANT]  
> 1. 原工程目前有一个并列存在的 `zs-datahub-backend/` 目录以及 `twin-platform/` 目录，通过评估发现 `twin-platform` 是主要完整的业务代码库。**确认之后所有的后端开发和运行都在 `twin-platform` 里完成**，后续可以废弃 `zs-datahub-backend`。
> 2. 当前 JDK 版本要求为 JDK 17，请确认您本机的默认 `java -version` 是否满足要求。

## Verification Plan

### Automated Tests
1. 执行更新基座环境命令 `docker compose up -d` 拉起 Redis 和 MQTT。
2. 运行 `mvn spring-boot:run -Dspring-boot.run.profiles=local`。

### Manual Verification
1. 观察控制台输出，期望看到：`数字孪生数据中台 v2.1.0 启动成功!` 且没有任何异常报错（表示数据库、缓存等全部连通）。
2. 调用 `/api/actuator/health` 端口，验证后端服务的健康指征（特别是 db 和 redis 连接状态应为 `UP`）。
