import 'dart:math' as math;

class ArmstrongNumbers extends Object{
  bool isArmstrongNumber(int num){
    List<int> numbers = num.toString().split('').map((e)=>int.parse(e)).toList();
    return num == numbers.reduce((prev, element)=>math.pow(element, numbers.length).floor() + prev );
  }
}
