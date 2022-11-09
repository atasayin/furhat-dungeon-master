package furhatos.app.newskill.nlu

import furhatos.nlu.EnumEntity
import furhatos.nlu.ListEntity
import furhatos.nlu.ComplexEnumEntity
import furhatos.nlu.Intent
import furhatos.util.Language

// Our Fruit entity.
class Fruit : EnumEntity(stemming = true, speechRecPhrases = true) {
    override fun getEnum(lang: Language): List<String> {
        return listOf("banana", "orange", "apple", "cherimoya")
    }
}

// Our BuyFruit intent
class BuyFruit(val fruits : FruitList? = null) : Intent() {
    override fun getExamples(lang: Language): List<String> {
        return listOf("@fruits", "I want a bananas", "I would like an apple", "I want to buy a @fruits")
    }
}

class RequestOptions: Intent() {
    override fun getExamples(lang: Language): List<String> {
        return listOf("What options do you have?",
            "What fruits do you have?",
            "What are the alternatives?",
            "What do you have?")
    }
}

class FruitList : ListEntity<QuantifiedFruit>()

class QuantifiedFruit(
    val count : furhatos.nlu.common.Number? = furhatos.nlu.common.Number(1),
    val fruit : Fruit? = null) : ComplexEnumEntity() {

    override fun getEnum(lang: Language): List<String> {
        return listOf("@count @fruit", "@fruit")
    }

    override fun toText(): String {
        return generate("$count $fruit")
    }
}
