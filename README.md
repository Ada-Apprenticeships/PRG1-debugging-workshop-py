# Debugging Workshop 🐛

## Background

The term "bug" in computing has an interesting origin. In 1947, Grace Hopper and her team at Harvard were working on the Mark II computer when they encountered a malfunction. Upon investigation, they discovered a moth trapped in a relay, causing the issue. This incident is often cited as the origin of the term "bug" in computer science, although the term had been used in engineering contexts before this event.

## 📖 Key terms

A **bug** is a flaw or error in a computer program that causes it to produce an incorrect or unexpected result, or to behave in unintended ways. More specifically, a bug occurs when there is a discrepancy between:

- The **expected behaviour**: How the program is intended or specified to function under certain conditions.
- The **actual behaviour**: How the program actually performs when those conditions are met.

This discrepancy can arise in various ways, such as:

- Incorrect output or calculations
- Unexpected program termination
- Unresponsive or frozen applications
- Security vulnerabilities
- Performance issues

> 🔑 **Debugging** is the process of identifying, analysing, and resolving these discrepancies to align the actual behaviour of the program with its expected behaviour.

---

## A Brief Guide to Debugging

Effective debugging involves several key steps:

1.  Establish or clarify the **expected behaviour** of your program. For example, if you call a function with a certain set of inputs, we should expect to get back a particular return value.
2.  Call the function/program you want to debug.
3.  Identify the difference between the **expected behaviour** and the actual behaviour (what happens when you actually run the code).
4.  Use various strategies (see below) to find out why the bug is occurring.
5.  Fix the bug and verify that the program now works as expected.

---

## 🧭 Debugging strategies

### 🖨️ Printing to the console

In Python, you can print or log variables to check if they're being updated with the correct values during program execution. The `print()` function is a simple and effective way to log variables to the console, giving you a better idea of what's happening inside your program.

### 👣 Step Through Execution

Stepping through code, also known as "playing computer," is a technique where you step through the execution of a program line by line to check the values in memory as the program runs. You can do this manually using a piece of paper or use a tool like **Python Tutor** for visualisation.

### 🔬 Static Analysis

**Static analysis** tools are powerful allies in the battle against bugs. These tools analyse your code without executing it, helping you identify potential issues early in the development process. **Pylint** and **Flake8** are popular static analysis tools for Python that can check your code for errors and ensure it adheres to style guidelines.

### 💡 Rubber Duck Debugging

This technique involves explaining your code, line by line, to an inanimate object (traditionally a rubber duck). By verbalising your code, you often spot the issue yourself. This method can be surprisingly effective in helping you understand your own code better and identify logical errors.

---

## 🎢 Running order

We recommend you tackle these problems in the following order. The problems will generally increase in difficulty so it's important you're comfortable with the earlier problems before you start tackling the later problems.

### 🍵 Warm up

As a group, you should check you understand the task by going through some problems together and asking questions. We recommend you debug the following problems together:

001.  `square`
002.  `increment`
003.  `capitalise`

### 🍎 Core

101.  `percentage-change`
102.  `pence-to-pounds`
103.  `12-hour-clock`
104.  `convert-temperature`
105.  `times-table`
106.  `rotate-angle`
107.  `right-angled-triangle`
108.  `fizz-buzz`
109.  `sum-digits`
110. `count-char`

### 🧠 Challenge

In this section, you can develop your skills further by using the **VSCode debugger** to step through the execution of the code in the problems below. Check out the documentation to familiarise yourself with this tool and debug the code.

201.  `multiple-of-five`
202.  `find-century`
203.  `is-valid-triangle`
204.  `text-in-div`
205.  `is-palindrome`
206.  `find-closing-parenthesis`