// dart 2.5.0
import 'dart:math' show pow;
Iterable<int> list(int n)=>Iterable<int>.generate(n, (i)=>i+1);
int sum(int result,int e) => result + e;
int square(int n) => n * n;

class DifferenceOfSquares {
  int squareOfSum(int firstNaturalNumber)=> square(list(firstNaturalNumber).reduce(sum));
  int sumOfSquare(int firstNaturalNumber)=> list(firstNaturalNumber).map(square).reduce(sum);
  int differenceOfSquares(int firstNaturalNumber) => squareOfSum(firstNaturalNumber) - sumOfSquare(firstNaturalNumber);
}
