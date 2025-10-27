# Test Generator Plugin

A Claude Code plugin agent specialized in automatically generating high-quality test cases.

## Features

- 🎯 **Intelligent Analysis**: Automatically identifies code changes and new features
- 📝 **Auto Generation**: Generates corresponding test cases for modified code
- 🔧 **Framework Adaptation**: Supports multiple testing frameworks (Jest, pytest, RSpec, etc.)
- ✅ **Best Practices**: Follows testing best practices and AAA pattern
- 🚀 **Proactive Triggering**: Automatically suggests generating tests after code changes

## Usage

### Automatic Invocation

After you modify code or create new features, Claude Code will automatically suggest using the test-generator agent:

```
> I've added a new user authentication function
// Claude will automatically identify and may invoke test-generator
```

### Explicit Invocation

You can also explicitly request to use the test-generator agent:

```
> Use the test-generator agent to create tests for my recent changes
> Ask test-generator to add tests for the payment module
> Have test-generator generate tests for the user service
```

### View via /agents Command

```bash
/agents
```

You can see the test-generator agent and its configuration in the interactive interface.

## Supported Testing Frameworks

### JavaScript/TypeScript
- **Unit Testing**: Jest, Vitest, Mocha + Chai
- **Component Testing**: React Testing Library, Vue Test Utils
- **E2E Testing**: Cypress, Playwright
- **Mocking**: jest.mock, sinon

### Python
- **Unit Testing**: pytest, unittest
- **Mocking**: pytest-mock, unittest.mock
- **Property Testing**: hypothesis
- **Web Testing**: pytest-django, pytest-flask

### Ruby
- **Unit Testing**: RSpec, Minitest
- **Mocking**: RSpec Mocks, Mocha
- **Web Testing**: Capybara (Rails integration tests)
- **Factory Pattern**: FactoryBot

The agent automatically identifies testing frameworks based on project dependency files (package.json, requirements.txt, Gemfile).

## Test Generation Examples

### JavaScript/TypeScript Example

Suppose you added the following function:

```javascript
function validateEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}
```

Test Generator would generate tests like this:

```javascript
describe('validateEmail', () => {
  it('should return true for valid email addresses', () => {
    expect(validateEmail('user@example.com')).toBe(true);
    expect(validateEmail('test.user@company.co.uk')).toBe(true);
  });

  it('should return false for invalid email addresses', () => {
    expect(validateEmail('invalid')).toBe(false);
    expect(validateEmail('@example.com')).toBe(false);
    expect(validateEmail('user@')).toBe(false);
    expect(validateEmail('user @example.com')).toBe(false);
  });

  it('should handle edge cases', () => {
    expect(validateEmail('')).toBe(false);
    expect(validateEmail(null)).toBe(false);
    expect(validateEmail(undefined)).toBe(false);
  });
});
```

### Python Example

Suppose you added the following function:

```python
def calculate_discount(price: float, discount_rate: float) -> float:
    if discount_rate < 0 or discount_rate > 1:
        raise ValueError("Discount rate must be between 0 and 1")
    return price * (1 - discount_rate)
```

Test Generator would generate:

```python
import pytest
from your_module import calculate_discount

class TestCalculateDiscount:
    def test_normal_discount(self):
        assert calculate_discount(100, 0.1) == 90.0
        assert calculate_discount(50, 0.5) == 25.0

    def test_boundary_values(self):
        assert calculate_discount(100, 0) == 100.0
        assert calculate_discount(100, 1) == 0.0

    def test_invalid_discount_rate(self):
        with pytest.raises(ValueError, match="between 0 and 1"):
            calculate_discount(100, -0.1)

        with pytest.raises(ValueError, match="between 0 and 1"):
            calculate_discount(100, 1.5)

    def test_decimal_precision(self):
        result = calculate_discount(99.99, 0.15)
        assert abs(result - 84.9915) < 0.001
```

### Ruby Example

Suppose you added the following class:

```ruby
class UserValidator
  def self.valid_username?(username)
    return false if username.nil? || username.empty?
    username.length >= 3 && username.length <= 20 && username.match?(/^[a-zA-Z0-9_]+$/)
  end
end
```

Test Generator would generate:

```ruby
require 'rspec'
require_relative '../lib/user_validator'

RSpec.describe UserValidator do
  describe '.valid_username?' do
    context 'with valid usernames' do
      it 'returns true for alphanumeric usernames' do
        expect(UserValidator.valid_username?('john_doe')).to be true
        expect(UserValidator.valid_username?('user123')).to be true
      end

      it 'returns true for usernames at boundary lengths' do
        expect(UserValidator.valid_username?('abc')).to be true
        expect(UserValidator.valid_username?('a' * 20)).to be true
      end
    end

    context 'with invalid usernames' do
      it 'returns false for usernames that are too short' do
        expect(UserValidator.valid_username?('ab')).to be false
      end

      it 'returns false for usernames that are too long' do
        expect(UserValidator.valid_username?('a' * 21)).to be false
      end

      it 'returns false for usernames with special characters' do
        expect(UserValidator.valid_username?('user@name')).to be false
        expect(UserValidator.valid_username?('user-name')).to be false
      end

      it 'returns false for nil or empty usernames' do
        expect(UserValidator.valid_username?(nil)).to be false
        expect(UserValidator.valid_username?('')).to be false
      end
    end
  end
end
```

## Configuration

### Agent Configuration

The Test Generator agent is configured in `agents/test-generator.md`, where you can customize:

- **name**: Agent name
- **description**: Description of when to invoke this agent
- **tools**: List of tools the agent can use
- **model**: AI model to use (defaults to inheriting from main conversation's model)

### Tool Permissions

Currently configured tools:
- `Read`: Read code files
- `Write`: Create test files
- `Grep`: Search for existing tests
- `Glob`: Find project files
- `Bash`: Run test commands

## Best Practices

1. **Generate Tests Promptly**: Generate tests immediately after completing feature development
2. **Review Generated Tests**: Although the agent generates high-quality tests, human review is still recommended
3. **Run Tests**: Run tests immediately after generation to ensure they pass
4. **Progressive Improvement**: Generate basic tests first, then supplement edge cases as needed
5. **Keep Tests Updated**: Update corresponding tests when code changes

## How It Works

1. Analyze code changes (using git diff or file comparison)
2. Identify functions, classes, or modules that need testing
3. Check the testing framework used by the project
4. Generate test scenarios based on code logic
5. Create test files (following project's test directory structure)
6. Verify tests can run

## Troubleshooting

### Agent Not Auto-Triggering

Ensure the description includes the "PROACTIVELY" keyword, or explicitly request:
```
> Use test-generator to create tests
```

### Generated Tests Don't Match Project Standards

You can edit `agents/test-generator.md` to customize the agent's behavior and add project-specific guidance.

### Testing Framework Not Recognized

Ensure your project's package.json, requirements.txt, or other dependency files include the testing framework dependency.

## Contributing

Improvements to this plugin are welcome! You can:
- Add support for more testing frameworks
- Improve test generation quality
- Optimize the agent's system prompt
- Provide feedback and suggestions

## License

MIT
