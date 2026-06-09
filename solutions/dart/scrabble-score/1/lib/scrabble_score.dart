int score(String word){
  int sum = 0;
  final englishWord = word.toUpperCase();
  final Map<String, int> score = {'AEIOULNRST': 1, 'DG': 2, 'BCMP': 3, 'FHVWY': 4, 'K': 5, 'JX': 8, 'QZ': 10};
  for(String s in englishWord.split('')){
    score.forEach((k,v){
      if(k.contains(s))
        sum += v;
    });
  }
  return sum;
}