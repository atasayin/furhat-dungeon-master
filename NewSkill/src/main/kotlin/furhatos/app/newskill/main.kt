package furhatos.app.newskill

import furhatos.app.newskill.flow.*
import furhatos.skills.Skill
import furhatos.flow.kotlin.*

class NewskillSkill : Skill() {
    override fun start() {
        Flow().run(Init)
    }
}

fun main(args: Array<String>) {
    Skill.main(args)
}
