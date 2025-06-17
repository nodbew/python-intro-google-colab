import json
import os

notebook_path = 'src/beginner.ipynb'

# Define the cells for Chapter 7
chapter7_cells = [
    # CHAPTER 7 Header
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# [JP_MD_CH7_TITLE_PH]\n\n",
        "[JP_MD_CH7_INTRO_P1_PH]\n",
        "[JP_MD_CH7_INTRO_P2_PH]"
      ]
    },
    # Section 7.1 Explanation
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH7_SEC1_TITLE_PH]\n\n",
        "[JP_MD_CH7_SEC1_EXPLAIN_P1_PH]\n",
        "[JP_MD_CH7_SEC1_EXPLAIN_P2_PH]\n",
        "*   `'r'` ([JP_MD_CH7_SEC1_MODE_R_PH])\n",
        "[JP_MD_CH7_SEC1_EXPLAIN_P3_PH]\n",
        "*   `read()` ([JP_MD_CH7_SEC1_METHOD_READ_PH])\n",
        "*   `readline()` ([JP_MD_CH7_SEC1_METHOD_READLINE_PH])\n",
        "*   `readlines()` ([JP_MD_CH7_SEC1_METHOD_READLINES_PH])\n",
        "[JP_MD_CH7_SEC1_EXPLAIN_P4_PH]\n",
        "```python\n",
        "# [JP_PY_COMMENT_CH7_FILE_READ_EXAMPLE_PH]\n",
        "# [JP_PY_COMMENT_CH7_ASSUME_SAMPLE_TXT_EXISTS_PH]\n",
        "# with open(\"sample_placeholder.txt\", \"r\", encoding=\"utf-8\") as f:\n",
        "#     content = f.read()\n",
        "#     print(content)\n",
        "```\n",
        "[JP_MD_CH7_SEC1_EXPLAIN_P5_PH]"
      ]
    },
    # Section 7.1 Exercise
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH7_SEC1_EX_TITLE_PH]\n\n",
        "[JP_MD_CH7_SEC1_EX_TEXT_P1_PH]\n",
        "```text\n",
        "[JP_MD_CH7_SEC1_EX_SAMPLE_TEXT_LINE1_PH]\n",
        "[JP_MD_CH7_SEC1_EX_SAMPLE_TEXT_LINE2_PH]\n",
        "[JP_MD_CH7_SEC1_EX_SAMPLE_TEXT_LINE3_PH]\n",
        "```\n",
        "[JP_MD_CH7_SEC1_EX_TEXT_P2_PH]"
      ]
    },
    # Section 7.1 Answer Space
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def read_sample_file_exercise_ch7_sec1():\n",
        "  # [JP_PY_COMMENT_CH7_SEC1_AS_ENSURE_FILE_EXISTS_PH]\n",
        "  file_name_placeholder = \"poem_placeholder.txt\" \n",
        "  # [JP_PY_COMMENT_CH7_SEC1_AS_CREATE_SAMPLE_FILE_PH]\n",
        "  # try:\n",
        "  #   with open(file_name_placeholder, \"w\", encoding=\"utf-8\") as f_create:\n",
        "  #     f_create.write(\"[JP_PY_STRING_CH7_SEC1_AS_LINE1]\\n\")\n",
        "  #     f_create.write(\"[JP_PY_STRING_CH7_SEC1_AS_LINE2]\\n\")\n",
        "  #     f_create.write(\"[JP_PY_STRING_CH7_SEC1_AS_LINE3]\")\n",
        "  # except IOError:\n",
        "  #   print(f\"[JP_PY_STRING_CH7_SEC1_AS_FILE_CREATE_ERROR_PH] {file_name_placeholder}\")\n",
        "  #   return\n",
        "\n",
        "  # [JP_PY_COMMENT_CH7_SEC1_AS_READ_AND_PRINT_PH]\n",
        "  # try:\n",
        "  #   with open(file_name_placeholder, \"r\", encoding=\"utf-8\") as f_read:\n",
        "  #     # [JP_PY_COMMENT_CH7_SEC1_AS_YOUR_CODE_HERE_PH]\n",
        "  #     pass \n",
        "  # except FileNotFoundError:\n",
        "  #   print(f\"[JP_PY_STRING_CH7_SEC1_AS_FILE_NOT_FOUND_PH] {file_name_placeholder}\")\n",
        "  # except IOError:\n",
        "  #   print(f\"[JP_PY_STRING_CH7_SEC1_AS_FILE_READ_ERROR_PH] {file_name_placeholder}\")\n",
        "  pass\n",
        "# read_sample_file_exercise_ch7_sec1()"
      ],
      "outputs": [], "execution_count": None
    },
    # Section 7.1 Check Code
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH7_SEC1_PH]"},
      "source": [
        "#@title [JP_CHECK_TITLE_CH7_SEC1_PH] { display-mode: \"form\" }\n",
        "print(\"[JP_CHECK_TEXT_CH7_SEC1_PH]\")"
      ],
      "outputs": [], "execution_count": None
    },
    # Section 7.1 Solution
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "def read_sample_file_exercise_ch7_sec1_solution():\n",
        "  file_name = \"poem.txt\"\n",
        "  file_content = \"ふるいけや\\nかわずとびこむ\\nみずのおと\"\n",
        "  try:\n",
        "    with open(file_name, \"w\", encoding=\"utf-8\") as f:\n",
        "      f.write(file_content)\n",
        "    print(f\"'{file_name}' を準備しました。\")\n",
        "  except IOError as e:\n",
        "    print(f\"ファイル準備中にエラーが発生しました: {e}\")\n",
        "    return\n",
        "\n",
        "  print(f\"--- '{file_name}' の内容 ---\")\n",
        "  try:\n",
        "    with open(file_name, \"r\", encoding=\"utf-8\") as f:\n",
        "      content = f.read()\n",
        "      print(content)\n",
        "  except FileNotFoundError:\n",
        "    print(f\"エラー: ファイル '{file_name}' が見つかりません。\")\n",
        "  except IOError as e:\n",
        "    print(f\"ファイル読み込み中にエラーが発生しました: {e}\")\n",
        "\n",
        "read_sample_file_exercise_ch7_sec1_solution()"
      ],
      "outputs": [], "execution_count": None
    },
    # Section 7.2 Skeleton (Markdown explanation, exercise, code answer, check, solution)
    { "cell_type": "markdown", "metadata": {}, "source": ["## [JP_MD_CH7_SEC2_TITLE_PH]\n\n", "[JP_MD_CH7_SEC2_EXPLAIN_P1_PH]"] },
    { "cell_type": "markdown", "metadata": {}, "source": ["### [JP_MD_CH7_SEC2_EX_TITLE_PH]\n\n", "[JP_MD_CH7_SEC2_EX_PROMPT_PH]"] },
    { "cell_type": "code", "metadata": {}, "source": ["# [JP_PY_COMMENT_CH7_SEC2_AS_PH]"], "outputs": [], "execution_count": None },
    { "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH7_SEC2_PH]"}, "source": ["#@title [JP_CHECK_TITLE_CH7_SEC2_PH] { display-mode: \"form\" }\nprint(\"[JP_CHECK_TEXT_CH7_SEC2_PH]\")"], "outputs": [], "execution_count": None },
    { "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}}, "source": ["# [JP_PY_COMMENT_CH7_SEC2_SOL_PH]\nprint(\"第7章2節の解答例です。\")"], "outputs": [], "execution_count": None },
    # Section 7.3 Skeleton (Markdown explanation, exercise, code answer, check, solution)
    { "cell_type": "markdown", "metadata": {}, "source": ["## [JP_MD_CH7_SEC3_TITLE_PH]\n\n", "[JP_MD_CH7_SEC3_EXPLAIN_P1_PH]"] },
    { "cell_type": "markdown", "metadata": {}, "source": ["### [JP_MD_CH7_SEC3_EX_TITLE_PH]\n\n", "[JP_MD_CH7_SEC3_EX_PROMPT_PH]"] },
    { "cell_type": "code", "metadata": {}, "source": ["# [JP_PY_COMMENT_CH7_SEC3_AS_PH]"], "outputs": [], "execution_count": None },
    { "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH7_SEC3_PH]"}, "source": ["#@title [JP_CHECK_TITLE_CH7_SEC3_PH] { display-mode: \"form\" }\nprint(\"[JP_CHECK_TEXT_CH7_SEC3_PH]\")"], "outputs": [], "execution_count": None },
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "import csv\n",
        "def write_and_read_csv_ch7_sec3_solution():\n",
        "  product_data = [\n",
        "      [\"商品名\", \"価格\", \"在庫数\"],\n",
        "      [\"リンゴ\", 150, 30],\n",
        "      [\"バナナ\", 100, 50],\n",
        "      [\"みかん\", 120, 40]\n",
        "  ]\n",
        "  csv_file_name = \"products_solution.csv\"\n",
        "  try:\n",
        "      with open(csv_file_name, \"w\", newline='', encoding=\"utf-8\") as f:\n",
        "          writer = csv.writer(f)\n",
        "          writer.writerows(product_data)\n",
        "      print(f\"'{csv_file_name}' に商品データを書き出しました。\")\n",
        "  except Exception as e:\n",
        "      print(f\"CSV書き出しエラー: {e}\")\n",
        "\n",
        "  print(f\"\\n--- '{csv_file_name}' の内容 --- \")\n",
        "  try:\n",
        "      with open(csv_file_name, \"r\", encoding=\"utf-8\") as f:\n",
        "          reader = csv.reader(f)\n",
        "          header = next(reader)\n",
        "          print(f\"ヘッダー: {header}\")\n",
        "          print(\"\\n商品詳細：\")\n",
        "          for row in reader:\n",
        "              if len(row) == 3:\n",
        "                  print(f\"{row[0]}：{row[1]}円、在庫：{row[2]}個\")\n",
        "  except Exception as e:\n",
        "      print(f\"CSV読み込みエラー: {e}\")\n",
        "write_and_read_csv_ch7_sec3_solution()"
      ],
      "outputs": [], "execution_count": None
    }
]

# Define the cells for Chapter 8
chapter8_cells = [
    # CHAPTER 8 Header
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# [JP_MD_CH8_TITLE_PH]\n\n",
        "[JP_MD_CH8_INTRO_P1_PH]\n",
        "[JP_MD_CH8_INTRO_P2_PH]"
      ]
    },
    # Section 8.1 Explanation
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH8_SEC1_TITLE_PH]\n\n",
        "[JP_MD_CH8_SEC1_EXPLAIN_P1_PH]\n",
        "*   **[JP_MD_CH8_SEC1_SYNTAX_ERROR_TITLE_PH]** [JP_MD_CH8_SEC1_SYNTAX_ERROR_TEXT_PH]\n",
        "*   **[JP_MD_CH8_SEC1_EXCEPTION_TITLE_PH]** [JP_MD_CH8_SEC1_EXCEPTION_TEXT_PH]\n",
        "[JP_MD_CH8_SEC1_EXPLAIN_P2_PH]"
      ]
    },
    # Section 8.1 Exercise
    { "cell_type": "markdown", "metadata": {}, "source": ["### [JP_MD_CH8_SEC1_EX_TITLE_PH]\n\n", "[JP_MD_CH8_SEC1_EX_TEXT_P1_PH]\n1. [JP_MD_CH8_SEC1_EX_STEP1_PH]\n2. [JP_MD_CH8_SEC1_EX_STEP2_PH]\n[JP_MD_CH8_SEC1_EX_TEXT_P2_PH]"] },
    # Section 8.1 Answer Space (Code)
    { "cell_type": "code", "metadata": {}, "source": ["# [JP_PY_COMMENT_CH8_SEC1_AS_SYNTAX_ERROR_PH]\n# print(\"Hello\"\n\n# [JP_PY_COMMENT_CH8_SEC1_AS_RUNTIME_ERROR_PH]\n# result = 10 / 0"], "outputs": [], "execution_count": None },
    # Section 8.1 Check Code
    { "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH8_SEC1_PH]"}, "source": ["#@title [JP_CHECK_TITLE_CH8_SEC1_PH] { display-mode: \"form\" }\nprint(\"[JP_CHECK_TEXT_CH8_SEC1_PH]\")"], "outputs": [], "execution_count": None },
    # Section 8.1 Solution
    { "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}}, "source": ["print(\"シンタックスエラーの例は、コメントを外すとPythonインタープリタがエラーを出します。\")\nprint(\"実行時エラーの例は、コメントを外して実行すると ZeroDivisionError が発生します。\")"], "outputs": [], "execution_count": None },
    # ... (Skeleton for sections 8.2, 8.3 with placeholders for markdown)
    { "cell_type": "markdown", "metadata": {}, "source": ["## [JP_MD_CH8_SEC2_TITLE_PH]\n\n", "[JP_MD_CH8_SEC2_EXPLAIN_P1_PH]"] },
    { "cell_type": "markdown", "metadata": {}, "source": ["## [JP_MD_CH8_SEC3_TITLE_PH]\n\n", "[JP_MD_CH8_SEC3_EXPLAIN_P1_PH]"] },
    # Section 8.4 (Example from prompt)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [ "## [JP_MD_CH8_SEC4_TITLE_PH]\n\n", "[JP_MD_CH8_SEC4_EXPLAIN_P1_PH]\n\n", "[JP_MD_CH8_SEC4_EXPLAIN_P2_PH]" ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [ "### [JP_MD_CH8_SEC4_EX_TITLE_PH]\n\n", "[JP_MD_CH8_SEC4_EX_TEXT_P1_PH]" ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "def evaluate_student_score_ch8_sec4(score):\n",
            "    # [JP_PY_COMMENT_CH8_SEC4_AS_TYPE_CHECK_PH]\n",
            "    # if not isinstance(score, (int, float)):\n",
            "    #     raise TypeError(\"[JP_PY_STRING_CH8_SEC4_AS_TYPE_ERROR_MSG_PH]\")\n",
            "    # [JP_PY_COMMENT_CH8_SEC4_AS_VALUE_CHECK_PH]\n",
            "    # if not (0 <= score <= 100):\n",
            "    #     raise ValueError(\"[JP_PY_STRING_CH8_SEC4_AS_VALUE_ERROR_MSG_PH]\")\n",
            "    # \n",
            "    # [JP_PY_COMMENT_CH8_SEC4_AS_GRADE_PH]\n",
            "    # if score < 60:\n",
            "    #     return \"[JP_PY_STRING_CH8_SEC4_AS_FAIL_PH]\"\n",
            "    # else:\n",
            "    #     return \"[JP_PY_STRING_CH8_SEC4_AS_PASS_PH]\"\n",
            "    pass\n",
            "\n",
            "def check_score_and_raise_exercise_ch8_sec4():\n",
            "    # [JP_PY_COMMENT_CH8_SEC4_AS_TEST_CASES_PH]\n",
            "    # scores_to_test = [85, 55, 105, -10, \"abc\", 95.5]\n",
            "    # for s in scores_to_test:\n",
            "    #     try:\n",
            "    #         result = evaluate_student_score_ch8_sec4(s)\n",
            "    #         print(f\"[JP_PY_STRING_CH8_SEC4_AS_SCORE_LABEL_PH] {s}: {result}\")\n",
            "    #     except TypeError as te:\n",
            "    #         print(f\"[JP_PY_STRING_CH8_SEC4_AS_SCORE_LABEL_PH] {s}: [JP_PY_STRING_CH8_SEC4_AS_ERROR_LABEL_PH] - {te}\")\n",
            "    #     except ValueError as ve:\n",
            "    #         print(f\"[JP_PY_STRING_CH8_SEC4_AS_SCORE_LABEL_PH] {s}: [JP_PY_STRING_CH8_SEC4_AS_ERROR_LABEL_PH] - {ve}\")\n",
            "    pass\n",
            "# check_score_and_raise_exercise_ch8_sec4() # [JP_PY_COMMENT_CH8_SEC4_AS_CALL_FUNC_PH]"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": { "jupyter": { "source_hidden": True }, "title": "[JP_CHECK_TITLE_CH8_SEC4_PH]" },
        "outputs": [],
        "source": [
            "#@title [JP_CHECK_TITLE_CH8_SEC4_PH] { display-mode: \"form\" }\n",
            "print(\"[JP_CHECK_TEXT_CH8_SEC4_PH]\")"
        ]
    },
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "def check_score_and_raise_exercise_ch8_sec4_solution():\n",
        "  def evaluate_student_score(score):\n",
        "    if not isinstance(score, (int, float)): \n",
        "        raise TypeError(\"点数は数値でなければなりません。\")\n",
        "    if score < 0 or score > 100:\n",
        "      raise ValueError(\"点数は0から100の間でなければなりません。\")\n",
        "    elif score < 60:\n",
        "      return \"不可\"\n",
        "    else:\n",
        "      return \"合格\"\n",
        "\n",
        "  scores_to_test = [85, 55, 105, -10, \"abc\"] \n",
        "  for s_val in scores_to_test:\n",
        "    print(f\"\\nテストする点数: {s_val}\")\n",
        "    try:\n",
        "      result = evaluate_student_score(s_val)\n",
        "      print(f\"結果: {result}\")\n",
        "    except ValueError as e_val:\n",
        "      print(f\"値エラー: {e_val}\")\n",
        "    except TypeError as e_type:\n",
        "      print(f\"型エラー: {e_type}\")\n",
        "\n",
        "check_score_and_raise_exercise_ch8_sec4_solution()"
      ],
      "outputs": [], "execution_count": None
    }
]

try:
    print(f"Python script to append Ch7 & Ch8 skeletons. Notebook path: {os.path.abspath(notebook_path)}")

    base_dir = "/app"
    full_notebook_path = os.path.join(base_dir, notebook_path.lstrip('/'))

    notebook_dir = os.path.dirname(full_notebook_path)
    if not os.path.exists(notebook_dir):
        os.makedirs(notebook_dir)
        print(f"Created directory: {notebook_dir}")

    if not os.path.exists(full_notebook_path):
        print(f"Error: Notebook file '{full_notebook_path}' not found. It should contain Chapters 1-6.")
        notebook_data = { "cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 5 } # Basic new notebook
        notebook_data["metadata"] = {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.10.12"}
        }
        print("Initialized new notebook data as existing file was not found.")
    else:
        with open(full_notebook_path, 'r', encoding='utf-8') as f:
            notebook_data = json.load(f)
        print("Existing notebook (Chapters 1-6) loaded successfully.")

    notebook_data['cells'].extend(chapter7_cells)
    print(f"Appended {len(chapter7_cells)} cells for Chapter 7 skeleton.")
    notebook_data['cells'].extend(chapter8_cells)
    print(f"Appended {len(chapter8_cells)} cells for Chapter 8 skeleton.")

    with open(full_notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook_data, f, ensure_ascii=False, indent=2)
    print(f"Successfully appended Chapters 7-8 skeletons to {full_notebook_path}")
    print(f"File {full_notebook_path} exists. Size: {os.path.getsize(full_notebook_path)}")

except FileNotFoundError as fnf_error:
    print(f"Error - File Not Found (unexpected): {fnf_error}")
except json.JSONDecodeError as json_error:
    print(f"Error - JSON Decode Error: {json_error}")
except Exception as e:
    print(f"Script execution error: {e}")
