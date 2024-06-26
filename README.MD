# FastAPI Text Summarizer

## Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate    # on Windows 
   source venv/bin/activate   # on Linux
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

4. Test the endpoint:
    - Using ```sendrequest.py```
    
    - Using ```curl``` utility in the terminal:
    ```
    curl -X POST "http://127.0.0.1:8000/summarize" -H "Content-Type: application/json" -d "{\"text\": \"Often, programmers fall in love with Python because of the increased productivity it provides. Since there is no compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault. Instead, when the interpreter discovers an error, it raises an exception. When the program doesn't catch the exception, the interpreter prints a stack trace. A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on. The debugger is written in Python itself, testifying to Python's introspective power. On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective.\"}"
    ```
    
