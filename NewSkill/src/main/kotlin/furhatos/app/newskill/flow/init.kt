package furhatos.app.newskill.flow

import furhatos.app.newskill.flow.main.Idle
import furhatos.app.newskill.setting.distanceToEngage
import furhatos.app.newskill.setting.maxNumberOfUsers
import furhatos.flow.kotlin.*
import furhatos.flow.kotlin.voice.Voice

val Init : State = state() {
    init {
        /** Set our default interaction parameters */
        users.setSimpleEngagementPolicy(distanceToEngage, maxNumberOfUsers)
        furhat.voice = Voice("Matthew")
        /** start the interaction */
        goto(Idle)
    }
}
