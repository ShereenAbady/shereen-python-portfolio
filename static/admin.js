document.addEventListener("DOMContentLoaded", function () {
    loadTeachers();
});
async function loadTeachers() {
    try {
        const response = await fetch('/get/teachers');
        const data = await response.json();

        const teachersList = document.getElementById("teachersList");
        teachersList.innerHTML = "";

        data.teachers.forEach(teacher => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${teacher.name}</td>
                <td>${teacher.email}</td>
                <td>${teacher.phone}</td>
                <td>${teacher.age}</td>
                <td>${teacher.experience}</td>
                <td>${teacher.specialization}</td>
                <td><button onclick="deleteTeacher(${teacher.id})">حذف</button></td>
            `;
            teachersList.appendChild(row);
        });

    } catch (error) {
        console.error("خطأ في تحميل قائمة المدرسين:", error);
    }
}

async function addTeacher() {
    const name = document.getElementById("teacherName").value.trim();
    const email = document.getElementById("teacherEmail").value.trim();
    const phone = document.getElementById("teacherPhone").value.trim();
    const age = document.getElementById("teacherAge").value.trim();
    const experience = document.getElementById("teacherExperience").value.trim();
    const specialization = document.getElementById("teacherSpecialization").value.trim();

    if (!name || !email || !phone || !age || !experience || !specialization) {
        alert("يرجى ملء جميع الحقول.");
        return;
    }

    try {
        const response = await fetch('/teachers/add', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, email, phone, age, experience, specialization })
        });

        const data = await response.json();
        alert(data.message);
        loadTeachers(); // reload after adding

    } catch (error) {
        console.error("خطأ في إضافة المدرس:", error);
    }
}


async function deleteTeacher(id) {
    if (!confirm("هل أنت متأكد من حذف هذا المدرس؟")) return;

    try {
        const response = await fetch(`/teachers/delete`,
             { method: 'POST' ,
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ id})
            });
        const data = await response.json();
        alert(data.message);
        loadTeachers(); // update list after delete

    } catch (error) {
        console.error("خطأ في حذف المدرس:", error);
    }
}
