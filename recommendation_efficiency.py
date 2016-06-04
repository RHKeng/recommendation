from recommendations import sim_pearson

# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity function are optional params.
def recommendation_efficiency(prefs,person,similarity=sim_pearson):
  scores=[(similarity(prefs,person,other),other)
                  for other in prefs if other!=person]
  scores.sort()
  scores.reverse()

  if len(scores)<=5:
      return scores[0:]
  else:
      return scores[0:5]