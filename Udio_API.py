from udio_wrapper import UdioWrapper
import hcaptcha

def generate_song_sequence(auth_token0, auth_token1, captcha_token, num_extensions, custom_lyrics_short, custom_lyrics_extend, custom_lyrics_outro):
    udio_wrapper = UdioWrapper(auth_token0=auth_token0, auth_token1=auth_token1)
    
    short_prompt = input("Enter the prompt for the short song: ")
    extend_prompts = [input(f"Enter the prompt for extension {i+1}: ") for i in range(num_extensions)]
    outro_prompt = input("Enter the prompt for the outro: ")
    
    short_song = udio_wrapper.create_song(
        prompt=short_prompt,
        seed=-1,
        captchaToken=captcha_token,
        custom_lyrics=custom_lyrics_short
    )
    
    last_song_id = short_song
    for i in range(num_extensions):
        last_song_id = udio_wrapper.extend(
            prompt=extend_prompts[i],
            seed=-1,
            audio_conditioning_path="url-generated-song",
            audio_conditioning_song_id=last_song_id,
            custom_lyrics=custom_lyrics_extend[i]
        )
    
    final_song = udio_wrapper.add_outro(
        prompt=outro_prompt,
        seed=-1,
        audio_conditioning_path="url-generated-song",
        audio_conditioning_song_id=last_song_id,
        custom_lyrics=custom_lyrics_outro
    )
    
    return final_song

captcha_token = hcaptcha.get_captcha()

final_song = generate_song_sequence(
    auth_token0 = "base64-eyJhY2Nlc3NfdG9rZW4iOiJleUpoYkdjaU9pSklVekkxTmlJc0ltdHBaQ0k2SWxKSFZrdG9Wek5OY1NzeVZ6aHhjRGtpTENKMGVYQWlPaUpLVjFRaWZRLmV5SmhZV3dpT2lKaFlXd3hJaXdpWVcxeUlqcGJleUp0WlhSb2IyUWlPaUp2WVhWMGFDSXNJblJwYldWemRHRnRjQ0k2TVRjeU16WTBOakF5TkgxZExDSmhjSEJmYldWMFlXUmhkR0VpT25zaWNISnZkbWxrWlhJaU9pSmthWE5qYjNKa0lpd2ljSEp2ZG1sa1pYSnpJanBiSW1ScGMyTnZjbVFpWFgwc0ltRjFaQ0k2SW1GMWRHaGxiblJwWTJGMFpXUWlMQ0psYldGcGJDSTZJbUp2Y25semIyWm1NakZBWjIxaGFXd3VZMjl0SWl3aVpYaHdJam94TnpJek5qUTVOakkwTENKcFlYUWlPakUzTWpNMk5EWXdNalFzSW1selgyRnViMjU1Ylc5MWN5STZabUZzYzJVc0ltbHpjeUk2SW1oMGRIQnpPaTh2YldadGNIaHFaVzFoWTNOb1ptTndlbTl6YkhVdWMzVndZV0poYzJVdVkyOHZZWFYwYUM5Mk1TSXNJbkJvYjI1bElqb2lJaXdpY205c1pTSTZJbUYxZEdobGJuUnBZMkYwWldRaUxDSnpaWE56YVc5dVgybGtJam9pTkRkbE9UaGpPVFF0TURaalpTMDBNakJpTFRnNU4yTXRORGRpT0dFek0ySTFOelk0SWl3aWMzVmlJam9pT1dNMk9UZzVabUl0TWpZMU9DMDBaamRoTFRoaE9UZ3RaV1ExWVRNd1pEWTBNbU0wSWl3aWRYTmxjbDl0WlhSaFpHRjBZU0k2ZXlKaGRtRjBZWEpmZFhKc0lqb2lhSFIwY0hNNkx5OWpaRzR1WkdselkyOXlaR0Z3Y0M1amIyMHZaVzFpWldRdllYWmhkR0Z5Y3k4d0xuQnVaeUlzSW1OMWMzUnZiVjlqYkdGcGJYTWlPbnNpWjJ4dlltRnNYMjVoYldVaU9pSkNiM0o1YzJWdWEyOGdWbTkyWVNBb1ZVRXBJRVJsYkdWbllYUmxJbjBzSW1WdFlXbHNJam9pWW05eWVYTnZabVl5TVVCbmJXRnBiQzVqYjIwaUxDSmxiV0ZwYkY5MlpYSnBabWxsWkNJNmRISjFaU3dpWm5Wc2JGOXVZVzFsSWpvaVltOXllWE5sYm10dmRtOXNiMlI1YlhseUlpd2lhWE56SWpvaWFIUjBjSE02THk5a2FYTmpiM0prTG1OdmJTOWhjR2tpTENKdVlXMWxJam9pWW05eWVYTmxibXR2ZG05c2IyUjViWGx5SXpBaUxDSnVaV1ZrYzE5dmJtSnZZWEprYVc1bklqcDBjblZsTENKdVpYZGZkWE5sY2lJNmRISjFaU3dpY0dodmJtVmZkbVZ5YVdacFpXUWlPbVpoYkhObExDSndhV04wZFhKbElqb2lhSFIwY0hNNkx5OWpaRzR1WkdselkyOXlaR0Z3Y0M1amIyMHZaVzFpWldRdllYWmhkR0Z5Y3k4d0xuQnVaeUlzSW5CeWIzWnBaR1Z5WDJsa0lqb2lOamc0TXpZd05ETTVNalF5T1RRNE5qTTNJaXdpYzNWaUlqb2lOamc0TXpZd05ETTVNalF5T1RRNE5qTTNJbjBzSW5WelpYSmZjbTlzWlNJNmJuVnNiSDAuTDhjdC1qWFp0MXNFWU1TVVBiR3Z5aERFTUhFeEdWdzF3eWE5X1ZPRExGVSIsInRva2VuX3R5cGUiOiJiZWFyZXIiLCJleHBpcmVzX2luIjozNjAwLCJleHBpcmVzX2F0IjoxNzIzNjQ5NjI0LCJyZWZyZXNoX3Rva2VuIjoiOHlxOEttX2tJYXROdE5tRjZ3MWQ5dyIsInVzZXIiOnsiaWQiOiI5YzY5ODlmYi0yNjU4LTRmN2EtOGE5OC1lZDVhMzBkNjQyYzQiLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJlbWFpbCI6ImJvcnlzb2ZmMjFAZ21haWwuY29tIiwiZW1haWxfY29uZmlybWVkX2F0IjoiMjAyNC0wOC0xNFQwOToyOTozMS43NjgxMloiLCJwaG9uZSI6IiIsImNvbmZpcm1lZF9hdCI6IjIwMjQtMDgtMTRUMDk6Mjk6MzEuNzY4MTJaIiwibGFzdF9zaWduX2luX2F0IjoiMjAyNC0wOC0xNFQxNDozMzo0NC42ODAzMDMwNzlaIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZGlzY29yZCIsInByb3ZpZGVycyI6WyJkaXNjb3JkIl19LCJ1c2VyX21ldGFkYXRhIjp7ImF2YXRhcl91cmwiOiJodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9lbWJlZC9hdmF0YXJzLzAucG5nIiwiY3VzdG9tX2NsYWltcyI6eyJnbG9iYWxfbmFtZSI6IkJvcnlzZW5rbyBWb3ZhIChVQSkgRGVsZWdhdGUifSwiZW1haWwiOiJib3J5c29mZjIxQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmdWxsX25hbWUiOiJib3J5c2Vua292b2xvZHlteXIiLCJpc3MiOiJodHRwczovL2Rpc2NvcmQuY29tL2FwaSIsIm5hbWUiOiJib3J5c2Vua292b2xvZHlteXIjMCIsIm5lZWRzX29uYm9hcmRpbmciOnRydWUsIm5ld191c2VyIjp0cnVlLCJwaG9uZV92ZXJpZmllZCI6ZmFsc2UsInBpY3R1cmUiOiJodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9lbWJlZC9hdmF0YXJzLzAucG5nIiwicHJvdmlkZXJfaWQiOiI2ODgzNjA0MzkyNDI5NDg2MzciLCJzdWIiOiI2ODgzNjA0MzkyNDI5NDg2MzcifSwiaWRlbnRpdGllcyI6W3siaWRlbnRpdHlfaWQiOiIyODQ0ODhiMy1kOTA3LTQxM2UtOGRmMS00OTc3ODZkYWVjZGQiLCJpZCI6IjY4ODM2MDQzOTI0Mjk0ODYzNyIsInVzZXJfa",
    auth_token1 = "WQiOiI5YzY5ODlmYi0yNjU4LTRmN2EtOGE5OC1lZDVhMzBkNjQyYzQiLCJpZGVudGl0eV9kYXRhIjp7ImF2YXRhcl91cmwiOiJodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9lbWJlZC9hdmF0YXJzLzAucG5nIiwiY3VzdG9tX2NsYWltcyI6eyJnbG9iYWxfbmFtZSI6IkJvcnlzZW5rbyBWb3ZhIChVQSkgRGVsZWdhdGUifSwiZW1haWwiOiJib3J5c29mZjIxQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmdWxsX25hbWUiOiJib3J5c2Vua292b2xvZHlteXIiLCJpc3MiOiJodHRwczovL2Rpc2NvcmQuY29tL2FwaSIsIm5hbWUiOiJib3J5c2Vua292b2xvZHlteXIjMCIsIm5lZWRzX29uYm9hcmRpbmciOnRydWUsIm5ld191c2VyIjp0cnVlLCJwaG9uZV92ZXJpZmllZCI6ZmFsc2UsInBpY3R1cmUiOiJodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9lbWJlZC9hdmF0YXJzLzAucG5nIiwicHJvdmlkZXJfaWQiOiI2ODgzNjA0MzkyNDI5NDg2MzciLCJzdWIiOiI2ODgzNjA0MzkyNDI5NDg2MzcifSwicHJvdmlkZXIiOiJkaXNjb3JkIiwibGFzdF9zaWduX2luX2F0IjoiMjAyNC0wOC0xNFQwOToyOTozMS43NjM4NTRaIiwiY3JlYXRlZF9hdCI6IjIwMjQtMDgtMTRUMDk6Mjk6MzEuNzYzOTAyWiIsInVwZGF0ZWRfYXQiOiIyMDI0LTA4LTE0VDA5OjI5OjMxLjc2MzkwMloiLCJlbWFpbCI6ImJvcnlzb2ZmMjFAZ21haWwuY29tIn1dLCJjcmVhdGVkX2F0IjoiMjAyNC0wOC0xNFQwOToyOTozMS43NTY3MzZaIiwidXBkYXRlZF9hdCI6IjIwMjQtMDgtMTRUMDk6Mjk6MzEuOTU3NDEzWiIsImlzX2Fub255bW91cyI6ZmFsc2V9LCJwcm92aWRlcl90b2tlbiI6Im9najFjNnJGWmQ2VmI2RVBZb3d4UGxKQjZsR2FhRCIsInByb3ZpZGVyX3JlZnJlc2hfdG9rZW4iOiJ1Mm1tUlBraU1BUWp6R0lkdWRQWXVmbnplZ1pvU0YifQ",
    captcha_token=captcha_token,
    num_extensions=2,
    custom_lyrics_short="Short song lyrics here",
    custom_lyrics_extend=["Lyrics for first extension", "Lyrics for second extension"],
    custom_lyrics_outro="Outro lyrics here"
)
