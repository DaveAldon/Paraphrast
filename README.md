<p align="center">
<b>Paraphrast</b>
</p>

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0a57fc8d35f74e6e9611b57a808b7556)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=DaveAldon/Paraphrast&amp;utm_campaign=Badge_Grade) [![Build Status](https://travis-ci.com/DaveAldon/Paraphrast.svg?token=eCnosqg9nhqR9WqTkK12&branch=master)](https://travis-ci.com/DaveAldon/Paraphrast) ![Coverage Status](coverage.svg)


***

It all started when I accidentally typed "ls" into a Windows command prompt for the _**last**_ time...

![Wrong command](https://scontent.xx.fbcdn.net/v/t1.0-9/20294488_807229002782102_3555223817833664693_n.jpg?oh=5aafd12f3b0eca1a35afd0a4db1cea57&oe=5A085F8C "Failure!")

If you frequently work between Unix and DOS prompts, it can be a pain switching between syntaxes. Or even if you work solely on Unix and have to check something quick, and the only thing around is a Windows machine and you _don't know any DOS commands_, it makes happy people sad.

### "But wait! There's already terminal emulators out there that do this!"

Yes, but not like this.
1. [Cygwin](https://www.cygwin.com/): one of the most popular, but it doesn't have a Unix version that translates DOS commands, it wasn't made in Python :grin:, and it needs an emulation layer so more like a GNU OS without a kernel than a terminal emulator. While I won't deny that it will give you the ability to run Unix commands in Windows, and it does it well, I want a less invasive installation and setup process. I also want something that hardly takes up any space.
2. [MSYS](http://www.mingw.org/wiki/MSYS) or [GnuWin32](http://gnuwin32.sourceforge.net/): Go ahead and try! More power to ya. Also no Unix compatibility so good luck running DOS commands on a Mac/Linux OS.
3. [Windows 10 Bash](https://msdn.microsoft.com/commandline/wsl/about): Only for Windows 10+ and also there's [some precious filespace](https://superuser.com/questions/1201269/what-size-does-basic-bash-wsl-subsystem-on-windows-occupy) needed. I want something really small.
4. _Your Favorite VM_: Of course you could always just fire up a VM of your favorite OS, but that's a tad bit inconvenient, isn't it? All we want are our commands translated into whatever OS we're using.

## Enter Paraphrast
We want what we type _paraphrased_ into the correct syntax for our OS. Paraphrast takes the work out of remembering two syntaxes, and let's you just focus on one.
That's right, not only does it translate Unix into DOS commands, it goes the other way too!

#### Current Features
- Cross Compatible Windows/Unix
- Small
- Really, really straightforward translation of commands
- Auto-complete that's better than what you have (if you're still using a default CLI)

## The Mission
I have a firm belief in magical user experiences, where what the user wants happens without any extra interaction beyond what's expected.

Because of this, each of my planned steps in developing this product must revolve around making the user's CLI work like it should on their favorite OS.

So now we can do this and stay happy...

![ls on DOS](https://scontent.xx.fbcdn.net/v/t1.0-9/20294187_807244809447188_8117695787448058930_n.jpg?oh=8e8cb5ffc768b874e75a6e6a2b60ee34&oe=59FCDBB7 "Success!")

## Development Focus Before v1.0 Release
- Get the most frequently used CLI commands working
- Dynamic Headers (current working directory displayed)
- Command elevation (sudo equivalents)
- Make it portable so that machines without Python can run it
- Special Paraphrast configuration commands
- Adherance to CI and code review results

## Current Requirements
- Python 3.3+
- Windows or Unix OS

## 3rd Party Plugins
- Prompt-Toolkit

## Current Instructions
1. Download and extract Paraphrast from Github
2. cd to the extracted folder and run main.py
3. Begin entering commands opposite the OS you're on
4. Submit bug reports to the issues section of this project

## Reviews
> "It's great!" - David Crawford
