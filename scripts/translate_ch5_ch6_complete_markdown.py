import json
import os

notebook_path = 'src/beginner.ipynb'
mapping_file_path = '/tmp/jp_markdown_ch5_ch6_complete.json'

try:
    print(f"Python script started for Ch5-6 (Complete). Notebook path: {os.path.abspath(notebook_path)}")
    print(f"Mapping file path: {os.path.abspath(mapping_file_path)}")

    if not os.path.exists(notebook_path):
        print(f"Error: Notebook file not found at '{notebook_path}'")
        exit(1)
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook_data = json.load(f)
    print("Notebook loaded successfully.")

    if not os.path.exists(mapping_file_path):
        print(f"Error: Mapping file not found at '{mapping_file_path}'")
        print("Listing /tmp directory:")
        if os.path.exists("/tmp"):
            for item in os.listdir("/tmp"): print(f"- {item}")
        else:
            print("/tmp directory does not exist.")
        exit(1)

    with open(mapping_file_path, 'r', encoding='utf-8') as f:
        jp_mapping = json.load(f)
    print(f"Comprehensive mapping file for Ch5-6 loaded successfully. Contains {len(jp_mapping)} mappings.")

    cells_modified_count = 0

    for cell_index, cell in enumerate(notebook_data.get('cells', [])):
        if cell.get('cell_type') == 'markdown':
            original_source_as_list = cell.get('source', [])
            if not original_source_as_list:
                continue

            original_source_as_string = "".join(original_source_as_list)
            modified_source_string = original_source_as_string

            placeholder_found_and_replaced_in_cell = False

            is_target_chapter_cell = False
            # Using uppercase for checking to make it case-insensitive for prefixes
            temp_str_for_check = original_source_as_string.upper()
            ch5_ch6_prefixes = ["[JP_MD_CH5_", "[JP_MD_CH6_", "[JP_CHECK_TITLE_CH5_", "[JP_CHECK_TITLE_CH6_"]

            if any(prefix.upper() in temp_str_for_check for prefix in ch5_ch6_prefixes):
                is_target_chapter_cell = True

            if is_target_chapter_cell:
                for placeholder, japanese_text in jp_mapping.items():
                    if placeholder in modified_source_string: # Placeholder matching is case-sensitive
                        modified_source_string = modified_source_string.replace(placeholder, japanese_text)
                        placeholder_found_and_replaced_in_cell = True

            if placeholder_found_and_replaced_in_cell:
                # Convert the modified string back to a list of strings for the cell source
                lines = modified_source_string.splitlines()
                new_source_list = [line + '\\n' for line in lines[:-1]]
                if lines:
                    new_source_list.append(lines[-1])
                else: # If modified_source_string became empty
                    new_source_list = []

                if cell['source'] != new_source_list:
                    cell['source'] = new_source_list
                    cells_modified_count += 1
                    # print(f"Replaced content in markdown cell {cell_index} (Targeting Chapters 5-6).") # Verbose

    if cells_modified_count > 0:
        print(f"Total markdown cells modified for Chapters 5-6 (Comprehensive): {cells_modified_count}")
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook_data, f, ensure_ascii=False, indent=2)
        print(f"Successfully updated notebook with Japanese markdown for Chapters 5-6: {notebook_path}")
    else:
        print("No placeholders for Chapters 5-6 found or replaced. Check notebook structure, placeholders, and mapping file.")
        debug_cell_count = 0
        for cell_debug_idx, cell_debug_val in enumerate(notebook_data.get('cells', [])):
            if cell_debug_val.get('cell_type') == 'markdown':
                 source_str_debug = "".join(cell_debug_val.get('source', []))
                 if any(prefix.upper() in source_str_debug.upper() for prefix in ch5_ch6_prefixes):
                    print(f"Debug: Ch5/6 MD Cell {cell_debug_idx} Source: {source_str_debug[:200]}...")
                    debug_cell_count+=1
            if debug_cell_count > 30 :
                break
        if debug_cell_count == 0:
            print("Debug: No Ch5/Ch6 markdown cells with expected placeholders found during debug scan.")


except FileNotFoundError as fnf_error:
    print(f"Error - File Not Found: {fnf_error}")
except json.JSONDecodeError as json_error:
    print(f"Error - JSON Decode Error: {json_error}")
    if os.path.exists(mapping_file_path):
        with open(mapping_file_path, 'r', encoding='utf-8') as f_err:
            print(f"First 500 chars of {mapping_file_path}:\n{f_err.read(500)}")
except Exception as e:
    print(f"Script execution error: {e}")
