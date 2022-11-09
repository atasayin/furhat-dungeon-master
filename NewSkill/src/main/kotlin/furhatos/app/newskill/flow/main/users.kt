package furhatos.app.newskill.flow.main

import furhatos.app.newskill.nlu.*
import furhatos.records.User

class FruitData (
    var fruits : FruitList = FruitList()
)

val User.order : FruitData
    get() = data.getOrPut(FruitData::class.qualifiedName, FruitData())