import json
import os

notebook_path = 'src/beginner.ipynb'
mapping_file_path = '/tmp/jp_markdown_ch1_ch2.json'

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
    for cell_index, cell in enumerate(notebook_data.get('cells', [])):
        if cell.get('cell_type') == 'markdown':
            original_source_as_list = cell.get('source', [])
            if not original_source_as_list:
                continue
            original_source_as_string = "".join(original_source_as_list)

            modified_source_string = original_source_as_string

            placeholder_found_in_cell = False
            # For this script, we assume placeholders are unique enough globally for Ch1 & Ch2
            # or this script targets the whole notebook for these specific Ch1/Ch2 placeholders.
            for placeholder, japanese_text in jp_mapping.items():
                if placeholder in modified_source_string:
                    modified_source_string = modified_source_string.replace(placeholder, japanese_text)
                    placeholder_found_in_cell = True

            if placeholder_found_in_cell and modified_source_string != original_source_as_string:
                # Convert string back to list of lines for JSON
                lines = modified_source_string.splitlines()
                new_source_list = [line + '\\n' for line in lines[:-1]]
                if lines:
                    new_source_list.append(lines[-1])

                if not new_source_list and modified_source_string == "":
                    cell['source'] = []
                elif original_source_as_list == [''] and not modified_source_string.strip(): # Handles if original was [''] and became empty
                     cell['source'] = ['']
                else:
                    cell['source'] = new_source_list
                cells_modified_count += 1
                # print(f"Replaced content in markdown cell {cell_index} (Chapters 1-2).")

    if cells_modified_count > 0:
        print(f"Total markdown cells modified for Chapters 1-2: {cells_modified_count}")
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook_data, f, ensure_ascii=False, indent=2)
        print(f"Successfully updated notebook with Japanese markdown for Chapters 1-2: {notebook_path}")
    else:
        print("No placeholders for Chapters 1-2 found or replaced in any markdown cells. Check notebook structure, placeholder content, and mapping file.")
        # Debugging output
        debug_cell_count = 0
        for cell_debug_idx, cell_debug_val in enumerate(notebook_data.get('cells', [])):
            if cell_debug_val.get('cell_type') == 'markdown':
                 source_str_debug = "".join(cell_debug_val.get('source', []))
                 # Check for Chapter 1 or 2 specific placeholders
                 if "[JP_MD_CH1_" in source_str_debug or "[JP_MD_CH2_" in source_str_debug:
                    print(f"Debug: Ch1/2 MD Cell {cell_debug_idx} Source: {source_str_debug[:200]}...")
                    debug_cell_count+=1
            if debug_cell_count > 20 : # Print up to some MD cells for debugging
                break
        if debug_cell_count == 0:
             print("Debug: No Ch1/Ch2 markdown cells with expected placeholders found during debug scan.")


except FileNotFoundError as fnf_error:
    print(f"Error - File Not Found: {fnf_error}")
except json.JSONDecodeError as json_error:
    print(f"Error - JSON Decode Error: {json_error}")
    if os.path.exists(mapping_file_path):
        with open(mapping_file_path, 'r', encoding='utf-8') as f_err:
            print(f"First 500 chars of {mapping_file_path}:\n{f_err.read(500)}")
except Exception as e:
    print(f"Script execution error: {e}")
