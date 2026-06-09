// dart 2.5.0-dev2.1
import 'dart:math' show pow;

class ArmstrongNumbers extends Object{
  bool isArmstrongNumber(int num){
    List<String> digits = num.toString().split('');
    return num == digits.fold<int>(0, (prev, d)=> prev + pow(int.parse(d), digits.length).floor());
  }
}
