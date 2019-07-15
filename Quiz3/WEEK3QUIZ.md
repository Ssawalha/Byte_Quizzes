
## Quiz: FizzBuzzer class

### Part 1

* Create a class called FizzBuzzer

* It has an init method and a next val. The init method has an argument, `start`
whose default value is 0. An integer instance property called `number` is set 
to equal `start`

* It has a (normal, not class) method called `next` that takes no arguments.

This method increases number by 1 and then returns a string of that number's
fizzbuzz value.

Fizzbuzz value of n = "fizz" if n is evenly divisible by 3, "buzz" if n is
evenly divisible by 5, and "fizzbuzz" if n is evenly divisible by 3 and 5. If
n is not divisible by 3 or 5 then the fizzbuzz value is the value of n converted
into a string.

Example

```py
buzzer = FizzBuzzer(11)
print(buzzer.next())
print(buzzer.next())
print(buzzer.next())
print(buzzer.next())
print(buzzer.next())
```

outputs

```
fizz
13
14
fizzbuzz
16
```

and 

```py
buzzer = FizzBuzzer()
print(buzzer.next())
print(buzzer.next())
print(buzzer.next())
```

produces

```
1
2
fizz
```

### Part 2 - Unit test

* Now write a unit test for the FizzBuzzer class using the python unittest
module.

* Test that the following.

    * when `x = FizzBuzzer()`, `x.number` is 0

    * when `x = FizzBuzzer()`, `x.next()` returns the string `"1"`

    * when `x = FizzBuzzer(2)`, `x.next()` returns `"fizz"` and calling `x.next()`
a second time returns `"4"`

* You may write other tests as well. Hint: you should not need a setUp() method.

### Open book, open notes

* You are free to use Google & look at your code from class. Do not ask anyone
to help you write or debug your code. If the question is unclear, please ask an
instructor or T.A. to clarify over Discord.
