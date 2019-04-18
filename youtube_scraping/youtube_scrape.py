import sys
import pandas as pd
sys.path.append("/home/aspiring1/.Private/precily.ai/youtube_tutorial")

from youtube_videos import youtube_search

# API key to be entered in youtube_videos.py


# Created video_dict for storing the various column values from the requests
# by the youtube API
video_dict = {'Video id':[], 'Title': [], 'Description':[], 'Category':[]}

def grab_videos(keyword, token=None):
    res = youtube_search(keyword)
    token = res[0]
    videos = res[1]
    
    for vid in videos:
        video_dict['Video id'].append(vid['id']['videoId'])
        video_dict['Title'].append(vid['snippet']['title'])
        video_dict['Description'].append(vid['snippet']['description'])
        video_dict['Category'].append(keyword)
    print("added " + str(len(videos)) + " videos to a total of " +
              str(len(video_dict['Video id'])))
    
    return token


# For every 2000 requests I am changing the scraper's API key. Thus, this
# has to be done manually.
# So, from 2000 to 12000 for six categories and the value of Travel and Blogs,
# changes to Arts and Music.
    
searches = ['Travel and Blogs', 'Science and Technology', 'Food', 'Manufacturing', 'History', 'Art and Music']

while len(video_dict['Video id']) < 12000:
    token = grab_videos("Art and Music", token=token)
    

# If I was only using single API key, which could handle 12000+ requests.
for keyword in list(enumerate(searches, start=1)):
    while len(video_dict['Video id']) < 2000 * keyword[0]:
        token = grab_videos(keyword[1], token=token)
        
    

# Creating a pandas dataframe to import file to csv ultimately and xlsx.
df = pd.DataFrame(video_dict)
print(len(df))
df.columns
df['Category'].unique()
df.head()
df.groupby('Category').agg('count')

# video_dict to csv file
df.to_csv('youtube_scraped.csv')

#Excel sheet to be submitted.
df.to_excel('youtube_excel.xlsx', sheet_name='Sheet_name_1')