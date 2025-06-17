import json
import os

notebook_path = 'src/beginner.ipynb'
mapping_file_path = '/tmp/jp_markdown_ch9.json' # Using /tmp/ as per previous subtask report

try:
    print(f"Python script started. Notebook path: {os.path.abspath(notebook_path)}")
    print(f"Mapping file path: {os.path.abspath(mapping_file_path)}")

    if not os.path.exists(notebook_path):
        print(f"Error: Notebook file not found at '{notebook_path}'")
        exit(1)
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook_data = json.load(f)
    print("Notebook loaded successfully.")

    if not os.path.exists(mapping_file_path):
        print(f"Error: Mapping file not found at '{mapping_file_path}'")
        # Debug: List files in common locations
        print("Listing /app (repo root):")
        for item in os.listdir("/app"): print(f"- {item}")
        if os.path.exists("/app/src"):
            print("Listing /app/src directory:")
            for item_s in os.listdir("/app/src"): print(f"- {item_s}")
        if os.path.exists("/tmp"):
            print("Listing /tmp directory:")
            for item_t in os.listdir("/tmp"): print(f"- {item_t}")
        exit(1)

    with open(mapping_file_path, 'r', encoding='utf-8') as f:
        jp_mapping = json.load(f)
    print("Mapping file loaded successfully.")

    cells_modified_count = 0

    # Iterate through all cells in the notebook
    for cell_index, cell in enumerate(notebook_data.get('cells', [])):
        if cell.get('cell_type') == 'markdown':
            original_source_as_list = cell.get('source', [])
            if not original_source_as_list:
                continue
            original_source_as_string = "".join(original_source_as_list)

            modified_source_string = original_source_as_string

            placeholder_found_in_cell = False
            # Check if the cell content is likely part of Chapter 9
            is_chapter_9_cell = False
            # Using specific Chapter 9 placeholder prefixes for targeting
            ch9_prefixes = ["[JP_CHAP9_", "[JP_SEC9_", "[JP_EX9_", "[JP_AS_9_", "[JP_SOL_9_", "[JP_CHECK_CODE_TITLE_EX9_"]
            # Note: "[JP_PY_COMMENT_" and "[JP_PY_STRING_" are for code cells, not markdown, so excluded here.

            if any(prefix in original_source_as_string for prefix in ch9_prefixes):
                is_chapter_9_cell = True

            if is_chapter_9_cell: # Only process if identified as a Chapter 9 cell
                for placeholder, japanese_text in jp_mapping.items():
                    if placeholder in modified_source_string:
                        modified_source_string = modified_source_string.replace(placeholder, japanese_text)
                        placeholder_found_in_cell = True

            if placeholder_found_in_cell and modified_source_string != original_source_as_string:
                # Convert string back to list of lines for JSON
                # Each string in the list should represent a line.
                # splitlines(True) keeps line endings, but Jupyter usually doesn't store them for the last line of a cell.
                # So, we split and re-add '\n' only if needed.
                lines = modified_source_string.splitlines()
                new_source_list = [line + '\n' for line in lines[:-1]] # Add \n for all but last line
                if lines: # if there are any lines
                    new_source_list.append(lines[-1]) # Add last line without \n

                # Handle case where a cell might become truly empty or was ['']
                if not new_source_list and modified_source_string == "":
                    cell['source'] = [] # Or [''] - Jupyter often uses [] for empty markdown cells
                elif original_source_as_list == [''] and not modified_source_string.strip():
                    cell['source'] = ['']
                else:
                    cell['source'] = new_source_list

                cells_modified_count += 1
                # print(f"Replaced content in markdown cell {cell_index} (Chapter 9).")

    if cells_modified_count > 0:
        print(f"Total Chapter 9 markdown cells modified: {cells_modified_count}")
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook_data, f, ensure_ascii=False, indent=2)
        print(f"Successfully updated notebook with Japanese Chapter 9 markdown: {notebook_path}")
    else:
        print("No Chapter 9 placeholders found or replaced in any markdown cells. Check notebook structure, placeholder content, and mapping file.")
        debug_cell_count = 0
        for cell_debug_idx, cell_debug_val in enumerate(notebook_data.get('cells', [])):
            if cell_debug_val.get('cell_type') == 'markdown':
                 source_str_debug = "".join(cell_debug_val.get('source', []))
                 if any(prefix in source_str_debug for prefix in ch9_prefixes):
                    print(f"Debug: Ch9 MD Cell {cell_debug_idx} Source: {source_str_debug[:200]}...")
                    debug_cell_count+=1
            if debug_cell_count > 10 and cells_modified_count == 0:
                print("Debug: Further Ch9 placeholder cell content suppressed...")
                break
        if debug_cell_count == 0 and cells_modified_count == 0 :
            print("Debug: No markdown cells with Chapter 9 placeholders found during debug scan either.")


except FileNotFoundError as fnf_error:
    print(f"Error - File Not Found: {fnf_error}")
except json.JSONDecodeError as json_error:
    print(f"Error - JSON Decode Error: {json_error}")
    if os.path.exists(mapping_file_path):
        with open(mapping_file_path, 'r', encoding='utf-8') as f_err:
            print(f"First 500 chars of {mapping_file_path}:\n{f_err.read(500)}")
except Exception as e:
    print(f"Script execution error: {e}")
