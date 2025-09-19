# Producer

A Python automation framework for creating coding videos on macOS. Still very much a work in progress!

## What It Does

Automates terminal applications (mainly iTerm2) to create scripted sequences for coding videos. Think of it as a way to programmatically control your terminal for video content.

## Current State

⚠️ **Things are still in flux** - the API might change, new features are being added, and the whole thing is pretty experimental right now.

## Installation

```bash
pip install -e .
```

## Usage

```bash
producer scripts/hello_world.yml
```

## Script Format (Current)

The YAML format is pretty clean now with scenes and parts:

```yaml
name: "My Script"
description: "What this does"

scenes:
  - name: "Setup"
    app: "iTerm"           # App for this scene
    parts:
      - action: "sleep"
        duration: 0.5
      - action: "write"
        text: "echo 'Hello!'"

  - name: "Demo"
    app: "iTerm"           # Same app = reuses window
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
      - action: "close"    # or "quit" to kill the whole app
```

## Available Actions

- **`write`** - Types text into the terminal
- **`sleep`** - Pauses for X seconds
- **`position`** - Moves window around
  - Predefined: `"center center"`, `"top left"`, `"top right"`, `"bottom left"`, `"bottom right"`
  - Custom: `"100 200"` (x y coordinates)
- **`close`** - Closes current window (Cmd+W)
- **`quit`** - Quits entire app (Cmd+Q)

## App Registry (Current)

Right now the registry is pretty minimal:

### Registered Apps
- **`iTerm`** → TerminalApp (handles iTerm2)

### Fallback Behavior
- If you specify an unknown app, it defaults to iTerm
- The registry is basically just for me right now

### Adding New Apps
The architecture is there to add more apps, but currently it's just iTerm. The plan is to add:
- Vim (when I get around to it)
- VS Code terminal (maybe)
- Other terminal apps as needed

## Architecture (Simplified)

```
producer/
├── apps/
│   ├── base.py      # BaseApp - abstract class
│   ├── terminal.py  # TerminalApp - iTerm2 stuff
│   └── registry.py  # AppRegistry - manages apps
├── automator.py     # ProducerAutomator - main engine
└── main.py          # CLI entry point
```

## Key Features (What Works)

- **Scene-based scripts** - organized into logical sections
- **Implicit app starting** - don't need to specify `start` action
- **Window reuse** - same app across scenes = same window
- **Dynamic positioning** - works on any screen size
- **Clean YAML** - no repetition, intuitive structure

## What's Still Evolving

- **More apps** - only iTerm right now
- **More actions** - basic set is working
- **Error handling** - could be better
- **Testing** - none yet
- **Documentation** - this is it!

## Development Notes

This is built for macOS using AppleScript. The positioning uses System Events to move windows around, which is pretty reliable but might break if Apple changes things.

The whole thing is designed to be extensible - adding new apps or actions should be straightforward once the patterns are established.

## License

MIT License
