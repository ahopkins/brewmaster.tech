from medium import Client
import os


PATH = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(PATH, 'KEYS', 'medium'), 'r') as file:
    application_id, application_secret, access_token = tuple(file.readlines())


client = Client(application_id=application_id, application_secret=application_secret)
client.access_token = access_token
user = client.get_current_user()

# # Create a draft post.
# post = client.create_post(user_id=user["id"], title="Title", content="<h2>Title</h2><p>Content</p>",
#                           content_format="html", publish_status="draft")

# # When your access token expires, use the refresh token to get a new one.
# client.exchange_refresh_token(auth["refresh_token"])

# Confirm everything went ok. post["url"] has the location of the created post.
# print "My new post!", post["url"]


def main():
    input('Go here: {}'.format(auth_url))


if __name__ == '__main__':
    main()
