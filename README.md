# FeedMob Claude Code Plugin Marketplace

A curated collection of Claude Code plugins designed to enhance development workflows and productivity. This marketplace provides specialized tools, agents, and skills that integrate seamlessly with Claude Code's plugin system.

## 🚀 Available Plugins

### 📊 CSV URL Parser
**Type**: Agent Skill
**Description**: Automatically parses URLs in CSV files and extracts query parameters as new columns.

**Features**:
- 🎯 Automatic URL detection in CSV files
- 📊 Dynamic parameter extraction and column creation
- ✅ Data preservation with new parameter columns
- 🚀 Batch processing for multiple files

**Use Cases**:
- Marketing campaign analysis
- URL parameter tracking
- Data enrichment from web analytics
- E-commerce link analysis

[View Plugin Details →](plugins/csv-url-parser/README.md)

### 🧪 Test Generator
**Type**: Agent
**Description**: Automatically generates high-quality test cases for code changes and new features.

**Features**:
- 🎯 Intelligent code analysis and change detection
- 📝 Multi-framework test generation (Jest, pytest, RSpec, etc.)
- ✅ Best practices and AAA pattern compliance
- 🚀 Proactive triggering after code changes

**Supported Frameworks**:
- **JavaScript/TypeScript**: Jest, Vitest, Mocha, React Testing Library
- **Python**: pytest, unittest, hypothesis
- **Ruby**: RSpec, Minitest, FactoryBot

[View Plugin Details →](plugins/test-generator/README.md)

### 💾 Easy Commit
**Type**: Command
**Description**: Streamlined git commit creation with intelligent change analysis.

**Features**:
- 🔍 Automatic git status and diff analysis
- 📝 Context-aware commit message generation
- ⚡ Single-command staging and commit
- 🎯 Focused on current changes only

[View Plugin Details →](plugins/easy-commit/commands/smart-commit.md)

## 📋 Plugin Types

This marketplace includes different types of Claude Code plugins:

### 🤖 Agents
Specialized subagents that Claude can invoke automatically based on context:
- **Test Generator**: Automatically creates test cases for code changes
- **CSV URL Parser**: Processes CSV files with URL data

### 🛠️ Skills
Model-invoked capabilities that extend Claude's functionality:
- **CSV URL Parser Skill**: Extracts URL parameters from CSV data

### ⚡ Commands
Custom slash commands for specific workflows:
- **Smart Commit**: Intelligent git commit creation

## 🚀 Quick Start

### Installation

1. **Clone the marketplace**:
   ```bash
   git clone https://github.com/feedmob/claude-code-marketplace.git
   cd claude-code-marketplace
   ```

2. **Install individual plugins**:
   Each plugin can be installed independently by copying the plugin directory to your Claude Code plugins folder.

3. **Plugin Structure**:
   ```
   your-claude-plugins/
   ├── csv-url-parser/
   │   ├── .claude-plugin/
   │   │   └── plugin.json
   │   ├── skills/
   │   └── README.md
   ├── test-generator/
   │   ├── .claude-plugin/
   │   │   └── plugin.json
   │   ├── agents/
   │   └── README.md
   └── easy-commit/
       ├── .claude-plugin/
       │   └── plugin.json
       ├── commands/
       └── README.md
   ```

### Usage

Once installed, plugins are automatically available in Claude Code:

- **Agents**: Use `/agents` to see available agents or let Claude invoke them automatically
- **Skills**: Mention relevant keywords to trigger skills automatically
- **Commands**: Use slash commands like `/smart-commit` for specific actions

## 🔧 Plugin Development

### Creating New Plugins

Follow the [Claude Code Plugin Reference](https://docs.claude.com/en/docs/claude-code/plugins-reference) for complete development guidelines.

#### Basic Plugin Structure

```bash
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Required: Plugin manifest
├── commands/                # Optional: Slash commands
│   └── my-command.md
├── agents/                  # Optional: Subagents
│   └── my-agent.md
├── skills/                  # Optional: Agent Skills
│   └── my-skill/
│       └── SKILL.md
├── hooks/                   # Optional: Event handlers
│   └── hooks.json
├── .mcp.json               # Optional: MCP servers
├── scripts/                # Optional: Supporting scripts
└── README.md               # Plugin documentation
```

#### Plugin Manifest Example

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "Brief plugin description",
  "author": {
    "name": "Your Name",
    "email": "your@email.com"
  },
  "repository": "https://github.com/your-org/my-plugin",
  "license": "MIT",
  "keywords": ["keyword1", "keyword2"]
}
```

### Contributing

We welcome contributions to this marketplace! Here's how to contribute:

1. **Fork the repository**
2. **Create a new plugin** following the structure above
3. **Add comprehensive documentation** in the plugin's README.md
4. **Test your plugin** thoroughly
5. **Submit a pull request** with your plugin

#### Contribution Guidelines

- Follow the [Claude Code Plugin Reference](https://docs.claude.com/en/docs/claude-code/plugins-reference)
- Include comprehensive documentation
- Test plugins before submission
- Use semantic versioning
- Include appropriate license information

## 📚 Documentation

- [Claude Code Plugin Reference](https://docs.claude.com/en/docs/claude-code/plugins-reference)
- [Plugin Commands Guide](https://docs.claude.com/en/docs/claude-code/slash-commands)
- [Agent Skills Overview](https://docs.claude.com/en/docs/claude-code/skills)
- [Subagents Documentation](https://docs.claude.com/en/docs/claude-code/sub-agents)

## 🏢 About FeedMob

FeedMob is committed to enhancing developer productivity through innovative tools and integrations. This plugin marketplace represents our ongoing effort to provide valuable extensions for the Claude Code ecosystem.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/feedmob/claude-code-marketplace/issues)
- **Discussions**: Join community discussions in [GitHub Discussions](https://github.com/feedmob/claude-code-marketplace/discussions)
- **Documentation**: Check individual plugin README files for specific usage instructions

---

**Made with ❤️ by the FeedMob team**
