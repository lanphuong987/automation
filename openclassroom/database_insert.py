from openclassroom.database import connect
def insert_course(c):
    query = "INSERT INTO course(course_name, system_id, description, course_url, picture_url, intro) " \
            "VALUES(%s, %s, %s, %s, %s, %s)"
    args = (c.name, c.system_id, c.description, c.url, c.picture_url, c.intro )
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, args)
    course_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    if course_id:
        return course_id
    else:
        return False


def insert_chapter(ch):
    query = "INSERT INTO chapter(chapter_name, course_id) " \
            "VALUES(%s, %s)"
    args = (ch.name, ch.course_id)
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, args)
    chapter_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    if chapter_id:
        return chapter_id
    else:
        return False

def insert_lesson(l):
    query = "INSERT INTO lesson(lesson_name, lesson_url, chapter_id, content) " \
            "VALUES(%s, %s, %s, %s)"
    args = (l.name, l.url, l.chapter_id, l.content)
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, args)
    lesson_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    if lesson_id:
        return lesson_id
    else:
        return False



