package furhatos.app.newskill.flow.main

import furhatos.app.newskill.flow.Options
import furhatos.app.newskill.nlu.*
import furhatos.flow.kotlin.*
import furhatos.nlu.common.No
import furhatos.nlu.common.Yes
import furhatos.util.Language

val TakingOrder = state(Options) {
    onEntry {
        random(
            { furhat.ask("How about some fruits?") },
            { furhat.ask("Do you want some fruits?") }

        )
    }

    onResponse<No> {
        furhat.say("Okay, that's a shame. Have a splendid day!")
        goto(Idle)
    }

}

fun orderReceived(fruits: FruitList) :  State = state(Options) {
    onEntry {
        furhat.say("${fruits.text}, what a lovely choice!")
        fruits.list.forEach {
            users.current.order.fruits.list.add(it)
        }
        furhat.ask("Anything else?")
    }

    onReentry {
        furhat.ask("Did you want something else?")
    }

    onResponse<No> {
        furhat.say("Okay, here is your order of ${users.current.order.fruits}. Have a great day!")
        goto(Idle)
    }


}