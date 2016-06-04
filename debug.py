from recommendations import critics
from recommendations import sim_distance
from recommendations import sim_pearson
from recommendations import topMatches
from recommendations import getRecommendations
from Tanimoto import Tanimoto_distance
from recommendation_efficiency import recommendation_efficiency

# print sim_distance(critics,'Lisa Rose','Gene Seymour')
# print sim_pearson(critics,'Lisa Rose','Gene Seymour')
# print topMatches(critics,'Toby',n=3)
# print getRecommendations(critics,'Toby')
#
# from recommendations import transformPrefs
# moives=transformPrefs(critics)
# print topMatches(moives,'Superman Returns')
# print getRecommendations(moives,'Just My Luck')
#
# # import pydelicious
# from PIL import Image,ImageDraw
# from bs4 import BeautifulStoneSoup
# from pysqlite2 import dump
# from numpy import *
# from pylab import *
# import pydelicious
#
# print pydelicious.get_popular(tag='programming')

print Tanimoto_distance(critics,'Lisa Rose','Gene Seymour')
print recommendation_efficiency(critics,'Toby')