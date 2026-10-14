# 📚 Arabic-English Vocabulary Quiz

A command-line vocabulary quiz built with Python to help users practice translating Arabic words into English. The program tracks progress by saving correctly answered words and removing them from the remaining word list.

## ✨ Features

- 📖 **Arabic-to-English practice:** Translate Arabic vocabulary into English.
- ✅ **Answer checking:** Keep trying until you provide the correct English answer.
- 💾 **Automatic progress tracking:** Save correctly answered words to `savedwords.txt`.
- 🔄 **Resume learning:** Continue with the words remaining in `2500.txt`.
- 🎉 **Completion message:** Get congratulated when the word list is empty.

## 🖥️ Requirements

- Python 3.13 or compatible Python 3 version.
- A terminal or command prompt.

No external Python packages are required.

## 📂 Project Structure

```text
python-vocabulary-quiz/
├── 2500.txt          # Remaining vocabulary words
├── savedwords.txt    # Correctly answered words
├── quiz.py           # Main quiz program
├── .gitignore
└── README.md
```

## 🎮 How It Works

1. The program loads vocabulary entries from `2500.txt`.
2. Each entry is split into an English word and its Arabic translation.
3. You are asked to provide the English equivalent of the Arabic word.
4. Incorrect answers prompt you to try again.
5. Correct answers are appended to `savedwords.txt`.
6. The completed entry is removed from `2500.txt`.
7. When no entries remain, the program displays a completion message.

## 🧠 What I Practiced

This project helped me practice:

- Reading and writing text files.
- Working with lists and strings.
- Splitting text into structured data.
- Using functions to organize code.
- Implementing loops and conditional logic.
- Handling user input and normalizing answers with `lower()` and `strip()`.
- Saving application progress between sessions.

## 🔮 Future Improvements

- 🎲 Randomize the order of questions.
- 📊 Track correct answers and total attempts.
- 🏆 Add a score and completion percentage.
- 🛡️ Handle malformed vocabulary entries and missing files.
- 🔤 Support multiple accepted English translations.
- 🗂️ Preserve the original word list and store progress separately.

