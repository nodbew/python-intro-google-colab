import json
import os

notebook_path = 'src/beginner.ipynb'

notebook_content = {
  "cells": [
    # CHAPTER 1 CELLS
    # Cell 1: Markdown (Chapter Title, Sec 1.1 Title & Explanation)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# [JP_MD_CH1_TITLE_PH]\n\n",
        "## [JP_MD_CH1_SEC1_TITLE_PH]\n\n",
        "[JP_MD_CH1_SEC1_P1_PH]\n",
        "[JP_MD_CH1_SEC1_P2_PH]\n\n",
        "**[JP_MD_CH1_SEC1_PHILOSOPHY_TITLE_PH]**\n",
        "[JP_MD_CH1_SEC1_PHILOSOPHY_TEXT_PH]\n\n",
        "**[JP_MD_CH1_SEC1_USES_TITLE_PH]**\n",
        "[JP_MD_CH1_SEC1_USES_TEXT_PH]"
      ]
    },
    # Cell 2: Markdown (Exercise 1.1)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH1_SEC1_EX_TITLE_PH]\n\n",
        "[JP_MD_CH1_SEC1_EX_PROMPT_PH]"
      ]
    },
    # Cell 3: Markdown (Answer Space 1.1)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "[JP_MD_CH1_SEC1_AS_PROMPT_PH]\n",
        "1. [JP_MD_CH1_SEC1_AS_USE1_LABEL_PH]\n",
        "   [JP_MD_CH1_SEC1_AS_DESC_LABEL_PH]\n",
        "2. [JP_MD_CH1_SEC1_AS_USE2_LABEL_PH]\n",
        "   [JP_MD_CH1_SEC1_AS_DESC_LABEL_PH]"
      ]
    },
    # Cell 4: Markdown (Solution 1.1 - hidden)
    {
      "cell_type": "markdown",
      "metadata": {"jupyter": {"source_hidden": True}}, # Corrected metadata key
      "source": [
        "---<details><summary>[JP_MD_CH1_SEC1_SOL_SUMMARY_PH]</summary>\n\n",
        "[JP_MD_CH1_SEC1_SOL_DETAIL_P1_PH]\n",
        "[JP_MD_CH1_SEC1_SOL_DETAIL_P2_PH]\n",
        "</details>"
      ]
    },
    # Cell 5: Markdown (Sec 1.2 Title & Explanation)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH1_SEC2_TITLE_PH]\n\n",
        "[JP_MD_CH1_SEC2_P1_PH]\n",
        "*   **[JP_MD_CH1_SEC2_ITEM1_TITLE_PH]** [JP_MD_CH1_SEC2_ITEM1_TEXT_PH]\n",
        "*   **[JP_MD_CH1_SEC2_ITEM2_TITLE_PH]** [JP_MD_CH1_SEC2_ITEM2_TEXT_PH]\n",
        "*   **[JP_MD_CH1_SEC2_ITEM3_TITLE_PH]** [JP_MD_CH1_SEC2_ITEM3_TEXT_PH]\n",
        "*   **[JP_MD_CH1_SEC2_ITEM4_TITLE_PH]** [JP_MD_CH1_SEC2_ITEM4_TEXT_PH]\n",
        "*   **[JP_MD_CH1_SEC2_ITEM5_TITLE_PH]** [JP_MD_CH1_SEC2_ITEM5_TEXT_PH]"
      ]
    },
    # Cell 6: Markdown (Exercise 1.2)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH1_SEC2_EX_TITLE_PH]\n\n",
        "[JP_MD_CH1_SEC2_EX_PROMPT_PH]"
      ]
    },
    # Cell 7: Markdown (Answer Space 1.2)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": ["[JP_MD_CH1_SEC2_AS_PROMPT_PH]"]
    },
    # Cell 8: Markdown (Solution 1.2 - hidden)
    {
      "cell_type": "markdown",
      "metadata": {"jupyter": {"source_hidden": True}}, # Corrected metadata key
      "source": [
        "---<details><summary>[JP_MD_CH1_SEC2_SOL_SUMMARY_PH]</summary>\n\n",
        "[JP_MD_CH1_SEC2_SOL_DETAIL_P1_PH]\n",
        "</details>"
      ]
    },
    # Cell 9: Markdown (Sec 1.3 Title & Explanation)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH1_SEC3_TITLE_PH]\n\n",
        "[JP_MD_CH1_SEC3_P1_PH]\n",
        "*   **[JP_MD_CH1_SEC3_ITEM1_TITLE_PH]** [JP_MD_CH1_SEC3_ITEM1_TEXT_PH]\n",
        "*   **[JP_MD_CH1_SEC3_ITEM2_TITLE_PH]** [JP_MD_CH1_SEC3_ITEM2_TEXT_PH]\n",
        "*   **[JP_MD_CH1_SEC3_ITEM3_TITLE_PH]** [JP_MD_CH1_SEC3_ITEM3_TEXT_PH]\n\n",
        "[JP_MD_CH1_SEC3_P2_PH]"
      ]
    },
    # Cell 10: Markdown (Exercise 1.3)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH1_SEC3_EX_TITLE_PH]\n\n",
        "[JP_MD_CH1_SEC3_EX_PROMPT_PH]"
      ]
    },
    # Cell 11: Code (Answer Space 1.3)
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "def first_execution():\n",
        "  # [JP_PY_COMMENT_CH1_SEC3_EX_PH]\n",
        "  pass"
      ],
      "outputs": [], "execution_count": None # Using None for execution_count
    },
    # Cell 12: Code (Check Code 1.3 - hidden)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}}, # Corrected metadata key
      "source": [
        "#@title [JP_CHECK_TITLE_CH1_SEC3_PH] { display-mode: \"form\" }\n",
        "try:\n",
        "    import io; import sys; captured_output = io.StringIO(); sys.stdout = captured_output\n",
        "    # Assuming first_execution is defined in the user's answer cell\n",
        "    # For this check to work, the user must have executed their answer cell first\n",
        "    if 'first_execution' in globals() and callable(globals()['first_execution']):\n",
        "        globals()['first_execution']()\n",
        "        output = captured_output.getvalue().strip()\n",
        "        if output == \"学習開始！\":\n",
        "            print(\"素晴らしい！正しく「学習開始！」と表示できました。\")\n",
        "        else:\n",
        "            print(f\"表示内容が異なります。「学習開始！」と表示されるように修正してみましょう。あなたの出力: '{output}'\")\n",
        "    else:\n",
        "        print(\"first_execution関数が定義されていないか、呼び出し可能ではありません。前のセルで定義・実行してください。\")\n",
        "    sys.stdout = sys.__stdout__\n",
        "except Exception as e:\n",
        "    sys.stdout = sys.__stdout__\n",
        "    print(f\"エラーが発生しました: {e}\")"
      ],
      "outputs": [], "execution_count": None # Using None
    },
    # Cell 13: Code (Solution 1.3 - hidden)
    {
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}}, # Corrected metadata key
      "source": [
        "def first_execution():\n",
        "  print(\"学習開始！\")\n",
        "first_execution()"
      ],
      "outputs": [], "execution_count": None # Using None
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": { "name": "ipython", "version": 3 },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.10.12" # Example version
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}

# Ensure the /src directory exists
# The path in the notebook_path is relative to /app
base_dir = "/app/"
full_notebook_path = os.path.join(base_dir, notebook_path)
os.makedirs(os.path.dirname(full_notebook_path), exist_ok=True)

with open(full_notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook_content, f, ensure_ascii=False, indent=2)

print(f"Notebook skeleton for Chapter 1 created at {full_notebook_path}")
# Verify file
if os.path.exists(full_notebook_path):
    print(f"File {full_notebook_path} exists. Size: {os.path.getsize(full_notebook_path)}")
else:
    print(f"Error: File {full_notebook_path} was not created.")
