import pytube
import pandas as pd
import re 
from tqdm import tqdm


def extract_game_idx(title: str):
     """
     Uses a regular expression to extract the game number from the title

     :returns integer with the game number
     """

     # Regular expression pattern to match the number after "Partie"
     pattern = r'Partie (\d+)'

     # Using search to find the first match
     match = re.search(pattern, title)
     if match:
          # Extracting the number
          extracted_number = match.group(1)
     else:
          print("No number found after 'Partie'.")
          extracted_number = pd.NA
     return extracted_number

     
     


def get_youtube_data(playlist_url:str):
     """
     Returning views of Youtube Playlist including url and publish data as pandas dataframe
     with following columns: 
     """
     p = pytube.Playlist(playlist_url)
     views = []
     url = []
     publish_date = []
     title = []
     idx = 0
     for video in tqdm(p.videos):
          views.append(video.views)
          url.append(video.watch_url)
          publish_date.append(video.publish_date)
          title.append(video.title)
     df = pd.DataFrame({'url': url,'title':title, 'views': views, 'publish_data': publish_date})
     df['gamer_number'] = df['title'].apply(extract_game_idx)
     return df 


JANISTAN_PLAYLIST = "https://www.youtube.com/playlist?list=PLag27ig3EyHIktHFUU9dLCZX4aOUC8Qx3"


print(extract_game_idx("Hallo Partie 133dddd"))
jan_df = get_youtube_data(JANISTAN_PLAYLIST)
print(jan_df.head(10))
print(len(jan_df))

