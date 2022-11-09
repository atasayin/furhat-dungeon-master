package furhatos.app.newskill.flow.main

import furhatos.app.newskill.flow.Parent
import furhatos.flow.kotlin.*
import furhatos.nlu.common.No
import furhatos.nlu.common.Yes

val Greeting : State = state(Parent) {
    onEntry {
        random (
            {furhat.say("Hi there")},
            { furhat.say("Oh, hello there")}
        )

        goto(TakingOrder)
    }

}
