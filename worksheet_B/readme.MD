code:
***

START

Attempts=0
i=0
Likeness=0
OriginalWord=Generate

while (attempts <= 4):
	Output ("enter your first attempt: ")
	UserEntery=UserInput
	attempts+1
	
	For (each character in OriginalWord):
		i+1
		if (letter == letter in UserEntery)
			Likeness+1
		else
			next character
		END IF
	Output ("your likeness is: " + Likeness)
	END FOR
END WHILE

if (Likeness == 4)
	output ("congratulations")
else
	output ("you have failed")
END IF

END

***
