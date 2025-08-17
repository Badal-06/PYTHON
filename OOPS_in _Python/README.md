# Object-Oriented Programming (OOP) in Python 🚀

This repository contains examples and implementations of **Object-Oriented Programming (OOP)** concepts in Python.  
It is designed for beginners and intermediate learners to understand how OOP principles work in practice.

---

## 📑 Table of Contents
- [Repository Structure](#-repository-structure)
- [Example](#-example)
- [Learning Goals](#-learning-goals)
- [Requirements](#-requirements)
- [How to Run](#-how-to-run)
- [Author](#-author)
- [Contribute](#-contribute)
- [License](#-license)

---

## 📂 Repository Structure

The repo includes Python scripts demonstrating the following OOP concepts:

- **Classes & Objects**
- **Constructors (`__init__` method)**
- **Instance & Class Variables**
- **Instance, Class, and Static Methods**
- **Inheritance**
  - Single Inheritance  
  - Multiple Inheritance  
  - Multilevel Inheritance  
- **Method Overriding**
- **Abstract Classes & Methods (`abc` module)**
- **Polymorphism**
- **Operator Overloading (`__add__`, etc.)**
- **Encapsulation & Properties (`@property`)**
- **Nested Classes**

---

## 📝 Example

Here’s a simple example of **Inheritance** from the repo:

```python
class Father:
    def showF(self):
        print("Father Class Method")

class Son(Father):
    def showS(self):
        print("Son Class Method")

s = Son()
s.showF()
s.showS()

## ✅ Output

Father Class Method
Son Class Method


---

## 🎯 Learning Goals

By going through the code in this repo, you will learn:

- How to design Python classes effectively.  
- How inheritance helps in reusing code.  
- How polymorphism allows flexibility in method usage.  
- The difference between class methods, static methods, and instance methods.  
- How Python supports abstraction and operator overloading.  

---

## 📖 Requirements

- Python **3.x**  
- No external libraries required – everything is based on **core Python**.  

---

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/Badal-06/PYTHON.git
cd PYTHON/OOPS_in_Python

## ▶️ Run Any Python File

```bash
python filename.py
---

## 📌 Author  

👤 **Badal**  
- GitHub: [Badal-06](https://github.com/Badal-06)  

---

## ⭐ Contribute  

If you’d like to add more examples or improve explanations:  

1. **Fork** the repo  
2. **Create a new branch**  

   ```bash
   git checkout -b feature-xyz

3. **Commit Your Changes**  

```bash
git commit -m "Added new OOP example"

4. ** 🚀 Push to Your Branch ** 

```bash
git push origin feature-xyz

5. ** 🔀 Create a Pull Request**  

After pushing, go to your forked repo on GitHub and click **"Compare & Pull Request"**.  

---

## 📌 License  

This project is **open-source** and available under the **MIT License**.  

---

✨ If you found this helpful, don’t forget to **star ⭐ the repo**!
