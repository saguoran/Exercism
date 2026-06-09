import java.util.stream.IntStream;

class Hamming {
    private String leftStrand;
    private String rightStrand;
    Hamming(final String leftStrand, final String rightStrand){
        this.leftStrand = leftStrand;
        this.rightStrand = rightStrand;
        if(rightStrand.length() != leftStrand.length())
            if(leftStrand.equals(""))
                throw new IllegalArgumentException("left strand must not be empty.");
            else if(rightStrand.equals(""))
                throw new IllegalArgumentException("right strand must not be empty.");
        else
            throw new IllegalArgumentException("leftStrand and rightStrand must be of equal length.");
    }
    int getHammingDistance() {
        return (int)IntStream.range(0,this.leftStrand.length())
                        .filter(i->leftStrand.charAt(i)!=rightStrand.charAt(i))
                        .count();
    }
}


//import java.util.ArrayList;
//import java.util.List;
//
//class Hamming {
//    private List<Character> LeftStrand = new ArrayList<>();
//    private List<Character> RightStrand = new ArrayList<>();
//    Hamming(String leftStrand, String rightStrand){
//        int lenLeft = leftStrand.length();
//        int lenRight = rightStrand.length();
//        try{
//            for(int i=0; i< (lenLeft>lenRight? lenLeft:lenRight); i++){
//                this.LeftStrand.add(leftStrand.charAt(i));
//                this.RightStrand.add(rightStrand.charAt(i));
//            }
//        }catch(IndexOutOfBoundsException ex){
//            boolean leftIsEmpty = leftStrand.equals("");
//            boolean rightIsEmpty = rightStrand.equals("");
//            if(leftIsEmpty||rightIsEmpty){
//               throw new IllegalArgumentException((leftIsEmpty?"left":"right")+" strand must not be empty.");
//            }
//            throw new IllegalArgumentException("leftStrand and rightStrand must be of equal length.");
//        }
//    }
//
//    int getHammingDistance() {
//        int leftLen = this.LeftStrand.size();
//        int distance = 0;
//        for (int i = 0; i < leftLen; i++) {
//            if(this.LeftStrand.get(i)!=this.RightStrand.get(i)){
//                distance += 1;
//            }
//        }
//        return distance;
//    }
//
//}
