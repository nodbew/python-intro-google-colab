import json
import os

notebook_path = 'src/beginner.ipynb'

# Japanese content for Chapter 8 Markdown, embedded as a Python dictionary
jp_mapping_ch8 = {
  "[JP_CHAP8_TITLE_PH]": "# 第8章：エラー処理 (Exception Handling)",
  "[JP_CHAP8_INTRO_P1_PH]": "プログラムを書いていると、予期せぬ問題や誤りによってプログラムが途中で停止してしまうことがあります。これらの問題は「エラー」や「例外」と呼ばれます。",
  "[JP_CHAP8_INTRO_P2_PH]": "適切にエラー処理を行うことで、プログラムが突然クラッシュするのを防いだり、ユーザーに分かりやすいメッセージを伝えたり、問題の原因を特定しやすくしたりすることができます。この章では、Pythonにおけるエラーの種類と、それらを扱うための基本的な方法（例外処理）について学びます。",
  "[JP_SEC8_1_TITLE_PH]": "## 8.1 エラーとは？",
  "[JP_SEC8_1_EXPLAIN_P1_PH]": "Pythonにおけるエラーは、大きく分けて2つの種類があります。",
  "[JP_SEC8_1_SYNTAX_ERROR_TITLE_PH]": "*   **シンタックスエラー (SyntaxError)：**",
  "[JP_SEC8_1_SYNTAX_ERROR_TEXT_PH]": "文法的な誤りです。Pythonのルールに従っていないコードを書いた場合に発生します。プログラムが実行される前にPythonインタープリタによって検出されます。例えば、括弧の閉じ忘れ、コロンの付け忘れなどです。",
  "[JP_SEC8_1_EXCEPTION_TITLE_PH]": "*   **例外 (Exception)：**",
  "[JP_SEC8_1_EXCEPTION_TEXT_PH]": "プログラムの文法は正しいものの、実行中に何らかの問題が発生した場合に起こります。例えば、0で割り算をしようとした場合 (ZeroDivisionError)、存在しないファイルを開こうとした場合 (FileNotFoundError)、異なるデータ型同士で不適切な演算をしようとした場合 (TypeError) などがあります。",
  "[JP_SEC8_1_EXPLAIN_P2_PH]": "例外が発生すると、プログラムはその時点で処理を中断し、エラーメッセージ（トレースバックといいます）を表示します。このトレースバックには、エラーの種類、発生場所、原因に関する情報が含まれています。",
  "[JP_EX8_1_TITLE_PH]": "### 練習問題 8.1",
  "[JP_EX8_1_TEXT_P1_PH]": "以下のコードをそれぞれ別のコードセルに入力し、実行してみてください。",
  "[JP_EX8_1_STEP1_PH]": "1.  シンタックスエラーが発生する例：",
  "[JP_EX8_1_STEP2_PH]": "2.  実行時エラー（例外）が発生する例：",
  "[JP_EX8_1_TEXT_P2_PH]": "それぞれどのような種類のエラーメッセージが表示されるか確認し、エラーメッセージが何を示しているか（例：どの行で、どのような問題が起きたか）を読み取ってみましょう。",
  "[JP_CHECK_CODE_TITLE_EX8_1_PH]": "練習問題8.1の確認",
  "[JP_CHECK_CODE_8_1_MANUAL_PROMPT_PH]": "上記のコード例をそれぞれ実行し、表示されるエラーメッセージを確認してください。シンタックスエラーと実行時エラーの違いを理解しましょう。",
  "[JP_SEC8_2_TITLE_PH]": "## 8.2 `try...except`ブロック (The `try...except` block)",
  "[JP_SEC8_2_EXPLAIN_P1_PH]": "プログラム実行中に発生する可能性のある例外を捕捉し、それに対して適切な処理を行う仕組みを「例外処理 (Exception Handling)」といいます。Pythonでは、主に `try...except` ブロックを使って例外処理を記述します。",
  "[JP_SEC8_2_EXPLAIN_P2_PH]": "基本的な構文は以下の通りです。",
  "[JP_SEC8_2_EXPLAIN_P3_PH]": "*   `try`：このキーワードから始まるブロックの中に、例外が発生する可能性のある処理を書きます。\n*   `except`：`try`ブロック内で例外が発生した場合に、実行される処理をこのキーワードから始まるブロックに書きます。\n*   `[JP_ERROR_TYPE_PLACEHOLDER_PH]`：捕捉したい例外の型（種類）を指定します（例：`ValueError`, `ZeroDivisionError`）。特定の例外型を指定せず、単に `except:` と書くと、全ての種類の例外を捕捉しますが、これは通常推奨されません（予期せぬエラーまで隠蔽してしまう可能性があるため）。複数の異なる例外を処理したい場合は、`except`ブロックを複数書くことができます。\n*   `as e`：(任意) 発生した例外オブジェクト（エラーの詳細情報を持つ）を変数 `e`（任意の変数名で可）に代入します。これにより、エラーメッセージなどをプログラム内で利用できます。",
  "[JP_SEC8_2_EXPLAIN_P4_PH]": "例：ユーザーからの入力値を数値に変換し、割り算を行う",
  "[JP_EX8_2_TITLE_PH]": "### 練習問題 8.2",
  "[JP_EX8_2_TEXT_P1_PH]": "ユーザーに割られる数（分子）と割る数（分母）をそれぞれ入力してもらい、割り算の結果を表示するプログラムを作成してください。ただし、以下のエラーに対応できるように `try...except` ブロックを使用してください。\n1.  ユーザーが数値以外の文字を入力した場合 (`ValueError`)：「エラー：有効な数値（整数または小数）を入力してください。」と表示する。\n2.  ユーザーが分母として0を入力した場合 (`ZeroDivisionError`)：「エラー：0で割ることはできません。」と表示する。",
  "[JP_CHECK_CODE_TITLE_EX8_2_PH]": "練習問題8.2の回答をチェック",
  "[JP_CHECK_CODE_8_2_MANUAL_PROMPT_PH]": "robust_division_exercise() 関数を実行し、数値以外の入力や0での除算を試して、エラーメッセージが正しく表示されるか確認してください。",
  "[JP_SEC8_3_TITLE_PH]": "## 8.3 `else`と`finally` (The `else` and `finally` clauses)",
  "[JP_SEC8_3_EXPLAIN_P1_PH]": "`try...except` ブロックには、さらに `else` 句と `finally` 句を追加することができます。",
  "[JP_SEC8_3_ELSE_DEF_PH]": "`else`：`try` ブロック内で例外が発生しなかった場合にのみ実行される処理を記述します。",
  "[JP_SEC8_3_FINALLY_DEF_PH]": "`finally`：例外が発生したかどうかに関わらず、`try` ブロックの処理が終わった後に必ず実行される処理を記述します。ファイルクローズやリソース解放など、後始末の処理によく使われます。",
  "[JP_SEC8_3_EXPLAIN_P2_PH]": "構文：",
  "[JP_SEC8_3_EXPLAIN_P3_PH]": "例：ファイル読み込み処理",
  "[JP_EX8_3_TITLE_PH]": "### 練習問題 8.3",
  "[JP_EX8_3_TEXT_P1_PH]": "ファイル `data_exercise.txt` を読み込み、その内容を表示するプログラムを `try...except...else...finally` を使って作成してください。\n- `try` ブロックでファイルを開き、内容を読み込んで表示します。\n- `FileNotFoundError` が発生した場合は、「エラー：ファイルが見つかりません。」と表示します。\n- `IOError` (その他の入出力エラー) が発生した場合は、「エラー：ファイルの読み書き中に問題が発生しました。」と表示します。\n- `else` ブロックでは、「ファイルは正常に読み込まれました。」と表示します。\n- `finally` ブロックでは、「ファイル処理を終了します。」と表示します。\n\nファイルが存在する場合としない場合の両方で、各ブロックがどのように実行されるか確認しましょう。",
  "[JP_CHECK_CODE_TITLE_EX8_3_PH]": "練習問題8.3の回答をチェック",
  "[JP_CHECK_CODE_8_3_MANUAL_PROMPT_PH]": "file_read_with_else_finally_exercise() 関数を実行し、ファイルが存在する場合としない場合（手動でファイルを作成・削除して試す）で、期待通りのメッセージが表示されるか確認してください。",
  "[JP_SEC8_4_TITLE_PH]": "## 8.4 例外を発生させる (`raise`) (Raising exceptions)",
  "[JP_SEC8_4_EXPLAIN_P1_PH]": "プログラムの中で、特定の条件が満たされたときに意図的に例外を発生させたい場合があります。このような場合には `raise` キーワードを使います。",
  "[JP_SEC8_4_EXPLAIN_P2_PH]": "`raise 例外クラス(エラーメッセージ)` のようにして、指定した例外クラスのインスタンスを発生させることができます。",
  "[JP_EX8_4_TITLE_PH]": "### 練習問題 8.4",
  "[JP_EX8_4_TEXT_P1_PH]": "学生の点数（0から100点）を評価する関数 `evaluate_student_score(score)` を作成します。\n- 点数が数値でない場合（例：文字列）は `TypeError` を発生させ、「点数は数値でなければなりません。」というメッセージを持たせます。\n- 点数が0未満または100を超える場合は `ValueError` を発生させ、「点数は0から100の間でなければなりません。」というメッセージを持たせます。\n- 点数が60点未満の場合は文字列「不可」を返します。\n- 点数が60点以上の場合は文字列「合格」を返します。\n\n作成した関数を、有効な点数、無効な点数（範囲外）、数値でない入力のそれぞれで呼び出し、`try...except` を使って適切にエラーメッセージを表示するか、結果を表示するようにしてください。",
  "[JP_CHECK_CODE_TITLE_EX8_4_PH]": "練習問題8.4の回答をチェック",
  "[JP_CHECK_CODE_8_4_MANUAL_PROMPT_PH]": "check_score_and_raise_exercise() 関数を実行し、様々な点数（85, 55, 105, -10, \"abc\"など）でテストして、期待通りの結果またはエラーメッセージが表示されるか確認してください。"
}

try:
    print(f"Python script started. Notebook path: {os.path.abspath(notebook_path)}")

    if not os.path.exists(notebook_path):
        print(f"Error: Notebook file not found at '{notebook_path}'")
        exit(1)
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook_data = json.load(f)
    print("Notebook loaded successfully.")

    cells_modified_count = 0

    for cell_index, cell in enumerate(notebook_data.get('cells', [])):
        if cell.get('cell_type') == 'markdown':
            original_source_as_list = cell.get('source', [])
            if not original_source_as_list:
                continue
            original_source_as_string = "".join(original_source_as_list)

            modified_source_string = original_source_as_string

            placeholder_found_in_cell = False
            is_chapter_8_cell = False
            # Check for Chapter 8 specific placeholders
            if ("[JP_CHAP8_" in original_source_as_string or
                "[JP_SEC8_" in original_source_as_string or
                "[JP_EX8_" in original_source_as_string or
                "[JP_AS_8_" in original_source_as_string or # Though not in current map, good to keep for robustness
                "[JP_SOL_8_" in original_source_as_string or # Though not in current map, good to keep for robustness
                "[JP_CHECK_CODE_TITLE_EX8_" in original_source_as_string or
                "[JP_CHECK_CODE_8_" in original_source_as_string): # Covers _MANUAL_PROMPT_PH
                is_chapter_8_cell = True

            if is_chapter_8_cell:
                for placeholder, japanese_text in jp_mapping_ch8.items():
                    if placeholder in modified_source_string:
                        modified_source_string = modified_source_string.replace(placeholder, japanese_text)
                        placeholder_found_in_cell = True

            if placeholder_found_in_cell and modified_source_string != original_source_as_string:
                # Convert the modified string back to a list of strings (lines)
                # Jupyter notebook format expects a list of strings for the 'source' field.
                # Each string in the list is a line, ending with '\n' if it's not the last line.
                # However, json.load usually preserves line endings as they are.
                # The safest way is to split by lines and then re-add newlines only where needed

                # Splitting the string into lines
                lines = modified_source_string.splitlines(True) # True keeps line endings

                # If the original cell source was just [''], and modified is also empty, keep it as ['']
                if original_source_as_list == [''] and not modified_source_string:
                    new_source_list = ['']
                # If the original cell source was empty or ['\n'] etc. and modified is empty, make it empty list
                elif not modified_source_string:
                     new_source_list = [] # or [''] depending on how empty cells are preferred
                else:
                    new_source_list = lines

                cell['source'] = new_source_list
                cells_modified_count += 1
                # print(f"Replaced content in markdown cell {cell_index} (Chapter 8). Original: {original_source_as_string[:50]}, New: {modified_source_string[:50]}")


    if cells_modified_count > 0:
        print(f"Total Chapter 8 markdown cells modified: {cells_modified_count}")
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook_data, f, ensure_ascii=False, indent=2)
        print(f"Successfully updated notebook with Japanese Chapter 8 markdown: {notebook_path}")
    else:
        print("No Chapter 8 placeholders found or replaced in any markdown cells. Check notebook structure and placeholder content.")
        # Debugging output
        debug_cell_count = 0
        for cell_debug_idx, cell_debug_val in enumerate(notebook_data.get('cells', [])):
            if cell_debug_val.get('cell_type') == 'markdown':
                 source_str_debug = "".join(cell_debug_val.get('source', []))
                 if ("[JP_CHAP8_" in source_str_debug or
                     "[JP_SEC8_" in source_str_debug or
                     "[JP_EX8_" in source_str_debug or
                     "[JP_CHECK_CODE_TITLE_EX8_" in source_str_debug or
                     "[JP_CHECK_CODE_8_" in source_str_debug):
                    print(f"Debug: Ch8 MD Cell {cell_debug_idx} Source: {source_str_debug[:200]}...")
                    debug_cell_count+=1
            if debug_cell_count > 10 :
                break
        if debug_cell_count == 0:
            print("Debug: No markdown cells with Chapter 8 placeholders found during debug scan either.")


except FileNotFoundError as fnf_error:
    print(f"Error - File Not Found: {fnf_error}")
except json.JSONDecodeError as json_error:
    print(f"Error - JSON Decode Error: {json_error}")
except Exception as e:
    print(f"Script execution error: {e}")
