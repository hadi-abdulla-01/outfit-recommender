from recommender.logic import recommend_outfit

occasion = input("Enter the occasion (casual/formal/party): ")
weather = input("Enter the weather (sunny/rainy/cloudy): ")

print("Recommended outfit:", recommend_outfit(occasion, weather))
