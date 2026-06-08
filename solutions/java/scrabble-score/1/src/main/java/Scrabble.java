import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Stream;

class Scrabble {

    private final String word;

    Scrabble(String word) {
        this.word = word.toUpperCase();
    }

    int getScore() {
        Map<String, Integer> score = new HashMap<>();
        score.put("AEIOULNRST", 1);
        score.put("DG", 2);
        score.put("BCMP", 3);
        score.put("FHVWY", 4);
        score.put("K", 5);
        score.put("JX", 8);
        score.put("QZ", 10);
        return this.word.chars().map(e->{
            return score.entrySet().stream().mapToInt(s->{
                if(s.getKey().indexOf((char)e)!=-1)
                    return s.getValue();
                else return 0;
            }).sum();
        }).sum();
    }

}
