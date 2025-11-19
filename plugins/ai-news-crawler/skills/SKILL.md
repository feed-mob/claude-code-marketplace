---
name: AI新闻爬取器
description: 触发词"去吧小飞机"；仅在当前目录创建时间命名的.json，抓取按时间降序的10条AI相关新闻并输出中文概要
---

# 目的
从多个网站抓取最新AI相关新闻，合并去重并按时间降序选取10条，摘要统一为中文，写入JSON文件。

# 何时触发
当请求包含"去吧小飞机"。

# 输入
- optional keywords?: 主题关键词（可选）
- optional time_window?: 时间窗口（默认144h）

# 输出
- news_json_file_only

# 约束
- 仅创建一个文件：`<YYYYMMDD_HHMMSS>.json`，位置为当前工作目录；不在对话中输出任何文本或路径。
- 每条记录字段：`title`、`source`、`url`、`published_at`(ISO8601)、`summary_zh`、`language`(`zh`/`en`/`mixed`)。
- 数量固定为10条，按`published_at`降序；严格去重（以`url`与`title`作为键）。
- 英文内容的摘要必须为中文；保留原文语言标识于`language`。
- 避免抓取付费墙与需登录的页面；不包含广告与软文；不写入敏感信息或密钥。
- 若缺失发布时间，使用页面显式时间；无法获取时剔除该条或标注`published_at: null`并降权，不猜测。

# 源站候选
- The Verge / AI标签
- TechCrunch / AI标签
- 量子位 / AI栏目
- 36氪 / 人工智能标签
- 官方公告 / Anthropic、Google AI Blog（选最新公告）

# 步骤
1 确定`time_window`与`keywords`（若提供）。
2 遍历源站候选，抓取最近内容列表，解析`title/url/published_at`与正文摘要。
3 将英文摘要压缩并翻译为中文，保持中立与信息密度。
4 归一化时间为ISO8601，合并列表并按`url/title`去重。
5 按`published_at`降序排序，选取前10条；写入`<YYYYMMDD_HHMMSS>.json`为JSON数组。
6 不在对话中输出任何文本；仅创建文件。

# 输出示例（结构）
```json
[
  {
    "title": "示例标题",
    "source": "TechCrunch",
    "url": "https://example.com/news/123",
    "published_at": "2025-11-16T08:30:00Z",
    "summary_zh": "用中文概括要点，80-150字，覆盖背景、事件与影响。",
    "language": "en"
  }
]
