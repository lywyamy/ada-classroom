import StudentList from "./components/StudentList";
import ClassInfo from "./components/ClassInfo";
import NewStudentForm from "./components/NewStudentForm";
import { useState } from "react";

function App() {
  const [studentData, setStudentData] = useState([
    {
      id: 1,
      nameData: "Ada",
      emailData: "ada@dev.org",
      isPresentData: false,
    },
    {
      id: 2,
      nameData: "Soo-ah",
      emailData: "sooah@dev.org",
      isPresentData: false,
    },
    {
      id: 3,
      nameData: "Chrissy",
      emailData: "chrissy@dev.org",
      isPresentData: true,
    },
  ]);

  const updateStudentData = (updatedStudent) => {
    const students = studentData.map((student) => {
      if (student.id === updatedStudent.id) {
        return updatedStudent;
      } else {
        return student;
      }
    });

    setStudentData(students);
  };

  const deleteStudentData = () => {
    setStudentData([]);
  };

  const addStudentData = (newStudent) => {
    const newStudentList = [...studentData];

    const nextId = Math.max(...newStudentList.map((student) => student.id)) + 1;

    newStudentList.push({
      id: nextId,
      nameData: newStudent.nameData,
      emailData: newStudent.emailData,
      isPresentData: false,
    });

    setStudentData(newStudentList);
  };

  return (
    <main>
      <h1>Attendance</h1>
      <ClassInfo
        studentCount={studentData.length}
        onClearStudentData={deleteStudentData}
      ></ClassInfo>
      <StudentList
        students={studentData}
        onUpdateStudent={updateStudentData}
      ></StudentList>
      <NewStudentForm onAddStudentData={addStudentData}></NewStudentForm>
    </main>
  );
}

export default App;
