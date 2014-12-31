

var numberList = [ 6, 4, 8, 15, 16, 23, 42, 2, 7]
var wordList = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

//Write a function that takes a list of numbers and returns a new list with only the odd numbers.

function allOdd(numberList){
    allOdd = []
    for(i = 0 ; i < numberList.length; i ++ ){
        if(numberList[i] % 2 != 0){
            allOdd.push(numberList[i])
        }
    }
    return allOdd 
}

print(allOdd(numberList))


//Write a function that takes a list of numbers and returns a new list with only the even numbers.

function allEven(numberList){
    allEven = []
    for(i = 0; i <numberList.length; i ++){
        if(numberList[i] % 2 == 0){
            allEven.push(numberList[i])
        }
    }
    return allEven
}
print("all_even");
print(allEven(numberList));



//Write a function that takes a list of strings and  returns a new list with all strings of length 4 or greater.

function greaterthanFour(wordList){
    greaterthanFour = [];
    for(i = 0; i <wordList.length; i ++){
        if(wordList[i].length >= 4){
            greaterthanFour.push(wordList[i])
        }
    }
    return greaterthanFour
}
print(greaterthanFour(wordList))


//Write a function that finds the smallest element in a list of integers and returns it.
function findSmallest(numberList){
    var smallest = numberList[0];
    for(i = 1; i <numberList.length; i ++){
        if(numberList[i] < smallest){
            smallest = numberList[i]
        }
    }
    return smallest
}

print(findSmallest(numberList));

//Write a function that finds the largest element in a list of integers and returns it.

function findLargest(numberList){
    var largest = numberList[0];
    for(i = 1; i<numberList.length; i ++){
        if(numberList[i] > largest){
            largest = numberList[i]
        }
    } 
    return largest
}

print(findLargest(numberList));

//Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.

// function forEach(array, process){
//     for(i = 0; i<array.length; i++){
//         function(array[i]);
//     }
// }

function dividebyTwo(numberList){
    var dividedbyTwo = [];
    for(i = 0; i < numberList.length; i++ ){
        dividedbyTwo.push(numberList[i]/2)
    }
    return dividedbyTwo
}

print(dividebyTwo(numberList))

//Write a function that takes a list of words and returns a list of all the lengths of those words.

function wordLength(wordList){
    var wordLength = [];
    for(i = 0; i < wordList.length; i++){
        wordLength.push(wordList[i].length)
    }
    return wordLength
}

print(wordLength(wordList))

//Write a function (using iteration) that sums all the numbers in a list.

function sumNumbers(numberList){
    var sum = 0;
    for(i=0; i<numberList.length; i++){
        sum += numberList[i]
    }
    return sum
}

print(sumNumbers(numberList))

//Write a function that multiplies all the numbers in a list together.

function multiplyNumbers(numberList){
    var multiplied = 1;
    for(i=0; i<numberList.length; i++){
        multiplied *= numberList[i]
    }
    return multiplied
}

print(multiplyNumbers(numberList))


// Write a function that joins all the strings in a list together without using the join method and returns a single string.
function combineStrings(wordList){
    combineString = "";
    for(i=0; i<wordList.length; i++){
        combineString += wordList[i];
    }
    return combineString
}

print(combineStrings(wordList));


//Write a function that takes a list of integers and returns the average (without using the avg method)

function average(numberList){
    var sum = 0 ;
    for (i = 0; i<numberList.length; i++){
        sum += numberList[i];
    } 
    print(sum)
    var average = sum/numberList.length;
    return average
}

print(average(numberList))



