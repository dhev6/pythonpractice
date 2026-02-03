import random
import sys
import time

def is_windows():
    return sys.platform.startswith("win")

def timed_input(prompt, timeout_secs=10):
    """
    Returns (text, timed_out: bool). On Windows, enforces timeout using msvcrt.
    On non-Windows: tries inputimeout; falls back to measuring time (best-effort).
    """
    if is_windows():
        # Windows: non-blocking character input
        try:
            import msvcrt
        except ImportError:
            # Very rare on Windows
            start = time.monotonic()
            text = input(f"{prompt} (you have {timeout_secs}s): ")
            return (text, (time.monotonic() - start) > timeout_secs)

        sys.stdout.write(f"{prompt} (you have {timeout_secs}s): ")
        sys.stdout.flush()
        buf = []
        deadline = time.monotonic() + timeout_secs
        last_second_shown = None

        while True:
            now = time.monotonic()
            if now >= deadline:
                # time's up -> print newline so next prints start on new line
                print()
                return ("", True)

            # Display a light countdown at the end of the line (no heavy redraws)
            secs_left = int(deadline - now)
            if secs_left != last_second_shown:
                last_second_shown = secs_left
                # Show time left as a right-end hint without disturbing input too much
                sys.stdout.write(f"\r{prompt} (you have {timeout_secs}s): {''.join(buf)}  [{secs_left}s left]")
                sys.stdout.flush()

            if msvcrt.kbhit():
                ch = msvcrt.getwch()
                # Handle special keys (prefix \x00 or \xe0) -> skip the next code
                if ch in ('\x00', '\xe0'):
                    _ = msvcrt.getwch()
                    continue
                if ch in ('\r', '\n'):
                    print()  # move to the next line
                    return ("".join(buf), False)
                if ch == '\b':  # backspace
                    if buf:
                        buf.pop()
                        # Redraw current line
                        sys.stdout.write("\r" + " " * 200 + "\r")
                        sys.stdout.write(f"{prompt} (you have {timeout_secs}s): {''.join(buf)}  [{secs_left}s left]")
                        sys.stdout.flush()
                    continue
                # Append normal character
                buf.append(ch)
                sys.stdout.write(ch)
                sys.stdout.flush()
            else:
                time.sleep(0.03)
    else:
        # Non-Windows: try inputimeout first
        try:
            from inputimeout import inputimeout, TimeoutOccurred
            try:
                text = inputimeout(prompt=f"{prompt} (you have {timeout_secs}s): ", timeout=timeout_secs)
                return (text, False)
            except TimeoutOccurred:
                print()  # newline after prompt when timing out
                return ("", True)
        except Exception:
            # Best-effort fallback: cannot truly enforce timeout, but we penalize slow entries
            start = time.monotonic()
            text = input(f"{prompt} (target {timeout_secs}s): ")
            took = time.monotonic() - start
            return (text, took > timeout_secs)

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            return False
        f += 2
    return True

def rotating_clue(attempt_idx, secret, low, high):
    # attempt_idx is 1-based
    clues = []
    # Always include narrowed range
    clues.append(f"It is between {low} and {high}.")

    # Rotating extra hints
    extra_idx = (attempt_idx - 1) % 5
    if extra_idx == 0:
        clues.append(f"It is {'even' if secret % 2 == 0 else 'odd'}.")
    elif extra_idx == 1:
        clues.append(f"It is{' ' if secret % 3 == 0 else ' not '}divisible by 3.")
    elif extra_idx == 2:
        clues.append(f"The last digit is {secret % 10}.")
    elif extra_idx == 3:
        tens_low = (secret // 10) * 10
        clues.append(f"It falls in the {tens_low}-{tens_low + 9} range.")
    else:
        clues.append(f"It is{' ' if is_prime(secret) else ' not '}a prime number.")
    return " ".join(clues)

def play(max_attempts=7, time_per_attempt=10, lo=1, hi=100):
    secret = random.randint(lo, hi)
    low, high = lo, hi

    print("Guess the number!")
    print(f"I'm thinking of a number between {lo} and {hi}.")
    print(f"You have {max_attempts} attempts, {time_per_attempt} seconds each.")

    for attempt in range(1, max_attempts + 1):
        print(f"\nAttempt {attempt}/{max_attempts}")
        text, timed_out = timed_input("Your guess", time_per_attempt)

        if timed_out:
            print("Time's up! Attempt counted.")
            print("Clue:", rotating_clue(attempt, secret, low, high))
            continue

        # Validate integer input
        try:
            guess = int(text.strip())
        except ValueError:
            print("Not a valid integer. Attempt counted.")
            print("Clue:", rotating_clue(attempt, secret, low, high))
            continue

        if guess == secret:
            print(f"Correct! The number was {secret}. You won in {attempt} attempt(s).")
            return
        elif guess < secret:
            print("Too low.")
            low = max(low, guess + 1)
        else:
            print("Too high.")
            high = min(high, guess - 1)

        print("Clue:", rotating_clue(attempt, secret, low, high))

    print(f"\nOut of attempts. The number was {secret}. Better luck next time!")

if __name__ == "__main__":
    play()