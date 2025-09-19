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
        """Execute a parsed script by running each scene"""
        scenes = script_data.get('scenes', [])
        
        # Check if scenes are organized into parts
        if isinstance(scenes, dict):
            # Scenes are organized into parts (old format: scene_name: parts)
            for scene_name, scene_parts in scenes.items():
                print(f"\n🎬 Scene: {scene_name}")
                self._run_parts(scene_parts)
        elif isinstance(scenes, list) and len(scenes) > 0 and isinstance(scenes[0], dict) and 'name' in scenes[0]:
            # Scenes are organized into parts (new format: [{name: "setup", app: "iTerm", parts: [...]}])
            for scene in scenes:
                scene_name = scene.get('name', 'Unnamed Scene')
                scene_app = scene.get('app', 'iTerm')
                scene_parts = scene.get('parts', [])
                print(f"\n🎬 Scene: {scene_name} (App: {scene_app})")
                
                # Only start the app if it's different from the current one
                if not self.current_app or self.current_app.app_name != scene_app:
                    self.current_app = self.app_registry.get_app(scene_app)
                    self.current_app.start()
                
                self._run_parts(scene_parts, scene_app)
        else:
            # Scenes are a flat list
            self._run_parts(scenes)
    
    def _run_parts(self, parts, scene_app=None):
        """Run a list of parts"""
        for i, part in enumerate(parts, 1):
            action = part.get('action')
            print(f"  Part {i}: {action}")
            
            if action == 'sleep':
                duration = part.get('duration', 0.5)
                if self.current_app:
                    self.current_app.wait(duration)
                else:
                    import time
                    time.sleep(duration)
            elif action == 'write':
                text = part.get('text', '')
                if self.current_app:
                    # Extract only the additional parameters, not 'text' or 'action'
                    extra_params = {k: v for k, v in part.items() if k not in ['text', 'action']}
                    self.current_app.write(text, **extra_params)
                else:
                    print(f"    ⚠️  No active app to write to")
            elif action == 'position':
                position = part.get('text', 'center center')
                if self.current_app:
                    # Extract only the additional parameters, not 'text' or 'action'
                    extra_params = {k: v for k, v in part.items() if k not in ['text', 'action']}
                    self.current_app.position(position, **extra_params)
                else:
                    print(f"    ⚠️  No active app to position")
            elif action == 'close':
                if self.current_app:
                    # Extract only the additional parameters, not 'action'
                    extra_params = {k: v for k, v in part.items() if k not in ['action']}
                    self.current_app.close(**extra_params)
                else:
                    print(f"    ⚠️  No active app to close")
            elif action == 'quit':
                if self.current_app:
                    # Extract only the additional parameters, not 'action'
                    extra_params = {k: v for k, v in part.items() if k not in ['action']}
                    self.current_app.quit(**extra_params)
                    # Clear current app since we quit it
                    self.current_app = None
                else:
                    print(f"    ⚠️  No active app to quit")
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