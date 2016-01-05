import math

class Dataset (object):
    def __init__ (self, file_name):
        self.file_name=file_name
        text_file=open(file_name, "r")
        self.testTopic = text_file.readline().strip()
        self.testDate = text_file.readline().strip()
        self.__num_list=[]
        for line in text_file:
            self.__num_list.append(int(line))
        

    def getMean (self):
        self.mean=0
        for n in self.__num_list: #Algorithm for finding the mean
            self.mean+=n
            self.mean /= len(self.__num_list)
        return self.mean
        """ Returns the statistical mean of the dataset. """

    def getRange (self):
        return max(self.__num_list)-min(self.__num_list)
        """ Returns the statistical range of the dataset."""

    def getMedian (self):
        self.__num_list.sort()
        if len(self.__num_list)%2==0: #If there are an even amount of integers in the list
            median=self.__num_list[len(self.__num_list)//2]
            median=(median+self.__num_list[len(self.__num_list)//2-1])/2
            return median
        else: #If there are an odd number of integers in the list
            median=self.__num_list[len(self.__num_list)//2]
            return median
        """ Returns the median of the dataset."""

    def getStdDev (self):
        dev=0
        mean=self.mean
        for i in range (0, len(self.__num_list)): #Algorithm for standard deviaton
            dev+=(self.__num_list[i]-self.mean)**2
        return math.sqrt(dev/len(self.__num_list))
        """ Returns the standard deviation of the dataset."""