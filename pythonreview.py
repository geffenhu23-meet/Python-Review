def create_youtube_videa(title, description):
	channel = {"title":title, "description":description, "likes":0, "dislikes":0, "comments":{}}
	
	return channel

v1 = create_youtube_videa("food", "human need")


def like(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"]+=1
		return youtube_video
v1 = like(v1)

print(v1)

def dislikes(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"]+=1
		return youtube_video
v1 = dislikes(v1)
print(v1)

def add_comment(youtube_video, username , comment_text):
	comments.append("comment_text")
	print(comments)
	return comments

for i in range(495):
	v1= like(v1)

v1 = print (v1)



