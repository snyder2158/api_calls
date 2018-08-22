# MAPBOX API CALL

from MapFig import MAPBOX_API_KEY
import requests 

#sets up positional parameters that will be passed
sat_parameters={
"position":"-77.03955,38.89750,", #recomend 5 sig figs

"zoom":"20,", 
#options of 1-20, level= 1:World, 5:Landmass
#/continent, 10:City, 15:Streets, 20:Buildings

"bearing":"0,", 
#ranges form 0 to 180, 
#equivlent of thetha in circular coordinates

"pitch":"180",  
#ranges form 0 to 180, 
#equivlent of tilt
}


#sets up image parameters that will be passed
img_parameters={	
"width":"500",
# number of pixels produced in image width

"height":"500",
# number of pixels produced in image height
}


#concatinates positional parameters
def get_sat_parameters(sat_parameters):
	sat_para=""

	for key,value in sat_parameters.items():
		sat_para += value

	return sat_para


#concatinates image parameters
def get_img_parameters(img_parameters):
	img_para="/"+img_parameters["width"]+"x"+img_parameters["height"]+"?"

	return img_para

#creates url that will be passed by concatenates key with paramters base of URL
def get_URL(sat_para,img_para,URL="https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/",access_token=MAPBOX_API_KEY):
	return URL+sat_para+img_para+"access_token="+access_token[0]


#creates url, sends request, saves image
def main():
	url=get_URL(get_sat_parameters(sat_parameters),get_img_parameters(img_parameters))
	print(url)
	r=requests.get(url)
	pos=sat_parameters["position"]
	open(pos+".JPEG", "wb").write(r.content)


if __name__=="__main__":
  main()