#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2022 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.

"""
Entry point script for Render.com deployment
"""

import os
import sys
import pathlib
import importlib
import logging

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S"
)

logger = logging.getLogger("render_start")

if __name__ == "__main__":
    print("Starting Userge...")
    
    # Create necessary directories
    base_dir = os.path.dirname(os.path.abspath(__file__))
    logs_dir = os.path.join(base_dir, "logs")
    downloads_dir = os.path.join(base_dir, "downloads")
    
    # Create logs directory if it doesn't exist
    print(f"Creating logs directory at: {logs_dir}")
    pathlib.Path(logs_dir).mkdir(parents=True, exist_ok=True)
    
    # Create downloads directory if it doesn't exist
    print(f"Creating downloads directory at: {downloads_dir}")
    pathlib.Path(downloads_dir).mkdir(parents=True, exist_ok=True)
    
    # Check if all required environment variables are set
    required_vars = ["API_ID", "API_HASH", "DATABASE_URL", "LOG_CHANNEL_ID"]
    missing_vars = [var for var in required_vars if not os.environ.get(var)]
    
    if missing_vars:
        print(f"Error: The following required environment variables are not set: {', '.join(missing_vars)}")
        print("Please set these variables in your Render.com dashboard.")
        sys.exit(1)
    
    # Check if at least one mode is configured
    has_user_mode = bool(os.environ.get("SESSION_STRING"))
    has_bot_mode = bool(os.environ.get("BOT_TOKEN") and os.environ.get("OWNER_ID"))
    
    if not (has_user_mode or has_bot_mode):
        print("Error: Neither USER mode nor BOT mode is configured.")
        print("Please set either SESSION_STRING (for USER mode) or BOT_TOKEN and OWNER_ID (for BOT mode).")
        sys.exit(1)
    
    # Add the current directory to the Python path
    sys.path.insert(0, base_dir)
    
    # Import and run Userge directly
    try:
        print("Importing userge module...")
        # First, try to import userge directly
        try:
            from userge import userge
            print("Successfully imported userge module")
            userge.begin()
        except ImportError as e:
            print(f"Direct import failed: {e}")
            print("Trying alternative import method...")
            
            # If direct import fails, try to run the module using runpy
            import runpy
            print("Running userge module using runpy...")
            runpy.run_module("userge", run_name="__main__")
            
    except Exception as e:
        print(f"Error starting Userge: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

