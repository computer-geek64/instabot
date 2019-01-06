#!/usr/bin/python3
# Main.py
# Ashish D'Souza
# January 6th, 2019

import instaloader
import sys


if "-l" in sys.argv:
    username, password = sys.argv[sys.argv.index("-u") + 1].split(":")
else:
    username = input("Username >> ")
    password = input("Password >> ")

if "-u" in sys.argv:
    target = sys.argv[sys.argv.index("-u") + 1]
else:
    target = input("Target User >> ")

instagram = instaloader.Instaloader()

instagram.login(username, password)

profile = instaloader.Profile.from_username(instagram.context, target)
target_user = instaloader.Profile.from_username(instagram.context, target)
followers = list(target_user.get_followers())
followees = list(target_user.get_followees())

no_follow_back = [x.username for x in followees if x not in followers and x.followers < 3000]
print("\n".join(no_follow_back))
