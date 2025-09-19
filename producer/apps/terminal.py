#!/usr/bin/env python3
"""
iTerm2 App implementation
"""

from .base import BaseApp

class TerminalApp(BaseApp):
    """iTerm2 application handler"""
    
    def __init__(self, app_name="iTerm2"):
        super().__init__(app_name)
    
    def start(self, **kwargs):
        """Activate iTerm2 and create a new window"""
        # Try to activate iTerm2 first
        activate_script = f'tell application "{self.app_name}" to activate'
        result = self.run_applescript(activate_script)
        
        if result is None:
            print(f"    ⚠️  Could not activate {self.app_name}, trying to launch...")
            # Try to launch iTerm2 if activation failed
            launch_script = f'tell application "{self.app_name}" to launch'
            self.run_applescript(launch_script)
            self.wait(2.0)  # Wait longer for launch
        
        # Wait a moment for iTerm2 to be ready
        self.wait(1.0)
        
        # Create new window in iTerm2
        window_script = f'tell application "{self.app_name}" to create window with default profile'
        
        return self.run_applescript(window_script)
    
    def write(self, text, **kwargs):
        """Write text to the current active iTerm2 session"""
        # Use System Events to send keystrokes to the current active application
        script = f'''
        tell application "System Events"
            keystroke "{text}"
            key code 36
        end tell
        '''
        return self.run_applescript(script)
    
    def create_window(self, profile="default"):
        """Create a new iTerm2 window"""
        script = f'''
        tell application "{self.app_name}"
            create window with default profile
        end tell
        '''
        return self.run_applescript(script)
    
    def position(self, position, **kwargs):
        """Position the current iTerm window using System Events"""
        # Get screen dimensions using a different approach
        screen_script = '''
        tell application "Finder"
            set screenSize to bounds of window of desktop
        end tell
        '''
        screen_result = self.run_applescript(screen_script)
        
        # Parse screen dimensions (format: "x, y, width, height")
        if screen_result:
            try:
                coords = screen_result.split(', ')
                width = int(coords[2]) - int(coords[0])  # width = right - left
                height = int(coords[3]) - int(coords[1])  # height = bottom - top
            except:
                # Fallback to common resolution
                width, height = 1920, 1080
        else:
            width, height = 1920, 1080
        
        # Calculate window size and positions
        window_width, window_height = 800, 600
        
        # Parse position string and get coordinates
        if position == "center center":
            x = (width - window_width) // 2
            y = (height - window_height) // 2
        elif position == "top left":
            x, y = 0, 0
        elif position == "top right":
            x = width - window_width
            y = 0
        elif position == "bottom left":
            x = 0
            y = height - window_height
        elif position == "bottom right":
            x = width - window_width
            y = height - window_height
        else:
            # Try to parse as "x y" coordinates
            try:
                coords = position.split()
                if len(coords) == 2:
                    x, y = int(coords[0]), int(coords[1])
                else:
                    print(f"    ⚠️  Invalid position format: {position}")
                    return None
            except ValueError:
                print(f"    ⚠️  Invalid position format: {position}")
                return None
        
        # Use System Events to move the current active window
        # This will position whatever window is currently focused
        script = f'''
        tell application "System Events"
            set frontApp to first application process whose frontmost is true
            tell frontApp
                set position of window 1 to {{{x}, {y}}}
                set size of window 1 to {{{window_width}, {window_height}}}
            end tell
        end tell
        '''
        
        return self.run_applescript(script)
    
    def close(self, **kwargs):
        """Close the current iTerm window (like Cmd+W)"""
        script = f'''
        tell application "{self.app_name}"
            close current window
        end tell
        '''
        return self.run_applescript(script)
    
    def quit(self, **kwargs):
        """Quit the entire iTerm application (like Cmd+Q)"""
        script = f'tell application "{self.app_name}" to quit'
        return self.run_applescript(script)
    
    def supports_action(self, action):
        """Check if this iTerm2 app supports a specific action"""
        iterm_actions = ['start', 'write', 'wait', 'create_window', 'position', 'close', 'quit']
        return action in iterm_actions
