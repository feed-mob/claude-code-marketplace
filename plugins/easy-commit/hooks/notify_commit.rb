#!/usr/bin/env ruby
require 'json'
require 'open3'

def send_macos_notification(title, message)
  begin
    # Use osascript to display a macOS notification
    Open3.popen3('osascript', '-e', %(display notification "#{message}" with title "#{title}")) do |_stdin, _stdout, _stderr, _wait_thr|
      # Best-effort, ignore output/errors
    end
  rescue StandardError
    # Ignore failures
  end
end

def main
  input = nil
  begin
    # Try to read JSON from stdin
    stdin_data = STDIN.read
    if stdin_data && !stdin_data.strip.empty?
      input = JSON.parse(stdin_data)
    end
  rescue JSON::ParserError
    # Continue without JSON input
  end

  # If we have JSON input, check for git commit
  if input
    tool_name = input.fetch('tool_name', '')
    tool_input = input.fetch('tool_input', {}) || {}

    # Only process Bash tool calls
    return 0 unless tool_name == 'Bash'

    command = tool_input['command'] || tool_input['cmd'] || tool_input['bash'] || ''

    # Detect git commit in the executed bash command (PostToolUse implies success)
    if command =~ /\bgit\s+commit\b/
      project_dir = ENV['CLAUDE_PROJECT_DIR'] || ''
      title = 'Easy Commit'
      message = project_dir.empty? ? 'Commit completed successfully' : "Commit completed in #{project_dir}"

      send_macos_notification(title, message)
      puts '[easy-commit] Commit detected: notification sent.'
    end
  else
    # Fallback: Try to detect git commit from environment or recent history
    # This is a best-effort approach when JSON input is not available
    project_dir = ENV['CLAUDE_PROJECT_DIR'] || Dir.pwd

    # Check if we're in a git repo and there was a recent commit
    if File.exist?(File.join(project_dir, '.git'))
      title = 'Easy Commit'
      message = project_dir.empty? ? 'Commit completed successfully' : "Commit completed in #{File.basename(project_dir)}"

      send_macos_notification(title, message)
      puts '[easy-commit] Fallback: notification sent based on git repository detection.'
    end
  end

  0
end

exit(main)
