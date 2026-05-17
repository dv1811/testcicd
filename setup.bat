@echo off

mkdir .github\workflows
mkdir src
mkdir tests

type nul > .github\workflows\ci.yml
type nul > src\train.py
type nul > src\predict.py
type nul > tests\test_train.py

type nul > requirements.txt
type nul > README.md
type nul > .gitignore

echo Project structure created successfully!
pause