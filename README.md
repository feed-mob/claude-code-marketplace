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

### 📊 PPT Generator
**Type**: Agent Skill
**Description**: Create and edit PowerPoint presentations using Python and python-pptx library.

**Features**:
- 🎯 Easy creation of PowerPoint presentations from simple commands
- 📊 Support for command-line and JSON-based slide definitions
- 🖼️ Image insertion with custom positioning
- 📝 Multiple slide types (title, content, blank)
- ✅ Standard .pptx format compatible with all major presentation software

**Use Cases**:
- Meeting presentations
- Project proposals
- Training materials
- Business reports
- Quick slide deck creation

[View Plugin Details →](plugins/ppt-generator/README.md)

## 📋 Plugin Types

This marketplace includes different types of Claude Code plugins:

### 🤖 Agents
Specialized subagents that Claude can invoke automatically based on context:
- **Test Generator**: Automatically creates test cases for code changes
- **CSV URL Parser**: Processes CSV files with URL data

### 🛠️ Skills
Model-invoked capabilities that extend Claude's functionality:
- **CSV URL Parser Skill**: Extracts URL parameters from CSV data
- **PPT Generator Skill**: Creates and edits PowerPoint presentations

### ⚡ Commands
Custom slash commands for specific workflows:
- **Smart Commit**: Intelligent git commit creation

## 🚀 Quick Start

### Installation

#### Method 1: Add as Marketplace (Recommended)

Add the entire FeedMob marketplace to Claude Code:

```bash
/plugin marketplace add git@github.com:feed-mob/claude-code-marketplace.git
```

Or using HTTPS:
```bash
/plugin marketplace add https://github.com/feed-mob/claude-code-marketplace.git
```

#### Method 2: Add Individual Plugins

You can also install individual plugins directly:

```bash
# Install CSV URL Parser
/plugin install csv-url-parser@feedmob-marketplace

# Install Test Generator
/plugin install test-generator@feedmob-marketplace

# Install Easy Commit
/plugin install easy-commit@feedmob-marketplace
```

#### Method 3: Browse and Install Interactively

1. **Add the marketplace**:
   ```bash
   /plugin marketplace add git@github.com:feed-mob/claude-code-marketplace.git
   ```

2. **Browse available plugins**:
   ```bash
   /plugin
   ```

3. **Install from the interactive interface**:
   Select the plugins you want to install from the marketplace.

### Verification

After adding the marketplace, verify the installation:

1. **List marketplaces**:
   ```bash
   /plugin marketplace list
   ```

2. **Check available plugins**:
   ```bash
   /plugin
   ```

3. **Test a plugin**:
   Try using one of the installed plugins to ensure everything works correctly.

### Plugin Structure

Once installed, plugins will be available in your Claude Code environment:

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

## 📦 Marketplace Configuration

This repository serves as a Claude Code plugin marketplace. To enable marketplace functionality, a `.claude-plugin/marketplace.json` file is required at the repository root.

### Marketplace Structure

The marketplace configuration follows the [Claude Code Plugin Marketplaces](https://docs.claude.com/en/docs/claude-code/plugin-marketplaces#add-and-use-marketplaces) specification:

```json
{
  "name": "feedmob-marketplace",
  "owner": {
    "name": "FeedMob Team",
    "email": "dev@feedmob.com"
  },
  "metadata": {
    "description": "FeedMob's curated collection of Claude Code plugins for enhanced development workflows",
    "version": "1.0.0"
  },
  "plugins": [
    {
      "name": "csv-url-parser",
      "source": "./plugins/csv-url-parser",
      "description": "Parse URLs in CSV files and extract query parameters as new columns",
      "version": "1.0.0",
      "author": {
        "name": "FeedMob Team"
      },
      "keywords": ["csv", "url", "parsing", "data-processing"],
      "category": "data-processing"
    },
    {
      "name": "test-generator",
      "source": "./plugins/test-generator",
      "description": "Automatically generate high-quality test cases for code changes",
      "version": "1.0.0",
      "author": {
        "name": "FeedMob Team"
      },
      "keywords": ["testing", "test-generation", "automation", "quality"],
      "category": "testing"
    },
    {
      "name": "easy-commit",
      "source": "./plugins/easy-commit",
      "description": "Streamlined git commit creation with intelligent change analysis",
      "version": "1.0.0",
      "author": {
        "name": "FeedMob Team"
      },
      "keywords": ["git", "commit", "workflow", "automation"],
      "category": "productivity"
    },
    {
      "name": "ppt-generator",
      "source": "./plugins/ppt-generator",
      "description": "Create and edit PowerPoint presentations using Python and python-pptx library",
      "version": "1.0.0",
      "author": {
        "name": "FeedMob Team"
      },
      "keywords": ["ppt", "powerpoint", "presentation", "slides", "office"],
      "category": "productivity"
    }
  ]
}
```

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

## 🔧 Troubleshooting

### Marketplace Installation Issues

#### Marketplace Not Loading
If you can't add the marketplace or see plugins from it:

1. **Verify repository access**:
   ```bash
   # Test SSH access
   ssh -T git@github.com

   # Or test HTTPS access
   curl -I https://github.com/feed-mob/claude-code-marketplace
   ```

2. **Check marketplace file exists**:
   Ensure `.claude-plugin/marketplace.json` exists in the repository root

3. **Validate JSON syntax**:
   ```bash
   claude plugin validate .
   ```

#### Plugin Installation Failures
If the marketplace appears but plugin installation fails:

1. **Check plugin sources**:
   Verify that plugin directories contain required files

2. **Test individual plugins**:
   Try installing plugins one by one to identify issues

3. **Check permissions**:
   Ensure you have access to the repository

### Common Commands

```bash
# List all marketplaces
/plugin marketplace list

# Update marketplace metadata
/plugin marketplace update feedmob-marketplace

# Remove marketplace
/plugin marketplace remove feedmob-marketplace

# List available plugins
/plugin

# Install specific plugin
/plugin install csv-url-parser@feedmob-marketplace
```

## 🤝 Support

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/feedmob/claude-code-marketplace/issues)
- **Discussions**: Join community discussions in [GitHub Discussions](https://github.com/feedmob/claude-code-marketplace/discussions)
- **Documentation**: Check individual plugin README files for specific usage instructions
- **Claude Code Docs**: [Plugin Marketplaces Reference](https://docs.claude.com/en/docs/claude-code/plugin-marketplaces#add-and-use-marketplaces)

---

**Made with ❤️ by the FeedMob team**
