# MOSS Script for Java Project Comparison

A Python script to Java project using Stanford's MOSS plagiarism detection system.

The script operates in directory mode, allowing it to compare a project with multiple files instead of just a single file.

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Set Up Your MOSS Account

1. Go to [MOSS](https://theory.stanford.edu/~aiken/moss/) and create an account.
1. Create a `config.ini` file in the root directory of the project and add the following line to it:

    ```bash
    [moss]
    userid = 123456789  # Replace this with your user ID
    ```

## Running the script

1. Create a folder containing the base files and another folder containing all the files you want to compare, the structure of the folders should be as follows:

    ```plaintext
    .
    ├── base_folder
    |   ├── templateA.java
    |   └── templateB.java
    └── comparing_folder
        ├── student1
        |   ├── Homework.java
        |   └── Helper.java
        └── student2
            ├── Homework.java
            └── Helper.java
    ```

1. Execute the following command:

    ```bash
    python moss.py
    ```

1. A pop-up window will appear asking you to select the base folder and the comparing folder, if there is no base folder (no template code), simply press 'Cancel' on the pop-up window.

1. Wait for the script to finish executing. The results will be displayed in the terminal and a link to the MOSS report will be generated.
