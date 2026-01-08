# Schema
----------
Each database has some “schema”—the tables and columns into which the data is organized. In `cyberchase.db` you’ll find a single table, `episodes`. In the `episodes` table, you’ll find the following columns:

- `id`, which uniquely identifies each row (episode) in the table
- `season`, which is the season number in which the episode aired
- `episode_in_season`, which is the episode’s number within its given season
- `title`, which is the episode’s title
- `topic`, which identifies the ideas the episode aimed to teach
- `air_date`, which is the date (expressed as `YYYY-MM-DD`) on which the episode “aired” (i.e., was published)
- `production_code`, which is the unique ID used by PBS to refer to each episode internally

# Specifications
For each of the following questions, you should write a single SQL query that outputs the results specified by each problem. Your response must take the form of a single SQL query. Finally, each query should return only the data necessary to answer the question: if the problem only asks you to output the names of episodes, for example, then your query should not also output each episodes’s air date.

1. In `1.sql`, write a SQL query to list the titles of all episodes in Cyberchase’s original season, Season 1.
2. In `2.sql`, list the season number of, and title of, the first episode of every season.
3. In `3.sql`, find the production code for the episode “Hackerized!”.
4. In `4.sql`, write a query to find the titles of episodes that do not yet have a listed topic.
5. In `5.sql`, find the title of the holiday episode that aired on December 31st, 2004.
6. In `6.sql`, list the titles of episodes from season 6 (2008) that were released early, in 2007.
7. In `7.sql`, write a SQL query to list the titles and topics of all episodes teaching fractions.
8. In `8.sql`, write a query that counts the number of episodes released in the last 6 years, from 2018 to 2023, inclusive.
    - You might find it helpful to know you can use `BETWEEN` with dates, such as `BETWEEN '2000-01-01' AND '2000-12-31'`.
9. In `9.sql`, write a query that counts the number of episodes released in Cyberchase’s first 6 years, from 2002 to 2007, inclusive.
10. In `10.sql`, write a SQL query to list the ids, titles, and production codes of all episodes. Order the results by production code, from earliest to latest.
11. In `11.sql`, list the titles of episodes from season 5, in reverse alphabetical order.
12. In `12.sql`, count the number of unique episode titles.
13. In `13.sql`, write a SQL query to explore a question of your choice. This query should:
    - Involve at least one condition, using `WHERE` with `AND` or `OR`

# სქემა (Schema)
----------
თითოეულ მონაცემთა ბაზას აქვს თავისი „სქემა“ — ცხრილები და სვეტები, რომლებშიც მონაცემებია ორგანიზებული. მონაცემთა ბაზაში `cyberchase.db` თქვენ იპოვით ერთ ცხრილს, სახელად `episodes`. ცხრილში `episodes` მოცემულია შემდეგი სვეტები:

- `id`: თითოეული რიგის (ეპიზოდის) უნიკალური იდენტიფიკატორი.
- `season`: სეზონის ნომერი, რომელშიც ეპიზოდი გავიდა ეთერში.
- `episode_in_season`: ეპიზოდის ნომერი კონკრეტულ სეზონში.
- `title`: ეპიზოდის სათაური.
- `topic`: თემატიკა, რომლის სწავლებასაც ისახავდა მიზნად ეპიზოდი.
- `air_date`: ეთერში გასვლის თარიღი (ფორმატით `YYYY-MM-DD`).
- `production_code`: უნიკალური საწარმოო კოდი, რომელსაც PBS იყენებს შიდა მოხმარებისთვის.


# gemini-ს თარგმანი

# სპეციფიკაციები
თითოეული ქვემოთ მოცემული კითხვისთვის უნდა დაწეროთ ერთი SQL მოთხოვნა (query), რომელიც გამოიტანს დავალებაში მითითებულ შედეგს. თქვენი პასუხი უნდა შედგებოდეს მხოლოდ ერთი SQL მოთხოვნისგან. გარდა ამისა, თითოეულმა მოთხოვნამ უნდა დააბრუნოს მხოლოდ კითხვისთვის საჭირო მონაცემები: მაგალითად, თუ დავალება ითხოვს მხოლოდ ეპიზოდების სათაურებს, თქვენმა მოთხოვნამ არ უნდა გამოიტანოს ამ ეპიზოდების გამოშვების თარიღები.

1. ფაილში `1.sql`, დაწერეთ SQL მოთხოვნა, რომელიც ჩამოთვლის Cyberchase-ის პირველი სეზონის (Season 1) ყველა ეპიზოდის სათაურს.
2. ფაილში `2.sql`, ჩამოთვალეთ ყოველი სეზონის პირველი ეპიზოდის სეზონის ნომერი და სათაური.
3. ფაილში `3.sql`, იპოვეთ ეპიზოდის — „Hackerized!“ — საწარმოო კოდი (production code).
4. ფაილში `4.sql`, დაწერეთ მოთხოვნა იმ ეპიზოდების სათაურების საპოვნელად, რომლებსაც ჯერ არ აქვთ მითითებული თემა (topic).
5. ფაილში `5.sql`, იპოვეთ იმ სადღესასწაულო ეპიზოდის სათაური, რომელიც ეთერში გავიდა 2004 წლის 31 დეკემბერს.
6. ფაილში `6.sql`, ჩამოთვალეთ მე-6 სეზონის (2008 წელი) იმ ეპიზოდების სათაურები, რომლებიც ვადაზე ადრე, 2007 წელს გამოვიდა.
7. ფაილში `7.sql`, დაწერეთ SQL მოთხოვნა, რომელიც ჩამოთვლის ყველა იმ ეპიზოდის სათაურსა და თემას, რომლებიც წილადებს (fractions) ეხება.
8. ფაილში `8.sql`, დაწერეთ მოთხოვნა, რომელიც დაითვლის ბოლო 6 წლის განმავლობაში (2018-დან 2023 წლის ჩათვლით) გამოშვებული ეპიზოდების რაოდენობას.
    - გაითვალისწინეთ, რომ თარიღებთან შეგიძლიათ გამოიყენოთ `BETWEEN`, მაგალითად: `BETWEEN '2000-01-01' AND '2000-12-31'`.
9. ფაილში `9.sql`, დაწერეთ მოთხოვნა, რომელიც დაითვლის Cyberchase-ის პირველი 6 წლის განმავლობაში (2002-დან 2007 წლის ჩათვლით) გამოშვებული ეპიზოდების რაოდენობას.
10. ფაილში `10.sql`, დაწერეთ SQL მოთხოვნა, რომელიც ჩამოთვლის ყველა ეპიზოდის ID-ს, სათაურს და საწარმოო კოდს. დაალაგეთ შედეგები საწარმოო კოდის მიხედვით, უძველესიდან უახლესისკენ.
11. ფაილში `11.sql`, ჩამოთვალეთ მე-5 სეზონის ეპიზოდების სათაურები საპირისპირო ანბანური თანმიმდევრობით.
12. ფაილში `12.sql`, დაითვალეთ ეპიზოდების უნიკალური სათაურების რაოდენობა.
13. ფაილში `13.sql`, დაწერეთ თქვენი სურვილისამებრ შერჩეული კითხვის გამოსაკვლევი SQL მოთხოვნა. ეს მოთხოვნა უნდა:
    - შეიცავდეს მინიმუმ ერთ პირობას, სადაც გამოიყენებთ `WHERE`-ს `AND` ან `OR` ოპერატორებთან ერთად.