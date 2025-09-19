#!/usr/bin/env python3
"""
Coding Video Automator
Main application entry point
"""

import sys
import argparse
import yaml
import os
from .automator import ProducerAutomator

def parse_script(script_path):
    """Parse a YAML script file and return the script data"""
    try:
        with open(script_path, 'r') as file:
            script_data = yaml.safe_load(file)
        return script_data
    except FileNotFoundError:
        print(f"❌ Script file not found: {script_path}")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"❌ Error parsing YAML script: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Producer - Terminal Automation Script Runner')
    parser.add_argument('script', help='Path to the script file to run')
    
    args = parser.parse_args()
    
    # Resolve script path
    script_path = os.path.abspath(args.script)
    
    print("🎬 Producer - Terminal Automation")
    print("==================================")
    print(f"📄 Running script: {script_path}")
    
    # Parse the script
    script_data = parse_script(script_path)
    
    # Create automator instance
    automator = ProducerAutomator()
    
    # Run the script
    print(f"🚀 Executing: {script_data.get('name', 'Unnamed Script')}")
    print(f"📝 {script_data.get('description', 'No description')}")
    
    try:
        automator.run_script(script_data)
        print("✅ Script completed successfully!")
    except Exception as e:
        print(f"❌ Script execution failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
