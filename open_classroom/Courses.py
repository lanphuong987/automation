class Courses:
    def __init__(self, name, description, url, system_id, intro, picture_url, course_language, video_duration):
        self.name = name
        self.description = description
        self.url = url
        self.system_id = system_id
        self.intro = intro
        self.picture_url = picture_url
        self.course_language = course_language
        self.video_duration = video_duration


class Chapter:
    def __init__(self, name, course_id, id):
        self.name = name
        self.course_id = course_id
        self.id = id



class Lesson:
    def __init__(self, name, chapter_id, url, content, video_duration):
        self.name = name
        self.url = url
        self.chapter_id = chapter_id
        self.id = id
        self.content = content
        self.video_duration = video_duration

