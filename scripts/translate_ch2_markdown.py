import json
import os

notebook_path = 'src/beginner.ipynb'
# We reuse the mapping file that contains mappings for both Ch1 and Ch2
mapping_file_path = '/tmp/jp_markdown_ch1_ch2.json'

try:
    print(f"Python script for Chapter 2 started. Notebook path: {os.path.abspath(notebook_path)}")
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
    print("Mapping file loaded successfully.")

    cells_modified_count = 0

    for cell_index, cell in enumerate(notebook_data.get('cells', [])):
        if cell.get('cell_type') == 'markdown':
            original_source_as_list = cell.get('source', [])
            if not original_source_as_list:
                continue
            original_source_as_string = "".join(original_source_as_list)

            modified_source_string = original_source_as_string

            placeholder_found_in_cell = False
            # Target only Chapter 2 placeholders
            ch2_prefixes = ["[JP_MD_CH2_", "[JP_CHECK_TITLE_CH2_"]

            is_chapter_2_cell = False
            if any(prefix in original_source_as_string for prefix in ch2_prefixes):
                is_chapter_2_cell = True

            if is_chapter_2_cell:
                for placeholder, japanese_text in jp_mapping.items():
                    # Ensure we only use Ch2 placeholders from the map, even if it has more
                    if placeholder.startswith("[JP_MD_CH2_") or placeholder.startswith("[JP_CHECK_TITLE_CH2_"):
                        if placeholder in modified_source_string:
                            modified_source_string = modified_source_string.replace(placeholder, japanese_text)
                            placeholder_found_in_cell = True

            if placeholder_found_in_cell and modified_source_string != original_source_as_string:
                lines = modified_source_string.splitlines()
                new_source_list = [line + '\\n' for line in lines[:-1]]
                if lines:
                    new_source_list.append(lines[-1])

                if not new_source_list and modified_source_string == "":
                    cell['source'] = []
                elif original_source_as_list == [''] and not modified_source_string.strip():
                     cell['source'] = ['']
                else:
                    cell['source'] = new_source_list
                cells_modified_count += 1
                # print(f"Replaced content in markdown cell {cell_index} (Chapter 2).")

    if cells_modified_count > 0:
        print(f"Total markdown cells modified for Chapter 2: {cells_modified_count}")
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook_data, f, ensure_ascii=False, indent=2)
        print(f"Successfully updated notebook with Japanese markdown for Chapter 2: {notebook_path}")
    else:
        print("No placeholders for Chapter 2 found or replaced. Check Ch2 cells for placeholders like [JP_MD_CH2_...]")
        debug_cell_count = 0
        for cell_debug_idx, cell_debug_val in enumerate(notebook_data.get('cells', [])):
            if cell_debug_val.get('cell_type') == 'markdown':
                 source_str_debug = "".join(cell_debug_val.get('source', []))
                 if any(prefix in source_str_debug for prefix in ch2_prefixes):
                    print(f"Debug: Ch2 MD Cell {cell_debug_idx} Source: {source_str_debug[:200]}...")
                    debug_cell_count+=1
            if debug_cell_count > 10:
                break
        if debug_cell_count == 0:
            print("Debug: No Ch2 markdown cells with expected placeholders found during debug scan.")

except FileNotFoundError as fnf_error:
    print(f"Error - File Not Found: {fnf_error}")
except json.JSONDecodeError as json_error:
    print(f"Error - JSON Decode Error: {json_error}")
    if os.path.exists(mapping_file_path):
        with open(mapping_file_path, 'r', encoding='utf-8') as f_err:
            print(f"First 500 chars of {mapping_file_path}:\n{f_err.read(500)}")
except Exception as e:
    print(f"Script execution error: {e}")
