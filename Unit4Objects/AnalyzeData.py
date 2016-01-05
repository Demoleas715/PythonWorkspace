from Dataset import Dataset

def main():
    d1 = Dataset("test1.txt")
    d2 = Dataset("test2.txt")
    d3 = Dataset("test3.txt")
    d4 = Dataset("test4.txt")
    
    """ A bunch of print statements here. That's it! """
    print("%-20s %20s %20s %20s %20s" % ("Test Name", d1.testTopic, d2.testTopic, d3.testTopic, d4.testTopic))
    print("%-20s %20s %20s %20s %20s" % ("Test Date", d1.testDate, d2.testDate, d3.testDate, d4.testDate))
    print("%-20s %20.1f %20.1f %20.1f %20.1f" % ("Median", d1.getMedian(), d2.getMedian(), d3.getMedian(), d4.getMedian())) #Median of numbers
    print("%-20s %20.2f %20.2f %20.2f %20.2f" % ("Mean", d1.getMean(), d2.getMean(), d3.getMean(), d4.getMean())) #Mean of numbers
    print("%-20s %20d %20d %20d %20d" % ("Range", d1.getRange(), d2.getRange(), d3.getRange(), d4.getRange())) #Range of number list
    print("%-20s %20.2f %20.2f %20.2f %20.2f" % ("Standard Deviation", d1.getStdDev(), d2.getStdDev(), d3.getStdDev(), d4.getStdDev())) #Standard deviation of numbers

    
main()