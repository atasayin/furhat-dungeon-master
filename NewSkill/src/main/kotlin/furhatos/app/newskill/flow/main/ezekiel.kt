package furhatos.app.newskill.flow.main

import furhatos.app.newskill.flow.Parent
import furhatos.flow.kotlin.*
import furhatos.nlu.common.No
import furhatos.nlu.common.Yes

val Ezekiel : State = state(Parent) {
    onEntry {
        furhat.say{
            +"Now, I'm going to give you a monologue from Pulp Fiction."
            + furhatos.gestures.Gestures.Roll()
            + delay(1000)
        }

        furhat.say("The path of the  ${furhat.voice.emphasis("righteous")} man is beset on all sides "
                +"By the inequities of the selfish, and the tyranny, of evil men. "
                +"Blessed is he who, in the name of charity and good will "
                +"Shepherds the weak through the valley of darkness. "
                +"For he is truly his brother's keeper and the finder of lost children. "
                +"And I will strike down upon thee "
                +"With great vengeance and furious anger "
                +"Those who attempt to poison and destroy my brothers. "
                +"And you will know my name is the Lord When I lay my vengeance upon thee")
    }

    onResponse<Yes> {


    }



    onResponse<No> {
        furhat.say("Ok.")
    }
}
