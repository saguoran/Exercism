// dart 2.5.0
import 'dart:math' show pow;


class DifferenceOfSquares {
  int squareOfSum(int firstNaturalNumber){
    return List<int>.generate(firstNaturalNumber+1, (i)=>
       pow(i, 2).toInt()
    ).reduce((sum, element)=>sum+element);
  }
  int sumOfSquare(int firstNaturalNumber){
    return pow(List<int>.generate(firstNaturalNumber+1, (i)=>
      i+1
    ).reduce((sum, element)=>sum+element), 2).toInt();
  }
  int differenceOfSquares(int firstNaturalNumber){
    return squareOfSum(firstNaturalNumber) - sumOfSquare(firstNaturalNumber);
  }
}
