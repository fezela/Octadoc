var QuizDB = {
	Answers: [
	    {answer: {Question_ID: "1.0", Answer: "“true”" }},
	    {answer: {Question_ID: "2.0", Answer: "“false”" }},
	    {answer: {Question_ID: "14.0", Answer: "*" }},
	    {answer: {Question_ID: "15.0", Answer: "UPDATE EMPLOYEES SET SALARY NULL WHERE DEPARTMENT_ID =90;" }},
	    {answer: {Question_ID: "16.0", Answer: "CONCAT" }},
	    {answer: {Question_ID: "17.0", Answer: "BFILE" }},
	    {answer: {Question_ID: "20.0", Answer: "2.0" }},
	    {answer: {Question_ID: "21.0", Answer: "The table name is invalid." }},
	    {answer: {Question_ID: "22.0", Answer: "None of the above" }},
	    {answer: {Question_ID: "23.0", Answer: "None of the above" }},
	    {answer: {Question_ID: "24.0", Answer: "JOIN … ON clause" }},
	    {answer: {Question_ID: "25.0", Answer: "2910.0" }},
	    {answer: {Question_ID: "26.0", Answer: "Singe solid line with a crowfoot at one end." }},
	    {answer: {Question_ID: "27.0", Answer: "Table/view within user’s schema" }},
	    {answer: {Question_ID: "28.0", Answer: "Primary key" }}
	],

	Personality_Points: [
	    {personality: {Question_ID: "3.0", Personality_KEY: "EI" }},
	    {personality: {Question_ID: "4.0", Personality_KEY: "EI" }},
	    {personality: {Question_ID: "5.0", Personality_KEY: "EI" }},
	    {personality: {Question_ID: "6.0", Personality_KEY: "EI" }},
	    {personality: {Question_ID: "7.0", Personality_KEY: "EI" }},
	    {personality: {Question_ID: "8.0", Personality_KEY: "EI" }},
	    {personality: {Question_ID: "9.0", Personality_KEY: "EI" }},
	    {personality: {Question_ID: "10.0", Personality_KEY: "EI" }},
	    {personality: {Question_ID: "11.0", Personality_KEY: "EI" }},
	    {personality: {Question_ID: "12.0", Personality_KEY: "EI" }},
	    {personality: {Question_ID: "13.0", Personality_KEY: "EI" }}
	],

	Questions: [
	    {question: {Question_ID: "1.0", Type_ID: "1.0", Topic_ID: "1.0", Text: "George Washington was the first President of The United States." }},
	    {question: {Question_ID: "2.0", Type_ID: "1.0", Topic_ID: "1.0", Text: "Abraham Lincoln was the 32nd President of The United States." }},
	    {question: {Question_ID: "3.0", Type_ID: "1.0", Topic_ID: "2.0", Text: "You feel its worse to be…" }},
	    {question: {Question_ID: "4.0", Type_ID: "1.0", Topic_ID: "2.0", Text: "In friendships you’d rather have…" }},
	    {question: {Question_ID: "5.0", Type_ID: "1.0", Topic_ID: "2.0", Text: "For everyday work you’d rather…" }},
	    {question: {Question_ID: "6.0", Type_ID: "1.0", Topic_ID: "2.0", Text: "When talking to strangers you speak…" }},
	    {question: {Question_ID: "7.0", Type_ID: "1.0", Topic_ID: "2.0", Text: "When with other people" }},
	    {question: {Question_ID: "8.0", Type_ID: "1.0", Topic_ID: "2.0", Text: "The later it gets at a parties" }},
	    {question: {Question_ID: "9.0", Type_ID: "1.0", Topic_ID: "2.0", Text: "With friends and coworkers" }},
	    {question: {Question_ID: "10.0", Type_ID: "1.0", Topic_ID: "2.0", Text: "When at a social event" }},
	    {question: {Question_ID: "11.0", Type_ID: "1.0", Topic_ID: "2.0", Text: "New and varied experiences with others…" }},
	    {question: {Question_ID: "12.0", Type_ID: "1.0", Topic_ID: "2.0", Text: "Before a phone call you…" }},
	    {question: {Question_ID: "13.0", Type_ID: "1.0", Topic_ID: "2.0", Text: "When the doorbell rings you…" }},
	    {question: {Question_ID: "14.0", Type_ID: "1.0", Topic_ID: "3.0", Text: "Which operator will be evaluated first in the following SELECT statement?" }},
	    {question: {Question_ID: "15.0", Type_ID: "1.0", Topic_ID: "3.0", Text: "A user wants to remove the values present in column SALARY in the EMPLOYEES table for all employees who belong to DEPARTMENT_ID 90.  Which SQL would accomplish the task?" }},
	    {question: {Question_ID: "16.0", Type_ID: "1.0", Topic_ID: "3.0", Text: "Which function can possibly return a non-NULL value when one of the arguments is NULL?" }},
	    {question: {Question_ID: "17.0", Type_ID: "1.0", Topic_ID: "3.0", Text: "Which datatype stores data outside the Oracle database?" }},
	    {question: {Question_ID: "20.0", Type_ID: "1.0", Topic_ID: "3.0", Text: "At  a minimum" }},
	    {question: {Question_ID: "21.0", Type_ID: "1.0", Topic_ID: "3.0", Text: "Why does the following statement fail?  ‘CREATE TABLE FRUITS-N-VEGETABLES (NAME VARCHAR2 (40));’" }},
	    {question: {Question_ID: "22.0", Type_ID: "1.0", Topic_ID: "3.0", Text: "Table CUSTOMERS has a column named CUST_ZIP which could be NULL. Which of the following functions include the NULL rows in its result?" }},
	    {question: {Question_ID: "23.0", Type_ID: "1.0", Topic_ID: "3.0", Text: "Which option is not available in Oracle when modifying tables?" }},
	    {question: {Question_ID: "24.0", Type_ID: "1.0", Topic_ID: "3.0", Text: "In ANSI SQL" }},
	    {question: {Question_ID: "25.0", Type_ID: "1.0", Topic_ID: "3.0", Text: "What will be result of trunc(2916.16" }},
	    {question: {Question_ID: "26.0", Type_ID: "1.0", Topic_ID: "3.0", Text: "How do you represent the following business rule in an ER diagram? ‘A customer may have one or more orders; an order must belong to one and only one customer.’" }},
	    {question: {Question_ID: "27.0", Type_ID: "1.0", Topic_ID: "3.0", Text: "What order does Oracle use in resolving a table or view referenced in a SQL statement?" }},
	    {question: {Question_ID: "28.0", Type_ID: "1.0", Topic_ID: "3.0", Text: "Which types of constraints can be created on a view?" }},
	    {question: {Question_ID: "29.0", Type_ID: "1.0", Topic_ID: "4.0", Text: "What letter is this?" }}
	],

	Topics: [
	    {topic: {Topic_ID: "1.0", Topic: "History" }},
	    {topic: {Topic_ID: "2.0", Topic: "Personality" }},
	    {topic: {Topic_ID: "3.0", Topic: "OracleDB" }},
	    {topic: {Topic_ID: "4.0", Topic: "Alphabet" }}
	],

	Types: [
	    {type: {Type_ID: "1.0", Name: "Multiple Choice" }}
	],

	Multi_Choices: [
	    {multi_choice: {Question_ID: "1.0", Choice_1: "“true”", Choice_2: "“false”", Choice_3: "null", Choice_4: "null", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "2.0", Choice_1: "“true”", Choice_2: "“false”", Choice_3: "null", Choice_4: "null", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "3.0", Choice_1: "Reserved", Choice_2: "Out-going", Choice_3: "null", Choice_4: "null", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "4.0", Choice_1: "Quantity over depth", Choice_2: "Depth over quantity", Choice_3: "null", Choice_4: "null", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "5.0", Choice_1: "Talk to people face-to-face", Choice_2: "Send an email", Choice_3: "null", Choice_4: "null", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "6.0", Choice_1: "Easily", Choice_2: "Reservedly", Choice_3: "null", Choice_4: "null", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "7.0", Choice_1: "Start conversations", Choice_2: "Wait for the right moment", Choice_3: "null", Choice_4: "null", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "8.0", Choice_1: "Gain energy and want to stay", Choice_2: "Lose energy and want to leave", Choice_3: "null", Choice_4: "null", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "9.0", Choice_1: "Up to date on things", Choice_2: "Out of date on things", Choice_3: "null", Choice_4: "null", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "10.0", Choice_1: "As many people as possible", Choice_2: "As few people as possible", Choice_3: "null", Choice_4: "null", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "11.0", Choice_1: "Energizes you", Choice_2: "Depletes you", Choice_3: "null", Choice_4: "null", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "12.0", Choice_1: "Don’t plan what to say", Choice_2: "Practice what to say", Choice_3: "null", Choice_4: "null", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "13.0", Choice_1: "Jump to attention", Choice_2: "Hunker down", Choice_3: "null", Choice_4: "null", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "14.0", Choice_1: "+", Choice_2: "*", Choice_3: "/", Choice_4: "-", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "15.0", Choice_1: "DELETE FROM EMPLOYEES (SALARY) WHERE DEPARTMENT_ID = 90;", Choice_2: "INSERT INTO EMPLOYEES (SALARY) VALUES (NULL) WHERE DEPARTMENT_ID = 90;", Choice_3: "UPDATE EMPLOYEES SET SALARY NULL WHERE DEPARTMENT_ID =90;", Choice_4: "MERGE EMPLOYEES SET SALARY IS NULL WHERE DEPARTMENT_ID = 90;", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "16.0", Choice_1: "NULLIF", Choice_2: "LENGTH", Choice_3: "CONCAT", Choice_4: "INSTR", Choice_5: "TAN" }},
	    {multi_choice: {Question_ID: "17.0", Choice_1: "UROWID", Choice_2: "BFILE", Choice_3: "BLOB", Choice_4: "NCLOB", Choice_5: "EXTERNAL" }},
	    {multi_choice: {Question_ID: "20.0", Choice_1: "1.0", Choice_2: "2.0", Choice_3: "3.0", Choice_4: "There is no minimum", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "21.0", Choice_1: "The table should have more than one column in its definition.", Choice_2: "NAME is a reserved word", Choice_3: " which cannot be used as a column name.", Choice_4: "The table name is invalid.", Choice_5: "Column length cannot exceed 30 characters." }},
	    {multi_choice: {Question_ID: "22.0", Choice_1: "COUNT (CUST_ZIP)", Choice_2: "SUM (CUST_ZIP)", Choice_3: "AVG (DISTINCT CUST_ZIP)", Choice_4: "None of the above", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "23.0", Choice_1: "Add new columns", Choice_2: "rename existing column", Choice_3: "Drop existing column", Choice_4: "None of the above", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "24.0", Choice_1: "NATURAL JOIN clause", Choice_2: "CROSS JOIN clause", Choice_3: "JOIN … USING clause", Choice_4: "JOIN … ON clause", Choice_5: "All of the above" }},
	    {multi_choice: {Question_ID: "25.0", Choice_1: "2916.2", Choice_2: "290.0", Choice_3: "2916.1", Choice_4: "2900.0", Choice_5: "2910.0" }},
	    {multi_choice: {Question_ID: "26.0", Choice_1: "Single solid line.", Choice_2: "Single line that is solid at one end and dotted at another end.", Choice_3: "Singe solid line with a crowfoot at one end.", Choice_4: "The business rule cannot be represented in the ER diagram.", Choice_5: "null" }},
	    {multi_choice: {Question_ID: "27.0", Choice_1: "Table/view within user’s schema", Choice_2: " public synonym", Choice_3: " private synonym", Choice_4: "Table/view within user’s schema", Choice_5: " private synonym" }},
	    {multi_choice: {Question_ID: "28.0", Choice_1: "Check", Choice_2: " NOT NULL", Choice_3: "Primary key", Choice_4: " foreign key", Choice_5: " unique key" }}
	],

	Alphabet_Images: [
	    {alphabet_image: {Image_ID: "1.0", Image_Path: "alif.png", Pronounciation_ID: "1.0", Type_ID: "1.0" }},
	    {alphabet_image: {Image_ID: "2.0", Image_Path: "bah.png", Pronounciation_ID: "2.0", Type_ID: "1.0" }},
	    {alphabet_image: {Image_ID: "3.0", Image_Path: "yah.png", Pronounciation_ID: "26.0", Type_ID: "1.0" }}
	],

	Pronounciations: [
	    {pronounciation: {pronounciation_ID: "1.0", pronounciation_TEXT: "Alif" }},
	    {pronounciation: {pronounciation_ID: "2.0", pronounciation_TEXT: "Bah" }},
	    {pronounciation: {pronounciation_ID: "3.0", pronounciation_TEXT: "Taa" }},
	    {pronounciation: {pronounciation_ID: "4.0", pronounciation_TEXT: "Thaa" }},
	    {pronounciation: {pronounciation_ID: "5.0", pronounciation_TEXT: "Jeem" }},
	    {pronounciation: {pronounciation_ID: "6.0", pronounciation_TEXT: "Ha" }},
	    {pronounciation: {pronounciation_ID: "7.0", pronounciation_TEXT: "Kha" }},
	    {pronounciation: {pronounciation_ID: "8.0", pronounciation_TEXT: "Daal" }},
	    {pronounciation: {pronounciation_ID: "9.0", pronounciation_TEXT: "Dhal" }},
	    {pronounciation: {pronounciation_ID: "10.0", pronounciation_TEXT: "Ra" }},
	    {pronounciation: {pronounciation_ID: "11.0", pronounciation_TEXT: "Zay" }},
	    {pronounciation: {pronounciation_ID: "12.0", pronounciation_TEXT: "Seen" }},
	    {pronounciation: {pronounciation_ID: "13.0", pronounciation_TEXT: "Sheen" }},
	    {pronounciation: {pronounciation_ID: "14.0", pronounciation_TEXT: "Saad" }},
	    {pronounciation: {pronounciation_ID: "15.0", pronounciation_TEXT: "Daad" }},
	    {pronounciation: {pronounciation_ID: "16.0", pronounciation_TEXT: "Zah" }},
	    {pronounciation: {pronounciation_ID: "17.0", pronounciation_TEXT: "Ayn" }},
	    {pronounciation: {pronounciation_ID: "18.0", pronounciation_TEXT: "Ghayn" }},
	    {pronounciation: {pronounciation_ID: "19.0", pronounciation_TEXT: "Fa" }},
	    {pronounciation: {pronounciation_ID: "20.0", pronounciation_TEXT: "Qaf" }},
	    {pronounciation: {pronounciation_ID: "21.0", pronounciation_TEXT: "Calf" }},
	    {pronounciation: {pronounciation_ID: "22.0", pronounciation_TEXT: "Lamb" }},
	    {pronounciation: {pronounciation_ID: "23.0", pronounciation_TEXT: "Meem" }},
	    {pronounciation: {pronounciation_ID: "24.0", pronounciation_TEXT: "Noon" }},
	    {pronounciation: {pronounciation_ID: "25.0", pronounciation_TEXT: "wah" }},
	    {pronounciation: {pronounciation_ID: "26.0", pronounciation_TEXT: " Yah" }}
	],

	Alphabet_TYPE: [
	    {alphabet_TYPE: {Type_ID: "1.0", Type: "Isolated" }}
	],
};