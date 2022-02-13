#################################################
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
#------------------------봇-----------------------#


def insta_like(account, like_num, hash_tag):
    driver: WebDriver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    time.sleep(3)
    # 로그인
    e = driver.find_element(By.CLASS_NAME, '_2hvTZ')
    e.send_keys(account["login_id"])  # 아이디
    e = driver.find_element(By.NAME, 'password')
    e.send_keys(account["login_pw"])  # 비번
    e.send_keys(Keys.ENTER)
    time.sleep(20)
    # 검색
    for tag in hash_tag:
        e = driver.find_element(By.CLASS_NAME, 'XTCLo')
        e.send_keys("#"+tag)
        time.sleep(3)
        e = driver.find_element(By.XPATH, """//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]""")
        e.click()
        time.sleep(7)

        # 게시물선택(최근)
        e = driver.find_element(By.XPATH,
                                """//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]/div[2]""")
        e.click()
        time.sleep(5)

        # 좋아요
        for i in range(like_num):
            # time.sleep(2)
            # fl = driver.find_element(By.CLASS_NAME, "bY2yH")#팔로우누르기
            # fl.click()
            time.sleep(2)
            like = driver.find_element(By.CLASS_NAME, "fr66n")  # 좋아요누르기
            like.click()
            time.sleep(2)
            nxt = driver.find_element(By.CLASS_NAME, 'l8mY4')  # 다음넘기기
            nxt.click()
            time.sleep(3)
        cl = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/button')
        cl.click()
        time.sleep(2)
        print(f"{tag} 좋아요 {like_num}개 완료")
    print(f"{account['login_id']} 좋아요 끝!")
def insta_like2(account, like_num, hash_tag):
    driver: WebDriver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    time.sleep(3)
    # 로그인
    e = driver.find_element(By.CLASS_NAME, '_2hvTZ')
    e.send_keys(account["login_id"])  # 아이디
    e = driver.find_element(By.NAME, 'password')
    e.send_keys(account["login_pw"])  # 비번
    e.send_keys(Keys.ENTER)
    time.sleep(20)
    # 검색
    for tag in hash_tag:
        e = driver.find_element(By.CLASS_NAME, 'XTCLo')
        e.send_keys("#"+tag)
        time.sleep(3)
        e = driver.find_element(By.XPATH, """//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div""")
        e.click()
        time.sleep(7)

        # 게시물선택(최근)
        e = driver.find_element(By.XPATH,
                                """//*[@id="react-root"]/div/div/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]""")
        e.click()
        time.sleep(5)

        # 좋아요
        for i in range(like_num):
            # time.sleep(2)
            # fl = driver.find_element(By.CLASS_NAME, "bY2yH")#팔로우누르기
            # fl.click()
            time.sleep(2)
            like = driver.find_element(By.CLASS_NAME, "fr66n")  # 좋아요누르기
            like.click()
            time.sleep(2)
            nxt = driver.find_element(By.CLASS_NAME, 'l8mY4')  # 다음넘기기
            nxt.click()
            time.sleep(3)
        cl = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/button')
        cl.click()
        time.sleep(2)
        print(f"{tag} 좋아요 {like_num}개 완료")
    print(f"{account['login_id']} 좋아요 끝!")

#---------------------개인 설정---------------------#



account1 = {
    "login_id": '아이디',
    "login_pw": '비밀번호'}


hashtag = ["디자이너브랜드", "자체제작", "스마트스토어"]
hashtag_2 = ["강아지옷", "아동복브랜드", "필라테스복"]
hashtag_3 = ["디자이너가방", "상호무페이"]



#-----------------------실행-----------------------#

# 계정이름, 좋아요 갯수, 해시태그 리스트 넣어주기
# insta_like(official, 300, hashtag)
insta_like2(rental, 100 , hashtag_2)


#####################################################


