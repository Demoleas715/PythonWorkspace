import urllib.request
import json

class Tour (object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.dest_list=[]

    def get_distance (self, from_city, to_city):
        from_city=from_city.replace(" ", "+")
        to_city=to_city.replace(" ", "+")
        
        request_str = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + from_city
        request_str+="&destinations=" + to_city + "&mode=walking&sensor=false"
        
        webObj=urllib.request.urlopen(request_str)
        
        rs=webObj.read().decode(webObj.headers.get_content_charset())
        
        webObj.close()
        
        j=json.load(rs)
        
        return j["rows"][0]["elements"][0]["distance"]["value"]["rows"][0]["elements"][0]["distance"]["value"]
        #
        # This function gets the distance between two cities by making an
        # API call to Google. 
        #
        
        #request_str = "http://maps.googleapis.com/maps/api/distancematrix/json?origins=" + from_city
        #request_str += "&destinations=" + to_city + "&mode=driving&sensor=false"

    
    def add_destination (self, dest):
        self.dest_list.append(dest)

    def distance (self):
        dist = 0
        for i in range(1, len(self.dest_list)):
            dist += self.get_distance (self.dest_list[i-1], self.dest_list[i])

        return dist

    def __str__ (self):
        out_str = ""
        for dest in self.dest_list:
            out_str += dest + "; "
        return out_str
    
    def __It__(self, right):
        self.distance() < right.distance()      
        
    def __getitem__(self, index):    
        return self.dest_list[index]
def main():

    t1 = Tour ()
    t1.add_destination ("New York NY")
    t1.add_destination ("Albany NY")
    t1.add_destination ("Rochester NY")
    
    t2 = Tour ()
    t2.add_destination ("Hackensack NJ")
    t2.add_destination ("Upper Saddle River NJ")
    t2.add_destination ("Park Ridge NJ")
    t2.add_destination ("Rutherford NJ")
    
    print(t2[2])
    
    if (t1 < t2):
        print("t1 is shorter")

main()