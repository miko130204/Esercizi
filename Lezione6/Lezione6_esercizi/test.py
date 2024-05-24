# 9-10
from lezione6_1_import import Restaurant

restaurant = Restaurant("Sushiko", "Japanese")
restaurant.describe_restaurant()


# 9-11
from lezione6_1_import import Admin
privileges_list = ["can add post", "can delete post", "can ban user", "can unban user"]
admin1 = Admin("Rick", "Astley", "RickRolled@gmail.com", privileges_list)
admin1.show_privileges()


# 9-12
from admin_privileges import Admin
privileges_list = ["can add post", "can delete post", "can ban user", "can unban user"]
admin1 = Admin("Rick", "Astley", "RickRolled@gmail.com", privileges_list)
admin1.describe_user()
admin1.show_privileges()