#!/usr/bin/env python3
"""
Producer Automator
Handles automation of various applications using AppleScript
"""

from .apps.registry import AppRegistry

class ProducerAutomator:
    def __init__(self):
        self.app_registry = AppRegistry()
        self.current_app = None
    
    def run_applescript(self, script):
        """Execute AppleScript and return the result"""
        try:
            result = subprocess.run(
                ['osascript', '-e', script],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"AppleScript error: {e.stderr}")
            return None
    
    def run_script(self, script_data):
        """Execute a parsed script by running each step"""
        steps = script_data.get('steps', [])
        
        # Check if steps is organized into parts
        if isinstance(steps, dict):
            # Steps are organized into parts (old format: part_name: steps)
            for part_name, part_steps in steps.items():
                print(f"\n📋 Part: {part_name}")
                self._run_steps(part_steps)
        elif isinstance(steps, list) and len(steps) > 0 and isinstance(steps[0], dict) and 'name' in steps[0]:
            # Steps are organized into parts (new format: [{name: "setup", steps: [...]}])
            for part in steps:
                part_name = part.get('name', 'Unnamed Part')
                part_steps = part.get('steps', [])
                print(f"\n📋 Part: {part_name}")
                self._run_steps(part_steps)
        else:
            # Steps are a flat list
            self._run_steps(steps)
    
    def _run_steps(self, steps):
        """Run a list of steps"""
        for i, step in enumerate(steps, 1):
            action = step.get('action')
            print(f"  Step {i}: {action}")
            
            if action == 'start':
                app_name = step.get('app', 'iTerm2')
                self.current_app = self.app_registry.get_app(app_name)
                self.current_app.start(**step)
            elif action == 'wait':
                duration = step.get('duration', 0.5)
                if self.current_app:
                    self.current_app.wait(duration)
                else:
                    import time
                    time.sleep(duration)
            elif action == 'write':
                text = step.get('text', '')
                if self.current_app:
                    # Extract only the additional parameters, not 'text' or 'action'
                    extra_params = {k: v for k, v in step.items() if k not in ['text', 'action']}
                    self.current_app.write(text, **extra_params)
                else:
                    print(f"    ⚠️  No active app to write to")
            elif action == 'position':
                position = step.get('text', 'center center')
                if self.current_app:
                    # Extract only the additional parameters, not 'text' or 'action'
                    extra_params = {k: v for k, v in step.items() if k not in ['text', 'action']}
                    self.current_app.position(position, **extra_params)
                else:
                    print(f"    ⚠️  No active app to position")
            else:
                print(f"    ⚠️  Unknown action: {action}")
    

    def run_iterm_test(self):
        """Simple test - open iTerm, create new window, run clear command"""
        # Use the new app system
        terminal_app = self.app_registry.get_app('iTerm2')
        
        print("Opening iTerm2 and running clear command...")
        
        # Start the app
        terminal_app.start()
        
        # Wait a moment
        terminal_app.wait(0.5)
        
        # Write the command
        terminal_app.write("clear")
        
        print("✅ iTerm automation successful!")
        return True