<!-- 5cbf4a36-380f-4e38-9fab-09db49eff381 53ddcdaf-31f4-47ad-ade6-31a91c5dd4db -->
# 创建 PPT 制作 Skill

## 目标

创建一个名为 `ppt-generator` 的 Skill，使用 Python-pptx 库来生成 PowerPoint 演示文稿，支持基础功能如创建幻灯片、添加文本和图片。

## 文件结构

```
plugins/ppt-generator/
├── README.md                    # 插件文档
└── skills/
    ├── SKILL.md                 # Skill 核心文件（YAML frontmatter + 说明）
    ├── EXAMPLES.md              # 使用示例
    └── scripts/
        └── create_ppt.py        # Python 脚本（使用 python-pptx）
```

## 实现步骤

### 1. 创建目录结构

- 创建 `plugins/ppt-generator/` 目录
- 创建 `plugins/ppt-generator/skills/` 目录
- 创建 `plugins/ppt-generator/skills/scripts/` 目录

### 2. 创建 SKILL.md

- YAML frontmatter：
  - `name`: ppt-generator
  - `description`: 创建和编辑 PowerPoint 演示文稿。当需要生成 PPT、创建幻灯片、添加文本或图片到演示文稿时使用。
  - `allowed-tools`: Read, Write, Bash
  - `dependencies`: python-pptx>=0.6.21
- Markdown 正文：
  - 概述和用途说明
  - 功能列表（创建幻灯片、添加文本、添加图片、设置标题等）
  - 使用说明和调用方式
  - 脚本使用方法

### 3. 创建 create_ppt.py 脚本

- 使用 python-pptx 库
- 支持功能：
  - 创建新的 PPT 文件
  - 添加幻灯片（标题页、内容页）
  - 添加文本内容（标题、正文）
  - 添加图片
  - 设置幻灯片布局
- 命令行参数支持（文件路径、内容等）
- 错误处理和用户友好的输出

### 4. 创建 EXAMPLES.md

- 展示常见使用场景
- 示例命令和输出
- 不同场景的用法说明

### 5. 创建 README.md

- 插件介绍和特性
- 安装说明
- 使用方法和示例
- 依赖要求

### 6. 更新主 README.md

- 在主 README 的插件列表中添加 ppt-generator
- 添加插件描述和链接

## 技术细节

### Python 脚本设计

- 使用 argparse 处理命令行参数
- 支持 JSON 或 YAML 输入格式定义幻灯片内容
- 或者支持简单的命令行参数创建基础 PPT
- 输出清晰的错误信息和进度反馈

### Skill 触发条件

- 关键词：PPT、PowerPoint、演示文稿、幻灯片、presentation
- 明确的使用场景描述

## 参考文件

- `plugins/csv-url-parser/skills/SKILL.md` - Skill 结构参考
- `plugins/csv-url-parser/skills/scripts/process_csv.rb` - 脚本实现参考
- Claude Skills 文档规范

### To-dos

- [ ] 创建 ppt-generator 插件的目录结构（plugins/ppt-generator/skills/scripts/）
- [ ] 创建 SKILL.md 文件，包含 YAML frontmatter 和详细的功能说明
- [ ] 创建 create_ppt.py 脚本，实现基于 python-pptx 的 PPT 生成功能
- [ ] 创建 EXAMPLES.md 文件，提供使用示例和场景说明
- [ ] 创建插件 README.md 文档
- [ ] 更新主 README.md，添加 ppt-generator 插件信息