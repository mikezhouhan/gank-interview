# 项目计划：客户端官网 + 支付订阅功能

## 1. 项目目标

为客户端产品设计并开发一个包含官网页面和支付订阅功能的 Web 应用。采用 Monorepo 方式管理前后端代码。

## 2. 技术栈

*   **前端**: React (使用 Vite 构建), TypeScript, React Router, Axios (或 Fetch API), Zustand (或 Redux Toolkit)
*   **后端**: FastAPI (Python), Poetry (依赖管理), Pydantic, Uvicorn, JWT (认证), 支付宝/微信支付 SDK
*   **数据库**: (可选，根据后续需求决定) PostgreSQL / MySQL / MongoDB (配合 SQLAlchemy 或其他 ORM)
*   **代码管理**: Git

## 3. Monorepo 目录结构

```
/
├── .git/
├── .gitignore
├── README.md
├── frontend/           # React 前端项目 (Vite)
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── contexts/     # (可选)
│   │   ├── hooks/        # (可选)
│   │   ├── layouts/
│   │   ├── pages/        # 基础页面 (后续添加具体页面)
│   │   ├── routes/
│   │   ├── services/     # API 请求封装
│   │   ├── styles/
│   │   ├── types/
│   │   └── main.tsx
│   ├── index.html
│   ├── package.json
│   ├── tsconfig.json
│   └── vite.config.ts
└── backend/            # FastAPI 后端项目 (Poetry)
    ├── app/
    │   ├── api/
    │   │   └── v1/
    │   │       ├── __init__.py
    │   │       ├── endpoints/ # 基础端点 (后续添加具体业务)
    │   │       │   └── __init__.py
    │   │       └── router.py
    │   ├── core/
    │   │   ├── __init__.py
    │   │   ├── config.py
    │   │   └── security.py # (后续添加)
    │   ├── db/         # (可选)
    │   ├── models/     # Pydantic 模型 (内部)
    │   ├── schemas/    # Pydantic Schemas (API)
    │   ├── services/   # 业务逻辑 (后续添加)
    │   ├── __init__.py
    │   └── main.py     # FastAPI 应用入口
    ├── tests/
    ├── .env            # (需加入 .gitignore)
    ├── .gitignore
    ├── poetry.lock
    └── pyproject.toml
```

**Mermaid 图示:**

```mermaid
graph TD
    A[项目根目录] --> B(frontend);
    A --> C(backend);
    A --> D(README.md);
    A --> E(.gitignore);

    B --> B1(src);
    B --> B3(package.json);
    B --> B4(vite.config.ts);

    C --> C1(app);
    C --> C3(pyproject.toml);

    subgraph 前端 (React + Vite)
        B
    end

    subgraph 后端 (FastAPI + Poetry)
        C
    end
```

## 4. 基础框架搭建步骤

1.  **初始化 Git 仓库**: `git init`
2.  **创建 `.gitignore`**: 添加 `node_modules`, `dist`, `__pycache__`, `.env`, `*.pyc` 等。
3.  **创建前端项目 (Vite)**:
    *   `npm create vite@latest frontend --template react-ts`
    *   `cd frontend`
    *   `npm install react-router-dom axios zustand` (或其他所需基础库)
    *   创建 `src` 下的基础目录结构。
4.  **创建后端项目 (Poetry)**:
    *   `poetry new backend`
    *   `cd backend`
    *   `poetry add fastapi uvicorn[standard] python-dotenv` (以及后续所需库如 `python-jose`, `passlib`, 支付 SDK 等)
    *   创建 `app` 下的基础目录结构。
    *   在 `app/main.py` 中初始化 FastAPI 应用，配置 CORS。
5.  **编写根目录 `README.md`**: 说明项目结构、安装和启动步骤。

## 5. 后续步骤

*   实现前端基础路由和页面布局。
*   实现后端基础 API 端点（如健康检查）。
*   逐步实现用户认证、支付集成、用户中心等具体功能。
*   根据需要添加数据库模型和交互。

---
*此计划由 Architect Mode 生成*