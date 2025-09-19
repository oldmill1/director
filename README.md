# Producer

A Python package for automating terminal applications and creating coding videos on macOS.

## Features

- **Scene-based automation** with organized parts
- **Smart window management** with automatic app starting
- **Dynamic window positioning** that works on any screen size
- **Modular app architecture** ready for expansion
- **Clean YAML scripting** with intuitive action names

## Installation

Install in development mode:

```bash
pip install -e .
```

## Usage

Run automation scripts:

```bash
producer scripts/hello_world.yml
```

## Script Format

Producer uses YAML files with scenes and parts:

```yaml
name: "My Automation Script"
description: "A demo of Producer capabilities"

scenes:
  - name: "Setup"
    app: "iTerm"
    parts:
      - action: "sleep"
        duration: 0.5
      - action: "write"
        text: "echo 'Hello World!'"

  - name: "Position Demo"
    app: "iTerm"
    parts:
      - action: "position"
        text: "center center"
      - action: "sleep"
        duration: 1.0
      - action: "position"
        text: "top left"

  - name: "Cleanup"
    app: "iTerm"
    parts:
      - action: "write"
        text: "echo 'Done!'"
      - action: "close"
```

## Available Actions

- **`write`** - Type text into the terminal
- **`sleep`** - Pause execution for specified duration
- **`position`** - Move window to specified location
  - `"center center"`, `"top left"`, `"top right"`, `"bottom left"`, `"bottom right"`
  - Or custom coordinates: `"100 200"`
- **`close`** - Close current window (like Cmd+W)
- **`quit`** - Quit entire application (like Cmd+Q)

## Architecture

Producer uses a modular app system:

- **BaseApp** - Abstract base class for all applications
- **TerminalApp** - Handles iTerm2 automation
- **AppRegistry** - Manages different application types
- **ProducerAutomator** - Main automation engine

## Development

This package provides automation tools for terminal applications using AppleScript, specifically designed for macOS environments.

## License

MIT License
