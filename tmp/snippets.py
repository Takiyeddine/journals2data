if(
    self.config.params["VERBOSE"] == 
    utils.enums.VerboseLevel.COLOR
):
    console.println_ctrl_sequence(
        "text",
        console.ANSICtrlSequence.PASSED
    )
    console.println_ctrl_sequence(
        "text",
        console.ANSICtrlSequence.PASSED
    )

if(self.config.params["VERBOSE"].value > 0):
    console.println_ctrl_sequence(
        "text",
        console.ANSICtrlSequence.PASSED
    )