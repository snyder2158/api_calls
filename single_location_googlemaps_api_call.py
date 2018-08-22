# api call that produces and saves a single google map image

from config import GMAPS_API_KEY
import requests 


parameters={
"center":"40.714728,-73.998672", # coordinate that will be in center of image

"zoom":"14",#approximate detail level at each zoom level= 1:World, 5:Landmass
  #/continent, 10:City, 15:Streets, 20:Buildings

"size":"500x500",  #quanity of pixels produced

"scale":"3",
 #optional affects # of pixels returned per size, default=1
 #scale=2 returns twice as many pixels as default useful for high-resolution
 #displays, accepted values are 1,2,4 but 4 is only for premium users

"format":"jpg", #format types: png8, png32, gif, jpg, jpg-baseline

"maptype":"satellite" # types of maps include: roadmap, satellite, hybrid, and terrain
}

#sets up parameters as string that will be passed
def get_parameters(parameters):
	para=""

	for key,value in parameters.items():
		para += key+"="+value+"&"

	return para

#Brings API key with parameters. Index the key based on key usage
def get_URL(para,URL="https://maps.googleapis.com/maps/api/staticmap?",key=GMAPS_API_KEY):
	return URL+para+"key="+key[0]



def main():
	url= get_URL(get_parameters(parameters))
	#print(url)
	r=requests.get(url)
	location=parameters["center"]
	open(location+".JPEG", "wb").write(r.content)
#makes api call and saves image as the lcoation passed


if __name__=="__main__":
  main()