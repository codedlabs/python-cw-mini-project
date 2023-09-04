# write your code here
def padel_court_cost(court_type):
  if court_type == "indoor":
    return 30
  elif court_type == "outdoor":
    return 20
#################
def rackets_cost(racket_brand):
  if racket_brand == "Bullpadel":
    return 100
  elif racket_brand == "Nox":
    return 140
  elif racket_brand == "Siux":
    return 200
#########
def padel_balls_cost(ball_boxes):
  if ball_boxes == "box":
    return 2
  elif ball_boxes == "two boxes":
    return 3.5
  elif ball_boxes == "three boxes":
    return 5
#######
def padel_game_cost():
  court_cost = input("Enter court cost: ")
  rackets_cost = input("Enter rackets cost: ")
  balles_cost = int(input("Enter balls boxes: "))
  return court_cost + rackets_cost + balles_cost
  print(f"""
  court cost: {court_cost}
  rackets cost: {rackets_cost}
  balles cost: {balles_cost}
  """)
  padel_game_cost()
