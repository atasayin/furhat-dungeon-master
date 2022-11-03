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

       // furhat.say{
        //    +"Welcome to our Progress Meeting."
        //    +"In this presentation, we will talk about what we have done in this week. "
         //   + furhatos.gestures.Gestures.BigSmile(duration=2.0, strength = 10.0)
        //}

        goto(Ezekiel)
    }

}
