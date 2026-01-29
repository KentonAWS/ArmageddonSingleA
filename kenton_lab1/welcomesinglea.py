import time
import sys
import random

def type_text(text, delay=0.05):
    """Types out text with a delay for a fancy effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fireworks_animation(iterations=3):
    """Simple terminal fireworks effect using ANSI escape codes."""
    # Define colors (ANSI escape codes)
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    reset = '\033[0m'
    
    # Firework frames (expanding patterns)
    frames = [
        ["       *       "],
        ["    *  .  *    ", "       .       "],
        ["  *    ...    *", "    *  ...  *  "],
        [" *      '      *", "  *    ' '    *"]
    ]

    for _ in range(iterations):
        color = random.choice(colors)
        for frame in frames:
            # Move cursor up to overwrite previous frames for animation
            sys.stdout.write("\033[F" * len(frame)) 
            for line in frame:
                print(f"{color}{line}{reset}")
            time.sleep(0.15)
        print("\n" * 2) # Space between bursts

def fancy_welcome(name):
    # Clear screen
    print("\033c", end="")

    banner = r"""
SSS I N   N GGG L   EEEEE     A    
S     I NN  N G   L   E      A A   
 SSS  I N N N G G L   EEE   A   A  
    S I N  NN G   L   E    AAAAAAA 
 SSS  I N   N GGG LLL EEEEE A     A

Welcome!
    """
    print(banner)

    type_text(f"Hello, {name}! Welcome to Single A Armageddon.", delay=0.03)
    type_text("Build your knowledge. Let's make some magic happen! ✨", delay=0.03)

    spinner = ['-', '\\', '|', '/']
    type_text("Loading awesomeness...", delay=0.05)
    for _ in range(20):
        for char in spinner:
            sys.stdout.write(f"\r{char}")
            sys.stdout.flush()
            time.sleep(0.1)
    
    print("\rDone! 🎉")
    fireworks_animation() # Trigger the new animation

if __name__ == "__main__":
    name = input("Enter your name: ")
    fancy_welcome(name)
