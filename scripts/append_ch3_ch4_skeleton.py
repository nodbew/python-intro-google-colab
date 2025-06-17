import json
import os

notebook_path = 'src/beginner.ipynb'

# Define the cells for Chapter 3
chapter3_cells = [
    # Cell 1: Markdown (Chapter Title, Sec 3.1 Title & Explanation)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# [JP_MD_CH3_TITLE_PH]\n\n",
        "[JP_MD_CH3_INTRO_P1_PH]\n\n",
        "## [JP_MD_CH3_SEC1_TITLE_PH]\n\n",
        "[JP_MD_CH3_SEC1_P1_PH]\n\n",
        "[JP_MD_CH3_SEC1_TABLE_PH_NOTE: This will be a placeholder for a markdown table definition in the JSON map.]\n\n",
        "[JP_MD_CH3_SEC1_P2_PH]\n",
        "```python\n",
        "x = 10\n",
        "y = 3\n",
        "addition_result = x + y\n",
        "print(f\"{x} + {y} = {addition_result}\") # [JP_PY_COMMENT_CH3_SEC1_FSTRING_EXPLAIN_PH]\n",
        "power_result = 2 ** 4  # [JP_PY_COMMENT_CH3_SEC1_POWER_EXPLAIN_PH]\n",
        "print(f\"[JP_PY_STRING_CH3_SEC1_POWER_RESULT_PH] {power_result} [JP_PY_STRING_CH3_SEC1_IS_PH]\")\n",
        "```"
      ]
    },
    # Cell 2: Markdown (Exercise 3.1)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH3_SEC1_EX_TITLE_PH]\n\n",
        "[JP_MD_CH3_SEC1_EX_PROMPT_P1_PH]\n",
        "1. [JP_MD_CH3_SEC1_EX_STEP1_PH]\n",
        "2. [JP_MD_CH3_SEC1_EX_STEP2_PH]\n",
        "3. [JP_MD_CH3_SEC1_EX_STEP3_PH]\n",
        "4. [JP_MD_CH3_SEC1_EX_STEP4_PH]\n",
        "5. [JP_MD_CH3_SEC1_EX_STEP5_PH]\n",
        "6. [JP_MD_CH3_SEC1_EX_STEP6_PH]\n",
        "7. [JP_MD_CH3_SEC1_EX_STEP7_PH]"
      ]
    },
    # Cell 3: Code (Answer Space 3.1)
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def all_arithmetic_ops_updated():\n",
        "  a = 7\n",
        "  b = 2\n",
        "  # [JP_PY_COMMENT_CH3_SEC1_AS_SUM_PH]\n",
        "  # print(\"[JP_PY_STRING_CH3_SEC1_AS_SUM_LABEL_PH]\", a + b)\n",
        "  # [JP_PY_COMMENT_CH3_SEC1_AS_DIFF_PH]\n",
        "  # print(\"[JP_PY_STRING_CH3_SEC1_AS_DIFF_LABEL_PH]\", a - b)\n",
        "  # [JP_PY_COMMENT_CH3_SEC1_AS_PROD_PH]\n",
        "  # print(\"[JP_PY_STRING_CH3_SEC1_AS_PROD_LABEL_PH]\", a * b)\n",
        "  # [JP_PY_COMMENT_CH3_SEC1_AS_DIV_FLOAT_PH]\n",
        "  # print(\"[JP_PY_STRING_CH3_SEC1_AS_DIV_FLOAT_LABEL_PH]\", a / b)\n",
        "  # [JP_PY_COMMENT_CH3_SEC1_AS_DIV_FLOOR_PH]\n",
        "  # print(\"[JP_PY_STRING_CH3_SEC1_AS_DIV_FLOOR_LABEL_PH]\", a // b)\n",
        "  # [JP_PY_COMMENT_CH3_SEC1_AS_MODULO_PH]\n",
        "  # print(\"[JP_PY_STRING_CH3_SEC1_AS_MODULO_LABEL_PH]\", a % b)\n",
        "  # [JP_PY_COMMENT_CH3_SEC1_AS_POWER_PH]\n",
        "  # print(\"[JP_PY_STRING_CH3_SEC1_AS_POWER_LABEL_PH]\", a ** b)\n",
        "  pass\n",
        "# all_arithmetic_ops_updated() # [JP_PY_COMMENT_CH3_SEC1_AS_CALL_FUNC_PH]"
      ],
      "outputs": [], "execution_count": None
    },
    # Cell 4: Code (Check Code 3.1 - hidden)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH3_SEC1_PH]"},
      "source": [
        "#@title [JP_CHECK_TITLE_CH3_SEC1_PH] { display-mode: \"form\" }\n",
        "print(\"[JP_CHECK_TEXT_CH3_SEC1_PH]\")"
      ],
      "outputs": [], "execution_count": None
    },
    # Cell 5: Code (Solution 3.1 - hidden)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "def all_arithmetic_ops_updated_solution():\n",
        "  a = 7\n",
        "  b = 2\n",
        "  print(\"和:\", a + b)\n",
        "  print(\"差:\", a - b)\n",
        "  print(\"積:\", a * b)\n",
        "  print(\"商 (/):\", a / b)\n",
        "  print(\"商 (//):\", a // b)\n",
        "  print(\"余り:\", a % b)\n",
        "  print(\"べき乗:\", a ** b)\n",
        "all_arithmetic_ops_updated_solution()"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH3_SEC2_TITLE_PH]\n\n",
        "[JP_MD_CH3_SEC2_P1_PH]\n\n",
        "[JP_MD_CH3_SEC2_TABLE_PH_NOTE: Placeholder for comparison operators table]\n\n",
        "[JP_MD_CH3_SEC2_P2_PH]\n",
        "```python\n",
        "age = 20\n",
        "is_adult = age >= 18\n",
        "print(f\"[JP_PY_STRING_CH3_SEC2_IS_ADULT_PH] {is_adult}\")\n",
        "```"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH3_SEC2_EX_TITLE_PH]\n\n",
        "[JP_MD_CH3_SEC2_EX_PROMPT_P1_PH]\n",
        "1. [JP_MD_CH3_SEC2_EX_STEP1_PH]\n",
        "2. [JP_MD_CH3_SEC2_EX_STEP2_PH]\n",
        "3. [JP_MD_CH3_SEC2_EX_STEP3_PH]"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def check_score_conditions():\n",
        "  score = 85\n",
        "  # [JP_PY_COMMENT_CH3_SEC2_AS_COND1_PH]\n",
        "  # condition1 = score >= 80\n",
        "  # print(\"[JP_PY_STRING_CH3_SEC2_AS_COND1_LABEL_PH]\", condition1)\n",
        "  # [JP_PY_COMMENT_CH3_SEC2_AS_COND2_PH]\n",
        "  # condition2 = score < 50\n",
        "  # print(\"[JP_PY_STRING_CH3_SEC2_AS_COND2_LABEL_PH]\", condition2)\n",
        "  # [JP_PY_COMMENT_CH3_SEC2_AS_COND3_PH]\n",
        "  # condition3 = score == 100\n",
        "  # print(\"[JP_PY_STRING_CH3_SEC2_AS_COND3_LABEL_PH]\", condition3)\n",
        "  pass\n",
        "# check_score_conditions() # [JP_PY_COMMENT_CH3_SEC2_AS_CALL_FUNC_PH]"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH3_SEC2_PH]"},
      "source": [
        "#@title [JP_CHECK_TITLE_CH3_SEC2_PH] { display-mode: \"form\" }\n",
        "print(\"[JP_CHECK_TEXT_CH3_SEC2_PH]\")"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "def check_score_conditions_solution():\n",
        "  score = 85\n",
        "  condition1 = score >= 80\n",
        "  print(\"80点以上:\", condition1)\n",
        "  condition2 = score < 50\n",
        "  print(\"50点未満:\", condition2)\n",
        "  condition3 = score == 100\n",
        "  print(\"100点と等しい:\", condition3)\n",
        "check_score_conditions_solution()"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH3_SEC3_TITLE_PH]\n\n",
        "[JP_MD_CH3_SEC3_P1_PH]\n\n",
        "[JP_MD_CH3_SEC3_TABLE_PH_NOTE: Placeholder for logical operators table and truth table]\n\n",
        "[JP_MD_CH3_SEC3_P2_PH]\n",
        "```python\n",
        "age = 25\n",
        "has_license = True\n",
        "can_drive_legally = (age >= 20) and has_license\n",
        "print(f\"[JP_PY_STRING_CH3_SEC3_CAN_DRIVE_PH] {can_drive_legally}\")\n",
        "```"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH3_SEC3_EX_TITLE_PH]\n\n",
        "[JP_MD_CH3_SEC3_EX_PROMPT_P1_PH]\n",
        "1. [JP_MD_CH3_SEC3_EX_STEP1_PH]\n",
        "2. [JP_MD_CH3_SEC3_EX_STEP2_PH]\n",
        "3. [JP_MD_CH3_SEC3_EX_STEP3_PH]"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def weather_weekend_logic_evaluation():\n",
        "  is_sunny = True\n",
        "  is_weekend = False\n",
        "  # [JP_PY_COMMENT_CH3_SEC3_AS_COND_AND_PH]\n",
        "  # condition_and = is_sunny and is_weekend\n",
        "  # print(\"[JP_PY_STRING_CH3_SEC3_AS_COND_AND_LABEL_PH]\", condition_and)\n",
        "  # [JP_PY_COMMENT_CH3_SEC3_AS_COND_OR_PH]\n",
        "  # condition_or = is_sunny or is_weekend\n",
        "  # print(\"[JP_PY_STRING_CH3_SEC3_AS_COND_OR_LABEL_PH]\", condition_or)\n",
        "  # [JP_PY_COMMENT_CH3_SEC3_AS_COND_NOT_PH]\n",
        "  # condition_not_sunny = not is_sunny\n",
        "  # print(\"[JP_PY_STRING_CH3_SEC3_AS_COND_NOT_LABEL_PH]\", condition_not_sunny)\n",
        "  pass\n",
        "# weather_weekend_logic_evaluation() # [JP_PY_COMMENT_CH3_SEC3_AS_CALL_FUNC_PH]"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH3_SEC3_PH]"},
      "source": [
        "#@title [JP_CHECK_TITLE_CH3_SEC3_PH] { display-mode: \"form\" }\n",
        "print(\"[JP_CHECK_TEXT_CH3_SEC3_PH]\")"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "def weather_weekend_logic_evaluation_solution():\n",
        "  is_sunny = True\n",
        "  is_weekend = False\n",
        "  condition_and = is_sunny and is_weekend\n",
        "  print(\"晴れで週末:\", condition_and)\n",
        "  condition_or = is_sunny or is_weekend\n",
        "  print(\"晴れまたは週末:\", condition_or)\n",
        "  condition_not_sunny = not is_sunny\n",
        "  print(\"晴れていない:\", condition_not_sunny)\n",
        "weather_weekend_logic_evaluation_solution()"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH3_SEC4_TITLE_PH]\n\n",
        "[JP_MD_CH3_SEC4_P1_PH]\n\n",
        "[JP_MD_CH3_SEC4_TABLE_PH_NOTE: Placeholder for assignment operators table]\n\n",
        "[JP_MD_CH3_SEC4_P2_PH]\n",
        "```python\n",
        "count = 5\n",
        "count += 2  # [JP_PY_COMMENT_CH3_SEC4_ADD_ASSIGN_PH]\n",
        "print(f\"[JP_PY_STRING_CH3_SEC4_COUNT_VALUE_PH] {count}\")\n",
        "```"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH3_SEC4_EX_TITLE_PH]\n\n",
        "[JP_MD_CH3_SEC4_EX_PROMPT_PH]"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def operator_precedence_evaluation():\n",
        "  a = 5\n",
        "  b = 10\n",
        "  c = True\n",
        "  # [JP_PY_COMMENT_CH3_SEC4_AS_EXPR1_PH]\n",
        "  # result1 = a + b / 2 == 10.0 and not c\n",
        "  # print(\"[JP_PY_STRING_CH3_SEC4_AS_RESULT1_LABEL_PH]\", result1)\n",
        "  \n",
        "  # [JP_PY_COMMENT_CH3_SEC4_AS_EXPR2_PH]\n",
        "  # result2 = (a + b) / 2 == 10.0 and (not c)\n",
        "  # print(\"[JP_PY_STRING_CH3_SEC4_AS_RESULT2_LABEL_PH]\", result2)\n",
        "  pass\n",
        "# operator_precedence_evaluation() # [JP_PY_COMMENT_CH3_SEC4_AS_CALL_FUNC_PH]"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH3_SEC4_PH]"},
      "source": [
        "#@title [JP_CHECK_TITLE_CH3_SEC4_PH] { display-mode: \"form\" }\n",
        "print(\"[JP_CHECK_TEXT_CH3_SEC4_PH]\")"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "def operator_precedence_evaluation_solution():\n",
        "  a = 5\n",
        "  b = 10\n",
        "  c = True\n",
        "  result1 = a + b / 2 == 10.0 and not c\n",
        "  print(\"result1 の評価結果:\", result1) # False\n",
        "  result2 = (a + b) / 2 == 10.0 and (not c)\n",
        "  print(\"result2 の評価結果:\", result2) # False\n",
        "operator_precedence_evaluation_solution()"
      ],
      "outputs": [], "execution_count": None
    }
]

# Define the cells for Chapter 4
chapter4_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# [JP_MD_CH4_TITLE_PH]\n\n",
            "[JP_MD_CH4_INTRO_P1_PH]\n\n",
            "## [JP_MD_CH4_SEC1_TITLE_PH]\n\n",
            "[JP_MD_CH4_SEC1_P1_PH]\n\n",
            "**[JP_MD_CH4_SEC1_SYNTAX_TITLE_PH]**\n",
            "```python\n",
            "if condition_placeholder:\n",
            "    # [JP_PY_COMMENT_CH4_SEC1_IF_TRUE_PH]\n",
            "    pass\n",
            "```\n",
            "[JP_MD_CH4_SEC1_SYNTAX_DESC_PH]\n\n",
            "**[JP_MD_CH4_SEC1_EXAMPLE_TITLE_PH]**\n",
            "```python\n",
            "temperature = 30\n",
            "if temperature > 28:\n",
            "    print(\"[JP_PY_STRING_CH4_SEC1_HOT_TODAY_PH]\")\n",
            "print(\"[JP_PY_STRING_CH4_SEC1_REST_OF_PROGRAM_PH]\")\n",
            "```"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### [JP_MD_CH4_SEC1_EX_TITLE_PH]\n\n",
            "[JP_MD_CH4_SEC1_EX_PROMPT_P1_PH]\n",
            "[JP_MD_CH4_SEC1_EX_PROMPT_P2_PH]"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "def check_if_minor():\n",
            "  user_age = 17 # [JP_PY_COMMENT_CH4_SEC1_AS_CHANGE_AGE_PH]\n",
            "  # [JP_PY_COMMENT_CH4_SEC1_AS_IF_STATEMENT_PH]\n",
            "  # if user_age < 18:\n",
            "  #   print(\"[JP_PY_STRING_CH4_SEC1_AS_IS_MINOR_PH]\")\n",
            "  pass\n",
            "# check_if_minor() # [JP_PY_COMMENT_CH4_SEC1_AS_CALL_FUNC_PH]"
        ],
        "outputs": [], "execution_count": None
    },
    {
        "cell_type": "code",
        "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH4_SEC1_PH]"},
        "source": [
            "#@title [JP_CHECK_TITLE_CH4_SEC1_PH] { display-mode: \"form\" }\n",
            "print(\"[JP_CHECK_TEXT_CH4_SEC1_PH]\")"
        ],
        "outputs": [], "execution_count": None
    },
    {
        "cell_type": "code",
        "metadata": {"jupyter": {"source_hidden": True}},
        "source": [
            "def check_if_minor_solution():\n",
            "  user_age = 17\n",
            "  if user_age < 18:\n",
            "    print(\"あなたは未成年です。\")\n",
            "  \n",
            "  user_age = 20\n",
            "  if user_age < 18:\n",
            "    print(\"あなたは未成年です。\") #実行されない\n",
            "  else:\n",
            "    print(f\"{user_age}歳は未成年ではありません。\")\n",
            "check_if_minor_solution()"
        ],
        "outputs": [], "execution_count": None
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH4_SEC2_TITLE_PH]\n\n",
        "[JP_MD_CH4_SEC2_P1_PH]\n\n",
        "**[JP_MD_CH4_SEC2_ELSE_TITLE_PH]**\n",
        "[JP_MD_CH4_SEC2_ELSE_P1_PH]\n\n",
        "**[JP_MD_CH4_SEC2_ELSE_SYNTAX_TITLE_PH]**\n",
        "```python\n",
        "if condition_placeholder:\n",
        "    # [JP_PY_COMMENT_CH4_SEC2_IF_COND1_TRUE_PH]\n",
        "    pass\n",
        "else:\n",
        "    # [JP_PY_COMMENT_CH4_SEC2_IF_COND1_FALSE_PH]\n",
        "    pass\n",
        "```\n",
        "**[JP_MD_CH4_SEC2_ELSE_EXAMPLE_TITLE_PH]**\n",
        "```python\n",
        "score = 75\n",
        "if score >= 60:\n",
        "    print(\"[JP_PY_STRING_CH4_SEC2_PASS_PH]\")\n",
        "else:\n",
        "    print(\"[JP_PY_STRING_CH4_SEC2_FAIL_PH]\")\n",
        "```\n\n",
        "**[JP_MD_CH4_SEC2_ELIF_TITLE_PH]**\n",
        "[JP_MD_CH4_SEC2_ELIF_P1_PH]\n\n",
        "**[JP_MD_CH4_SEC2_ELIF_SYNTAX_TITLE_PH]**\n",
        "```python\n",
        "if condition1_placeholder:\n",
        "    # [JP_PY_COMMENT_CH4_SEC2_ELIF_COND1_TRUE_PH]\n",
        "    pass\n",
        "elif condition2_placeholder:\n",
        "    # [JP_PY_COMMENT_CH4_SEC2_ELIF_COND2_TRUE_PH]\n",
        "    pass\n",
        "else:\n",
        "    # [JP_PY_COMMENT_CH4_SEC2_ELIF_ALL_FALSE_PH]\n",
        "    pass\n",
        "```\n",
        "**[JP_MD_CH4_SEC2_ELIF_EXAMPLE_TITLE_PH]**\n",
        "```python\n",
        "score = 85\n",
        "if score >= 90:\n",
        "    print(\"[JP_PY_STRING_CH4_SEC2_ELIF_GRADE_A_PH]\")\n",
        "elif score >= 80:\n",
        "    print(\"[JP_PY_STRING_CH4_SEC2_ELIF_GRADE_B_PH]\")\n",
        "else:\n",
        "    print(\"[JP_PY_STRING_CH4_SEC2_ELIF_GRADE_C_PH]\")\n",
        "```\n",
        "[JP_MD_CH4_SEC2_ELIF_P2_PH]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH4_SEC2_EX_TITLE_PH]\n\n",
        "[JP_MD_CH4_SEC2_EX_PROMPT_P1_PH]\n",
        "[JP_MD_CH4_SEC2_EX_COND1_PH]\n",
        "[JP_MD_CH4_SEC2_EX_COND2_PH]\n",
        "[JP_MD_CH4_SEC2_EX_COND3_PH]\n",
        "[JP_MD_CH4_SEC2_EX_PROMPT_P2_PH]"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def check_number_sign(number):\n",
        "  # [JP_PY_COMMENT_CH4_SEC2_AS_NUM_INPUT_PH]\n",
        "  # if number > 0:\n",
        "  #   print(f\"{number}[JP_PY_STRING_CH4_SEC2_AS_IS_POSITIVE_PH]\")\n",
        "  # elif number < 0:\n",
        "  #   print(f\"{number}[JP_PY_STRING_CH4_SEC2_AS_IS_NEGATIVE_PH]\")\n",
        "  # else:\n",
        "  #   print(f\"{number}[JP_PY_STRING_CH4_SEC2_AS_IS_ZERO_PH]\")\n",
        "  pass\n",
        "# check_number_sign(0)\n",
        "# check_number_sign(10)\n",
        "# check_number_sign(-5) # [JP_PY_COMMENT_CH4_SEC2_AS_CALL_FUNC_PH]"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH4_SEC2_PH]"},
      "source": [
        "#@title [JP_CHECK_TITLE_CH4_SEC2_PH] { display-mode: \"form\" }\n",
        "print(\"[JP_CHECK_TEXT_CH4_SEC2_PH]\")"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "def check_number_sign_solution(number):\n",
        "  if number > 0:\n",
        "    print(f\"{number} は正の数です。\")\n",
        "  elif number < 0:\n",
        "    print(f\"{number} は負の数です。\")\n",
        "  else:\n",
        "    print(f\"{number} はゼロです。\")\n",
        "\n",
        "check_number_sign_solution(0)\n",
        "check_number_sign_solution(10)\n",
        "check_number_sign_solution(-5)"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH4_SEC3_TITLE_PH]\n\n",
        "[JP_MD_CH4_SEC3_P1_PH]\n\n",
        "**[JP_MD_CH4_SEC3_SYNTAX_TITLE_PH]**\n",
        "```python\n",
        "for item_variable_placeholder in iterable_placeholder:\n",
        "    # [JP_PY_COMMENT_CH4_SEC3_LOOP_BODY_PH]\n",
        "    pass\n",
        "```\n",
        "[JP_MD_CH4_SEC3_SYNTAX_DESC_PH]\n\n",
        "**[JP_MD_CH4_SEC3_EXAMPLE1_TITLE_PH]**\n",
        "```python\n",
        "fruits = [\"りんご\", \"バナナ\", \"みかん\"]\n",
        "for fruit in fruits:\n",
        "    print(fruit)\n",
        "```\n",
        "**[JP_MD_CH4_SEC3_EXAMPLE2_TITLE_PH]**\n",
        "```python\n",
        "for char_placeholder in \"Python\":\n",
        "    print(char_placeholder)\n",
        "```\n\n",
        "**[JP_MD_CH4_SEC3_RANGE_TITLE_PH]**\n",
        "[JP_MD_CH4_SEC3_RANGE_P1_PH]\n",
        "[JP_MD_CH4_SEC3_RANGE_DESC_PH]\n\n",
        "**[JP_MD_CH4_SEC3_EXAMPLE3_TITLE_PH]**\n",
        "```python\n",
        "for i in range(5):\n",
        "    print(i)\n",
        "```"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH4_SEC3_EX_TITLE_PH]\n\n",
        "1. [JP_MD_CH4_SEC3_EX_STEP1_PH]\n",
        "2. [JP_MD_CH4_SEC3_EX_STEP2_PH]"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def for_loop_practices():\n",
        "  # [JP_PY_COMMENT_CH4_SEC3_AS_STEP1_DESC_PH]\n",
        "  # for i in range(1, 6):\n",
        "  #   print(i)\n",
        "  \n",
        "  # [JP_PY_COMMENT_CH4_SEC3_AS_STEP2_DESC_PH]\n",
        "  # colors = [\"赤\", \"青\", \"黄\", \"緑\"]\n",
        "  # for color in colors:\n",
        "  #   print(f\"[JP_PY_STRING_CH4_SEC3_AS_FAVORITE_COLOR_PH]{color}\")\n",
        "  pass\n",
        "# for_loop_practices() # [JP_PY_COMMENT_CH4_SEC3_AS_CALL_FUNC_PH]"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH4_SEC3_PH]"},
      "source": [
        "#@title [JP_CHECK_TITLE_CH4_SEC3_PH] { display-mode: \"form\" }\n",
        "print(\"[JP_CHECK_TEXT_CH4_SEC3_PH]\")"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "def for_loop_practices_solution():\n",
        "  print(\"1から5までの数値:\")\n",
        "  for i in range(1, 6):\n",
        "    print(i)\n",
        "  \n",
        "  print(\"\\n好きな色リスト:\")\n",
        "  colors = [\"赤\", \"青\", \"黄\", \"緑\"]\n",
        "  for color in colors:\n",
        "    print(f\"好きな色：{color}\")\n",
        "for_loop_practices_solution()"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH4_SEC4_TITLE_PH]\n\n",
        "[JP_MD_CH4_SEC4_P1_PH]\n\n",
        "**[JP_MD_CH4_SEC4_SYNTAX_TITLE_PH]**\n",
        "```python\n",
        "while condition_placeholder:\n",
        "    # [JP_PY_COMMENT_CH4_SEC4_LOOP_BODY_PH]\n",
        "    pass\n",
        "```\n",
        "[JP_MD_CH4_SEC4_SYNTAX_DESC_PH]\n\n",
        "**[JP_MD_CH4_SEC4_INFINITE_LOOP_TITLE_PH]**\n",
        "[JP_MD_CH4_SEC4_INFINITE_LOOP_P1_PH]\n\n",
        "**[JP_MD_CH4_SEC4_EXAMPLE_TITLE_PH]**\n",
        "```python\n",
        "count = 1\n",
        "while count <= 3:\n",
        "    print(f\"[JP_PY_STRING_CH4_SEC4_COUNT_LABEL_PH]{count}\")\n",
        "    count += 1\n",
        "```"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH4_SEC4_EX_TITLE_PH]\n\n",
        "[JP_MD_CH4_SEC4_EX_PROMPT_P1_PH]\n",
        "[JP_MD_CH4_SEC4_EX_HINT_PH]"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def while_loop_countdown():\n",
        "  # [JP_PY_COMMENT_CH4_SEC4_AS_COUNTER_INIT_PH]\n",
        "  # count = 5\n",
        "  # [JP_PY_COMMENT_CH4_SEC4_AS_WHILE_LOOP_PH]\n",
        "  # while count >= 1:\n",
        "  #   print(count)\n",
        "  #   count -= 1\n",
        "  pass\n",
        "# while_loop_countdown() # [JP_PY_COMMENT_CH4_SEC4_AS_CALL_FUNC_PH]"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH4_SEC4_PH]"},
      "source": [
        "#@title [JP_CHECK_TITLE_CH4_SEC4_PH] { display-mode: \"form\" }\n",
        "print(\"[JP_CHECK_TEXT_CH4_SEC4_PH]\")"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "def while_loop_countdown_solution():\n",
        "  count = 5\n",
        "  while count >= 1:\n",
        "    print(count)\n",
        "    count -= 1\n",
        "while_loop_countdown_solution()"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH4_SEC5_TITLE_PH]\n\n",
        "[JP_MD_CH4_SEC5_P1_PH]\n\n",
        "**[JP_MD_CH4_SEC5_BREAK_TITLE_PH]**\n",
        "[JP_MD_CH4_SEC5_BREAK_P1_PH]\n\n",
        "**[JP_MD_CH4_SEC5_BREAK_EXAMPLE_TITLE_PH]**\n",
        "```python\n",
        "for i in range(1, 10):\n",
        "    if i == 5:\n",
        "        print(\"[JP_PY_STRING_CH4_SEC5_FOUND_5_BREAK_PH]\")\n",
        "        break\n",
        "    print(f\"[JP_PY_STRING_CH4_SEC5_CURRENT_NUM_PH]{i}\")\n",
        "```\n\n",
        "**[JP_MD_CH4_SEC5_CONTINUE_TITLE_PH]**\n",
        "[JP_MD_CH4_SEC5_CONTINUE_P1_PH]\n\n",
        "**[JP_MD_CH4_SEC5_CONTINUE_EXAMPLE_TITLE_PH]**\n",
        "```python\n",
        "for i in range(1, 6):\n",
        "    if i == 3:\n",
        "        print(\"[JP_PY_STRING_CH4_SEC5_SKIPPING_3_PH]\")\n",
        "        continue\n",
        "    print(f\"[JP_PY_STRING_CH4_SEC5_PROCESSED_NUM_PH]{i}\")\n",
        "```\n",
        "[JP_MD_CH4_SEC5_P2_PH]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH4_SEC5_EX_TITLE_PH]\n\n",
        "[JP_MD_CH4_SEC5_EX_PROMPT_P1_PH]\n\n",
        "[JP_MD_CH4_SEC5_EX_PROMPT_P2_PH]"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def loop_control_break_continue():\n",
        "  # [JP_PY_COMMENT_CH4_SEC5_AS_BREAK_PRACTICE_PH]\n",
        "  # print(\"--- break の練習 ---\")\n",
        "  # for i in range(1, 11):\n",
        "  #   if i == 7:\n",
        "  #     print(\"[JP_PY_STRING_CH4_SEC5_AS_LUCKY7_BREAK_PH]\")\n",
        "  #     break\n",
        "  #   print(i)\n",
        "  \n",
        "  # [JP_PY_COMMENT_CH4_SEC5_AS_CONTINUE_PRACTICE_PH]\n",
        "  # print(\"\\n--- continue の練習 ---\")\n",
        "  # for i in range(1, 11):\n",
        "  #   if i % 3 == 0:\n",
        "  #     print(f\"{i}[JP_PY_STRING_CH4_SEC5_AS_MULTIPLE_OF_3_SKIP_PH]\")\n",
        "  #     continue\n",
        "  #   print(f\"[JP_PY_STRING_CH4_SEC5_AS_CURRENT_NUM_PH]{i}\")\n",
        "  pass\n",
        "# loop_control_break_continue() # [JP_PY_COMMENT_CH4_SEC5_AS_CALL_FUNC_PH]"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH4_SEC5_PH]"},
      "source": [
        "#@title [JP_CHECK_TITLE_CH4_SEC5_PH] { display-mode: \"form\" }\n",
        "print(\"[JP_CHECK_TEXT_CH4_SEC5_PH]\")"
      ],
      "outputs": [], "execution_count": None
    },
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "def loop_control_break_continue_solution():\n",
        "  print(\"--- break の練習 ---\")\n",
        "  for i in range(1, 11):\n",
        "    if i == 7:\n",
        "      print(\"ラッキーセブン！ループを終了します。\")\n",
        "      break\n",
        "    print(i)\n",
        "  \n",
        "  print(\"\\n--- continue の練習 ---\")\n",
        "  for i in range(1, 11):\n",
        "    if i % 3 == 0:\n",
        "      print(f\"{i}は3の倍数なのでスキップします。\")\n",
        "      continue\n",
        "    print(f\"現在の数値：{i}\")\n",
        "loop_control_break_continue_solution()"
      ],
      "outputs": [], "execution_count": None
    }
]


try:
    print(f"Python script to append Chapters 3 & 4 skeletons. Notebook path: {os.path.abspath(notebook_path)}")

    base_dir = "/app"
    full_notebook_path = os.path.join(base_dir, notebook_path.lstrip('/'))

    notebook_dir = os.path.dirname(full_notebook_path)
    if not os.path.exists(notebook_dir):
        os.makedirs(notebook_dir)
        print(f"Created directory: {notebook_dir}")

    if not os.path.exists(full_notebook_path):
        print(f"Error: Notebook file '{full_notebook_path}' not found. It should contain Chapters 1-2.")
        # Initialize with empty notebook structure if it doesn't exist, to prevent load error
        # This is a fallback, ideally the file from previous step (Ch1-2) should exist.
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
        print("Existing notebook (Chapters 1-2) loaded successfully.")

    # Append Chapter 3 and 4 cells
    notebook_data['cells'].extend(chapter3_cells)
    print(f"Appended {len(chapter3_cells)} cells for Chapter 3 skeleton.")
    notebook_data['cells'].extend(chapter4_cells)
    print(f"Appended {len(chapter4_cells)} cells for Chapter 4 skeleton.")

    with open(full_notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook_data, f, ensure_ascii=False, indent=2)
    print(f"Successfully appended Chapters 3-4 skeletons to {full_notebook_path}")
    print(f"File {full_notebook_path} exists. Size: {os.path.getsize(full_notebook_path)}")

except FileNotFoundError as fnf_error:
    print(f"Error - File Not Found: {fnf_error}")
except json.JSONDecodeError as json_error:
    print(f"Error - JSON Decode Error: {json_error}")
except Exception as e:
    print(f"Script execution error: {e}")
