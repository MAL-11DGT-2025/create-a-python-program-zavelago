season = input("what is your favourite season: ")

season_list = ["summer", "winter", "autumn", "sprint"]

if season.lower().strip() in season_list:
    print("That is a valid season")
else:
    print("that is not a vaild season")