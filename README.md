🌟# Project-4-Assignments🚀



*****************Assignments 00 to 05******************************* 

*****************Assignments 01**************************************

*****************Assignments 1 to 6**********************************

📌 Python Fundamentals & ANSI Escape Codes

🌟00 - Introduction & Basic Python Scripts

Welcome to Python! This section introduces fundamental concepts such as syntax, variables, running Python scripts, displaying output, accepting user input, and performing basic calculations.

🌟01 - Expressions

Expressions form the backbone of Python programming. This section explores mathematical operations, logical conditions, and variable manipulations to create meaningful computations.

🌟02 - Lists

Lists are a fundamental data structure in Python. Here, you’ll learn how to create lists, access elements using indexing and slicing, modify lists, and perform common operations like appending, sorting, and iterating through lists.

🌟03 - Dictionaries

Dictionaries store data in key-value pairs, making them a powerful tool for efficient lookups. This section covers dictionary creation, value retrieval, adding and removing elements, and iterating through dictionary items.

🌟04 - If Statements

Decision-making is key to programming! This section explains how to use if, elif, and else statements to execute code conditionally based on logical expressions.

🌟05 - Loops & Control Flow

Loops allow efficient execution of repetitive tasks. Learn how to use for and while loops, along with control flow mechanisms like break, continue, and pass to manage program execution.

🌟06 - Functions

Functions promote modular and reusable code. This section covers function definitions, argument passing, return values, and best practices for writing clean, maintainable functions.

🌟07 - Information Flow

Understanding how data moves within a program is crucial for efficient coding. This section delves into variable scope, data transfer between functions, and best practices for organizing code effectively.

✨ Each assignment in this module includes practical exercises to reinforce your Python skills. Happy coding! 🚀

🎨 Enhancing Terminal Output with ANSI Escape Codes

What Are ANSI Escape Codes?

ANSI escape codes are special character sequences that allow you to control text formatting, colors, and cursor movement in terminal displays. 
These codes work seamlessly on Linux, macOS, and supported Windows terminals.

Why Use ANSI Escape Codes?

✅ Add color to terminal output
✅ Apply bold, italic, or underline styles
✅ Improve readability and highlight key information
✅ Reset formatting when needed

🌟Code	Effect	Example Usage in Python	Output🌟

⭐\033[0m	Reset formatting	print("\033[0mReset Text")	Reset Text
⭐\033[1m	Bold text	print("\033[1mBold Text\033[0m")	Bold Text
⭐\033[3m	Italic text	print("\033[3mItalic Text\033[0m")	Italic Text
⭐\033[4m	Underlined text	print("\033[4mUnderlined Text\033[0m")	Underlined Text
⭐\033[31m	Red text	print("\033[31mRed Text\033[0m")	🔴 Red Text
⭐\033[32m	Green text	print("\033[32mGreen Text\033[0m")	🟢 Green Text
⭐\033[33m	Yellow text	print("\033[33mYellow Text\033[0m")	🟡 Yellow Text
⭐\033[34m	Blue text	print("\033[34mBlue Text\033[0m")	🔵 Blue Text
⭐\033[1;33m	Bold Yellow	print("\033[1;33mBold Yellow\033[0m")	🟡 Bold Yellow
⭐\033[1;34m	Bold Blue	print("\033[1;34mBold Blue\033[0m")	🔵 Bold Blue

🌟Why Use \033[0m?

Without resetting formatting, styles may persist in the terminal, affecting subsequent text.

❌ Without Reset:
python
Copy
Edit
print("\033[1mBold Text!")
print("Normal Text")  # This will also be bold!
The second line remains bold unintentionally.

✅ With Reset:
python
Copy
Edit

print("\033[1mBold Text!\033[0m")
print("Normal Text")  # Now it's normal
Now, the second line returns to default formatting.

🌟Additional ANSI Color Codes
🌟Code	Color

⭐\033[30m	Black
⭐\033[31m	Red
⭐\033[32m	Green
⭐\033[33m	Yellow
⭐\033[34m	Blue
⭐\033[35m	Magenta
⭐\033[36m	Cyan
⭐\033[37m	White

🌟Conclusion

ANSI escape codes provide a simple yet effective way to enhance terminal output. Whether you're formatting logs, debugging output, or styling CLI applications, these codes help improve clarity and readability.

📌 Tip: Windows Command Prompt does not support ANSI codes by default. Use Windows Terminal or enable ANSI support in PowerShell.🚀
















