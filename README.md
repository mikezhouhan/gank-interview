# 客户端官网与支付订阅项目

本项目包含一个客户端产品的官网和支付订阅功能，使用 React (Vite) 作为前端，FastAPI (Python) 作为后端，并采用 Monorepo 结构进行管理。

## 项目结构

```
/
├── .gitignore
├── README.md
├── PROJECT_PLAN.md  # 项目规划详情
├── frontend/        # React 前端项目
└── backend/         # FastAPI 后端项目
```

## 环境要求

*   Node.js (推荐 LTS 版本) 和 npm
*   Python 3.8+ 和 Poetry

## 快速开始

### 1. 克隆仓库 (如果尚未克隆)

```bash
git clone <your-repository-url>
cd <repository-name>
```

### 2. 前端 (Frontend - React)

**安装依赖:**

```bash
cd frontend
npm install
```

**启动开发服务器:**

```bash
npm run dev
```

前端应用默认运行在 `http://localhost:5173` (或 Vite 指定的其他端口)。

### 3. 后端 (Backend - FastAPI)

**安装依赖:**

确保你已经安装了 [Poetry](https://python-poetry.org/docs/#installation)。

```bash
cd backend
poetry install
```

**启动开发服务器:**

```bash
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

后端 API 默认运行在 `http://localhost:8000`。

*   `--reload`: 代码更改时自动重启服务器。
*   `--host 0.0.0.0`: 允许从本地网络访问 (如果需要)。

**API 文档:**

服务器运行后，可以在以下地址访问自动生成的 API 文档：

*   Swagger UI: `http://localhost:8000/docs`
*   ReDoc: `http://localhost:8000/redoc`

## 后续开发

请参考 `PROJECT_PLAN.md` 文件了解详细的技术选型、目录结构解释和后续开发步骤。