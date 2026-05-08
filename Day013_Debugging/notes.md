# Day 13 - Debugging

## What I Learned

Debugging is not random trial and error — it's a repeatable process. Angela Yu broke it down into steps that apply to any bug, in any project.

## Debugging Process

**1. Describe the Problem**
Put the bug into words before touching the code. Vague problem = vague fix. Be specific: _"The loop runs one extra time"_ is better than _"it's broken."_

**2. Reproduce the Bug**
A bug you can't reproduce consistently is a bug you can't fix reliably. Find the exact input or condition that triggers it every time.

**3. Play Computer**
Go through your code line by line _as if you are the interpreter_ — track variable values mentally, don't assume the code does what you intended. Most bugs live in the gap between what you meant and what you wrote.

**4. Fix the Error**

- **Syntax errors** — Python catches these immediately at run; read the traceback, it tells you the line
- **Logic errors** — code runs but produces wrong output; these need step 3 above
- **Name/Type errors** — wrong variable name, wrong data type passed somewhere

**5. Use `print()` Statements**
Cheapest debugging tool available. Drop `print()` before and after suspicious lines to see what values actually are at runtime — not what you think they are.

```python
print(f"Before loop: x = {x}")
# suspicious code
print(f"After loop: x = {x}")
```

Remove them once the bug is fixed.

**6. Use a Debugger**
IDE debuggers (VS Code has one built in) let you set **breakpoints** — the program pauses at that line and you can inspect every variable's value without adding print statements everywhere. More surgical than `print()` for complex bugs.

## Key Mindset

The silent bug in Day 12's `check_answer()` (returning `None` on a correct guess) is a real example of a logic error — the code ran, produced the right _visible_ output, but left `turns = None` silently. That kind of bug only surfaces when you play computer carefully instead of trusting that "it seems to work."
