from fastapi import FastAPI, HTTPException
import uvicorn
app = FastAPI()


students_db = {}
student_id_counter = 0

@app.get("/students")
async def get_students(student_id: int = None):
    if student_id is not None:
        student = students_db.get(student_id)
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        return [student]
    else:
        return list(students_db.values())

@app.post("/students")
async def create_student(name: str, age: int, grade: str):
    global student_id_counter
    student_id_counter += 1
    student_id = student_id_counter
    student = {"id": student_id, "name": name, "age": age, "grade": grade}
    students_db[student_id] = student
    return {"message": "Student created successfully", "student": student}

@app.put("/students/update/")
async def update_student(student_id: int, name: str, age: int, grade: str):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    student = students_db[student_id]
    student["name"] = name
    student["age"] = age
    student["grade"] = grade
    return {"message": "Student updated successfully", "student": student}

@app.delete("/students/")
async def delete_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    del students_db[student_id]
    return {"message": "Student deleted successfully"}



def start():
    uvicorn.run("assignment:app", host="127.0.0.1", port=8080)

if __name__ == "__main__":
    start()