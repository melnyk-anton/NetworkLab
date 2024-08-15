# from selenium import webdriver
import undetected_chromedriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import json

# Function to perform the example
def get_captcha():
    chrome_options = Options()
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument('--type=crashpad-handler')
    # chrome_options.add_argument('--user-data-dir=C:\\Users\\Asus\\AppData\\Local\\Google\\Chrome\\User Data')
    # chrome_options.add_argument('/prefetch:4')
    # chrome_options.add_argument('--monitor-self-annotation=ptype=crashpad-handler')
    # chrome_options.add_argument('--database=C:\\Users\\Asus\\AppData\\Local\\Google\\Chrome\\User Data\\Crashpad')
    # chrome_options.add_argument('--url=https://clients2.google.com/cr/report')
    # chrome_options.add_argument('--annotation=channel=')
    # chrome_options.add_argument('--annotation=plat=Win64')
    # chrome_options.add_argument('--annotation=prod=Chrome')
    # chrome_options.add_argument('--annotation=ver=127.0.6533.100')
    # chrome_options.add_argument('--initial-client-data=0x228,0x22c,0x230,0x204,0x234,0x7ff9eaf9e790,0x7ff9eaf9e79c,0x7ff9eaf9e7a8')

    chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--no-sandbox") # linux only
    # chrome_options.add_argument("--headless=new") # for Chrome >= 109
    # chrome_options.add_argument("--headless")
    # chrome_options.headless = True # also works
    driver = webdriver.Chrome(options=chrome_options)

    # Set the script timeout to 60 seconds
    driver.set_script_timeout(60)  # Set script timeout in seconds

    # Get the current timeouts set for the driver
    timeouts = driver.timeouts
    print(timeouts)

    # Navigate to the website
    driver.get("https://www.udio.com/home")
    

    """
    TODO: Apply these cookies in our selenium browser session. There is an example below how to add cookies to our selenium session.
    _ga=GA1.1.1306355284.1723460359; _gcl_au=1.1.418846752.1723460390; CookieScriptConsent={"googleconsentmap":{"ad_storage":"targeting","analytics_storage":"performance","ad_user_data":"targeting","ad_personalization":"targeting","functionality_storage":"functionality","personalization_storage":"functionality","security_storage":"functionality"},"bannershown":1,"action":"accept","consenttime":1722613384,"categories":"[\"targeting\",\"performance\",\"functionality\"]","key":"147e2e84-ea51-4186-b603-e52476928fff"}; _ga_RF4WWQM7BF=GS1.1.1723572659.9.0.1723572659.60.0.76950932; sb-ssr-production-auth-token.0=base64-eyJhY2Nlc3NfdG9rZW4iOiJleUpoYkdjaU9pSklVekkxTmlJc0ltdHBaQ0k2SWxKSFZrdG9Wek5OY1NzeVZ6aHhjRGtpTENKMGVYQWlPaUpLVjFRaWZRLmV5SmhZV3dpT2lKaFlXd3hJaXdpWVcxeUlqcGJleUp0WlhSb2IyUWlPaUp2WVhWMGFDSXNJblJwYldWemRHRnRjQ0k2TVRjeU16UTRNRGM0TUgxZExDSmhjSEJmYldWMFlXUmhkR0VpT25zaWNISnZkbWxrWlhJaU9pSm5iMjluYkdVaUxDSndjbTkyYVdSbGNuTWlPbHNpWjI5dloyeGxJbDE5TENKaGRXUWlPaUpoZFhSb1pXNTBhV05oZEdWa0lpd2laVzFoYVd3aU9pSmliM0o1YzI5bVpqSXhRR2R0WVdsc0xtTnZiU0lzSW1WNGNDSTZNVGN5TXpZeU5EYzFNQ3dpYVdGMElqb3hOekl6TmpJeE1UVXdMQ0pwYzE5aGJtOXVlVzF2ZFhNaU9tWmhiSE5sTENKcGMzTWlPaUpvZEhSd2N6b3ZMMjFtYlhCNGFtVnRZV056YUdaamNIcHZjMngxTG5OMWNHRmlZWE5sTG1OdkwyRjFkR2d2ZGpFaUxDSndhRzl1WlNJNklpSXNJbkp2YkdVaU9pSmhkWFJvWlc1MGFXTmhkR1ZrSWl3aWMyVnpjMmx2Ymw5cFpDSTZJbUZoTUdFNU16QTFMVGMzWW1RdE5EYzVPUzFoT1RFekxXSmxaV00yWVRreVpEQmlOeUlzSW5OMVlpSTZJbU0xTjJZNE5qZGtMV05pWWpBdE5EQmxOeTA1WWpFM0xXWXdNR1V3TldabVpESm1ZeUlzSW5WelpYSmZiV1YwWVdSaGRHRWlPbnNpWVhaaGRHRnlYM1Z5YkNJNkltaDBkSEJ6T2k4dmJHZ3pMbWR2YjJkc1pYVnpaWEpqYjI1MFpXNTBMbU52YlM5aEwwRkRaemh2WTB0U1NXdFdNV2xEWkhSTFFUQkRVbkoxT0VVMlVscHlTMmRzUjNWNWNVRTBRM2xKUW5sa1NYQjJUamszTTFJMlpESkNQWE01Tmkxaklpd2laVzFoYVd3aU9pSmliM0o1YzI5bVpqSXhRR2R0WVdsc0xtTnZiU0lzSW1WdFlXbHNYM1psY21sbWFXVmtJanAwY25WbExDSm1kV3hzWDI1aGJXVWlPaUxRa2RDLTBZRFF1TkdCMExYUXZkQzYwTDRnMEpMUXZ0QzcwTDdRdE5DNDBMelF1TkdBSWl3aWFYTnpJam9pYUhSMGNITTZMeTloWTJOdmRXNTBjeTVuYjI5bmJHVXVZMjl0SWl3aWJtRnRaU0k2SXRDUjBMN1JnTkM0MFlIUXRkQzkwTHJRdmlEUWt0Qy0wTHZRdnRDMDBMalF2TkM0MFlBaUxDSnVaV1ZrYzE5dmJtSnZZWEprYVc1bklqcDBjblZsTENKdVpYZGZkWE5sY2lJNlptRnNjMlVzSW5Cb2IyNWxYM1psY21sbWFXVmtJanBtWVd4elpTd2ljR2xqZEhWeVpTSTZJbWgwZEhCek9pOHZiR2d6TG1kdmIyZHNaWFZ6WlhKamIyNTBaVzUwTG1OdmJTOWhMMEZEWnpodlkwdFNTV3RXTVdsRFpIUkxRVEJEVW5KMU9FVTJVbHB5UzJkc1IzVjVjVUUwUTNsSlFubGtTWEIyVGprM00xSTJaREpDUFhNNU5pMWpJaXdpY0hKdmRtbGtaWEpmYVdRaU9pSXhNVGMyTlRRMk5qRTJNams0TlRZM09UTXlOakFpTENKemRXSWlPaUl4TVRjMk5UUTJOakUyTWprNE5UWTNPVE15TmpBaWZTd2lkWE5sY2w5eWIyeGxJanB1ZFd4c2ZRLl9EVDZOa3pQTl9pdTRGaWc5cXRtVjU2SHBiTUlpNjViU01HMTIyNEhpbEUiLCJ0b2tlbl90eXBlIjoiYmVhcmVyIiwiZXhwaXJlc19pbiI6MzYwMCwiZXhwaXJlc19hdCI6MTcyMzYyNDc1MCwicmVmcmVzaF90b2tlbiI6IjBXTndvc0pac2RWeW5BT0VKa2Y4cUEiLCJ1c2VyIjp7ImlkIjoiYzU3Zjg2N2QtY2JiMC00MGU3LTliMTctZjAwZTA1ZmZkMmZjIiwiYXVkIjoiYXV0aGVudGljYXRlZCIsInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiZW1haWwiOiJib3J5c29mZjIxQGdtYWlsLmNvbSIsImVtYWlsX2NvbmZpcm1lZF9hdCI6IjIwMjQtMDgtMTJUMTA6NTk6NDMuNzUzNDI0WiIsInBob25lIjoiIiwiY29uZmlybWVkX2F0IjoiMjAyNC0wOC0xMlQxMDo1OTo0My43NTM0MjRaIiwibGFzdF9zaWduX2luX2F0IjoiMjAyNC0wOC0xMlQxNjozOTo0MC45NTA3ODZaIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZ29vZ2xlIiwicHJvdmlkZXJzIjpbImdvb2dsZSJdfSwidXNlcl9tZXRhZGF0YSI6eyJhdmF0YXJfdXJsIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jS1JJa1YxaUNkdEtBMENScnU4RTZSWnJLZ2xHdXlxQTRDeUlCeWRJcHZOOTczUjZkMkI9czk2LWMiLCJlbWFpbCI6ImJvcnlzb2ZmMjFAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZ1bGxfbmFtZSI6ItCR0L7RgNC40YHQtdC90LrQviDQktC-0LvQvtC00LjQvNC40YAiLCJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYW1lIjoi0JHQvtGA0LjRgdC10L3QutC-INCS0L7Qu9C-0LTQuNC80LjRgCIsIm5lZWRzX29uYm9hcmRpbmciOnRydWUsIm5ld191c2VyIjpmYWxzZSwicGhvbmVfdmVyaWZpZWQiOmZhbHNlLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jS1JJa1YxaUNkdEtBMENScnU4RTZSWnJLZ2xHd; sb-ssr-production-auth-token.1=XlxQTRDeUlCeWRJcHZOOTczUjZkMkI9czk2LWMiLCJwcm92aWRlcl9pZCI6IjExNzY1NDY2MTYyOTg1Njc5MzI2MCIsInN1YiI6IjExNzY1NDY2MTYyOTg1Njc5MzI2MCJ9LCJpZGVudGl0aWVzIjpbeyJpZGVudGl0eV9pZCI6ImUzZDAxZWQ5LTE3ZTQtNDkxZS1hMDMzLWU0MTFkNDA3NTk1MiIsImlkIjoiMTE3NjU0NjYxNjI5ODU2NzkzMjYwIiwidXNlcl9pZCI6ImM1N2Y4NjdkLWNiYjAtNDBlNy05YjE3LWYwMGUwNWZmZDJmYyIsImlkZW50aXR5X2RhdGEiOnsiYXZhdGFyX3VybCI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0tSSWtWMWlDZHRLQTBDUnJ1OEU2UlpyS2dsR3V5cUE0Q3lJQnlkSXB2Tjk3M1I2ZDJCPXM5Ni1jIiwiZW1haWwiOiJib3J5c29mZjIxQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmdWxsX25hbWUiOiLQkdC-0YDQuNGB0LXQvdC60L4g0JLQvtC70L7QtNC40LzQuNGAIiwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50cy5nb29nbGUuY29tIiwibmFtZSI6ItCR0L7RgNC40YHQtdC90LrQviDQktC-0LvQvtC00LjQvNC40YAiLCJwaG9uZV92ZXJpZmllZCI6ZmFsc2UsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NLUklrVjFpQ2R0S0EwQ1JydThFNlJacktnbEd1eXFBNEN5SUJ5ZElwdk45NzNSNmQyQj1zOTYtYyIsInByb3ZpZGVyX2lkIjoiMTE3NjU0NjYxNjI5ODU2NzkzMjYwIiwic3ViIjoiMTE3NjU0NjYxNjI5ODU2NzkzMjYwIn0sInByb3ZpZGVyIjoiZ29vZ2xlIiwibGFzdF9zaWduX2luX2F0IjoiMjAyNC0wOC0xMlQxMDo1OTo0My43NTA1NzVaIiwiY3JlYXRlZF9hdCI6IjIwMjQtMDgtMTJUMTA6NTk6NDMuNzUwNjJaIiwidXBkYXRlZF9hdCI6IjIwMjQtMDgtMTJUMTY6Mzk6NDAuNzQ2NDY2WiIsImVtYWlsIjoiYm9yeXNvZmYyMUBnbWFpbC5jb20ifV0sImNyZWF0ZWRfYXQiOiIyMDI0LTA4LTEyVDEwOjU5OjQzLjc0ODY0M1oiLCJ1cGRhdGVkX2F0IjoiMjAyNC0wOC0xNFQwNzozOToxMC4xMTc0NFoiLCJpc19hbm9ueW1vdXMiOmZhbHNlfX0
    """
    


    with open('my_cookies.json', 'r') as f:
        cookies_dict = json.load(f)

    def convert_cookies_to_list(cookies_dict):
        return [{"name": name, "value": value} for name, value in cookies_dict.items()]

    cookies_list = convert_cookies_to_list(cookies_dict)
    # TODO: Load the file my_cookies.json and convert this json to python dictionary
    #my_cookies = # TOOD: Put here a dictionary of my cookies
    #driver.add_cookie(my_cookies)

    for cookie_obj in cookies_list:
        driver.add_cookie(cookie_obj)

    # Navigate to the website
    driver.get("https://www.udio.com/home")
    

    time.sleep(5)
    # Execute script with 1-second delay and return a value
    result = driver.execute_script("""
        const getCaptchaToken = () => {
            return new Promise((resolve) => {
                window.hcaptcha.execute({ async: true }).then(token => {
                    resolve(token?.response);
                });
            });
        };

        return getCaptchaToken();

        //const delay = ms => new Promise(resolve => setTimeout(() => resolve("Promise resolved!"), ms));
        //return delay(1000);
        //const thing = window.hcaptcha.execute({ async: true });
        //return window.hcaptcha;
        return 1;
    """)

    # Close the browser
    driver.quit()

    return result