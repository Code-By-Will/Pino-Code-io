# AI Code Debugging Agent - Pino-Code-io

An experimental, agentic debugging assistant that uses an LLM to:
- Analyze Python tracebacks and source code
- Propose fixes
- Optionally apply patches to the codebase
- Re-run tests to verify the fix

This is a toy, educational version of tools like Cursor/Zed Agentic Mode or Claude Code.

> **Warning**  
> This project is for learning and experimentation only. Do **not** point it at sensitive codebases, production systems, or machines you care about.

---

## Features

-  Parse error messages and traceback output
-  Use an LLM to reason about likely root causes
- Propose or apply code edits via a patching system
-  Re-run tests/commands to verify fixes
-  Simple CLI interface for running the agent on a repo

---

## Architecture

At a high level:

1. **Command Runner**
   Runs a specified command (e.g. `pytest`, `python main.py`) and collects:
   - `stdout`
   - `stderr`
   - exit code

2. **Context Builder**
   Gathers relevant context for the LLM:
   - Error output
   - Target file(s) and surrounding code
   - Optional additional notes/prompts

3. **LLM Client**
   Sends a prompt to the LLM (e.g. Gemini/other provider) with:
   - Error logs
   - Snippets of code
   - Tool instructions (how to propose or apply patches)

4. **Patch Applier**
   Takes the LLM’s suggestion (patch or file edits) and:
   - Validates the patch format
   - Applies it to the local files
   - Handles basic conflicts/validation

5. **Feedback Loop**
   Optionally re-runs the command to see if the issue is fixed and can:
   - Stop on success
   - Iterate for a fixed number of attempts
