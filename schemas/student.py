def studentEntity(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "name": db_item["student_name"],
        "email": db_item["student_email"],
        "phno": db_item["student_phno"]
    }
def listofStudentEntity(db_item_list) -> list:
    list_stud_entity = []
    for item in db_item_list:
        list_stud_entity.append(studentEntity(item))
    return list_stud_entity