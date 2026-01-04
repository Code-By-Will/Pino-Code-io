import os
import subprocess
from google import genai 
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
        if os.path.commonpath([working_dir_abs, file_path_abs]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path_abs):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", file_path_abs]
        if args:
            command.extend(args)

        run_command = subprocess.run(
            command,
            capture_output=True,
            cwd=working_dir_abs,
            timeout=30,
            text=True
            )
        
        output_parts = []

        if run_command.returncode != 0:
            output_parts.append(f"Process exited with code {run_command.returncode}")
        
        stdout = run_command.stdout or ""
        stderr = run_command.stderr or ""

        if not stdout and not stderr:
            output_parts.append("No output produced")
        else:
            if stdout:
                output_parts.append(f"STDOUT:{stdout}")
            if stderr:
                output_parts.append(f"STDERR:{stderr}")

        return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"



schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a specified python file and returns it's outputs (if any). Otherwise returns 'No output produced'",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path relative to the working directory of the python file to run."
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="List of string arguments to pass to the Python script (use [] for no args).",
                items=types.Schema(
                    type=types.Type.STRING,
                ),
            ),
        },
    ),
)