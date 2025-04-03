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
    
    alert('ส่งใบสมัครสำเร็จ! ขอบคุณที่สนใจเข้าร่วมค่าย CesCa#20');
    return true;
}

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Animation for houses when selected
const houseOptions = document.querySelectorAll('.house-option input');
houseOptions.forEach(option => {
    option.addEventListener('change', function() {
        if (this.checked) {
            document.querySelectorAll('.house-option').forEach(house => {
                house.style.transform = "scale(1)";
            });
            this.parentElement.style.transform = "scale(1.05)";
        }
    });
});