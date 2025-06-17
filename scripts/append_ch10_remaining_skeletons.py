import json
import os

notebook_path = 'src/beginner.ipynb'

# Define the cells for Chapter 10, Sections 10.2, 10.3, 10.4
chapter10_remaining_sections_cells = [
    # Section 10.2: サブクラスの定義 (Defining a subclass)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH10_SEC2_TITLE_PH]\n\n",
        "[JP_MD_CH10_SEC2_EXPLAIN_P1_PH]\n",
        "```python\n",
        "class ParentClassPlaceholder:\n",
        "    def __init__(self, name_ph):\n",
        "        self.name_ph = name_ph\n",
        "    def parent_method_placeholder(self):\n",
        "        print(f\"[JP_PY_STRING_CH10_SEC2_PARENT_METHOD_MSG_PH] {self.name_ph}\")\n",
        "\n",
        "class ChildClassPlaceholder(ParentClassPlaceholder): # [JP_PY_COMMENT_CH10_SEC2_INHERITANCE_SYNTAX_PH]\n",
        "    pass # [JP_PY_COMMENT_CH10_SEC2_CHILD_CAN_HAVE_OWN_METHODS_PH]\n",
        "\n",
        "# child_obj_placeholder = ChildClassPlaceholder(\"[JP_PY_STRING_CH10_SEC2_CHILD_NAME_PH]\")\n",
        "# child_obj_placeholder.parent_method_placeholder() # [JP_PY_COMMENT_CH10_SEC2_CHILD_USES_PARENT_METHOD_PH]\n",
        "```\n",
        "[JP_MD_CH10_SEC2_EXPLAIN_P2_PH]"
      ]
    },
    { # Exercise 10.2
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### [JP_MD_CH10_SEC2_EX_TITLE_PH]\n\n",
        "[JP_MD_CH10_SEC2_EX_TEXT_P1_PH]\n",
        "1. [JP_MD_CH10_SEC2_EX_STEP1_PH]\n",
        "2. [JP_MD_CH10_SEC2_EX_STEP2_PH]\n",
        "3. [JP_MD_CH10_SEC2_EX_STEP3_PH]"
      ]
    },
    { # Answer Space 10.2
      "cell_type": "code",
      "metadata": {},
      "source": [
        "# [JP_PY_COMMENT_CH10_SEC2_AS_ANIMAL_CLASS_PH]\n",
        "class Animal_CH10S2:\n",
        "    def __init__(self, name_param):\n",
        "        self.name = name_param\n",
        "        print(f\"{self.name}が誕生しました。\")\n",
        "\n",
        "    def speak(self):\n",
        "        print(f\"{self.name}は...と鳴きます。\")\n",
        "\n",
        "# [JP_PY_COMMENT_CH10_SEC2_AS_DOG_SUBCLASS_PH]\n",
        "# class Dog(Animal_CH10S2): # Animal_CH10S2クラスを継承\n",
        "#     pass\n",
        "\n",
        "# [JP_PY_COMMENT_CH10_SEC2_AS_CREATE_DOG_OBJECT_PH]\n",
        "# my_dog_placeholder = Dog(\"[JP_PY_STRING_CH10_SEC2_AS_DOG_NAME_POCHI_PH]\")\n",
        "# print(my_dog_placeholder.name)\n",
        "# my_dog_placeholder.speak()"
      ],
      "outputs": [], "execution_count": None
    },
    { # Check Code 10.2
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH10_SEC2_PH]"},
      "source": [
        "#@title [JP_CHECK_TITLE_CH10_SEC2_PH] { display-mode: \"form\" }\n",
        "print(\"[JP_CHECK_TEXT_CH10_SEC2_PH]\")"
      ],
      "outputs": [], "execution_count": None
    },
    { # Solution 10.2
      "cell_type": "code",
      "metadata": {"jupyter": {"source_hidden": True}},
      "source": [
        "class AnimalSolution_CH10S2:\n",
        "    def __init__(self, name):\n",
        "        self.name = name\n",
        "        print(f\"動物「{self.name}」が誕生しました。\")\n",
        "\n",
        "    def speak(self):\n",
        "        print(f\"{self.name}は...（一般的な鳴き声）...\")\n",
        "\n",
        "class DogFromAnimal_CH10S2(AnimalSolution_CH10S2):\n",
        "    pass\n",
        "\n",
        "pochi_ch10s2 = DogFromAnimal_CH10S2(\"ポチ\")\n",
        "print(f\"犬の名前: {pochi_ch10s2.name}\")\n",
        "pochi_ch10s2.speak()"
      ],
      "outputs": [], "execution_count": None
    },

    # Section 10.3: メソッドのオーバーライド (Overriding methods)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH10_SEC3_TITLE_PH]\n\n",
        "[JP_MD_CH10_SEC3_EXPLAIN_P1_PH]\n",
        "```python\n",
        "class ParentClassPlaceholder_CH10S3:\n",
        "    def greet_placeholder(self):\n",
        "        print(\"[JP_PY_STRING_CH10_SEC3_PARENT_GREETING_PH]\")\n",
        "\n",
        "class ChildClassPlaceholder_CH10S3(ParentClassPlaceholder_CH10S3):\n",
        "    def greet_placeholder(self): # [JP_PY_COMMENT_CH10_SEC3_OVERRIDE_PH]\n",
        "        print(\"[JP_PY_STRING_CH10_SEC3_CHILD_GREETING_PH]\")\n",
        "\n",
        "# parent_obj_ph = ParentClassPlaceholder_CH10S3()\n",
        "# child_obj_ph = ChildClassPlaceholder_CH10S3()\n",
        "# parent_obj_ph.greet_placeholder()\n",
        "# child_obj_ph.greet_placeholder() \n",
        "```\n",
        "[JP_MD_CH10_SEC3_EXPLAIN_P2_PH]"
      ]
    },
    { # Exercise 10.3
      "cell_type": "markdown", "metadata": {}, "source": ["### [JP_MD_CH10_SEC3_EX_TITLE_PH]\n\n","[JP_MD_CH10_SEC3_EX_TEXT_P1_PH]"]
    },
    { # Answer Space 10.3
      "cell_type": "code", "metadata": {}, "source": [
        "# [JP_PY_COMMENT_CH10_SEC3_AS_ANIMAL_CLASS_PH]\n",
        "class Animal_CH10S3:\n", # Using unique name for this context
        "    def __init__(self, name_param):\n",
        "        self.name = name_param\n",
        "    def speak(self):\n",
        "        print(f\"{self.name}は...と鳴きます。\")\n",
        "\n",
        "# [JP_PY_COMMENT_CH10_SEC3_AS_DOG_OVERRIDE_PH]\n",
        "# class Dog(Animal_CH10S3):\n",
        "#     def speak(self):\n",
        "#         print(f\"{self.name}: [JP_PY_STRING_CH10_SEC3_AS_DOG_BARK_PH]\")\n",
        "\n",
        "# [JP_PY_COMMENT_CH10_SEC3_AS_CAT_OVERRIDE_PH]\n",
        "# class Cat(Animal_CH10S3):\n",
        "#     def speak(self):\n",
        "#         print(f\"{self.name}: [JP_PY_STRING_CH10_SEC3_AS_CAT_MEOW_PH]\")\n",
        "\n",
        "# [JP_PY_COMMENT_CH10_SEC3_AS_CREATE_CALL_PH]\n",
        "# my_dog = Dog(\"[JP_PY_STRING_CH10_SEC3_AS_DOG_NAME_PH]\")\n",
        "# my_cat = Cat(\"[JP_PY_STRING_CH10_SEC3_AS_CAT_NAME_PH]\")\n",
        "# my_dog.speak()\n",
        "# my_cat.speak()"
        ], "outputs": [], "execution_count": None },
    { # Check Code 10.3
      "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH10_SEC3_PH]"}, "source": ["#@title [JP_CHECK_TITLE_CH10_SEC3_PH] { display-mode: \"form\" }\n", "print(\"[JP_CHECK_TEXT_CH10_SEC3_PH]\")"], "outputs": [], "execution_count": None },
    { # Solution 10.3
      "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}}, "source": [
        "class AnimalSolution_CH10S3:\n",
        "    def __init__(self, name):\n",
        "        self.name = name\n",
        "        print(f\"動物「{self.name}」が誕生しました。\")\n",
        "    def speak(self):\n",
        "        print(f\"{self.name}は...（一般的な鳴き声）...\")\n",
        "class DogFromAnimal_CH10S3(AnimalSolution_CH10S3):\n",
        "    def speak(self):\n",
        "        print(f\"{self.name}: ワンワン！\")\n",
        "class CatFromAnimal_CH10S3(AnimalSolution_CH10S3):\n",
        "    def speak(self):\n",
        "        print(f\"{self.name}: ニャーニャー！\")\n",
        "inu_ch10s3 = DogFromAnimal_CH10S3(\"タロウ\")\n",
        "neko_ch10s3 = CatFromAnimal_CH10S3(\"ミケ\")\n",
        "inu_ch10s3.speak()\n",
        "neko_ch10s3.speak()"
        ], "outputs": [], "execution_count": None },

    # Section 10.4: `super()`関数 (The `super()` function)
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## [JP_MD_CH10_SEC4_TITLE_PH]\n\n",
        "[JP_MD_CH10_SEC4_EXPLAIN_P1_PH]\n",
        "[JP_MD_CH10_SEC4_EXPLAIN_P2_PH]\n",
        "```python\n",
        "class ParentClassPlaceholder_CH10S4:\n",
        "    def __init__(self, name_ph):\n",
        "        print(\"[JP_PY_STRING_CH10_SEC4_PARENT_INIT_CALLED_PH]\")\n",
        "        self.name_ph = name_ph\n",
        "\n",
        "class ChildClassPlaceholder_CH10S4(ParentClassPlaceholder_CH10S4):\n",
        "    def __init__(self, name_ph, child_attr_ph):\n",
        "        print(\"[JP_PY_STRING_CH10_SEC4_CHILD_INIT_CALLED_PH]\")\n",
        "        super().__init__(name_ph) # [JP_PY_COMMENT_CH10_SEC4_SUPER_CALL_PH]\n",
        "        self.child_attribute_ph = child_attr_ph # [JP_PY_COMMENT_CH10_SEC4_CHILD_SPECIFIC_ATTR_PH]\n",
        "\n",
        "# child_obj_ph = ChildClassPlaceholder_CH10S4(\"[JP_PY_STRING_CH10_SEC4_CHILD_NAME_PH]\", \"[JP_PY_STRING_CH10_SEC4_CHILD_ATTR_VALUE_PH]\")\n",
        "# print(child_obj_ph.name_ph)\n",
        "# print(child_obj_ph.child_attribute_ph)\n",
        "```\n",
        "[JP_MD_CH10_SEC4_EXPLAIN_P3_PH]"
      ]
    },
    { # Exercise 10.4
      "cell_type": "markdown", "metadata": {}, "source": ["### [JP_MD_CH10_SEC4_EX_TITLE_PH]\n\n","[JP_MD_CH10_SEC4_EX_TEXT_P1_PH]\n","1. [JP_MD_CH10_SEC4_EX_STEP1_PH]\n","2. [JP_MD_CH10_SEC4_EX_STEP2_PH]\n","3. [JP_MD_CH10_SEC4_EX_STEP3_PH]\n","4. [JP_MD_CH10_SEC4_EX_STEP4_PH]"]},
    { # Answer Space 10.4
      "cell_type": "code", "metadata": {}, "source": [
        "# [JP_PY_COMMENT_CH10_SEC4_AS_ANIMAL_CLASS_PH]\n",
        "class Animal_CH10S4:\n", # Using unique name
        "    def __init__(self, name_param):\n",
        "        self.name = name_param\n",
        "        print(f\"Animal __init__: {self.name} が作成されました。\")\n",
        "    def eat(self):\n",
        "        print(f\"{self.name}は食事をしています。\")\n",
        "\n",
        "# [JP_PY_COMMENT_CH10_SEC4_AS_BIRD_SUBCLASS_PH]\n",
        "# class Bird(Animal_CH10S4):\n",
        "#     def __init__(self, name_param, wingspan_param):\n",
        "#         # [JP_PY_COMMENT_CH10_SEC4_AS_CALL_SUPER_INIT_PH]\n",
        "#         # super().__init__(name_param)\n",
        "#         # self.wingspan = wingspan_param # [JP_PY_COMMENT_CH10_SEC4_AS_WINGSPAN_ATTR_PH]\n",
        "#         # print(f\"Bird __init__: {self.name} (翼長: {self.wingspan}cm) が作成されました。\")\n",
        "#         pass\n",
        "#     def fly(self):\n",
        "#         # print(f\"{self.name}は翼長{self.wingspan}cmの翼で飛んでいます。\")\n",
        "#         pass\n",
        "\n",
        "# [JP_PY_COMMENT_CH10_SEC4_AS_CREATE_BIRD_OBJECT_PH]\n",
        "# sparrow_placeholder = Bird(\"[JP_PY_STRING_CH10_SEC4_AS_SPARROW_NAME_PH]\", 20)\n",
        "# sparrow_placeholder.eat()  # [JP_PY_COMMENT_CH10_SEC4_AS_CALL_PARENT_METHOD_PH]\n",
        "# sparrow_placeholder.fly()  # [JP_PY_COMMENT_CH10_SEC4_AS_CALL_CHILD_METHOD_PH]"
        ], "outputs": [], "execution_count": None },
    { # Check Code 10.4
      "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}, "title": "[JP_CHECK_TITLE_CH10_SEC4_PH]"}, "source": ["#@title [JP_CHECK_TITLE_CH10_SEC4_PH] { display-mode: \"form\" }\n", "print(\"[JP_CHECK_TEXT_CH10_SEC4_PH]\")"], "outputs": [], "execution_count": None },
    { # Solution 10.4
      "cell_type": "code", "metadata": {"jupyter": {"source_hidden": True}}, "source": [
        "class AnimalSolution_CH10S4:\n",
        "    def __init__(self, name):\n",
        "        self.name = name\n",
        "        print(f\"Animal __init__: 動物「{self.name}」が作成されました。\")\n",
        "    def eat(self):\n",
        "        print(f\"{self.name}は食事をしています。モグモグ。\")\n",
        "class BirdFromAnimal_CH10S4(AnimalSolution_CH10S4):\n",
        "    def __init__(self, name, wingspan):\n",
        "        print(f\"Bird __init__ が呼ばれました (super().__init__ の前)。\")\n",
        "        super().__init__(name)\n",
        "        self.wingspan = wingspan\n",
        "        print(f\"Bird __init__: 鳥「{self.name}」(翼長: {self.wingspan}cm) が完全に作成されました。\")\n",
        "    def fly(self):\n",
        "        print(f\"{self.name}は、翼長{self.wingspan}cmの美しい翼を広げて空を飛んでいます。\")\n",
        "tsubame_ch10s4 = BirdFromAnimal_CH10S4(\"ツバメ\", 30)\n",
        "print(f\"作成された鳥の名前: {tsubame_ch10s4.name}\")\n",
        "print(f\"翼長: {tsubame_ch10s4.wingspan}cm\")\n",
        "tsubame_ch10s4.eat()\n",
        "tsubame_ch10s4.fly()"
        ], "outputs": [], "execution_count": None }
]

try:
    print(f"Python script to append Ch9 & Ch10 skeletons. Notebook path: {os.path.abspath(notebook_path)}")

    base_dir = "/app"
    full_notebook_path = os.path.join(base_dir, notebook_path.lstrip('/'))

    notebook_dir = os.path.dirname(full_notebook_path)
    if not os.path.exists(notebook_dir):
        os.makedirs(notebook_dir)
        print(f"Created directory: {notebook_dir}")

    if not os.path.exists(full_notebook_path):
        print(f"Error: Notebook file '{full_notebook_path}' not found. It should contain Chapters 1-8.")
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
        print("Existing notebook (Chapters 1-8) loaded successfully.")

    # Append Chapter 9 cells
    notebook_data['cells'].extend(chapter9_cells)
    print(f"Appended {len(chapter9_cells)} cells for Chapter 9 skeleton.")

    # Append Chapter 10 (remaining sections) cells
    notebook_data['cells'].extend(chapter10_remaining_sections_cells)
    print(f"Appended {len(chapter10_remaining_sections_cells)} cells for Chapter 10 (remaining sections) skeleton.")

    with open(full_notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook_data, f, ensure_ascii=False, indent=2)
    print(f"Successfully appended Chapters 9 & 10 (remaining sections) skeletons to {full_notebook_path}")
    print(f"File {full_notebook_path} exists. Size: {os.path.getsize(full_notebook_path)}")

except FileNotFoundError:
    print(f"Error - File Not Found (unexpected): {notebook_path}")
except json.JSONDecodeError as json_error:
    print(f"Error - JSON Decode Error: {json_error}")
except Exception as e:
    print(f"Script execution error: {e}")
