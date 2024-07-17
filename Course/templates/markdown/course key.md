Welcome to the course builder guide! 

Courses support the addition of images, flashcards, multi-choice questions, gap-fills, single answer questions. All components are quite straightforward to add. Refer to the first section for the key.

All courses are written in markdown, which is essentially English with a few key elements to change text type. For example, a title is written as 
## Title
Most of the important components are included in section 2. I have also linked a markdown cheat sheet for further additions.

-------Section 1-------
For the addition of images, you will need to upload all image files to a folder named Images. JPEG and PNG images are currently supported. Images will be automatically resized to fill the width of the screen. You will then need to use the following syntax:
%image%
filename.png
%end image%

For the remaining components, you can copy and paste the keys found below and then replace the filler with your content.

%flashcard block%
%flashcard%
%front%
The content found on the front of the flashcard goes here
%end front%
%back%
The content found on the back of the flashcard goes here
%end back%
%end flashcard%
%end flashcard block%

%multi-choice%
%question1%
Question 1 goes here
%choices%
choice 1
choice 2
choice 3
choice 4
%end choices%
%answer%
The correct answer
%end answer%
%end question1%
%end multi-choice%

%gap-fill%
The quick brown %_% jumps over the lazy dog
%end gap-fill%

%single-answer%
The question content goes here
%end single-answer%