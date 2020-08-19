from setuptools import setup, find_packages

long_description = "Placeholder"

setup(
    name = "noteprompt", # Replace with your own username
    version = "1.0.0",
    author = "Aditya Pal",
    author_email = "adityapa.nghss@gmail.com",
    description = "A small CLI TODO app in Python",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/PalAditya/NotePrompt",
    packages = find_packages(),
    install_requires = ["plyer", "colored", "apscheduler", "pyautogui", "fpdf"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=['src/cli.py']
)