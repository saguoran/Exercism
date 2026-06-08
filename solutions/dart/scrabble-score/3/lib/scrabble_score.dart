const Map<String, int> scores = const {'AEIOULNRST': 1, 'DG': 2, 'BCMP': 3, 'FHVWY': 4, 'K': 5, 'JX': 8, 'QZ': 10};
int score(String word){
  return word.split('').fold<int>(0, (sum, element){
    var key = scores.keys.singleWhere((k)=>k.contains(element.toUpperCase()));
    return sum + scores[key];
    });
}