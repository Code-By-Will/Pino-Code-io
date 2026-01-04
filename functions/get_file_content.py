import os
from config import MAX_CHARS
from google import genai 
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
        if os.path.commonpath([working_dir_abs, file_path_abs]) != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(file_path_abs, "r") as f:
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except Exception as e:
        return f"Error: {e}"
    return file_content


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Gets the content of a file, up to the first {MAX_CHARS} characters",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File Path for file to get the content of, relative to the working directory.",
            ),
        },
    ),
)