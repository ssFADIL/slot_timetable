# Ex02 Time Table
## Date:

## AIM
To write a html webpage page to display your slot timetable.

## ALGORITHM
### STEP 1
Create a Django-admin Interface.

### STEP 2
Create a static folder and inert HTML code.

### STEP 3
Create a simple table using ```<table>``` tag in html.

### STEP 4
Add header row using ```<th>``` tag.

### STEP 5
Add your timetable using ```<td>``` tag.

### STEP 6
Execute the program using runserver command.

## PROGRAM:
~~~

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weekly Timetable</title>
    <style>
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background-color: #f5f5f5;
            padding: 20px;
            margin: 0;
        }
        h1 {
            text-align: center;
            color: #1a237e;
            margin-bottom: 25px;
        }
        .table-container {
            overflow-x: auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        table {
            width: 100%;
            border-collapse: collapse;
            min-width: 900px;
        }
        th {
            background-color: #3949ab;
            color: white;
            padding: 14px 8px;
            text-align: center;
            font-weight: 600;
            border: 1px solid #303f9f;
            font-size: 15px;
        }
        td {
            padding: 12px 8px;
            border: 1px solid #e0e0e0;
            text-align: center;
            vertical-align: top;
            font-size: 13px;
            line-height: 1.5;
        }
        .time-col {
            background-color: #e8eaf6;
            font-weight: bold;
            color: #283593;
            width: 130px;
        }
        tr:nth-child(even) td:not(.time-col) {
            background-color: #fafafa;
        }
        tr:hover td:not(.time-col) {
            background-color: #f1f8e9;
        }
        .class-info {
            font-weight: 600;
            color: #1a237e;
            margin-bottom: 3px;
        }
        .slot, .venue {
            font-size: 11px;
            color: #555;
        }
        .empty {
            color: #bdbdbd;
        }
    </style>
</head>
<body>
    <h1>Weekly Class Timetable</h1>
    
    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th>Time</th>
                    <th>Monday</th>
                    <th>Tuesday</th>
                    <th>Wednesday</th>
                    <th>Thursday</th>
                    <th>Friday</th>
                    <th>Saturday</th>
                    <th>Sunday</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="time-col">08:00 - 09:59 AM</td>
                    <td>
                        <div class="class-info">19AI301 - Python Programming</div>
                        <div class="slot">Slot: 25EJ2040</div>
                        <div class="venue">Venue: 2511</div>
                    </td>
                    <td>
                        <div class="class-info">19CS406 - Computer Networks</div>
                        <div class="slot">Slot: 25EJ2070</div>
                        <div class="venue">Venue: 2482</div>
                    </td>
                    <td>
                        <div class="class-info">19AI301 - Python Programming</div>
                        <div class="slot">Slot: 25EJ2040</div>
                        <div class="venue">Venue: 2411</div>
                    </td>
                    <td class="empty">-</td>
                    <td class="empty">-</td>
                    <td class="empty">-</td>
                    <td class="empty">-</td>
                </tr>
                <tr>
                    <td class="time-col">10:00 - 11:59 AM</td>
                    <td class="empty">-</td>
                    <td>
                        <div class="class-info">19AI414 - Fundamentals of Web Application Development</div>
                        <div class="slot">Slot: 25EJ2042</div>
                        <div class="venue">Venue: 2853</div>
                    </td>
                    <td>
                        <div class="class-info">19AI414 - Fundamentals of Web Application Development</div>
                        <div class="slot">Slot: 25EJ2042</div>
                        <div class="venue">Venue: 2851</div>
                    </td>
                    <td>
                        <div class="class-info">19AI301 - Python Programming</div>
                        <div class="slot">Slot: 25EJ2040</div>
                        <div class="venue">Venue: 2511</div>
                    </td>
                    <td>
                        <div class="class-info">19AI414 - Fundamentals of Web Application Development</div>
                        <div class="slot">Slot: 25EJ2042</div>
                        <div class="venue">Venue: 6872</div>
                    </td>
                    <td class="empty">-</td>
                    <td class="empty">-</td>
                </tr>
                <tr>
                    <td class="time-col">01:00 - 02:59 PM</td>
                    <td class="empty">-</td>
                    <td>
                        <div class="class-info">19AI414 - Fundamentals of Web Application Development</div>
                        <div class="slot">Slot: 25EJ2042</div>
                        <div class="venue">Venue: 2871</div>
                    </td>
                    <td>
                        <div class="class-info">ECA-M - Mentor Meet</div>
                        <div class="slot">Slot: 25EJ2M008</div>
                        <div class="venue">Venue: 2412</div>
                    </td>
                    <td>
                        <div class="class-info">19AI301 - Python Programming</div>
                        <div class="slot">Slot: 25EJ2040</div>
                        <div class="venue">Venue: 2512</div>
                    </td>
                    <td class="empty">-</td>
                    <td class="empty">-</td>
                    <td class="empty">-</td>
                </tr>
                <tr>
                    <td class="time-col">03:00 - 04:59 PM</td>
                    <td class="empty">-</td>
                    <td>
                        <div class="class-info">19CS406 - Computer Networks</div>
                        <div class="slot">Slot: 25EJ2070</div>
                        <div class="venue">Venue: 2482</div>
                    </td>
                    <td>
                        <div class="class-info">19CS406 - Computer Networks</div>
                        <div class="slot">Slot: 25EJ2070</div>
                    </td>
                    <td class="empty">-</td>
                    <td>
                        <div class="class-info">19CS406 - Computer Networks</div>
                        <div class="slot">Slot: 25EJ2070</div>
                        <div class="venue">Venue: 2482</div>
                    </td>
                    <td class="empty">-</td>
                    <td class="empty">-</td>
                </tr>
            </tbody>
        </table>
    </div>

</body>
</html>
~~~


## OUTPUT:


<img width="1910" height="751" alt="Screenshot 2026-05-19 124221" src="https://github.com/user-attachments/assets/cd3f95df-62a0-4f71-9971-e4a5631c37a8" />



## RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
