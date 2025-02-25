# L Syntax Guide

Welcome to the **My Language Syntax Guide**! This language uses a conversational style with unique keywords. Below is an overview of the syntax along with examples for each construct.

---

## 1. Variable Declaration

To declare a variable, use the keyword `maan le`, followed by the variable name, an assignment operator (`=`), and its initial value. Every declaration must end with a semicolon (`;`).

### Example:

```plaintext
maan le x = 10;
maan le name = "Alice";
```

---

## 2. Print Statement

To print output, use the keyword `likh bey` followed by one or more expressions (separated by commas). End the statement with a semicolon.

### Example:

```plaintext
likh bey "The value of x is:", x;
```

---

## 3. Conditional Statements

### If Statement

Start an if-statement with `bhai agar` followed by the condition in parentheses. Then, provide a block of code enclosed in braces `{ ... }`.

### Example:

```plaintext
bhai agar (x < 20) {
    likh bey "x is less than 20";
}
```

### Else-If Statement

For additional conditions, use `nahi to bhai` followed by the condition and a block.

### Example:

```plaintext
nahi to bhai (x < 30) {
    likh bey "x is less than 30";
}
```

### Else Statement

Provide a default block using `warna last option` followed by a block of code.

### Example:

```plaintext
warna last option {
    likh bey "x is 30 or more";
}
```

---

## 4. Looping

### While Loop

To execute a block of code repeatedly while a condition is true, use the `jab tak` keyword with a condition and a code block.

### Example:

```plaintext
jab tak (x < 15) {
    maan le x = x + 1;
    likh bey "x is now:", x;
}
```

---

## 5. Control Flow within Loops

### Break Statement

To exit a loop prematurely, use `bahar nikal ja` followed by a semicolon.

### Example:

```plaintext
bahar nikal ja;
```

### Continue Statement

To skip to the next iteration of a loop, use `chal aage badh` followed by a semicolon.

### Example:

```plaintext
chal aage badh;
```

---

## 6. Operators

### Assignment:
- `=`

### Arithmetic Operators:
- **Addition:** `+`
- **Subtraction:** `-`
- **Multiplication:** `*`
- **Division:** `/`

### Compound Assignment Operators:
- `+=`, `-=`, `*=`, `/=`

### Comparison Operators:
- **Equal:** `==`
- **Not Equal:** `!=`
- **Less Than:** `<`
- **Greater Than:** `>`
- **Less Than or Equal:** `<=`
- **Greater Than or Equal:** `>=`

---

## 7. Literals

### Numbers:
Write numbers normally (e.g., `10`, `3.14`).

### Strings:
Enclose text in double or single quotes (e.g., `"hello"` or `'world'`).

### Boolean Values:
Use `Sahi` for `true` and `Galat` for `false`.

### Null Value:
Use `nalla` to represent a null value.

---

## 8. Identifiers

Identifiers (such as variable names) must start with a letter or underscore and can be followed by letters, digits, or underscores.

### Examples:
```plaintext
x, myVar, _temp
```

---

## 9. Complete Example

Below is a complete example program demonstrating the syntax:

```plaintext
Shuru Krte Hai
    maan le x = 10;
    maan le name = "Alice";

    likh bey "Initial value of x:", x;

    bhai agar (x < 20) {
        likh bey "x is less than 20";
    } nahi to bhai (x < 30) {
        likh bey "x is less than 30";
    } warna last option {
        likh bey "x is 30 or more";
    }

    jab tak (x < 15) {
        maan le x = x + 1;
        likh bey "x now is:", x;
        bhai agar (x == 13) {
            bahar nikal ja;
        }
    }
Ab Thak gaya
```

---

## 10. Summary

- **Program Boundaries:** Start with `Shuru Krte Hai` and end with `Ab Thak gaya`.
- **Variable Declaration:** Use `maan le` followed by an assignment.
- **Printing:** Use `likh bey` to display output.
- **Conditionals:** Use `bhai agar`, `nahi to bhai`, and `warna last option` for if, else-if, and else.
- **Loops:** Use `jab tak` for loops, with `bahar nikal ja` to break and `chal aage badh` to continue.
- **Operators and Literals:** Follow conventional rules with a unique twist in keywords.

This guide should help you quickly start writing programs in our custom language. Enjoy coding!

---

## 11. Running Your Program

To code in this language on your system:

1. Download the `APP` folder, which contains two files: `main.exe` and `1.L`.
2. Open the folder in **VS Code** or any other code editor.
3. write the code in `1.L` (you can change the file or can create your own file in the same dir and code in it)
4. Run the following command in the terminal:

   ```sh
   .\main.exe 1.L   # is using your own file replace 1.L with your file name
   ```
