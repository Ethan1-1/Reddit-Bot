import praw
import time

reddit = praw.Reddit(
    client_id="UK2vxQAxj9cSbg",
    client_secret="YfttyQzC1TTgbKfvE9MoeNxkAH625w",
    user_agent="<console:Post-Bot",
    user_name="Post-bot",
    password="Jadgon-4sonqu-pywfyw"

)
subreddit = reddit.subreddit("nba")

comment_replies = "whoah"

for submission in subreddit.hot(limit=10):
    print("xxxxxxxxxxx")
    print(submission.title)

    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " based " in comment_lower:
                print("xxxxxxxxxxx")
                print(comment.body)
                comment.reply(comment_replies)
                time.sleep=(660)
