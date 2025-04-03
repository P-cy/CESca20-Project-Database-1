from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS  # ใช้สำหรับจัดการ CORS (Cross-Origin Resource Sharing)

# สร้างแอป Flask
app = Flask(__name__)
CORS(app)  # เปิดใช้งาน CORS สำหรับทุกเส้นทาง

# ฟังก์ชันเชื่อมต่อกับฐานข้อมูล
def get_db_connection():
    # เชื่อมต่อกับฐานข้อมูล SQLite
    conn = sqlite3.connect("hogwarts_students.db")
    conn.row_factory = sqlite3.Row  # ทำให้ผลลัพธ์เป็นแบบ dictionary
    return conn

# สร้างตารางสำหรับเก็บข้อมูลนักเรียนฮอกวอตส์
@app.route("/hogwarts/create", methods=["POST"])
def create_table():
    # เชื่อมต่อฐานข้อมูล
    conn = get_db_connection()
    # สร้างตารางถ้ายังไม่มี
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- รหัสนักเรียน (สร้างอัตโนมัติ)
            name TEXT NOT NULL,                    -- ชื่อนักเรียน
            house TEXT NOT NULL,                   -- บ้าน (Gryffindor, Slytherin, etc.)
            year INTEGER NOT NULL,                 -- ปีการศึกษา (1-7)
            wand TEXT                              -- ไม้กายสิทธิ์ (เช่น "Holly, Phoenix Feather")
        )
        """
    )
    conn.commit()  # บันทึกการเปลี่ยนแปลง
    conn.close()   # ปิดการเชื่อมต่อ
    return jsonify({"message": "ตารางนักเรียนฮอกวอตส์ถูกสร้างเรียบร้อยแล้ว"}), 201

# เพิ่มข้อมูลนักเรียนใหม่
@app.route("/hogwarts", methods=["POST"])
def insert_student():
    data = request.json  # รับข้อมูลจากผู้ใช้ในรูปแบบ JSON
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO students (name, house, year, wand) VALUES (?, ?, ?, ?)",
        (data["name"], data["house"], data["year"], data["wand"]),
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "เพิ่มข้อมูลนักเรียนเรียบร้อยแล้ว"}), 201

# ดึงข้อมูลนักเรียนทั้งหมด
@app.route("/hogwarts", methods=["GET"])
def get_students():
    conn = get_db_connection()
    students = conn.execute("SELECT * FROM students").fetchall()  # ดึงข้อมูลทั้งหมด
    conn.close()
    return jsonify([dict(student) for student in students])  # แปลงข้อมูลเป็น JSON

# แก้ไขข้อมูลนักเรียน
@app.route("/hogwarts/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.json  # รับข้อมูลใหม่จากผู้ใช้
    conn = get_db_connection()
    conn.execute(
        "UPDATE students SET name = ?, house = ?, year = ?, wand = ? WHERE id = ?",
        (data["name"], data["house"], data["year"], data["wand"], student_id),
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "แก้ไขข้อมูลนักเรียนเรียบร้อยแล้ว"})

# ลบข้อมูลนักเรียน
@app.route("/hogwarts/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "ลบข้อมูลนักเรียนเรียบร้อยแล้ว"})

# เริ่มต้นเซิร์ฟเวอร์
if __name__ == "__main__":
    app.run(debug=True)
