#This is a sort of Business automation mini-project.
First of all, this is just for sending an email with Google automatically

# I use other way to log in at G-mail. 

      drive = webdriver.Chrome("./chromedriver")
      url = "https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f"
      drive.get(url)
      sleep(2)
