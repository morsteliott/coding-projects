# =============================================================================

# hello_world.py

# =============================================================================

# Project      : XAUUSD Trading Bot - Coinexx / MT4

# Description  : Entry-level script to verify the Python environment is

# configured correctly before building the trading bot.

# Author       : Trading Bot Assistant

# =============================================================================

def main():
“””
Main entry point of the script.
Prints a greeting message to the console to confirm the environment works.
“””

```
# Define the message we want to display
message = "Hello World"

# Print the message to the standard output (console)
print(message)
```

# —————————————————————————–

# Script entry point guard

# This block ensures main() is only called when the script is run directly,

# not when it is imported as a module into another script.

# —————————————————————————–

if **name** == “**main**”:
main()