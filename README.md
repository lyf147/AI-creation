# 🎮 AI Game Testing Agent

一个基于 Playwright 的 AI 游戏测试 Agent，能够自动探索网页游戏、执行操作、检测异常并生成测试报告。

---

## 🚀 项目简介

本项目实现了一个自动化游戏测试系统，通过模拟用户行为（点击、输入、滚动），对网页游戏进行随机探索测试，并在测试过程中：

* 自动执行操作路径
* 实时检测页面异常（崩溃 / 错误信息）
* 记录操作日志
* 自动截图
* 生成测试报告

该 Agent 可用于替代重复性人工测试，提高测试效率并发现潜在 UI/逻辑问题。

---

## 🧠 核心能力

* 🎯 自动化测试：模拟真实用户操作
* 🔍 异常检测：识别页面错误与崩溃
* 📸 全流程记录：每一步自动截图
* 📊 报告生成：输出结构化测试日志
* ⚙️ 可扩展 Agent 架构：支持接入 LLM（GPT/Claude）

---

## 🏗️ 项目结构

```bash
ai_game_tester/
├── main.py          # 程序入口
├── agent.py         # 核心 Agent 控制逻辑
├── actions.py       # 操作策略（点击/输入/滚动）
├── detector.py      # 异常检测模块
├── reporter.py      # 报告生成
├── requirements.txt
└── screenshots/     # 自动生成截图
```

---

## ⚡ 快速开始

### 1️⃣ 安装依赖

```bash
pip install -r requirements.txt
playwright install
```

---

### 2️⃣ 修改测试地址

打开 `main.py`：

```python
GAME_URL = "https://orteil.dashnet.org/cookieclicker/"
```

---

### 3️⃣ 运行项目

```bash
python main.py
```

---

## 🎮 运行效果

运行后系统将：

* 自动打开浏览器
* 执行随机操作（点击 / 输入 / 滚动）
* 记录测试过程
* 自动截图

生成内容：

* `screenshots/` 👉 每一步截图
* `report.json` 👉 测试日志

---

## 📊 示例输出

```json
{
  "step": 12,
  "action": {"action": "click"},
  "issues": [],
  "screenshot": "screenshots/step_12.png"
}
```

---

## 🔍 异常检测能力

当前支持：

* 页面错误文本检测（error）
* 页面崩溃检测（JS 执行失败）

可扩展：

* UI 状态异常识别
* 网络请求失败检测
* 性能问题检测

---

## 🚀 未来优化方向

* 🤖 接入 LLM，实现智能决策（非随机操作）
* 🧠 多 Agent 协作（Planner / Executor / Critic）
* 👁️ 视觉识别（按钮 / UI 元素理解）
* 📈 自动生成 Bug 分析报告
* 🔁 强化学习优化测试路径

---

## 📈 项目价值

* 提升测试效率（减少人工重复操作）
* 自动探索未知路径
* 提高 Bug 覆盖率
* 支持大规模自动化测试

---

## 🧑‍💻 适用场景

* Web 游戏测试
* 前端自动化测试
* UI 回归测试
* AI Agent 实验项目

---

## 📄 License

MIT License
