import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [teachers, setTeachers] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/get/teachers")
      .then(response => {
        console.log("API Response:", response.data); // Debugging
        if (response.data && Array.isArray(response.data.teachers)) {
          setTeachers(response.data.teachers); // Correctly accessing the "teachers" array
        } else {
          setTeachers([]); // Default to an empty array if response is invalid
        }
      })
      .catch(error => {
        console.error("Error fetching teachers:", error);
        setTeachers([]); // Prevent breaking the app on error
      });
  }, []);

  return (
    <div>
      <h1>Teachers List</h1>
      <ul>
        {teachers.map((teacher) => (
          <li key={teacher.id}>
            <strong>{teacher.name}</strong> - {teacher.specialization}  
            <br />
            📧 {teacher.email} | 📞 {teacher.phone} | 🎓 {teacher.experience} years experience
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
