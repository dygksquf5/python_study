# This is a sort of Business automation mini-project.
First of all, this is just for sending an email with Google automatically


# I use another way to log in at G-mail. 

      drive = webdriver.Chrome("./chromedriver")
      url = "https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f"
      drive.get(url)
      sleep(2)


# after login , you can see an Auto-work sending email

            
            write_email = WebDriverWait(drive, 8).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".T-I.T-I-KE.L3")))

            write_email.click()
            sleep(2)
            send_button = drive.find_element_by_css_selector(".dC")

            action = ActionChains(drive)

            (
                action.send_keys("dygksquf5@naver.com").pause(2).key_down(Keys.TAB).pause(2).key_down(Keys.TAB)
                    .send_keys("selenium 공부를 위한 이메일 입니다! ").pause(2).key_down(Keys.TAB)
                    .send_keys("내용을 넣어봐야 돼용!").key_down(Keys.ENTER)
                    .send_keys("abcd 이렇게 소문자를 먼저 넣은다음").key_down(Keys.ENTER).pause(2)
                    .key_down(Keys.SHIFT).send_keys("abcd 저는 소문자를 쳤지만 이걸 쉬프트로 대문자로 바꿔놓은 것 이 죠 !! ").key_up(Keys.SHIFT).pause(2)
                    .move_to_element(send_button).click()
                    .perform()
            )

<img width="610" alt="Screenshot 2020-12-04 at 6 05 42 PM" src="https://user-images.githubusercontent.com/66229916/101144663-0133df80-365c-11eb-8cfa-eb98772183ab.png">


# As you can see, I've got an email from Gmail which Python sent.

            
 <img width="442" alt="Screenshot 2020-12-04 at 6 07 26 PM" src="https://user-images.githubusercontent.com/66229916/101144657-fe38ef00-365b-11eb-8fff-017d1c63f1ee.png">
