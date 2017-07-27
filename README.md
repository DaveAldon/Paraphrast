<p align="center">
<b>Paraphrast</b>
</p>

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0a57fc8d35f74e6e9611b57a808b7556)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=DaveAldon/Paraphrast&amp;utm_campaign=Badge_Grade)


***

It all started when I accidentally typed "ls" into a Windows CLI for the _**last**_ time...

![Wrong command](https://scontent.xx.fbcdn.net/v/t1.0-9/20294488_807229002782102_3555223817833664693_n.jpg?oh=5aafd12f3b0eca1a35afd0a4db1cea57&oe=5A085F8C "Failure!")

If you frequently work between Unix and DOS prompts, it can be a pain switching between syntaxes. Or even if you work solely on Unix and have to check something quick, and the only thing around is a Windows machine and you _don't know any DOS commands_, it makes happy people sad.

## Enter Paraphrast
We want what we type _paraphrased_ into the correct syntax for our OS. Paraphrast takes the work out of remembering two syntaxes, and let's you just focus on one.
That's right, not only does it translate Unix into DOS commands, it goes the other way too!

## The Mission
I have a firm belief in magical user experiences, where what the user wants happens without any extra interaction beyond what's expected. 

Because of this, each of my planned steps in developing this product must revolve around making the user's CLI work like it should on their favorite OS.

So now we can do this and stay happy...

![ls on DOS](https://scontent.xx.fbcdn.net/v/t1.0-9/20294187_807244809447188_8117695787448058930_n.jpg?oh=8e8cb5ffc768b874e75a6e6a2b60ee34&oe=59FCDBB7 "Success!")

## Development Focus Before Release
- Get the most frequently used CLI commands working
- Dynamic Headers (current working directory displayed)
- Command elevation (sudo equivalents)
- Make it portable so that machines without Python can run it
- Special Paraphrast configuration commands
- Error pipeline built in (if a command should work but doesn't, make it easy for user to send relevant information to me from Paraphrast)
- Crowd Source Dictionary (While I continue to add commands, you might have a favorite one that you want next)
- Possible external dictionary? (This would allow for updating simple syntax translations without updating the code)

## Current Requirements
- Python 3+
- Windows or Unix OS

## Current Instructions
1. Download and extract Paraphrast from Github
2. cd to the extracted folder and run main.py
3. Begin entering commands opposite the OS your on
4. Submit bug reports to the issues section of this project
