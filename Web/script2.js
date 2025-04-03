// script.js
function validateForm() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const contact = document.getElementById('contact').value;
    const house = document.querySelector('input[name="house"]:checked');
    const dream = document.getElementById('dream').value;
    
    if (!name || !email || !contact || !house || !dream) {
        alert('กรุณากรอกข้อมูลให้ครบทุกช่องที่มีเครื่องหมาย *');
        return false;
    }
    
    if (!validateEmail(email)) {
        alert('กรุณากรอกอีเมลให้ถูกต้อง');
        return false;
    }
    
    return true;
}

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function submitForm() {
    if (validateForm()) {
        // แสดงหน้ายืนยันการลงทะเบียน
        document.getElementById('registrationForm').style.display = 'none';
        document.getElementById('confirmationPage').style.display = 'flex';
        return false; // ป้องกันการ submit แบบฟอร์มจริงๆ
    }
    return false;
}

// Animation for houses when selected
const houseOptions = document.querySelectorAll('.house-option input');
houseOptions.forEach(option => {
    option.addEventListener('change', function() {
        // รีเซ็ตการเลือกบ้านทั้งหมด
        document.querySelectorAll('.house-option').forEach(house => {
            house.style.transform = "scale(1)";
            house.style.borderColor = "#ddd";
        });
        
        // เน้นบ้านที่เลือก
        this.parentElement.style.transform = "scale(1.05)";
        this.parentElement.style.borderColor = "#0066cc";
    });
});

// เพิ่มความสวยงามให้แบบฟอร์ม
document.addEventListener('DOMContentLoaded', function() {
    const formGroups = document.querySelectorAll('.form-group');
    
    formGroups.forEach((group, index) => {
        setTimeout(() => {
            group.style.opacity = '1';
            group.style.transform = 'translateY(0)';
        }, 100 * index);
    });
});