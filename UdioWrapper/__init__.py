"""
Udio Wrapper
Author: Flowese
Version: 0.0.3
Date: 2024-04-15
Description: Generates songs using the Udio API using textual prompts.
"""

import requests
import os
import time

class UdioWrapper:
    API_BASE_URL = "https://www.udio.com/api"
    def __init__(self, auth_token0, auth_token1):
        self.auth_token0 = auth_token0
        self.auth_token1 = auth_token1
        self.all_track_ids = []

    def make_request(self, url, method, data=None, headers=None):
        try:
            if method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            else:
                response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error making {method} request to {url}: {e}")
            return None

    def get_headers(self, get_request=False):
        headers = {
            "Accept": "application/json, text/plain, */*" if get_request else "application/json",
            "Content-Type": "application/json",
          #  "Cookie": f"; sb-ssr-production-auth-token.0={self.auth_token0}; sb-ssr-production-auth-token.1={self.auth_token1}",
            "Cookie": '_ga=GA1.1.1306355284.1723460359; _gcl_au=1.1.418846752.1723460390; CookieScriptConsent={"googleconsentmap":{"ad_storage":"targeting","analytics_storage":"performance","ad_user_data":"targeting","ad_personalization":"targeting","functionality_storage":"functionality","personalization_storage":"functionality","security_storage":"functionality"},"bannershown":1,"action":"accept","consenttime":1722613384,"categories":"["targeting","performance","functionality"]","key":"147e2e84-ea51-4186-b603-e52476928fff"}; sb-ssr-production-auth-token.0=base64-eyJhY2Nlc3NfdG9rZW4iOiJleUpoYkdjaU9pSklVekkxTmlJc0ltdHBaQ0k2SWxKSFZrdG9Wek5OY1NzeVZ6aHhjRGtpTENKMGVYQWlPaUpLVjFRaWZRLmV5SmhZV3dpT2lKaFlXd3hJaXdpWVcxeUlqcGJleUp0WlhSb2IyUWlPaUp2WVhWMGFDSXNJblJwYldWemRHRnRjQ0k2TVRjeU16UTJNVE00TlgxZExDSmhjSEJmYldWMFlXUmhkR0VpT25zaWNISnZkbWxrWlhJaU9pSm5iMjluYkdVaUxDSndjbTkyYVdSbGNuTWlPbHNpWjI5dloyeGxJbDE5TENKaGRXUWlPaUpoZFhSb1pXNTBhV05oZEdWa0lpd2laVzFoYVd3aU9pSmliM0o1YzI5bVpqSXhRR2R0WVdsc0xtTnZiU0lzSW1WNGNDSTZNVGN5TXpRM05EVTROaXdpYVdGMElqb3hOekl6TkRjd09UZzJMQ0pwYzE5aGJtOXVlVzF2ZFhNaU9tWmhiSE5sTENKcGMzTWlPaUpvZEhSd2N6b3ZMMjFtYlhCNGFtVnRZV056YUdaamNIcHZjMngxTG5OMWNHRmlZWE5sTG1OdkwyRjFkR2d2ZGpFaUxDSndhRzl1WlNJNklpSXNJbkp2YkdVaU9pSmhkWFJvWlc1MGFXTmhkR1ZrSWl3aWMyVnpjMmx2Ymw5cFpDSTZJalJrWW1abU4yTm1MV0UzWkRNdE5HTXhZeTFpT1RRMExUVXlPRFppTXpNME4yWTJOU0lzSW5OMVlpSTZJbU0xTjJZNE5qZGtMV05pWWpBdE5EQmxOeTA1WWpFM0xXWXdNR1V3TldabVpESm1ZeUlzSW5WelpYSmZiV1YwWVdSaGRHRWlPbnNpWVhaaGRHRnlYM1Z5YkNJNkltaDBkSEJ6T2k4dmJHZ3pMbWR2YjJkc1pYVnpaWEpqYjI1MFpXNTBMbU52YlM5aEwwRkRaemh2WTB0U1NXdFdNV2xEWkhSTFFUQkRVbkoxT0VVMlVscHlTMmRzUjNWNWNVRTBRM2xKUW5sa1NYQjJUamszTTFJMlpESkNQWE01Tmkxaklpd2laVzFoYVd3aU9pSmliM0o1YzI5bVpqSXhRR2R0WVdsc0xtTnZiU0lzSW1WdFlXbHNYM1psY21sbWFXVmtJanAwY25WbExDSm1kV3hzWDI1aGJXVWlPaUxRa2RDLTBZRFF1TkdCMExYUXZkQzYwTDRnMEpMUXZ0QzcwTDdRdE5DNDBMelF1TkdBSWl3aWFYTnpJam9pYUhSMGNITTZMeTloWTJOdmRXNTBjeTVuYjI5bmJHVXVZMjl0SWl3aWJtRnRaU0k2SXRDUjBMN1JnTkM0MFlIUXRkQzkwTHJRdmlEUWt0Qy0wTHZRdnRDMDBMalF2TkM0MFlBaUxDSnVaV1ZrYzE5dmJtSnZZWEprYVc1bklqcDBjblZsTENKdVpYZGZkWE5sY2lJNlptRnNjMlVzSW5Cb2IyNWxYM1psY21sbWFXVmtJanBtWVd4elpTd2ljR2xqZEhWeVpTSTZJbWgwZEhCek9pOHZiR2d6TG1kdmIyZHNaWFZ6WlhKamIyNTBaVzUwTG1OdmJTOWhMMEZEWnpodlkwdFNTV3RXTVdsRFpIUkxRVEJEVW5KMU9FVTJVbHB5UzJkc1IzVjVjVUUwUTNsSlFubGtTWEIyVGprM00xSTJaREpDUFhNNU5pMWpJaXdpY0hKdmRtbGtaWEpmYVdRaU9pSXhNVGMyTlRRMk5qRTJNams0TlRZM09UTXlOakFpTENKemRXSWlPaUl4TVRjMk5UUTJOakUyTWprNE5UWTNPVE15TmpBaWZTd2lkWE5sY2w5eWIyeGxJanB1ZFd4c2ZRLjFIem5vaVU4OFlzM2RKUFVGampsU2tpUFJXQVF6eHo4UEEwczdzRmlwWlkiLCJ0b2tlbl90eXBlIjoiYmVhcmVyIiwiZXhwaXJlc19pbiI6MzYwMCwiZXhwaXJlc19hdCI6MTcyMzQ3NDU4NiwicmVmcmVzaF90b2tlbiI6Ikw4Vm8zYzhwQkYxaDQxRWw1ZjJGTHciLCJ1c2VyIjp7ImlkIjoiYzU3Zjg2N2QtY2JiMC00MGU3LTliMTctZjAwZTA1ZmZkMmZjIiwiYXVkIjoiYXV0aGVudGljYXRlZCIsInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiZW1haWwiOiJib3J5c29mZjIxQGdtYWlsLmNvbSIsImVtYWlsX2NvbmZpcm1lZF9hdCI6IjIwMjQtMDgtMTJUMTA6NTk6NDMuNzUzNDI0WiIsInBob25lIjoiIiwiY29uZmlybWVkX2F0IjoiMjAyNC0wOC0xMlQxMDo1OTo0My43NTM0MjRaIiwibGFzdF9zaWduX2luX2F0IjoiMjAyNC0wOC0xMlQxMzowNTozNC4wNTQ5OTlaIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZ29vZ2xlIiwicHJvdmlkZXJzIjpbImdvb2dsZSJdfSwidXNlcl9tZXRhZGF0YSI6eyJhdmF0YXJfdXJsIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jS1JJa1YxaUNkdEtBMENScnU4RTZSWnJLZ2xHdXlxQTRDeUlCeWRJcHZOOTczUjZkMkI9czk2LWMiLCJlbWFpbCI6ImJvcnlzb2ZmMjFAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZ1bGxfbmFtZSI6ItCR0L7RgNC40YHQtdC90LrQviDQktC-0LvQvtC00LjQvNC40YAiLCJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYW1lIjoi0JHQvtGA0LjRgdC10L3QutC-INCS0L7Qu9C-0LTQuNC80LjRgCIsIm5lZWRzX29uYm9hcmRpbmciOnRydWUsIm5ld191c2VyIjpmYWxzZSwicGhvbmVfdmVyaWZpZWQiOmZhbHNlLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jS1JJa1YxaUNkdEtBMENScnU4RTZSWnJLZ2xHd; sb-ssr-production-auth-token.1=XlxQTRDeUlCeWRJcHZOOTczUjZkMkI9czk2LWMiLCJwcm92aWRlcl9pZCI6IjExNzY1NDY2MTYyOTg1Njc5MzI2MCIsInN1YiI6IjExNzY1NDY2MTYyOTg1Njc5MzI2MCJ9LCJpZGVudGl0aWVzIjpbeyJpZGVudGl0eV9pZCI6ImUzZDAxZWQ5LTE3ZTQtNDkxZS1hMDMzLWU0MTFkNDA3NTk1MiIsImlkIjoiMTE3NjU0NjYxNjI5ODU2NzkzMjYwIiwidXNlcl9pZCI6ImM1N2Y4NjdkLWNiYjAtNDBlNy05YjE3LWYwMGUwNWZmZDJmYyIsImlkZW50aXR5X2RhdGEiOnsiYXZhdGFyX3VybCI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0tSSWtWMWlDZHRLQTBDUnJ1OEU2UlpyS2dsR3V5cUE0Q3lJQnlkSXB2Tjk3M1I2ZDJCPXM5Ni1jIiwiZW1haWwiOiJib3J5c29mZjIxQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmdWxsX25hbWUiOiLQkdC-0YDQuNGB0LXQvdC60L4g0JLQvtC70L7QtNC40LzQuNGAIiwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50cy5nb29nbGUuY29tIiwibmFtZSI6ItCR0L7RgNC40YHQtdC90LrQviDQktC-0LvQvtC00LjQvNC40YAiLCJwaG9uZV92ZXJpZmllZCI6ZmFsc2UsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NLUklrVjFpQ2R0S0EwQ1JydThFNlJacktnbEd1eXFBNEN5SUJ5ZElwdk45NzNSNmQyQj1zOTYtYyIsInByb3ZpZGVyX2lkIjoiMTE3NjU0NjYxNjI5ODU2NzkzMjYwIiwic3ViIjoiMTE3NjU0NjYxNjI5ODU2NzkzMjYwIn0sInByb3ZpZGVyIjoiZ29vZ2xlIiwibGFzdF9zaWduX2luX2F0IjoiMjAyNC0wOC0xMlQxMDo1OTo0My43NTA1NzVaIiwiY3JlYXRlZF9hdCI6IjIwMjQtMDgtMTJUMTA6NTk6NDMuNzUwNjJaIiwidXBkYXRlZF9hdCI6IjIwMjQtMDgtMTJUMTM6MDU6MzMuODU2OTY5WiIsImVtYWlsIjoiYm9yeXNvZmYyMUBnbWFpbC5jb20ifV0sImNyZWF0ZWRfYXQiOiIyMDI0LTA4LTEyVDEwOjU5OjQzLjc0ODY0M1oiLCJ1cGRhdGVkX2F0IjoiMjAyNC0wOC0xMlQxMzo1NjoyNi44NDc1OVoiLCJpc19hbm9ueW1vdXMiOmZhbHNlfX0; _ga_RF4WWQM7BF=GS1.1.1723470262.2.1.1723471037.60.0.1900003943',
            "Origin": "https://www.udio.com",
            "Referer": "https://www.udio.com/my-creations",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty"
        }
        if not get_request:
            headers.update({
                "sec-ch-ua": '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
                "sec-fetch-dest": "empty"
            })
        return headers

    def create_complete_song(self, short_prompt, extend_prompts, outro_prompt, captchaToken, seed=-1, custom_lyrics_short=None, custom_lyrics_extend=None, custom_lyrics_outro=None, num_extensions=1):
        print("Starting the generation of the complete song sequence...")

        # Generate the short song
        print("Generating the short song...")
        short_song_result = self.create_song(short_prompt=short_prompt, seed=seed, captchaToken=captchaToken, custom_lyrics_short=custom_lyrics_short)
        if not short_song_result:
            print("Error generating the short song.")
            return None

        last_song_result = short_song_result
        extend_song_results = []

        # Generate the extend songs
        for i in range(len(extend_prompts)):
            prompt = extend_prompts[i]
            lyrics = custom_lyrics_extend[i] if custom_lyrics_extend and i < len(custom_lyrics_extend) else None
        
            print(f"Generating extend song {i + 1}...")
            extend_song_result = self.extend(
                prompt,
                seed,
                audio_conditioning_path=last_song_result[0]['song_path'],
                audio_conditioning_song_id=last_song_result[0]['id'],
                custom_lyrics=lyrics
            )
            if not extend_song_result:
                print(f"Error generating extend song {i + 1}.")
                return None

            extend_song_results.append(extend_song_result)
            last_song_result = extend_song_result

        # Generate the outro
        print("Generating the outro...")
        outro_song_result = self.add_outro(
            outro_prompt,
            seed,
            audio_conditioning_path=last_song_result[0]['song_path'],
            audio_conditioning_song_id=last_song_result[0]['id'],
            custom_lyrics=custom_lyrics_outro
        )
        if not outro_song_result:
            print("Error generating the outro.")
            return None

        print("Complete song sequence generated and processed successfully.")
        return {
            "short_song": short_song_result,
            "extend_songs": extend_song_results,
            "outro_song": outro_song_result
        }

    def create_song(self, prompt, captchaToken, seed=-1, custom_lyrics=None):
        song_result = self.generate_song(prompt=prompt, seed=seed, captchaToken=captchaToken, custom_lyrics=custom_lyrics)
        if not song_result:
            return None
        track_ids = song_result.get('track_ids', [])
        self.all_track_ids.extend(track_ids)
        return self.process_songs(track_ids, "short_songs")

    def extend(self, prompt, seed=-1, audio_conditioning_path=None, audio_conditioning_song_id=None, custom_lyrics=None):
        extend_song_result = self.generate_extend_song(
            prompt=prompt, seed=seed, audio_conditioning_path=audio_conditioning_path, audio_conditioning_song_id=audio_conditioning_song_id, custom_lyrics=custom_lyrics
        )
        if not extend_song_result:
            return None
        extend_track_ids = extend_song_result.get('track_ids', [])
        self.all_track_ids.extend(extend_track_ids)
        return self.process_songs(extend_track_ids, "extend_songs")

    def add_outro(self, prompt, seed=-1, audio_conditioning_path=None, audio_conditioning_song_id=None, custom_lyrics=None):
        outro_result = self.generate_outro(
            prompt=prompt, seed=seed, audio_conditioning_path=audio_conditioning_path, audio_conditioning_song_id=audio_conditioning_song_id, custom_lyrics=custom_lyrics
        )
        if not outro_result:
            return None
        outro_track_ids = outro_result.get('track_ids', [])
        self.all_track_ids.extend(outro_track_ids)
        return self.process_songs(outro_track_ids, "outro_songs")

    def generate_song(self, prompt, seed, captchaToken, custom_lyrics=None):
        url = f"{self.API_BASE_URL}/generate-proxy"
        headers = self.get_headers()
        data = {"prompt": prompt, "samplerOptions": {"seed": seed, "bypass_prompt_optimization": False, "seed": -1, "crop_start_time": 0.4,"prompt_strength": 0.5,"clarity_strength": 0.25,"lyrics_strength": 0.5,"generation_quality": 0.75,"audio_conditioning_length_seconds": 130,"use_2min_model": False}, "captchaToken": captchaToken}
        if custom_lyrics:
            data["lyricInput"] = custom_lyrics
        response = self.make_request(url, 'POST', data, headers)
        return response.json() if response else None

    def generate_extend_song(self, prompt, seed, audio_conditioning_path, audio_conditioning_song_id, captchaToken, custom_lyrics=None):
        url = f"{self.API_BASE_URL}/generate-proxy"
        headers = self.get_headers()
        data = {
            "prompt": prompt,
            "samplerOptions": {
                "seed": seed,
                "audio_conditioning_path": audio_conditioning_path,
                "audio_conditioning_song_id": audio_conditioning_song_id,
                "audio_conditioning_type": "continuation"
            },
            "captchaToken": captchaToken
        }
        if custom_lyrics:
            data["lyricInput"] = custom_lyrics
        response = self.make_request(url, 'POST', data, headers)
        return response.json() if response else None

    def generate_outro(self, prompt, seed, audio_conditioning_path, audio_conditioning_song_id, custom_lyrics=None):
        url = f"{self.API_BASE_URL}/generate-proxy"
        headers = self.get_headers()
        data = {
            "prompt": prompt,
            "samplerOptions": {
                "seed": seed,
                "audio_conditioning_path": audio_conditioning_path,
                "audio_conditioning_song_id": audio_conditioning_song_id,
                "audio_conditioning_type": "continuation",
                "crop_start_time": 0.9
            }
        }
        if custom_lyrics:
            data["lyricInput"] = custom_lyrics
        response = self.make_request(url, 'POST', data, headers)
        return response.json() if response else None

    def process_songs(self, track_ids, folder):
        """Function to process generated songs, wait until they are ready, and download them."""
        print(f"Processing songs in {folder} with track_ids {track_ids}...")
        while True:
            status_result = self.check_song_status(track_ids)
            if status_result is None:
                print(f"Error checking song status for {folder}.")
                return None
            elif status_result.get('all_finished', False):
                songs = []
                for song in status_result['data']['songs']:
                    self.download_song(song['song_path'], song['title'], folder=folder)
                    songs.append(song)
                print(f"All songs in {folder} are ready and downloaded.")
                return songs
            else:
                time.sleep(5)

    def check_song_status(self, song_ids):
        url = f"{self.API_BASE_URL}/songs?songIds={','.join(song_ids)}"
        headers = self.get_headers(True)
        response = self.make_request(url, 'GET', None, headers)
        if response:
            data = response.json()
            all_finished = all(song['finished'] for song in data['songs'])
            return {'all_finished': all_finished, 'data': data}
        else:
            return None

    def download_song(self, song_url, song_title, folder="downloaded_songs"):
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, f"{song_title}.mp3")
        try:
            response = requests.get(song_url)
            response.raise_for_status()
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded {song_title} with url {song_url} to {file_path}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download the song. Error: {e}")

