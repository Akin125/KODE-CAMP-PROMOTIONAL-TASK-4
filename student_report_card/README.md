# 🎓 Student Report Card System

A terminal-based Python application for managing student scores, calculating averages, and assigning grades. Data is stored in JSON and can be viewed or updated easily.

## 🌟 Key Highlights

- **User-Friendly**: Simple terminal interface for easy navigation
- **Data Persistence**: All records safely stored in JSON format
- **Flexible**: Support for multiple subjects per student
- **Automatic Calculations**: Instant grade and average computation
- **Modular Design**: Well-organized code structure for easy maintenance

## 📁 Project Structure

```
student_report_card/
├── main.py             # App entry point and menu interface
├── student.py          # Student class with grading logic
├── operations.py       # Core operations: add, view, update
├── data_utils.py       # Load/save JSON data
├── data.json           # Stores student records (auto-generated)
└── README.md          # Project documentation
```

## ✅ Features

- Add student name and scores in multiple subjects
- Auto-calculate average and assign grade (A–F scale)
- View all students' reports in a formatted table
- Update existing scores with automatic recalculation
- Persistent storage using JSON file
- Clean modular code using functions and multiple Python files
- Error handling and input validation

## 📦 Prerequisites

- Python 3.6 or higher
- No external dependencies required
- Operating System: Windows/Linux/MacOS

## 💻 Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/student-report-card.git
   cd student-report-card
   ```

2. **Run the Application**
   ```bash
   python main.py
   ```

## 🎯 Usage Guide

### Main Menu Options:
```
1. Add Student    - Enter new student records
2. View Students  - Display all student reports
3. Update Score   - Modify existing scores
4. Exit          - Close the application
```

### Adding a Student:
1. Select option 1
2. Enter student name
3. Input scores for each subject
4. System automatically calculates average and grade

### Viewing Reports:
- Select option 2 to see a formatted table of all students

### Updating Scores:
1. Select option 3
2. Enter student name
3. Select subject to update
4. Enter new score

## 🧠 Grading System

| Average Score | Grade | Performance Level |
|--------------|-------|-------------------|
| 70 and above | A     | Excellent        |
| 60–69        | B     | Very Good        |
| 50–59        | C     | Good             |
| 45–49        | D     | Fair             |
| Below 45     | F     | Fail             |

## 💾 Data Storage

Student records are stored in `data.json` using the following format:

```json
[
  {
    "name": "John Doe",
    "subjects": {
      "Math": 85,
      "English": 70,
      "Science": 75
    },
    "average": 76.67,
    "grade": "A"
  }
]
```

