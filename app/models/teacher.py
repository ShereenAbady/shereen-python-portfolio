from database.DBConnecter import DBConnector


class Teacher:
    #@staticmethod
    def get_all_teachers(self):
        """
        Fetch all teachers from the database.
        """
        try:
            db_model = DBConnector()
            
            teachers = db_model.db_query("SELECT * FROM teachers", "read", "all")
            
            if not teachers:
                raise Exception("No teachers found")

            return teachers
        except Exception as e:
            raise Exception(str(e))

    
    def add_new_teacher(self,request_data):
        """
        Add a new teacher to the database.
        """
        try:
            name = request_data.get("name")
            email = request_data.get("email")
            phone = request_data.get("phone")
            age = request_data.get("age")
            experience = request_data.get("experience")
            specialization = request_data.get("specialization")
            
            if not all([name, email, phone, age, experience, specialization]):
                raise Exception("Error: All fields are required")

            query =  f"""
                INSERT INTO teachers (name, email, phone, age, experience, specialization)
                VALUES ('{name}', '{email}', '{phone}', '{age}', '{experience}', '{specialization}')
            """

            db_model = DBConnector()
            rows_inserted = db_model.db_query(query, "write")

            return {"success": True, "message": f"{rows_inserted} teacher(s) added"}
        except Exception as e:
            raise Exception(str(e))

    
    def edit_teacher(self,request_data):
        """
        Edit an existing teacher's details.
        """
        try:
            teacher_id = request_data.get("id")
            name = request_data.get("name")
            email = request_data.get("email")
            phone = request_data.get("phone")
            age = request_data.get("age")
            experience = request_data.get("experience")
            specialization = request_data.get("specialization")

            if not teacher_id:
                raise Exception("Error: Teacher ID is required")

            update_query = f"""
                UPDATE teachers 
                SET name='{name}', email='{email}',
                phone={phone}, age={age}, experience={experience},
                specialization='{specialization}'
                WHERE id={teacher_id}
            """
            db_model = DBConnector()
            rows_updated = db_model.db_query(update_query, "write")

            return {"success": True, "message": f"{rows_updated} teacher(s) updated"}
        except Exception as e:
            raise Exception(str(e))

    
    def delete_teacher(self,request_data):
        """
        Delete a teacher by ID.
        """
        try:
            teacher_id = request_data.get("id")

            if not teacher_id:
                raise Exception("Error: Teacher ID is required")

            db_model = DBConnector()
            delete_query = f"DELETE FROM teachers WHERE id = {teacher_id}"
            rows_deleted = db_model.db_query(delete_query, "write")

            return {"success": True, "message": f"{rows_deleted} teacher(s) deleted"}
        except Exception as e:
            raise Exception(str(e))