SIMPLE NUMBERS ADDER (9 MAX SUM)

/ input two numbers at cells 0 and 1
/ number at cell 1 is converted to its integer value;
/ cell 1 as an integer is added to cell 0 as a char; 
/ then cell 0 holds the result of the sum as a char;

! Note that if the char value at cell 0
exceeds 57 (ie sum result 
is larger than 9) its no longer gonna 
return a number; I gotta make a carry
flag for that; dont know how yet;

,>,                       inp cell(0) cell(1)
>>++++++++[<++++++>-]     mov cell(2) '0'
<[<->-]                   sub cell(1) cell(2)
<[<+>-]                   add cell(0) cell(1)
<.                        print cell(0)
