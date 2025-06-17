import json
import os

notebook_path = 'src/beginner.ipynb'

# Define the cells for Chapter 2
chapter2_cells = [
    # Cell 1: Markdown (Chapter Title, Sec 2.1 Title & Explanation)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# [JP_MD_CH2_TITLE_PH]\n\n",
        "[JP_MD_CH2_INTRO_P1_PH]\n\n",
        "## [JP_MD_CH2_SEC1_TITLE_PH]\n\n",
        "**[JP_MD_CH2_SEC1_VAR_DEF_TITLE_PH]** [JP_MD_CH2_SEC1_VAR_DEF_TEXT_PH]\n\n",
        "**[JP_MD_CH2_SEC1_PURPOSE_TITLE_PH]**\n",
        "[JP_MD_CH2_SEC1_PURPOSE_TEXT_PH]\n\n",
        "**[JP_MD_CH2_SEC1_NAMING_TITLE_PH]**\n",
        "[JP_MD_CH2_SEC1_NAMING_TEXT_PH]"
      ]
    },
    # Cell 2: Markdown (Exercise 2.1)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH2_SEC1_EX_TITLE_PH]\n\n",
        "[JP_MD_CH2_SEC1_EX_PROMPT_PH]"
      ]
    },
    # Cell 3: Markdown (Answer Space 2.1)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "[JP_MD_CH2_SEC1_AS_PROMPT_PH]\n\n",
        "**[JP_MD_CH2_SEC1_AS_VALID_LABEL_PH]**\n",
        "1. \n2. \n3. \n\n",
        "**[JP_MD_CH2_SEC1_AS_INVALID_LABEL_PH]**\n",
        "1. [JP_MD_CH2_SEC1_AS_INVALID1_NAME_PH]\n",
        "   [JP_MD_CH2_SEC1_AS_REASON_LABEL_PH]\n",
        "2. [JP_MD_CH2_SEC1_AS_INVALID2_NAME_PH]\n",
        "   [JP_MD_CH2_SEC1_AS_REASON_LABEL_PH]"
      ]
    },
    # Cell 4: Markdown (Solution 2.1 - hidden)
    {
      "cell_type": "markdown",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "---<details><summary>[JP_MD_CH2_SEC1_SOL_SUMMARY_PH]</summary>\n\n",
        "[JP_MD_CH2_SEC1_SOL_DETAIL_PH]\n",
        "</details>"
      ]
    },
    # Cell 5: Markdown (Sec 2.2 Title & Explanation)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH2_SEC2_TITLE_PH]\n\n",
        "[JP_MD_CH2_SEC2_P1_PH]\n",
        "1.  **[JP_MD_CH2_SEC2_TYPE1_NAME_PH]** ([JP_MD_CH2_SEC2_TYPE1_CODE_PH]): [JP_MD_CH2_SEC2_TYPE1_DESC_PH]\n",
        "2.  **[JP_MD_CH2_SEC2_TYPE2_NAME_PH]** ([JP_MD_CH2_SEC2_TYPE2_CODE_PH]): [JP_MD_CH2_SEC2_TYPE2_DESC_PH]\n",
        "3.  **[JP_MD_CH2_SEC2_TYPE3_NAME_PH]** ([JP_MD_CH2_SEC2_TYPE3_CODE_PH]): [JP_MD_CH2_SEC2_TYPE3_DESC_PH]\n",
        "4.  **[JP_MD_CH2_SEC2_TYPE4_NAME_PH]** ([JP_MD_CH2_SEC2_TYPE4_CODE_PH]): [JP_MD_CH2_SEC2_TYPE4_DESC_PH]\n\n",
        "[JP_MD_CH2_SEC2_P2_PH]"
      ]
    },
    # Cell 6: Markdown (Exercise 2.2)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH2_SEC2_EX_TITLE_PH]\n\n",
        "[JP_MD_CH2_SEC2_EX_PROMPT_PH]"
      ]
    },
    # Cell 7: Code (Answer Space 2.2)
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def my_profile_data():\n",
        "  # [JP_PY_COMMENT_CH2_SEC2_AS_PROMPT_PH]\n",
        "  # my_name = \"[JP_PY_COMMENT_CH2_SEC2_AS_NAME_PH]\"\n",
        "  # my_age = 0 # [JP_PY_COMMENT_CH2_SEC2_AS_AGE_PH]\n",
        "  # favorite_pi = 3.14 # [JP_PY_COMMENT_CH2_SEC2_AS_PI_PH]\n",
        "  # has_programming_experience = False # [JP_PY_COMMENT_CH2_SEC2_AS_EXP_PH]\n",
        "  # print(\"[JP_PY_COMMENT_CH2_SEC2_AS_PRINT_LABEL_PH]\", my_name, my_age, favorite_pi, has_programming_experience)\n",
        "  pass\n",
        "# my_profile_data() # [JP_PY_COMMENT_CH2_SEC2_AS_CALL_FUNC_PH]"
      ],
      "outputs": [], "execution_count": None
    },
    # Cell 8: Code (Check Code 2.2 - hidden)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH2_SEC2_PH]"}, # Added title here for consistency
      "source": [
        "#@title [JP_CHECK_TITLE_CH2_SEC2_PH] { display-mode: \"form\" }\n",
        "print(\"[JP_CHECK_TEXT_CH2_SEC2_PH]\")"
      ],
      "outputs": [], "execution_count": None
    },
    # Cell 9: Code (Solution 2.2 - hidden)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "def my_profile_data_solution():\n",
        "  my_name = \"鈴木一郎\"\n",
        "  my_age = 28\n",
        "  favorite_pi = 3.14159\n",
        "  has_programming_experience = True\n",
        "  print(\"名前:\", my_name)\n",
        "  print(\"年齢:\", my_age)\n",
        "  print(\"好きな円周率の近似値:\", favorite_pi)\n",
        "  print(\"プログラミング経験:\", has_programming_experience)\n",
        "my_profile_data_solution()"
      ],
      "outputs": [], "execution_count": None
    },
    # Cell 10: Markdown (Sec 2.3 Title & Explanation)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH2_SEC3_TITLE_PH]\n\n",
        "[JP_MD_CH2_SEC3_P1_PH]\n\n",
        "**[JP_MD_CH2_SEC3_SYNTAX_TITLE_PH]**\n",
        "`[JP_MD_CH2_SEC3_SYNTAX_CODE_PH]`\n\n",
        "[JP_MD_CH2_SEC3_P2_PH]\n",
        "```python\n",
        "age = 30\n",
        "```\n",
        "[JP_MD_CH2_SEC3_P3_PH]\n",
        "```python\n",
        "score = 85\n",
        "print(score) # [JP_MD_CH2_SEC3_PRINT_SCORE_COMMENT_PH]\n",
        "```\n\n",
        "**[JP_MD_CH2_SEC3_REASSIGN_TITLE_PH]**\n",
        "[JP_MD_CH2_SEC3_REASSIGN_P1_PH]\n",
        "```python\n",
        "message = \"おはよう\"\n",
        "print(message) # [JP_MD_CH2_SEC3_PRINT_OHAYO_COMMENT_PH]\n",
        "message = \"こんにちは\" # [JP_MD_CH2_SEC3_REASSIGN_MESSAGE_COMMENT_PH]\n",
        "print(message) # [JP_MD_CH2_SEC3_PRINT_KONNICHIWA_COMMENT_PH]\n",
        "```\n",
        "[JP_MD_CH2_SEC3_REASSIGN_P2_PH]"
      ]
    },
    # Cell 11: Markdown (Exercise 2.3)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH2_SEC3_EX_TITLE_PH]\n\n",
        "[JP_MD_CH2_SEC3_EX_PROMPT_P1_PH]\n",
        "1. [JP_MD_CH2_SEC3_EX_STEP1_PH]\n",
        "2. [JP_MD_CH2_SEC3_EX_STEP2_PH]\n",
        "3. [JP_MD_CH2_SEC3_EX_STEP3_PH]\n",
        "4. [JP_MD_CH2_SEC3_EX_STEP4_PH]"
      ]
    },
    # Cell 12: Code (Answer Space 2.3)
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def reassign_language_variable():\n",
        "  # [JP_PY_COMMENT_CH2_SEC3_AS_STEP1_PH]\n",
        "  # favorite_language = \"Python\"\n",
        "  # [JP_PY_COMMENT_CH2_SEC3_AS_STEP2_PH]\n",
        "  # print(favorite_language)\n",
        "  # [JP_PY_COMMENT_CH2_SEC3_AS_STEP3_PH]\n",
        "  # favorite_language = \"JavaScript\"\n",
        "  # [JP_PY_COMMENT_CH2_SEC3_AS_STEP4_PH]\n",
        "  # print(favorite_language)\n",
        "  pass\n",
        "# reassign_language_variable() # [JP_PY_COMMENT_CH2_SEC3_AS_CALL_FUNC_PH]"
      ],
      "outputs": [], "execution_count": None
    },
    # Cell 13: Code (Check Code 2.3 - hidden)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH2_SEC3_PH]"},
      "source": [
        "#@title [JP_CHECK_TITLE_CH2_SEC3_PH] { display-mode: \"form\" }\n",
        "print(\"[JP_CHECK_TEXT_CH2_SEC3_PH]\")"
      ],
      "outputs": [], "execution_count": None
    },
    # Cell 14: Code (Solution 2.3 - hidden)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "def reassign_language_variable_solution():\n",
        "  favorite_language = \"Python\"\n",
        "  print(favorite_language)\n",
        "  favorite_language = \"JavaScript\"\n",
        "  print(favorite_language)\n",
        "reassign_language_variable_solution()"
      ],
      "outputs": [], "execution_count": None
    },
    # Cell 15: Markdown (Sec 2.4 Title & Explanation)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH2_SEC4_TITLE_PH]\n\n",
        "[JP_MD_CH2_SEC4_P1_PH]\n\n",
        "**[JP_MD_CH2_SEC4_TYPECHECK_TITLE_PH]**\n",
        "[JP_MD_CH2_SEC4_TYPECHECK_P1_PH]\n",
        "```python\n",
        "age = 30\n",
        "print(type(age)) # [JP_MD_CH2_SEC4_TYPECHECK_EXAMPLE1_COMMENT_PH]\n",
        "name = \"Alice\"\n",
        "print(type(name)) # [JP_MD_CH2_SEC4_TYPECHECK_EXAMPLE2_COMMENT_PH]\n",
        "```\n",
        "[JP_MD_CH2_SEC4_TYPECHECK_P2_PH]\n\n",
        "**[JP_MD_CH2_SEC4_CONVERSION_TITLE_PH]**\n",
        "[JP_MD_CH2_SEC4_CONVERSION_P1_PH]\n",
        "*   `int(value)`: [JP_MD_CH2_SEC4_CONV_INT_DESC_PH]\n",
        "*   `float(value)`: [JP_MD_CH2_SEC4_CONV_FLOAT_DESC_PH]\n",
        "*   `str(value)`: [JP_MD_CH2_SEC4_CONV_STR_DESC_PH]\n",
        "*   `bool(value)`: [JP_MD_CH2_SEC4_CONV_BOOL_DESC_PH]\n\n",
        "```python\n",
        "num_string = \"123\"\n",
        "num_int = int(num_string)\n",
        "print(num_int + 100) # [JP_MD_CH2_SEC4_CONV_EXAMPLE1_COMMENT_PH]\n",
        "```\n",
        "[JP_MD_CH2_SEC4_CONVERSION_P2_PH]"
      ]
    },
    # Cell 16: Markdown (Exercise 2.4)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH2_SEC4_EX_TITLE_PH]\n\n",
        "[JP_MD_CH2_SEC4_EX_PROMPT_P1_PH]\n",
        "1. [JP_MD_CH2_SEC4_EX_STEP1_PH]\n",
        "2. [JP_MD_CH2_SEC4_EX_STEP2_PH]\n",
        "3. [JP_MD_CH2_SEC4_EX_STEP3_PH]"
      ]
    },
    # Cell 17: Code (Answer Space 2.4)
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def type_conversion_calculation():\n",
        "  price_string = \"1980.5\"\n",
        "  quantity = 3\n",
        "  # [JP_PY_COMMENT_CH2_SEC4_AS_STEP1_PH]\n",
        "  # price_float = float(price_string)\n",
        "  # print(type(price_float), price_float)\n",
        "  # [JP_PY_COMMENT_CH2_SEC4_AS_STEP2_PH]\n",
        "  # quantity_str = str(quantity)\n",
        "  # print(type(quantity_str), quantity_str)\n",
        "  # [JP_PY_COMMENT_CH2_SEC4_AS_STEP3_PH]\n",
        "  # total_amount = price_float * quantity\n",
        "  # print(\"[JP_PY_COMMENT_CH2_SEC4_AS_TOTAL_LABEL_PH]\", total_amount)\n",
        "  pass\n",
        "# type_conversion_calculation() # [JP_PY_COMMENT_CH2_SEC4_AS_CALL_FUNC_PH]"
      ],
      "outputs": [], "execution_count": None
    },
    # Cell 18: Code (Check Code 2.4 - hidden)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH2_SEC4_PH]"},
      "source": [
        "#@title [JP_CHECK_TITLE_CH2_SEC4_PH] { display-mode: \"form\" }\n",
        "print(\"[JP_CHECK_TEXT_CH2_SEC4_PH]\")"
      ],
      "outputs": [], "execution_count": None
    },
    # Cell 19: Code (Solution 2.4 - hidden)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "def type_conversion_calculation_solution():\n",
        "  price_string = \"1980.5\"\n",
        "  quantity = 3\n",
        "  price_float = float(price_string)\n",
        "  print(\"price_float の型:\", type(price_float), \"値:\", price_float)\n",
        "  quantity_str = str(quantity)\n",
        "  print(\"quantity_str の型:\", type(quantity_str), \"値:\", quantity_str)\n",
        "  total_amount = price_float * quantity\n",
        "  print(\"合計金額:\", total_amount)\n",
        "type_conversion_calculation_solution()"
      ],
      "outputs": [], "execution_count": None
    }
]

try:
    print(f"Python script to append Chapter 2 skeleton. Notebook path: {os.path.abspath(notebook_path)}")

    # Ensure the /app/src directory exists
    # The path in the notebook_path is relative to /app for the script's execution context
    base_dir = "/app" # Assuming script runs from /app or has access to /app
    full_notebook_path = os.path.join(base_dir, notebook_path.lstrip('/'))

    # Create directory if it doesn't exist
    notebook_dir = os.path.dirname(full_notebook_path)
    if not os.path.exists(notebook_dir):
        os.makedirs(notebook_dir)
        print(f"Created directory: {notebook_dir}")


    if not os.path.exists(full_notebook_path):
        print(f"Error: Notebook file '{full_notebook_path}' not found. It should contain Chapter 1.")
        # If Ch1 doesn't exist, we can't append, so exit or create a new notebook with Ch1&Ch2.
        # For this subtask, we assume Ch1 exists. If it might not, the logic to create a new notebook
        # with Ch1 skeleton first would be needed here.
        exit(1)

    with open(full_notebook_path, 'r', encoding='utf-8') as f:
        notebook_data = json.load(f)
    print("Existing notebook (Chapter 1) loaded successfully.")

    # Append Chapter 2 cells
    notebook_data['cells'].extend(chapter2_cells)
    print(f"Appended {len(chapter2_cells)} cells for Chapter 2 skeleton.")

    with open(full_notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook_data, f, ensure_ascii=False, indent=2)
    print(f"Successfully appended Chapter 2 skeleton to {full_notebook_path}")

    # Verification print
    print(f"File {full_notebook_path} exists. Size: {os.path.getsize(full_notebook_path)}")


except FileNotFoundError as fnf_error:
    print(f"Error - File Not Found: {fnf_error}")
except json.JSONDecodeError as json_error:
    print(f"Error - JSON Decode Error: {json_error}")
except Exception as e:
    print(f"Script execution error: {e}")
