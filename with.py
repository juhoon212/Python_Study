import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study_txt", "w", encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하자")

with open("study_txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())