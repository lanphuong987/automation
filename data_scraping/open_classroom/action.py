from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from database_insert import insert_chapter, insert_course, insert_lesson
from data_scraping.open_classroom.get_data_form_mysql import *
import time


def login(driver):
    try:
        driver.get("https://openclassrooms.com/en/login")
        username = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='userEmail']")))
        username.send_keys("caonguyenlanphuong2408@gmail.com")
        login_continue = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='continue-button']")))
        login_continue.click()
        password = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='field_password']")))
        password.send_keys("CYjP14FJ31kjluYNhQ")
        login = driver.find_element(By.XPATH, "//button[@id='login-button']")
        login.click()
        return True
    except Exception as e:
        driver.quit()
        print(e)
        return False


# sctrip chạy khi CSDL chưa hề có gì, chạy trong môi trường hoàn hảo (máy luôn mở, mạng mạnh)
def get_all_course(driver):

    # Trong TH bị đứt mạng giữa chừng, vào CSDL tìm số id cuối của course, VD: 167
    # Số trang = số id/10 + 1, ví dụ 167 thì trang 17
    page_number = 1
    time.sleep(6)
    # Thì ở đây chỉnh course_id = 167+1 = 168
    course_id = 1
    # Vào lesson xem số id cuối của lesson, ví dụ: 396, thay thế vào chapter_id=396
    chapter_id = 0
    while True:
        driver.get("https://openclassrooms.com/en/search?page=" + str(page_number) + "&type=course")
        time.sleep(6)
        # khi đứt mạng, thay đổi số này thành course_id/10 lấy dư, 168 => thay = 8
        # Sau khi số chạy đến 10, kết thúc chương trình,
        course_number = 1
        while course_number <= 10:
            course_info = Courses
            chapters_infor = []
            lessons_infor = []
            chapter_name = []
            try:
                courses = WebDriverWait(driver, 50).until(EC.presence_of_element_located
                                                          ((By.XPATH,
                                                            "//body/div[@id='mainSearchLegacy']/div/div/div/ul/div[" + str(
                                                                course_number) + "]"
                                                            )))
                course_img = WebDriverWait(driver, 50).until(EC.presence_of_element_located
                                                              ((By.XPATH,
                                                                "//body//div[@id='mainSearchLegacy']//div//div//div//div[" + str(
                                                                    course_number) + "]//div[1]//li[1]//a[1]//div[1]//div[1]//figure[1]"

                                                                )))
            except:
                driver.quit()
                print("Hết khóa học")
                break
            course_description = driver.find_element(By.XPATH,
                                                      "//div[@id='mainSearchLegacy']//div[" + str(
                                                          course_number) + "]//div[1]//li[1]//a[1]//div[1]//div[2]//p[1]")
            course_info.description = course_description.text
            course_info.picture_url = course_img.value_of_css_property("background-image").split('"')[1]
            ActionChains(driver).move_to_element(courses).click(courses).perform()
            intro = WebDriverWait(driver, 50).until(
                EC.presence_of_all_elements_located((By.XPATH, "//main[@role='main']//article")))
            c = ''
            for course_intro in intro:
                 c = c + course_intro.text
                 print(course_intro.text)
            course_info.intro = c
            try:
                time_line_steps = WebDriverWait(driver, 50).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "timeline__step")))
            except:
                time_line_steps = []
            try:
                course_review_url = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//iframe[@id='video_Player_1']")))
                course_info.url = course_review_url.get_attribute('src')
            except:
                course_info.url = driver.current_url
            course_name = driver.find_element(By.XPATH, "//h1[contains(@class,'courseHeader__title')]")
            course_info.name = course_name.text
            system_id = driver.current_url[(driver.current_url.rfind('/') + 1):driver.current_url.find('-')]
            course_info.system_id = system_id
            list_lesion_urls = []
            for time_line in time_line_steps:
                lesson_urls = time_line.get_attribute('href')
                list_lesion_urls.append(lesson_urls)
            for lesson_url in list_lesion_urls:
                driver.get(lesson_url)
                chapter = WebDriverWait(driver, 50).until(
                    EC.presence_of_element_located((By.XPATH, "//h6[@class='side-paginate__title']")))
                try:
                    title = WebDriverWait(driver, 50).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "part-title")))
                    part_title = title.text
                except:
                    part_title = course_info.name
                if chapter.text not in chapter_name:
                    chapter_name.append(chapter.text)
                    chapter_infor = Chapter(chapter.text, course_id, 0)
                    chapters_infor.append(chapter_infor)
                    chapter_id = chapter_id + 1

                try:
                    course_content = ''
                    content = WebDriverWait(driver, 20).until(
                        EC.presence_of_all_elements_located((By.XPATH, "//main[@role='main']//article")))
                    for c in content:
                        course_content = course_content + c.text
                    video_url = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.XPATH, "//iframe[@title='Video']")))
                    lesson_infor = Lesson(part_title, chapter_id, video_url.get_attribute('src'), course_content)
                    lessons_infor.append(lesson_infor)
                except:
                    course_content = ''
                    content = WebDriverWait(driver, 20).until(
                        EC.presence_of_all_elements_located((By.XPATH, "//main[@role='main']//article")))
                    for c in content:
                        course_content = course_content + c.text
                    print(course_content)
                    lesson_infor = Lesson(part_title, chapter_id, lesson_url, course_content)
                    print(course_content)
                    lessons_infor.append(lesson_infor)
            insert_course(course_info)
            course_number = course_number + 1
            course_id = course_id + 1
            for chap in chapters_infor:
                insert_chapter(chap)
            for less in lessons_infor:
                insert_lesson(less)
            if course_number == 11:
                page_number = page_number + 1
            else:
                driver.get("https://openclassrooms.com/en/search?page=" + str(page_number) + "&type=course")


def get_cour_by_link(url, driver):
    conn = make_cursor()
    system_id = url[(url.rfind('/') + 1):url.find('-')]
    chapter_id = get_last_chapter_id(conn)
    course_info = Courses
    chapters_infor = []
    lessons_infor = []
    chapter_name = []
    time.sleep(6)
    driver.get("https://openclassrooms.com/fr/search?page=1&language=en")
    search_bar = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "algolia-search-input")))
    search_bar.send_keys("/" + system_id + Keys.ENTER)
    course_img = WebDriverWait(driver, 50).until(EC.presence_of_element_located
                                                 ((By.XPATH,
                                                   "//body//div[@id='mainSearchLegacy']//div//div//div//div[1]//div[1]//li[1]//a[1]//div[1]//div[1]//figure[1]"
                                                   )))
    course_description = driver.find_element(By.XPATH,
                                             "//div[@id='mainSearchLegacy']//div[1]//div[1]//li[1]//a[1]//div[1]//div[2]//p[1]")
    course_info.description = course_description.text
    course_info.picture_url = course_img.value_of_css_property("background-image").split('"')[1]
    courses = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='mainSearchLegacy']//div//div//div//ul//div//div//li")))
    ActionChains(driver).move_to_element(courses).click(courses).perform()
    intro = WebDriverWait(driver, 50).until(
        EC.presence_of_all_elements_located((By.XPATH, "//main[@role='main']//article")))
    c = ''
    for course_intro in intro:
        c = c + course_intro.text
        print(course_intro.text)
    course_info.intro = c
    try:
        time_line_steps = WebDriverWait(driver, 50).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "timeline__step")))
    except:
        time_line_steps = []
    try:
        course_review_url = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//iframe[@id='video_Player_1']")))
        course_info.url = course_review_url.get_attribute('src')
    except:
        course_info.url = driver.current_url
    course_name = driver.find_element(By.XPATH, "//h1[contains(@class,'courseHeader__title')]")
    course_info.name = course_name.text
    system_id = driver.current_url[(driver.current_url.rfind('/') + 1):driver.current_url.find('-')]
    course_info.system_id = system_id
    course_id = insert_course(course_info)
    list_lesion_urls = []
    for time_line in time_line_steps:
        lesson_urls = time_line.get_attribute('href')
        list_lesion_urls.append(lesson_urls)
    for lesson_url in list_lesion_urls:
        driver.get(lesson_url)
        chapter = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, "//h6[@class='side-paginate__title']")))
        try:
            title = WebDriverWait(driver, 50).until(
                EC.presence_of_element_located((By.CLASS_NAME, "part-title")))
            part_title = title.text
        except:
            part_title = course_info.name
        if chapter.text not in chapter_name:
            chapter_name.append(chapter.text)
            chapter_infor = Chapter(chapter.text, course_id, 0)
            chapter_id = insert_chapter(chapter_infor)
        try:
            course_content = ''
            content = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//main[@role='main']//article")))
            for c in content:
                course_content = course_content + c.text
            video_url = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//iframe[@title='Video']")))
            lesson_infor = Lesson(part_title, chapter_id, video_url.get_attribute('src'), course_content)
            lessons_infor.append(lesson_infor)
        except:
            course_content = ''
            content = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//main[@role='main']//article")))
            for c in content:
                course_content = course_content + c.text
            print(course_content)
            lesson_infor = Lesson(part_title, chapter_id, lesson_url, course_content)
            print(course_content)
            lessons_infor.append(lesson_infor)
    for less in lessons_infor:
        insert_lesson(less)
