import pickle

with open('highscore.data','rb') as f:
  temp = pickle.load(f)

# temp.pop(0)
print(temp)
# with open('highscore.data','wb') as f:
#   pickle.dump(temp,f)