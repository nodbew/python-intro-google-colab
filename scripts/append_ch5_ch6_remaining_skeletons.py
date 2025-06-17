import json
import os

notebook_path = 'src/beginner.ipynb'

# Define cells for Chapter 5, Sections 5.3, 5.4, 5.5
chapter5_remaining_sections_cells = [
    # Section 5.3 Explanation
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH5_SEC3_TITLE_PH]\n\n", # Arguments/Parameters
        "[JP_MD_CH5_SEC3_EXPLANATION_P1_PH]\n\n",
        "**[JP_MD_CH5_SEC3_SYNTAX_TITLE_PH]**\n",
        "```python\n",
        "def function_name_placeholder(param1, param2_default_ph='[JP_PY_STRING_DEFAULT_VALUE_PH]'):\n",
        "    # [JP_PY_COMMENT_CH5_SEC3_FUNCTION_BODY_PH]\n",
        "    pass\n",
        "```\n",
        "[JP_MD_CH5_SEC3_EXPLANATION_P2_PH]\n\n",
        "**[JP_MD_CH5_SEC3_MULTI_ARG_TITLE_PH]**\n",
        "[JP_MD_CH5_SEC3_MULTI_ARG_P1_PH]\n\n",
        "**[JP_MD_CH5_SEC3_DEFAULT_ARG_TITLE_PH]**\n",
        "[JP_MD_CH5_SEC3_DEFAULT_ARG_P1_PH]"
      ]
    },
    # Section 5.3 Exercise
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": ["### [JP_MD_CH5_SEC3_EX_TITLE_PH]\n\n", "[JP_MD_CH5_SEC3_EX_PROMPT_PH]"]
    },
    # Section 5.3 Answer Space (Code)
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def arguments_practice_ch5_sec3():\n",
        "  # [JP_PY_COMMENT_CH5_SEC3_AS_DEFINE_FUNC_PH]\n",
        "  # def display_item_price(item_name, price):\n",
        "  #   print(f\"{item_name}[JP_PY_STRING_CH5_SEC3_PRICE_IS_PH]{price}[JP_PY_STRING_CH5_SEC3_YEN_PH]\")\n",
        "  # display_item_price(\"[JP_PY_STRING_CH5_SEC3_APPLE_PH]\", 150)\n\n",
        "  # [JP_PY_COMMENT_CH5_SEC3_AS_MODIFY_FUNC_PH]\n",
        "  # def display_item_price_default(item_name, price=100):\n",
        "  #   print(f\"{item_name}[JP_PY_STRING_CH5_SEC3_PRICE_IS_PH]{price}[JP_PY_STRING_CH5_SEC3_YEN_PH]\")\n",
        "  # display_item_price_default(\"[JP_PY_STRING_CH5_SEC3_BANANA_PH]\")\n",
        "  # display_item_price_default(\"[JP_PY_STRING_CH5_SEC3_ORANGE_PH]\", 120)\n",
        "  pass\n",
        "# arguments_practice_ch5_sec3()"
      ],
      "outputs": [], "execution_count": None
    },
    # Section 5.3 Check Code (Code - hidden)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH5_SEC3_PH]"},
      "source": ["#@title [JP_CHECK_TITLE_CH5_SEC3_PH] { display-mode: \"form\" }\n", "print(\"[JP_CHECK_TEXT_CH5_SEC3_PH]\")"],
      "outputs": [], "execution_count": None
    },
    # Section 5.3 Solution (Code - hidden, Japanese content)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "def arguments_practice_ch5_sec3_solution():\n",
        "  def display_item_price(item_name, price):\n",
        "    print(f\"{item_name}の価格は{price}円です。\")\n",
        "  print(\"--- 通常の引数 ---\")\n",
        "  display_item_price(\"リンゴ\", 150)\n",
        "  print(\"\\n--- デフォルト引数値を持つ関数 ---\")\n",
        "  def display_item_price_with_default(item_name, price=100):\n",
        "    print(f\"{item_name}の価格は{price}円です。\")\n",
        "  display_item_price_with_default(\"バナナ\")\n",
        "  display_item_price_with_default(\"オレンジ\", 120)\n",
        "arguments_practice_ch5_sec3_solution()"
      ],
      "outputs": [], "execution_count": None
    },
    # Section 5.4 Explanation
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
          "## [JP_MD_CH5_SEC4_TITLE_PH]\n\n", # Return values
          "[JP_MD_CH5_SEC4_EXPLANATION_P1_PH]\n\n",
          "**[JP_MD_CH5_SEC4_SYNTAX_TITLE_PH]**\n",
          "```python\n",
          "def function_name_placeholder(params_ph):\n",
          "    # [JP_PY_COMMENT_CH5_SEC4_PROCESS_PH]\n",
          "    # result_ph = ... \n",
          "    return result_ph\n",
          "```\n",
          "[JP_MD_CH5_SEC4_EXPLANATION_P2_PH]\n\n",
          "**[JP_MD_CH5_SEC4_EXAMPLE_TITLE_PH]**\n",
          "[JP_MD_CH5_SEC4_EXAMPLE_P1_PH]\n\n", # Example: sum_two_numbers
          "**[JP_MD_CH5_SEC4_MULTI_RETURN_TITLE_PH]**\n",
          "[JP_MD_CH5_SEC4_MULTI_RETURN_P1_PH]" # Example: get_point
      ]
    },
    # Section 5.4 Exercise
    { "cell_type": "markdown", "metadata": {}, "source": ["### [JP_MD_CH5_SEC4_EX_TITLE_PH]\n\n", "[JP_MD_CH5_SEC4_EX_PROMPT_PH]"] },
    # Section 5.4 Answer Space
    { "cell_type": "code", "metadata": {}, "source": ["def return_value_practice_ch5_sec4():\n  # [JP_PY_COMMENT_CH5_SEC4_AS_DEFINE_FUNC_PH]\n  # def calculate_rectangle_area(width, height):\n  #   # area = width * height\n  #   # return area\n  #   pass\n  # area1 = calculate_rectangle_area(5,3) # [JP_PY_COMMENT_CH5_SEC4_AS_CALL1_PH]\n  # print(\"[JP_PY_STRING_CH5_SEC4_AS_AREA1_LABEL_PH]\", area1)\n  # area2 = calculate_rectangle_area(10,7) # [JP_PY_COMMENT_CH5_SEC4_AS_CALL2_PH]\n  # print(\"[JP_PY_STRING_CH5_SEC4_AS_AREA2_LABEL_PH]\", area2)\n  pass\n# return_value_practice_ch5_sec4()"], "outputs": [], "execution_count": None },
    # Section 5.4 Check Code
    { "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH5_SEC4_PH]"}, "source": ["#@title [JP_CHECK_TITLE_CH5_SEC4_PH] { display-mode: \"form\" }\n", "print(\"[JP_CHECK_TEXT_CH5_SEC4_PH]\")"], "outputs": [], "execution_count": None },
    # Section 5.4 Solution
    { "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}}, "source": ["def return_value_practice_ch5_sec4_solution():\n  def calculate_rectangle_area(width, height):\n    area = width * height\n    return area\n  area1 = calculate_rectangle_area(5, 3)\n  print(f\"幅5, 高さ3の長方形の面積: {area1}\")\n  area2 = calculate_rectangle_area(10, 7)\n  print(f\"幅10, 高さ7の長方形の面積: {area2}\")\nreturn_value_practice_ch5_sec4_solution()"], "outputs": [], "execution_count": None },
    # Section 5.5 Explanation
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
          "## [JP_MD_CH5_SEC5_TITLE_PH]\n\n", # Variable scope
          "[JP_MD_CH5_SEC5_EXPLANATION_P1_PH]\n\n",
          "1.  **[JP_MD_CH5_SEC5_LOCAL_SCOPE_TITLE_PH]** [JP_MD_CH5_SEC5_LOCAL_SCOPE_P1_PH]\n",
          "2.  **[JP_MD_CH5_SEC5_GLOBAL_SCOPE_TITLE_PH]** [JP_MD_CH5_SEC5_GLOBAL_SCOPE_P1_PH]\n\n",
          "**[JP_MD_CH5_SEC5_EXAMPLE_TITLE_PH]**\n",
          "[JP_MD_CH5_SEC5_EXAMPLE_P1_PH]\n\n", # Example code block
          "**[JP_MD_CH5_SEC5_IMPORTANCE_TITLE_PH]**\n",
          "[JP_MD_CH5_SEC5_IMPORTANCE_P1_PH]\n\n",
          "**[JP_MD_CH5_SEC5_CAUTION_TITLE_PH]**\n",
          "[JP_MD_CH5_SEC5_CAUTION_P1_PH]"
      ]
    },
    # Section 5.5 Exercise
    { "cell_type": "markdown", "metadata": {}, "source": ["### [JP_MD_CH5_SEC5_EX_TITLE_PH]\n\n", "[JP_MD_CH5_SEC5_EX_PROMPT_PH]"] },
    # Section 5.5 Answer Space
    { "cell_type": "code", "metadata": {}, "source": ["# [JP_PY_COMMENT_CH5_SEC5_AS_GLOBAL_X_PH]\n# x_ch5_s5 = 10\n# [JP_PY_COMMENT_CH5_SEC5_AS_DEFINE_FUNC_PH]\n# def print_variables_ch5_s5():\n#   y_ch5_s5 = 20\n#   print(f\"[JP_PY_STRING_CH5_SEC5_AS_X_IN_FUNC_PH] {x_ch5_s5}\")\n#   print(f\"[JP_PY_STRING_CH5_SEC5_AS_Y_IN_FUNC_PH] {y_ch5_s5}\")\n# [JP_PY_COMMENT_CH5_SEC5_AS_CALL_FUNC_PH]\n# print_variables_ch5_s5()\n# [JP_PY_COMMENT_CH5_SEC5_AS_PRINT_GLOBAL_X_PH]\n# print(f\"[JP_PY_STRING_CH5_SEC5_AS_X_OUTSIDE_PH] {x_ch5_s5}\")\n# [JP_PY_COMMENT_CH5_SEC5_AS_TRY_PRINT_Y_PH]\n# # print(f\"[JP_PY_STRING_CH5_SEC5_AS_Y_OUTSIDE_PH] {y_ch5_s5}\")\npass"], "outputs": [], "execution_count": None },
    # Section 5.5 Check Code
    { "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH5_SEC5_PH]"}, "source": ["#@title [JP_CHECK_TITLE_CH5_SEC5_PH] { display-mode: \"form\" }\n", "print(\"[JP_CHECK_TEXT_CH5_SEC5_PH]\")"], "outputs": [], "execution_count": None },
    # Section 5.5 Solution
    { "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}}, "source": ["x_ch5_s5_solution = 10\ndef print_variables_ch5_s5_solution():\n  y_ch5_s5_solution = 20\n  print(f\"関数内のx: {x_ch5_s5_solution}\")\n  print(f\"関数内のy: {y_ch5_s5_solution}\")\nprint(\"--- 関数の実行 ---\")\nprint_variables_ch5_s5_solution()\nprint(\"--- 関数実行後 ---\")\nprint(f\"関数外のx: {x_ch5_s5_solution}\")\nprint(\"\\n--- ローカル変数yへのアクセス試行 ---\")\ntry:\n    print(f\"関数外のy: {y_ch5_s5_solution}\") # This would cause NameError\nexcept NameError as e:\n    print(f\"エラーが発生しました（期待通り）: {e}\")"], "outputs": [], "execution_count": None }
]

# Define cells for Chapter 6, Sections 6.3, 6.4
chapter6_remaining_sections_cells = [
    # Section 6.3 Explanation
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH6_SEC3_TITLE_PH]\n\n", # Dictionaries
        "[JP_MD_CH6_SEC3_EXPLAIN_P1_PH]\n",
        "[JP_MD_CH6_SEC3_EXPLAIN_P2_PH]\n",
        "*   [JP_MD_CH6_SEC3_EXPLAIN_ITEM1_PH]\n",
        "*   [JP_MD_CH6_SEC3_EXPLAIN_ITEM2_PH]\n",
        "*   [JP_MD_CH6_SEC3_EXPLAIN_ITEM3_PH]\n",
        "```python\n",
        "# [JP_PY_COMMENT_CH6_DICT_EXAMPLE_PH]\n",
        "my_dict_placeholder = {\"name_ph\": \"Alice_ph\", \"age_ph\": 30}\n",
        "print(my_dict_placeholder[\"name_ph\"])\n",
        "my_dict_placeholder[\"city_ph\"] = \"New York_ph\"\n",
        "print(my_dict_placeholder.get(\"age_ph\"))\n",
        "```"
      ]
    },
    # Section 6.3 Exercise
    { "cell_type": "markdown", "metadata": {}, "source": ["### [JP_MD_CH6_SEC3_EX_TITLE_PH]\n\n", "[JP_MD_CH6_SEC3_EX_TEXT_P1_PH]\n", "`student = {\"name\": \"山田\", \"age\": 20}` [JP_MD_CH6_SEC3_EX_TEXT_P2_PH]\n", "1. [JP_MD_CH6_SEC3_EX_STEP1_PH]\n", "2. [JP_MD_CH6_SEC3_EX_STEP2_PH]\n", "3. [JP_MD_CH6_SEC3_EX_STEP3_PH]\n", "4. [JP_MD_CH6_SEC3_EX_STEP4_PH]"] },
    # Section 6.3 Answer Space
    { "cell_type": "code", "metadata": {}, "source": ["def dictionary_manipulation_practice_ch6_sec3():\n  student = {\"name\": \"山田\", \"age\": 20} # [JP_PY_COMMENT_CH6_SEC3_AS_INITIAL_DICT_PH]\n  # [JP_PY_COMMENT_CH6_SEC3_AS_STEP1_PH]\n  # student[\"grade\"] = 3\n  # [JP_PY_COMMENT_CH6_SEC3_AS_STEP2_PH]\n  # student[\"age\"] = 21\n  # [JP_PY_COMMENT_CH6_SEC3_AS_STEP3_PH]\n  # # del student[\"name\"]\n  # [JP_PY_COMMENT_CH6_SEC3_AS_STEP4_PH]\n  # # print(student)\n  pass\n# dictionary_manipulation_practice_ch6_sec3()"], "outputs": [], "execution_count": None },
    # Section 6.3 Check Code
    { "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH6_SEC3_PH]"}, "source": ["#@title [JP_CHECK_TITLE_CH6_SEC3_PH] { display-mode: \"form\" }\n", "print(\"[JP_CHECK_TEXT_CH6_SEC3_PH]\")"], "outputs": [], "execution_count": None },
    # Section 6.3 Solution
    { "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}}, "source": ["def dictionary_manipulation_practice_ch6_sec3_solution():\n  student = {\"name\": \"山田\", \"age\": 20}\n  print(f\"初期辞書: {student}\")\n  student[\"grade\"] = 3\n  print(f\"grade追加後: {student}\")\n  student[\"age\"] = 21\n  print(f\"age更新後: {student}\")\n  del student[\"name\"]\n  print(f\"name削除後: {student}\")\n  print(f\"最終的な辞書: {student}\")\ndictionary_manipulation_practice_ch6_sec3_solution()"], "outputs": [], "execution_count": None },
    # Section 6.4 Explanation
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH6_SEC4_TITLE_PH]\n\n", # Sets
        "[JP_MD_CH6_SEC4_EXPLAIN_P1_PH]\n",
        "[JP_MD_CH6_SEC4_EXPLAIN_P2_PH]\n",
        "[JP_MD_CH6_SEC4_EXPLAIN_P3_PH]\n",
        "```python\n",
        "# [JP_PY_COMMENT_CH6_SET_EXAMPLE_PH]\n",
        "my_set_placeholder = {1, 2, 2, 3, \"hello_ph\"}\n",
        "print(my_set_placeholder)\n",
        "set1_ph = {1, 2, 3}\n",
        "set2_ph = {3, 4, 5}\n",
        "print(set1_ph | set2_ph) # [JP_PY_COMMENT_CH6_UNION_PH]\n",
        "```"
      ]
    },
    # Section 6.4 Exercise
    { "cell_type": "markdown", "metadata": {}, "source": ["### [JP_MD_CH6_SEC4_EX_TITLE_PH]\n\n", "[JP_MD_CH6_SEC4_EX_TEXT_P1_PH]\n", "`numbers1 = {1, 2, 3, 4, 5}` [JP_MD_CH6_SEC4_EX_TEXT_P2_PH] `numbers2 = {4, 5, 6, 7, 8}` [JP_MD_CH6_SEC4_EX_TEXT_P3_PH]\n", "1. [JP_MD_CH6_SEC4_EX_STEP1_PH]\n", "2. [JP_MD_CH6_SEC4_EX_STEP2_PH]\n", "3. [JP_MD_CH6_SEC4_EX_STEP3_PH]"] },
    # Section 6.4 Answer Space
    { "cell_type": "code", "metadata": {}, "source": ["def set_operations_practice_ch6_sec4():\n  numbers1 = {1, 2, 3, 4, 5}\n  numbers2 = {4, 5, 6, 7, 8}\n  # [JP_PY_COMMENT_CH6_SEC4_AS_UNION_PH]\n  # # union_set = numbers1 | numbers2\n  # # print(\"[JP_PY_STRING_CH6_SEC4_AS_UNION_LABEL_PH]\", union_set)\n  # [JP_PY_COMMENT_CH6_SEC4_AS_INTERSECTION_PH]\n  # # intersection_set = numbers1 & numbers2\n  # # print(\"[JP_PY_STRING_CH6_SEC4_AS_INTERSECTION_LABEL_PH]\", intersection_set)\n  # [JP_PY_COMMENT_CH6_SEC4_AS_DIFFERENCE_PH]\n  # # difference_set = numbers1 - numbers2\n  # # print(\"[JP_PY_STRING_CH6_SEC4_AS_DIFFERENCE_LABEL_PH]\", difference_set)\n  pass\n# set_operations_practice_ch6_sec4()"], "outputs": [], "execution_count": None },
    # Section 6.4 Check Code
    { "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH6_SEC4_PH]"}, "source": ["#@title [JP_CHECK_TITLE_CH6_SEC4_PH] { display-mode: \"form\" }\n", "print(\"[JP_CHECK_TEXT_CH6_SEC4_PH]\")"], "outputs": [], "execution_count": None },
    # Section 6.4 Solution
    { "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}}, "source": ["def set_operations_practice_ch6_sec4_solution():\n  numbers1 = {1, 2, 3, 4, 5}\n  numbers2 = {4, 5, 6, 7, 8}\n  union_set = numbers1 | numbers2\n  print(f\"和集合: {union_set}\")\n  intersection_set = numbers1 & numbers2\n  print(f\"積集合: {intersection_set}\")\n  difference_set = numbers1 - numbers2\n  print(f\"差集合 (numbers1 - numbers2): {difference_set}\")\nset_operations_practice_ch6_sec4_solution()"], "outputs": [], "execution_count": None }
]

try:
    print(f"Python script to append remaining Ch5 & Ch6 skeletons. Notebook path: {os.path.abspath(notebook_path)}")

    base_dir = "/app"
    full_notebook_path = os.path.join(base_dir, notebook_path.lstrip('/'))

    notebook_dir = os.path.dirname(full_notebook_path)
    if not os.path.exists(notebook_dir):
        os.makedirs(notebook_dir)
        print(f"Created directory: {notebook_dir}")

    if not os.path.exists(full_notebook_path):
        print(f"Error: Notebook file '{full_notebook_path}' not found.")
        exit(1)

    with open(full_notebook_path, 'r', encoding='utf-8') as f:
        notebook_data = json.load(f)
    print("Existing notebook loaded successfully.")

    # Append Chapter 5 remaining sections
    notebook_data['cells'].extend(chapter5_remaining_sections_cells)
    print(f"Appended {len(chapter5_remaining_sections_cells)} cells for remaining Chapter 5 sections.")

    # Append Chapter 6 remaining sections
    notebook_data['cells'].extend(chapter6_remaining_sections_cells)
    print(f"Appended {len(chapter6_remaining_sections_cells)} cells for remaining Chapter 6 sections.")

    with open(full_notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook_data, f, ensure_ascii=False, indent=2)
    print(f"Successfully appended remaining skeletons for Chapters 5-6 to {full_notebook_path}")
    print(f"File {full_notebook_path} exists. Size: {os.path.getsize(full_notebook_path)}")

except FileNotFoundError as fnf_error:
    print(f"Error - File Not Found: {fnf_error}")
except json.JSONDecodeError as json_error:
    print(f"Error - JSON Decode Error: {json_error}")
except Exception as e:
    print(f"Script execution error: {e}")
