# pip install selenium

from selenium import webdriver as wd

# 타켓 사이트 지정 (PC 웹, 모바일웹)
target_url = 'http://tour.interpark.com/'


# 브라우져 띠우기
# 에이전트 변조, 프록시 우회, 이미지는 제외하겠금 로드
driver = wd.Chrome(executable_path='./chromedriver.exe')

if False: #인터파크 투어에서 파리검색하는 샘플
    # 페이지로드
    driver.get( target_url )
    # 검색창으로 이동한다. #검색창은 크롬에서 페이지 검사로 찾는다.
    # 검색창에서 파리로 입력한다.
    driver.find_element_by_id('SearchGNBText').send_keys('파리')

    # 검색 버튼 클릭 #검색 버튼이 없다면, form tag에 summit으로 가면 된다.
    driver.find_element_by_class_name('search-btn').click()

#form tag에 summit으로 로그인 하는 예제
driver.get( 'https://www.naver.com/' )
driver.find_element_by_id('id').send_keys('id')
driver.find_element_by_id('pw').send_keys('pw')
driver.find_element_by_id('frmNIDLogin').submit()

#wait 예제 둘 중 하나를 쓰면 된다.
##references
### http://selenium-python.readthedocs.io/waits.html
driver.implicitly_wait(10)

#process에서 wait
import time
time.sleep(10)

# 크롤링은 반복 작업이라써 자원이 해제해야 된다.
## 브라우져에 대한 자원해제
driver.close()
driver.quit()
## 프로세서에 대한 자원해제
import sys
sys.exit()
