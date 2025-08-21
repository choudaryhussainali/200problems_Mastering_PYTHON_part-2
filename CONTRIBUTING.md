# 🤝 Contributing Guidelines

Thank you for considering contributing to **Mastering Python – 200 Exercises**!
This project exists to help learners practice Python effectively. Your ideas, exercises, and fixes are welcome.

---

## 📌 Ways to Contribute

* **Add Exercises** → New problems for Learners
* **Improve Solutions** → Alternate or optimized approaches with explanations.
* **Fix Issues** → Typos, bugs, unclear instructions — anything that improves learning.
* **Enhance Docs** → Better explanations, tips, or clarifications for beginners.

---

## 🧭 Exercise Guidelines

* **Placement:** Create a New Branch and Add PROBLEMS in a FOLDER
* **Naming:** Use a clear, incremental pattern:

  * `01_hello_world.py`
  * `102_functions.py`
  * `181_decorators.py`
* **Self-Contained:** No external libraries unless absolutely necessary.
* **I/O Style:** Keep input/output minimal. Prefer function-based solutions.
* **Clarity:** Include a brief docstring at the top with **task, examples, constraints**.

### Template

```python
"""
Title: Reverse a String
Level: Beginner
Task: Write a function reverse_string(s) that returns the reverse of s.
Examples:
    reverse_string("abc") -> "cba"
    reverse_string("") -> ""
"""

def reverse_string(s: str) -> str:
    return s[::-1]

if __name__ == "__main__":
    print(reverse_string("hello"))
```

---

## 🧑‍💻 Code Style

* Follow **PEP 8**.
* Use **type hints** where helpful.
* Prefer **pure functions**; avoid global state.
* Add **inline comments** for tricky logic.
* Use `if __name__ == "__main__":` guard for demos/tests.

---

## 🔀 Git Workflow

1. **Fork** the repository.
2. **Create a branch**

   ```bash
   git checkout -b feat/add-palindrome-exercise
   ```
3. **Commit** changes with clear messages

   ```bash
   git commit -m "feat: add palindrome checker exercise (intermediate)"
   ```
4. **Push** your branch

   ```bash
   git push origin feat/add-palindrome-exercise
   ```
5. **Open a Pull Request** explaining:

   * What you changed and why
   * Where it fits (**basics / intermediate / advanced**)
   * Any references or notes

---

## ✅ PR Checklist

* [ ] Files in the correct folder
* [ ] Clear, incremental **file name**
* [ ] Docstring with **task + examples**
* [ ] Code is **readable** and **self-contained**
* [ ] Tested locally

---

## 🗣 Code of Conduct

Be respectful, helpful, and constructive. The goal is to make learning Python enjoyable and accessible.

---

## 🏅 Recognition

All valid contributors will appear in GitHub’s **Contributors** section.
Thank you for helping learners grow 🚀🐍
