

#PART 1
class FizzBuzzer():
    
    def __init__(self, start = 0):
        self.number = start
        self.fizzcount = 0
        self.buzzcount = 0
        self.fizzbuzzcount = 0
        self.counts = {}

    def next(self):
        self.number += 1
        if self.number % 3 == 0 and self.number % 5 == 0:
            self.fizzbuzzcount += 1
            return 'fizzbuzz'
        elif self.number % 3 == 0:
            self.fizzcount += 1
            return 'fizz'
        elif self.number % 5 == 0:
            self.buzzcount += 1
            return 'buzz'   
        else:
            return str(self.number)
    
    def counter(self):
        self.counts['fizzcount'] = self.fizzcount
        self.counts['buzzcount'] = self.buzzcount
        self.counts['fizzbuzzcount'] = self.fizzbuzzcount
        return self.counts


if __name__ == "__main__":
    test = FizzBuzzer(14)
    print(test.next())
    print(test.next())
    print(test.next())
    print(test.next())
    print(test.counter())