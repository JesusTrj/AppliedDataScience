# AppliedDataScience
Set of activities developed for the study of Applied Data Science.
## Dev Environment
* MacOS, VSCode
* Python
  * .env to read secrets
  * python3-virtualenv, Create python environments
## VSCODE SETUP 
---
1) Create python environment (venv files should be good inside the project folder)
    ```
    pip3 install virtualenv
    virtualenv applied_data_science_env
    ```
2) Activate python environment
    ``` 
    source applied_data_science_env/bin/activate
    ```
3) Change in vscode the interpreter `ctrl+shift+p` to the python inside ambridge_project_env/bin/python3.8 
   1) This way you can run the .py with the extension RUN button with the env activated.
   2) Otherwise, you'll have to run it like `python3 fileName.py` and the env activated.

4) Add the folder of the environment to `.gitignore` as `applied_data_science_spec_env/`, the requirements you share in git should just be in `requirements.txt`

### Other
* Save requirements to install (activate the virtual env)
    `pip freeze > requirements.txt`
* Load the requirements (start a virtual env first)
    `sudo apt install python3-pip`
    `virtualenv <envName>`
    `pip install -r requirements.txt`
* If using WSL...
  * Close/Open the virtual env
  * Open/Shutdown WSL, Vscode, other .exe
  * Commit the changes with a meaninful commit message

### Deactivate & Delete Virtual Environment
* Make sure environment is activated.
* Deactivate environment using:
  ```
  deactivate
  ```
* Delete environmente using:
  ```
  rm -r env_name_path
  ```
