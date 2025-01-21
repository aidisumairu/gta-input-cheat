; Block all user input
BlockInput, On

; Set the send mode to Input for faster input
SendMode Input

; Retrieve the cheat code from the command line parameter
cheatCode := A_Args[1]

; Define the character delay (adjust as needed)
characterDelay := 25

; Send each character of the cheat code with a delay
Loop, Parse, cheatCode
{
    SendInput, %A_LoopField%
    Sleep, characterDelay
}

Sleep, 200

; Allow user input again
BlockInput, Off