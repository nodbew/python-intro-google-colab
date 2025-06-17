import json
import os

notebook_path = 'src/beginner.ipynb'

# Define the cells for Chapter 11 (Modules and Packages)
chapter11_cells = [
    # CHAPTER 11 Header
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# [JP_MD_CH11_TITLE_PH]\n\n",
        "[JP_MD_CH11_INTRO_P1_PH]\n",
        "[JP_MD_CH11_INTRO_P2_PH]"
      ]
    },
    # Section 11.1: モジュールとは？ (What are modules?)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH11_SEC1_TITLE_PH]\n\n",
        "[JP_MD_CH11_SEC1_EXPLAIN_P1_PH]\n",
        "[JP_MD_CH11_SEC1_EXPLAIN_P2_PH]"
      ]
    },
    { # Exercise 11.1
      "cell_type": "markdown",
      "metadata": {},
      "source": ["### [JP_MD_CH11_SEC1_EX_TITLE_PH]\n\n", "[JP_MD_CH11_SEC1_EX_PROMPT_PH]"]
    },
    { # Answer Space 11.1
      "cell_type": "markdown",
      "metadata": {},
      "source": ["[JP_MD_CH11_SEC1_AS_PROMPT_PH]\n", "1. ...\n", "2. ..."]
    },
    { # Solution 11.1 (hidden)
      "cell_type": "markdown",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": ["---<details><summary>[JP_MD_CH11_SEC1_SOL_SUMMARY_PH]</summary>\n\n", "[JP_MD_CH11_SEC1_SOL_DETAIL_PH]\n", "</details>"]
    },
    # Section 11.2: モジュールのインポート (`import`) (Importing modules)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH11_SEC2_TITLE_PH]\n\n",
        "[JP_MD_CH11_SEC2_EXPLAIN_P1_PH]\n",
        "**[JP_MD_CH11_SEC2_IMPORT_SYNTAX1_TITLE_PH]**\n",
        "```python\n",
        "import module_name_placeholder\n",
        "# module_name_placeholder.function_name_placeholder()\n",
        "```\n",
        "**[JP_MD_CH11_SEC2_IMPORT_SYNTAX2_TITLE_PH]**\n",
        "```python\n",
        "from module_name_placeholder import specific_function_placeholder\n",
        "# specific_function_placeholder()\n",
        "```\n",
        "**[JP_MD_CH11_SEC2_IMPORT_SYNTAX3_TITLE_PH]**\n",
        "```python\n",
        "from module_name_placeholder import *\n",
        "# function1_placeholder()\n",
        "# function2_placeholder()\n",
        "```\n",
        "[JP_MD_CH11_SEC2_EXPLAIN_P2_PH]\n",
        "**[JP_MD_CH11_SEC2_IMPORT_SYNTAX4_TITLE_PH]**\n",
        "```python\n",
        "import module_name_placeholder as alias_placeholder\n",
        "# alias_placeholder.function_name_placeholder()\n",
        "```"
      ]
    },
    { # Exercise 11.2
      "cell_type": "markdown", "metadata": {}, "source": ["### [JP_MD_CH11_SEC2_EX_TITLE_PH]\n\n","[JP_MD_CH11_SEC2_EX_PROMPT_PH]"]
    },
    { # Answer Space 11.2
      "cell_type": "code", "metadata": {}, "source": [
        "def import_math_module_exercise_ch11_sec2():\n",
        "  # [JP_PY_COMMENT_CH11_SEC2_AS_IMPORT_MATH_PH]\n",
        "  # [JP_PY_COMMENT_CH11_SEC2_AS_PRINT_PI_SQRT_PH]\n",
        "  pass\n",
        "# import_math_module_exercise_ch11_sec2()"
        ], "outputs": [], "execution_count": None },
    { # Check code 11.2
      "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH11_SEC2_PH]"}, "source": ["#@title [JP_CHECK_TITLE_CH11_SEC2_PH] { display-mode: \"form\" }\n", "print(\"[JP_CHECK_TEXT_CH11_SEC2_PH]\")"], "outputs": [], "execution_count": None },
    { # Solution 11.2
      "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}}, "source": [
        "def import_math_module_exercise_ch11_sec2_solution():\n",
        "  import math\n",
        "  print(f\"円周率 (math.pi): {math.pi}\")\n",
        "  print(f\"16の平方根 (math.sqrt(16)): {math.sqrt(16)}\")\n",
        "import_math_module_exercise_ch11_sec2_solution()"
        ], "outputs": [], "execution_count": None },

    # Section 11.3: 標準ライブラリの便利なモジュール (Useful modules in the Standard Library)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH11_SEC3_TITLE_PH]\n\n",
        "[JP_MD_CH11_SEC3_EXPLAIN_P1_PH]\n",
        "*   **`math`**: [JP_MD_CH11_SEC3_MATH_DESC_PH]\n",
        "*   **`random`**: [JP_MD_CH11_SEC3_RANDOM_DESC_PH]\n",
        "*   **`datetime`**: [JP_MD_CH11_SEC3_DATETIME_DESC_PH]\n",
        "*   **`os`**: [JP_MD_CH11_SEC3_OS_DESC_PH]\n",
        "*   **`json`**: [JP_MD_CH11_SEC3_JSON_DESC_PH]"
      ]
    },
    { # Exercise 11.3
      "cell_type": "markdown", "metadata": {}, "source": ["### [JP_MD_CH11_SEC3_EX_TITLE_PH]\n\n","[JP_MD_CH11_SEC3_EX_PROMPT_PH]"]},
    { # Answer Space 11.3
      "cell_type": "code", "metadata": {}, "source": [
        "def useful_modules_exercise_ch11_sec3():\n",
        "  # [JP_PY_COMMENT_CH11_SEC3_AS_IMPORT_PH]\n",
        "  # [JP_PY_COMMENT_CH11_SEC3_AS_DICE_ROLL_PH]\n",
        "  # [JP_PY_COMMENT_CH11_SEC3_AS_CURRENT_DATETIME_PH]\n",
        "  pass\n",
        "# useful_modules_exercise_ch11_sec3()"
        ], "outputs": [], "execution_count": None },
    { # Check code 11.3
      "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH11_SEC3_PH]"}, "source": ["#@title [JP_CHECK_TITLE_CH11_SEC3_PH] { display-mode: \"form\" }\n", "print(\"[JP_CHECK_TEXT_CH11_SEC3_PH]\")"], "outputs": [], "execution_count": None },
    { # Solution 11.3
      "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}}, "source": [
        "def useful_modules_exercise_ch11_sec3_solution():\n",
        "  import random\n",
        "  import datetime\n",
        "  dice_roll = random.randint(1, 6)\n",
        "  print(f\"サイコロの目: {dice_roll}\")\n",
        "  now = datetime.datetime.now()\n",
        "  print(f\"現在の日時: {now}\")\n",
        "useful_modules_exercise_ch11_sec3_solution()"
        ], "outputs": [], "execution_count": None },

    # Section 11.4: パッケージとは？ (What are packages?)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH11_SEC4_TITLE_PH]\n\n",
        "[JP_MD_CH11_SEC4_EXPLAIN_P1_PH]\n",
        "[JP_MD_CH11_SEC4_EXPLAIN_P2_PH]"
      ]
    },
    { # Exercise 11.4
      "cell_type": "markdown", "metadata": {}, "source": ["### [JP_MD_CH11_SEC4_EX_TITLE_PH]\n\n","[JP_MD_CH11_SEC4_EX_PROMPT_PH]"]},
    { # Answer Space 11.4
      "cell_type": "markdown", "metadata": {}, "source": ["[JP_MD_CH11_SEC4_AS_PROMPT_PH]"]},
    { # Solution 11.4
      "cell_type": "markdown", "metadata": {"jupyter": {"source_hidden": True}}, "source": ["---<details><summary>[JP_MD_CH11_SEC4_SOL_SUMMARY_PH]</summary>\n\n","[JP_MD_CH11_SEC4_SOL_DETAIL_PH]\n","</details>"]}
]

try:
    print(f"Python script to append Ch11 skeleton. Notebook path: {os.path.abspath(notebook_path)}")

    base_dir = "/app"
    full_notebook_path = os.path.join(base_dir, notebook_path.lstrip('/'))

    notebook_dir = os.path.dirname(full_notebook_path)
    if not os.path.exists(notebook_dir):
        os.makedirs(notebook_dir)
        print(f"Created directory: {notebook_dir}")

    if not os.path.exists(full_notebook_path):
        print(f"Error: Notebook file '{full_notebook_path}' not found. It should contain Chapters 1-10.")
        # Initialize with empty notebook structure if it doesn't exist.
        notebook_data = {
            "cells": [],
            "metadata": {
                "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                "language_info": {"name": "python", "version": "3.10.12"}
            },
            "nbformat": 4,
            "nbformat_minor": 5
        }
        print("Notebook not found, creating a new basic structure.")
    else:
        with open(full_notebook_path, 'r', encoding='utf-8') as f:
            notebook_data = json.load(f)
        print("Existing notebook (Chapters 1-10) loaded successfully.")

    notebook_data['cells'].extend(chapter11_cells)
    print(f"Appended {len(chapter11_cells)} cells for Chapter 11 skeleton.")

    with open(full_notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook_data, f, ensure_ascii=False, indent=2)
    print(f"Successfully appended Chapter 11 skeleton to {full_notebook_path}")
    print(f"File {full_notebook_path} exists. Size: {os.path.getsize(full_notebook_path)}")

except FileNotFoundError:
    print(f"Error - File Not Found (unexpected): {notebook_path}")
except json.JSONDecodeError as json_error:
    print(f"Error - JSON Decode Error: {json_error}")
except Exception as e:
    print(f"Script execution error: {e}")
