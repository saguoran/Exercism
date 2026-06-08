import Foundation
let pair = ["G":"C", "C":"G", "T":"A", "A": "U"]
class Nucleotide{
    let strands: String;
    init(_ strands:String){
        self.strands = strands;
    }

    func complementOfDNA() throws -> String {
        var rna = ""
        for strand in self.strands{
            guard pair[String(strand)] != nil else {
                throw TranscriptionError.invalidNucleotide("\(strand) is not a valid Nucleotide")
            }
                rna += pair[String(strand)]!
            
        }
        return rna
    }

}

enum TranscriptionError :Error{
    case invalidNucleotide(String)
}


