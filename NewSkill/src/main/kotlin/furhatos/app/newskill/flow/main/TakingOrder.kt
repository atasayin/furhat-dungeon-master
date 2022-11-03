package furhatos.app.newskill.flow.main

import furhatos.app.newskill.flow.Parent
import furhatos.flow.kotlin.*
import furhatos.nlu.common.No
import furhatos.nlu.common.Yes


val TakingOrder = state {
    onEntry{
        random(
            { furhat.ask("How about some fruits?") },
            { furhat.ask("Do you want some fruits?") }

        )
    }
    onResponse<Yes> {
        random(
            { furhat.ask("What kind of fruit do you want?") },
            { furhat.ask("What type of fruit?") }
        )
    }

    onResponse<No> {
        furhat.say("Okay, that's a shame. Have a splendid day!")
        goto(Idle)
    }


}
