from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS  # ใช้สำหรับจัดการ CORS (Cross-Origin Resource Sharing)

# สร้างแอป Flask
app = Flask(__name__)
CORS(app)  # เปิดใช้งาน CORS สำหรับทุกเส้นทาง

# ฟังก์ชันเชื่อมต่อกับฐานข้อมูล
def get_db_connection():
    # เชื่อมต่อกับฐานข้อมูล SQLite
    conn = sqlite3.connect("hogwarts_std.db")
    conn.row_factory = sqlite3.Row  # ทำให้ผลลัพธ์เป็นแบบ dictionary
    return conn


# เพิ่มข้อมูลนักเรียนใหม่
@app.route("/hogwarts", methods=["POST"])
def insert_student():
    data = request.json  # รับข้อมูลจากผู้ใช้ในรูปแบบ JSON
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO students (name, email, contact, home, goal, detal) VALUES (?, ?, ?, ?, ?, ?)",
        (data["name"], data["email"], data["contact"], data["home"], data["goal"], data["detal"])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "เพิ่มข้อมูลนักเรียนเรียบร้อยแล้ว"}), 201


# เริ่มต้นเซิร์ฟเวอร์
if __name__ == "__main__":
    app.run(debug=True)