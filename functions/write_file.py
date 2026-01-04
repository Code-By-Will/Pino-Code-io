import os
from google import genai 
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
        if os.path.commonpath([working_dir_abs, file_path_abs]) != working_dir_abs:
            return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(file_path_abs):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(file_path_abs), exist_ok=True)

        with open(file_path_abs, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content to a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path relative to the working directory of the file to write content to.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="A string containing the content to write to the file. This will overwrite the existing file content."
            ),
        },
    ),
)