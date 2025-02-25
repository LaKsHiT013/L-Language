My Language Syntax Guide
========================

Welcome to the My Language Syntax Guide! This language uses a conversational style with unique keywords. Below is an overview of the syntax along with examples for each construct.

1\. Program Structure
---------------------

Every program must start and end with specific tokens:

*   **Start of Program:**Shuru Krte Hai
    
*   **End of Program:**Ab Thak gaya
    

**Example:**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   plaintextCopyEditShuru Krte Hai      // Your code goes here  Ab Thak gaya   `

2\. Variable Declaration
------------------------

To declare a variable, use the keyword maan le, followed by the variable name, an assignment operator (=), and its initial value. Every declaration must end with a semicolon (;).

**Example:**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   plaintextCopyEditmaan le x = 10;  maan le name = "Alice";   `

3\. Print Statement
-------------------

To print output, use the keyword likh bey followed by one or more expressions (separated by commas). End the statement with a semicolon.

**Example:**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   plaintextCopyEditlikh bey "The value of x is:", x;   `

4\. Conditional Statements
--------------------------

### If Statement

Start an if-statement with bhai agar followed by the condition inside parentheses. Then, provide a block of code enclosed in braces { ... }.

**Example:**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   plaintextCopyEditbhai agar (x < 20) {      likh bey "x is less than 20";  }   `

### Else-If Statement

For additional conditions, use nahi to bhai followed by the condition and a block.

**Example:**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   plaintextCopyEditnahi to bhai (x < 30) {      likh bey "x is less than 30";  }   `

### Else Statement

Provide a default block using warna last option with a block of code.

**Example:**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   plaintextCopyEditwarna last option {      likh bey "x is 30 or more";  }   `

5\. Looping
-----------

### While Loop

To execute a block of code repeatedly while a condition is true, use the jab tak keyword with a condition and a code block.

**Example:**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   plaintextCopyEditjab tak (x < 15) {      maan le x = x + 1;      likh bey "x is now:", x;  }   `

6\. Control Flow within Loops
-----------------------------

### Break Statement

To exit a loop prematurely, use bahar nikal ja followed by a semicolon.

**Example:**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   plaintextCopyEditbahar nikal ja;   `

### Continue Statement

To skip to the next iteration of a loop, use chal aage badh followed by a semicolon.

**Example:**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   plaintextCopyEditchal aage badh;   `

7\. Operators
-------------

*   **Assignment:** =
    
*   **Arithmetic Operators:**
    
    *   Addition: +
        
    *   Subtraction: -
        
    *   Multiplication: \*
        
    *   Division: /
        
*   **Compound Assignment Operators:** +=, -=, \*=, /=
    
*   **Comparison Operators:**
    
    *   Equal: ==
        
    *   Not Equal: !=
        
    *   Less Than: <
        
    *   Greater Than: >
        
    *   Less Than or Equal: <=
        
    *   Greater Than or Equal: >=
        

8\. Literals
------------

*   **Numbers:**Write numbers normally (e.g., 10, 3.14).
    
*   **Strings:**Enclose text in double quotes or single quotes (e.g., "hello" or 'world').
    
*   **Boolean Values:**Use Sahi for true and Galat for false.
    
*   **Null Value:**Use nalla to represent a null value.
    

9\. Identifiers
---------------

Identifiers (such as variable names) must start with a letter or underscore and can be followed by letters, digits, or underscores.

**Examples:**x, myVar, \_temp

10\. Complete Example
---------------------

Below is a complete example program demonstrating the syntax:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   plaintextCopyEditShuru Krte Hai      maan le x = 10;      maan le name = "Alice";      likh bey "Initial value of x:", x;      bhai agar (x < 20) {          likh bey "x is less than 20";      } nahi to bhai (x < 30) {          likh bey "x is less than 30";      } warna last option {          likh bey "x is 30 or more";      }      jab tak (x < 15) {          maan le x = x + 1;          likh bey "x now is:", x;          bhai agar (x == 13) {              bahar nikal ja;          }      }  Ab Thak gaya   `

Summary
-------

*   **Program Boundaries:** Start with Shuru Krte Hai and end with Ab Thak gaya.
    
*   **Variable Declaration:** Use maan le followed by an assignment.
    
*   **Printing:** Use likh bey to display output.
    
*   **Conditionals:** Use bhai agar, nahi to bhai, and warna last option for if, else-if, and else.
    
*   **Loops:** Use jab tak for loops, with bahar nikal ja to break and chal aage badh to continue.
    
*   **Operators and Literals:** Follow conventional rules with a unique twist in keywords.
    

This guide should help you quickly start writing programs in our custom language. Enjoy coding!