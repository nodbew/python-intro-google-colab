import json
import os

notebook_path = 'src/beginner.ipynb'
mapping_file_path = '/tmp/jp_markdown_ch1.json'

try:
    print(f"Python script for Chapter 1 started. Notebook path: {os.path.abspath(notebook_path)}")
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
        print("Listing /tmp directory:")
        if os.path.exists("/tmp"):
            for item in os.listdir("/tmp"): print(f"- {item}")
        else:
            print("/tmp directory does not exist.")
        exit(1)

    with open(mapping_file_path, 'r', encoding='utf-8') as f:
        jp_mapping = json.load(f)
    print("Mapping file loaded successfully.")

    cells_modified_count = 0

    # Iterate through all cells in the notebook
    # For this script, assume all markdown cells currently in the notebook are for Chapter 1
    # as it's the first chapter being processed with this method.
    for cell_index, cell in enumerate(notebook_data.get('cells', [])):
        if cell.get('cell_type') == 'markdown':
            original_source_as_list = cell.get('source', [])
            if not original_source_as_list:
                continue
            original_source_as_string = "".join(original_source_as_list)

            modified_source_string = original_source_as_string

            placeholder_found_in_cell = False
            for placeholder, japanese_text in jp_mapping.items():
                if placeholder in modified_source_string:
                    # Ensure that the placeholder is for Chapter 1 if the jp_mapping could contain other chapters
                    # For this specific script, jp_mapping should only have Ch1 placeholders.
                    if placeholder.startswith("[JP_MD_CH1_") or placeholder.startswith("[JP_CHECK_TITLE_CH1_"):
                        modified_source_string = modified_source_string.replace(placeholder, japanese_text)
                        placeholder_found_in_cell = True

            if placeholder_found_in_cell and modified_source_string != original_source_as_string:
                # Convert string back to list of lines for JSON
                lines = modified_source_string.splitlines()
                new_source_list = [line + '\\n' for line in lines[:-1]]
                if lines:
                    new_source_list.append(lines[-1])

                if not new_source_list and modified_source_string == "": # Cell became empty
                    cell['source'] = []
                elif original_source_as_list == [''] and not modified_source_string.strip(): # Original was [''] and became empty
                     cell['source'] = ['']
                else:
                    cell['source'] = new_source_list
                cells_modified_count += 1
                # print(f"Replaced content in markdown cell {cell_index} (Chapter 1).") # Verbose logging

    if cells_modified_count > 0:
        print(f"Total markdown cells modified for Chapter 1: {cells_modified_count}")
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook_data, f, ensure_ascii=False, indent=2)
        print(f"Successfully updated notebook with Japanese markdown for Chapter 1: {notebook_path}")
    else:
        print("No placeholders for Chapter 1 found or replaced in any markdown cells. Check notebook structure, placeholder content, and mapping file.")
        debug_cell_count = 0
        for cell_debug_idx, cell_debug_val in enumerate(notebook_data.get('cells', [])):
            if cell_debug_val.get('cell_type') == 'markdown':
                 source_str_debug = "".join(cell_debug_val.get('source', []))
                 if "[JP_MD_CH1_" in source_str_debug or "[JP_CHECK_TITLE_CH1_" in source_str_debug:
                    print(f"Debug: Ch1 MD Cell {cell_debug_idx} Source: {source_str_debug[:200]}...")
                    debug_cell_count+=1
            if debug_cell_count > 10 :
                break
        if debug_cell_count == 0:
            print("Debug: No Ch1 markdown cells with expected placeholders found during debug scan.")


except FileNotFoundError as fnf_error:
    print(f"Error - File Not Found: {fnf_error}")
except json.JSONDecodeError as json_error:
    print(f"Error - JSON Decode Error: {json_error}")
    if os.path.exists(mapping_file_path):
        with open(mapping_file_path, 'r', encoding='utf-8') as f_err:
            print(f"First 500 chars of {mapping_file_path}:\n{f_err.read(500)}")
except Exception as e:
    print(f"Script execution error: {e}")
