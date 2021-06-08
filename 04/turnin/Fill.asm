// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

	@16383
	D=A
	@screen
	M=D

	@24576
	D=M
	@code
	M=D

	@i
	M=0

(LOOP)
	@8191
	D=A
	@i
	D=M-D
	@0
	D;JGT
	@screen
	M=M+1
	@code
	D=M
	@WHITEN
	D;JEQ
	@BLACKEN
	D;JNE

(WHITEN)
	@screen
	A=M
	M=0
	@i
	M=M+1
	@LOOP
	0;JMP
(BLACKEN)
	@screen
	A=M
	M=-1
	@i
	M=M+1
	@LOOP
	0;JMP

