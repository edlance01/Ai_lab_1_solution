### **Lab 01: Student Management System — Business Requirements**

**Overview:** Develop a modular system to manage High School and College student records. The system must prioritize data integrity and flexible class behaviors using proper Object-Oriented Design.

## **Project Architecture & Structure**

Your solution must not be a single script. You are required to follow a professional folder structure to ensure maintainability:

* **Project Root:** Contains your entry point (main.py) and a documentation folder (docs/).  
* **Logic Package:** Create a dedicated folder (package) for your classes.  
* **Modularization:** \* Define your interfaces/abstract rules in one file.  
  * Define concrete logic using the Single Responsibility Principle.  
  * Use an initialization file for the package to simplify imports for the end-user.

### ---

**1\. Functional Requirements**

* **Student Data:** \* Every student must have a **Name** and a **Grade**.  
  * The system must strictly enforce that grades are between **0 and 16**. Attempts to create a student with a grade outside this range must be rejected immediately.  
* **Attendance Behaviors:**  
  * **High School Students:** Must trigger a message stating that attendance is **mandatory** and roll call is required.  
  * **College Students:** Must trigger a message stating that attendance is **optional**.  
* **Special Capabilities:**  
  * **Academic Research:** Only **College Students** are permitted to perform research. 

### ---

**2\. Operational Requirements**

* **Programmatic Setup:** The system must automatically generate a collection of at least **6 students** with varying names and grades (spanning both High School and College levels).  
* **System Processing:** The application must loop through the collection and:  
  1. Identify the student and their current grade.  
  2. Execute their specific attendance logic.  
  3. Check if the student has the **capability** to do research; if they do, trigger the research activity.

### ---

**3\. Architectural Requirements (The "SOLID" Standard)**

* **Modularity:** Classes must be organized into a logical folder structure (Python package).  
* **Contract-Based Design:** Use an **Abstract Base Class** to define the core "Student" blueprint. No "generic" students should be allowed to exist.  
* **Interface Segregation:** High school students should not have access to (or even "empty" versions of) research methods.  
* **Polymorphism:** The main processing loop must interact with students through their shared "Student" interface, not by checking for specific names like "CollegeStudent."

---

