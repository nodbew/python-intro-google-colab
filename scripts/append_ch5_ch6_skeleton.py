import json
import os

notebook_path = 'src/beginner.ipynb'

# Define the cells for Chapter 5
chapter5_cells = [
    # CHAPTER 5 Header
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# [JP_MD_CH5_TITLE_PH]\n\n",
        "[JP_MD_CH5_INTRO_P1_PH]\n\n",
        "## [JP_MD_CH5_SEC1_TITLE_PH]\n\n",
        "[JP_MD_CH5_SEC1_P1_PH]\n\n",
        "**[JP_MD_CH5_SEC1_MERITS_TITLE_PH]**\n",
        "[JP_MD_CH5_SEC1_MERITS_LIST_PH]\n\n",
        "**[JP_MD_CH5_SEC1_REALWORLD_TITLE_PH]**\n",
        "[JP_MD_CH5_SEC1_REALWORLD_P1_PH]\n",
        "[JP_MD_CH5_SEC1_REALWORLD_P2_PH]"
      ]
    },
    # Section 5.1 Exercise
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH5_SEC1_EX_TITLE_PH]\n\n",
        "[JP_MD_CH5_SEC1_EX_PROMPT_PH]\n",
        "([JP_MD_CH5_SEC1_EX_EXAMPLE_LABEL_PH]: [JP_MD_CH5_SEC1_EX_EXAMPLE_TEXT_PH])"
      ]
    },
    # Section 5.1 Answer Space
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "[JP_MD_CH5_SEC1_AS_PROMPT_PH]\n\n",
        "**[JP_MD_CH5_SEC1_AS_WORK1_LABEL_PH]**\n",
        "*   [JP_MD_CH5_SEC1_AS_STEP_LABEL_PH]\n\n",
        "**[JP_MD_CH5_SEC1_AS_WORK2_LABEL_PH]**\n",
        "*   [JP_MD_CH5_SEC1_AS_STEP_LABEL_PH]"
      ]
    },
    # Section 5.1 Solution (hidden)
    {
      "cell_type": "markdown",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "---<details><summary>[JP_MD_CH5_SEC1_SOL_SUMMARY_PH]</summary>\n\n",
        "[JP_MD_CH5_SEC1_SOL_DETAIL_PH]\n",
        "</details>"
      ]
    },
    # Section 5.2 Explanation
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH5_SEC2_TITLE_PH]\n\n",
        "[JP_MD_CH5_SEC2_P1_PH]\n\n",
        "**[JP_MD_CH5_SEC2_DEF_TITLE_PH]**\n",
        "[JP_MD_CH5_SEC2_DEF_P1_PH]\n\n",
        "**[JP_MD_CH5_SEC2_DEF_SYNTAX_TITLE_PH]**\n",
        "```python\n",
        "def function_name_placeholder():\n",
        "    # [JP_PY_COMMENT_CH5_SEC2_PROCESS_HERE_PH]\n",
        "    pass\n",
        "```\n",
        "[JP_MD_CH5_SEC2_SYNTAX_DESC_PH]\n\n",
        "**[JP_MD_CH5_SEC2_DEF_EXAMPLE_TITLE_PH]**\n",
        "```python\n",
        "def say_hello_placeholder():\n",
        "    print(\"[JP_PY_STRING_CH5_SEC2_HELLO_EVERYONE_PH]\")\n",
        "    print(\"[JP_PY_STRING_CH5_SEC2_WELCOME_PYTHON_PH]\")\n",
        "```\n",
        "[JP_MD_CH5_SEC2_DEF_EXAMPLE_P1_PH]\n\n",
        "**[JP_MD_CH5_SEC2_CALL_TITLE_PH]**\n",
        "[JP_MD_CH5_SEC2_CALL_P1_PH]\n\n",
        "**[JP_MD_CH5_SEC2_CALL_SYNTAX_TITLE_PH]**\n",
        "`function_name_placeholder()`\n\n",
        "**[JP_MD_CH5_SEC2_CALL_EXAMPLE_TITLE_PH]**\n",
        "```python\n",
        "# [JP_PY_COMMENT_CH5_SEC2_ASSUME_DEFINED_PH]\n",
        "say_hello_placeholder() # [JP_PY_COMMENT_CH5_SEC2_EXECUTES_BODY_PH]\n",
        "```\n",
        "[JP_MD_CH5_SEC2_CALL_EXAMPLE_P1_PH]"
      ]
    },
    # Section 5.2 Exercise
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": ["### [JP_MD_CH5_SEC2_EX_TITLE_PH]\n\n", "[JP_MD_CH5_SEC2_EX_PROMPT_PH]"]
    },
    # Section 5.2 Answer Space (Code)
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def define_and_call_display_weather():\n",
        "  # [JP_PY_COMMENT_CH5_SEC2_AS_DEFINE_PH]\n",
        "  # def display_weather():\n",
        "  #   print(\"今日の天気は晴れです。\")\n",
        "  \n",
        "  # [JP_PY_COMMENT_CH5_SEC2_AS_CALL_PH]\n",
        "  # display_weather()\n",
        "  pass\n",
        "\n",
        "# [JP_PY_COMMENT_CH5_SEC2_AS_CALL_MAIN_PH]\n",
        "# define_and_call_display_weather()"
      ],
      "outputs": [], "execution_count": None
    },
    # Section 5.2 Check Code (Code - hidden)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH5_SEC2_PH]"},
      "source": [
        "#@title [JP_CHECK_TITLE_CH5_SEC2_PH] { display-mode: \"form\" }\n",
        "print(\"[JP_CHECK_TEXT_CH5_SEC2_PH]\")"
      ],
      "outputs": [], "execution_count": None
    },
    # Section 5.2 Solution (Code - hidden, Japanese content)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "def define_and_call_display_weather_solution():\n",
        "  def display_weather():\n",
        "    print(\"今日の天気は快晴です！素晴らしい一日になりそうですね。\")\n",
        "  display_weather()\n",
        "define_and_call_display_weather_solution()"
      ],
      "outputs": [], "execution_count": None
    },
    # Placeholder for sections 5.3, 5.4, 5.5
    { "cell_type": "markdown", "metadata": {}, "source": [ "<!-- Placeholder for full skeleton of Chapter 5 Section 3 (Arguments) with MD placeholders & JP code -->" ] },
    { "cell_type": "markdown", "metadata": {}, "source": [ "<!-- Placeholder for full skeleton of Chapter 5 Section 4 (Return values) with MD placeholders & JP code -->" ] },
    { "cell_type": "markdown", "metadata": {}, "source": [ "<!-- Placeholder for full skeleton of Chapter 5 Section 5 (Scope) with MD placeholders & JP code -->" ] },
    # Section 5.6 Explanation
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH5_SEC6_TITLE_PH]\n\n",
        "[JP_MD_CH5_SEC6_P1_PH]\n\n",
        "**[JP_MD_CH5_SEC6_PURPOSE_TITLE_PH]**\n",
        "[JP_MD_CH5_SEC6_PURPOSE_LIST_PH]\n\n",
        "**[JP_MD_CH5_SEC6_EXAMPLE_TITLE_PH]**\n",
        "```python\n",
        "def simple_greet_placeholder():\n",
        "    '''[JP_PY_DOCSTRING_CH5_SEC6_SIMPLE_GREET_PH]'''\n",
        "    print(\"[JP_PY_STRING_CH5_SEC6_HELLO_PH]\")\n",
        "\n",
        "help(simple_greet_placeholder) # [JP_PY_COMMENT_CH5_SEC6_SHOWS_DOCSTRING_PH]\n",
        "```\n",
        "[JP_MD_CH5_SEC6_P2_PH]"
      ]
    },
    # Section 5.6 Exercise
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": ["### [JP_MD_CH5_SEC6_EX_TITLE_PH]\n\n", "[JP_MD_CH5_SEC6_EX_PROMPT_PH]"]
    },
    # Section 5.6 Answer Space (Code)
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def docstring_practice():\n",
        "  # [JP_PY_COMMENT_CH5_SEC6_AS_REDEFINE_FUNC_PH]\n",
        "  # def calculate_rectangle_area(width, height):\n",
        "  #   '''[JP_PY_COMMENT_CH5_SEC6_AS_ADD_DOCSTRING_PH]'''\n",
        "  #   area = width * height\n",
        "  #   return area\n",
        "  \n",
        "  # [JP_PY_COMMENT_CH5_SEC6_AS_CALL_HELP_PH]\n",
        "  # help(calculate_rectangle_area)\n",
        "  pass\n",
        "\n",
        "# [JP_PY_COMMENT_CH5_SEC6_AS_CALL_MAIN_PH]\n",
        "# docstring_practice()"
      ],
      "outputs": [], "execution_count": None
    },
    # Section 5.6 Check Code (Code - hidden)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH5_SEC6_PH]"},
      "source": [
        "#@title [JP_CHECK_TITLE_CH5_SEC6_PH] { display-mode: \"form\" }\n",
        "print(\"[JP_CHECK_TEXT_CH5_SEC6_PH]\")"
      ],
      "outputs": [], "execution_count": None
    },
    # Section 5.6 Solution (Code - hidden, Japanese content)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "def docstring_practice_solution():\n",
        "  def calculate_rectangle_area(width, height):\n",
        "    '''長方形の面積を計算して返します。\n",
        "\n",
        "    この関数は、指定された幅と高さに基づいて長方形の面積を求めます。\n",
        "\n",
        "    Args:\n",
        "        width (int or float): 長方形の幅。正の数値を期待します。\n",
        "        height (int or float): 長方形の高さ。正の数値を期待します。\n",
        "\n",
        "    Returns:\n",
        "        int or float: 計算された長方形の面積。\n",
        "    '''\n",
        "    if width < 0 or height < 0:\n",
        "        print(\"エラー：幅と高さは正の数値である必要があります。\")\n",
        "        return None \n",
        "    area = width * height\n",
        "    return area\n",
        "  help(calculate_rectangle_area)\n",
        "docstring_practice_solution()"
      ],
      "outputs": [], "execution_count": None
    }
]

# Define the cells for Chapter 6
chapter6_cells = [
    # CHAPTER 6 Header
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# [JP_MD_CH6_TITLE_PH]\n\n",
        "[JP_MD_CH6_INTRO_P1_PH]\n",
        "[JP_MD_CH6_INTRO_P2_PH]"
      ]
    },
    # Section 6.1 Explanation
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH6_SEC1_TITLE_PH]\n\n",
        "[JP_MD_CH6_SEC1_EXPLAIN_P1_PH]\n",
        "[JP_MD_CH6_SEC1_EXPLAIN_P2_PH]\n",
        "*   [JP_MD_CH6_SEC1_EXPLAIN_ITEM1_PH]\n",
        "*   [JP_MD_CH6_SEC1_EXPLAIN_ITEM2_PH]\n",
        "*   [JP_MD_CH6_SEC1_EXPLAIN_ITEM3_PH]\n",
        "[JP_MD_CH6_SEC1_EXPLAIN_P3_PH]\n",
        "```python\n",
        "# [JP_PY_COMMENT_CH6_LIST_EXAMPLE_PH]\n",
        "my_list_placeholder = [1, \"apple_placeholder\", True]\n",
        "print(my_list_placeholder[1]) # [JP_PY_COMMENT_CH6_ACCESS_APPLE_PH]\n",
        "my_list_placeholder.append(\"orange_placeholder\")\n",
        "print(my_list_placeholder)\n",
        "```"
      ]
    },
    # Section 6.1 Exercise
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH6_SEC1_EX_TITLE_PH]\n\n",
        "[JP_MD_CH6_SEC1_EX_TEXT_P1_PH]\n",
        "`colors = [\"赤\", \"青\", \"緑\"]` [JP_MD_CH6_SEC1_EX_TEXT_P2_PH]\n",
        "1.  [JP_MD_CH6_SEC1_EX_STEP1_PH]\n",
        "2.  [JP_MD_CH6_SEC1_EX_STEP2_PH]\n",
        "3.  [JP_MD_CH6_SEC1_EX_STEP3_PH]\n",
        "4.  [JP_MD_CH6_SEC1_EX_STEP4_PH]"
      ]
    },
    # Section 6.1 Answer Space (Code)
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def list_manipulation_practice():\n",
        "  colors = [\"赤\", \"青\", \"緑\"] # [JP_PY_COMMENT_CH6_SEC1_AS_INITIAL_LIST_PH]\n",
        "  # [JP_PY_COMMENT_CH6_SEC1_AS_STEP1_PH]\n",
        "  # colors.append(\"黄色\")\n",
        "  # [JP_PY_COMMENT_CH6_SEC1_AS_STEP2_PH]\n",
        "  # colors[1] = \"紫\"\n",
        "  # [JP_PY_COMMENT_CH6_SEC1_AS_STEP3_PH]\n",
        "  # if \"青\" in colors: colors.remove(\"青\")\n",
        "  # [JP_PY_COMMENT_CH6_SEC1_AS_STEP4_PH]\n",
        "  # print(colors)\n",
        "  pass\n",
        "# list_manipulation_practice() # [JP_PY_COMMENT_CH6_SEC1_AS_CALL_FUNC_PH]"
      ],
      "outputs": [], "execution_count": None
    },
    # Section 6.1 Check Code (Code - hidden)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH6_SEC1_PH]"},
      "source": [
        "#@title [JP_CHECK_TITLE_CH6_SEC1_PH] { display-mode: \"form\" }\n",
        "print(\"[JP_CHECK_TEXT_CH6_SEC1_PH]\")"
      ],
      "outputs": [], "execution_count": None
    },
    # Section 6.1 Solution (Code - hidden, Japanese content)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "def list_manipulation_practice_solution():\n",
        "  colors = [\"赤\", \"青\", \"緑\"]\n",
        "  print(f\"初期リスト: {colors}\")\n",
        "  colors.append(\"黄色\")\n",
        "  print(f\"黄色を追加後: {colors}\")\n",
        "  colors[1] = \"紫\" \n",
        "  print(f\"2番目を紫に変更後: {colors}\")\n",
        "  if \"青\" in colors: \n",
        "    colors.remove(\"青\")\n",
        "    print(f\"青を削除後: {colors}\")\n",
        "  print(f\"最終的なリスト: {colors}\")\n",
        "list_manipulation_practice_solution()"
      ],
      "outputs": [], "execution_count": None
    },
    # Section 6.2 Explanation
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH6_SEC2_TITLE_PH]\n\n",
        "[JP_MD_CH6_SEC2_EXPLAIN_P1_PH]\n",
        "[JP_MD_CH6_SEC2_EXPLAIN_P2_PH]"
      ]
    },
    # Section 6.2 Exercise
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH6_SEC2_EX_TITLE_PH]\n\n",
        "[JP_MD_CH6_SEC2_EX_TEXT_P1_PH]\n",
        "`point = (30, 50)`\n",
        "[JP_MD_CH6_SEC2_EX_TEXT_P2_PH]"
      ]
    },
    # Section 6.2 Answer Space (Code)
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def tuple_unpacking_exercise():\n",
        "  # [JP_PY_COMMENT_CH6_SEC2_AS_POINT_TUPLE_PH]\n",
        "  # point = (30, 50)\n",
        "  # [JP_PY_COMMENT_CH6_SEC2_AS_UNPACK_PH]\n",
        "  # x_coord, y_coord = point\n",
        "  # [JP_PY_COMMENT_CH6_SEC2_AS_PRINT_PH]\n",
        "  # print(f\"X座標： {x_coord}, Y座標： {y_coord}\")\n",
        "  # [JP_PY_COMMENT_CH6_SEC2_AS_ERROR_TEST_PH]\n",
        "  # point[0] = 40 # この行はエラーになります\n",
        "  pass\n",
        "# tuple_unpacking_exercise() # [JP_PY_COMMENT_CH6_SEC2_AS_CALL_FUNC_PH]"
      ],
      "outputs": [], "execution_count": None
    },
    # Section 6.2 Check Code (Code - hidden)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH6_SEC2_PH]"},
      "source": [
        "#@title [JP_CHECK_TITLE_CH6_SEC2_PH] { display-mode: \"form\" }\n",
        "print(\"[JP_CHECK_TEXT_CH6_SEC2_PH]\")"
      ],
      "outputs": [], "execution_count": None
    },
    # Section 6.2 Solution (Code - hidden, Japanese content)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "def tuple_unpacking_solution():\n",
        "  point = (30, 50)\n",
        "  x_coord, y_coord = point\n",
        "  print(f\"X座標： {x_coord}, Y座標： {y_coord}\")\n",
        "  # point[0] = 40 # この行を実行しようとすると TypeError が発生します。\n",
        "  print(\"タプルの値を変更しようとするとエラーが発生します (コメントアウトされています)。\")\n",
        "tuple_unpacking_solution()"
      ],
      "outputs": [], "execution_count": None
    },
    # Placeholder for sections 6.3, 6.4
    { "cell_type": "markdown", "metadata": {}, "source": [ "<!-- Placeholder for full skeleton of Chapter 6 Section 3 (Dictionaries) with MD placeholders & JP code -->" ] },
    { "cell_type": "markdown", "metadata": {}, "source": [ "<!-- Placeholder for full skeleton of Chapter 6 Section 4 (Sets) with MD placeholders & JP code -->" ] }
]

try:
    print(f"Python script to append Chapters 5 & 6 skeletons. Notebook path: {os.path.abspath(notebook_path)}")

    base_dir = "/app"
    full_notebook_path = os.path.join(base_dir, notebook_path.lstrip('/'))

    notebook_dir = os.path.dirname(full_notebook_path)
    if not os.path.exists(notebook_dir):
        os.makedirs(notebook_dir)
        print(f"Created directory: {notebook_dir}")

    if not os.path.exists(full_notebook_path):
        print(f"Error: Notebook file '{full_notebook_path}' not found. It should contain Chapters 1-4.")
        notebook_data = {
            "cells": [],
            "metadata": {
                "kernelspec": { "display_name": "Python 3", "language": "python", "name": "python3" },
                "language_info": {
                    "codemirror_mode": { "name": "ipython", "version": 3 },
                    "file_extension": ".py", "mimetype": "text/x-python", "name": "python",
                    "nbconvert_exporter": "python", "pygments_lexer": "ipython3", "version": "3.10.12"
                }
            },
            "nbformat": 4, "nbformat_minor": 5
        }
        print("Initialized new notebook data as existing file was not found.")
    else:
        with open(full_notebook_path, 'r', encoding='utf-8') as f:
            notebook_data = json.load(f)
        print("Existing notebook (Chapters 1-4) loaded successfully.")

    notebook_data['cells'].extend(chapter5_cells)
    print(f"Appended {len(chapter5_cells)} cells for Chapter 5 skeleton.")
    notebook_data['cells'].extend(chapter6_cells)
    print(f"Appended {len(chapter6_cells)} cells for Chapter 6 skeleton.")

    with open(full_notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook_data, f, ensure_ascii=False, indent=2)
    print(f"Successfully appended Chapters 5-6 skeletons to {full_notebook_path}")
    print(f"File {full_notebook_path} exists. Size: {os.path.getsize(full_notebook_path)}")

except FileNotFoundError as fnf_error:
    print(f"Error - File Not Found: {fnf_error}")
except json.JSONDecodeError as json_error:
    print(f"Error - JSON Decode Error: {json_error}")
except Exception as e:
    print(f"Script execution error: {e}")
