# CS-340-Portfolio
## Client/Server Development: Project Reflection

### How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?

By separating the database operations into a dedicated CRUD Python module in Project One, I was able to create clean, reusable functions for creating, reading, updating, and deleting records in MongoDB. This approach made the code more maintainable because all database logic was centralized in one file, making it easier to debug and update. It improved readability by keeping the main dashboard application (Project Two) focused on user interface and widget logic rather than mixing in database queries. The module was adaptable because it used clear function names, parameters, and docstrings, allowing easy integration into the Dash/Plotly dashboard.

The main advantages were modularity and reusability—I could import the same CRUD module into the dashboard without rewriting code, which saved time and reduced errors. In the future, I could reuse this CRUD module in other applications that need to interact with the same MongoDB animal shelter database, such as a mobile app, a different web interface, or even automated data import scripts.

### How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?

As a computer scientist, I approach problems by first clearly defining requirements, breaking them into smaller components, designing solutions, implementing incrementally, and testing thoroughly. For Grazioso Salvare’s requirements, I started by analyzing their need for filtering rescue dogs by characteristics (breed, age, etc.) and creating an interactive dashboard. I designed the MongoDB queries to support their specific search criteria (water rescue, mountain/wilderness rescue, disaster/individual tracking), then built the dashboard to visualize results with tables, charts, and geolocation maps.

This project differed from previous assignments because it combined full-stack elements—database design, backend CRUD operations, and a frontend dashboard—while meeting real-world client specifications. Earlier courses often focused on isolated skills (e.g., just SQL or just basic Python). In the future, I would continue using iterative development, client-focused requirement gathering, modular design, and thorough documentation. I would also prioritize choosing the right database type (NoSQL vs SQL) based on data structure and query needs.

### What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

Computer scientists design, develop, and optimize systems that solve complex problems using computation, data, and algorithms. Their work matters because it enables organizations to process information efficiently, make data-driven decisions, and automate tasks that improve lives.

This dashboard project directly helps an organization like Grazioso Salvare by providing an intuitive tool to quickly filter and identify suitable rescue animals based on training requirements. Instead of manually searching spreadsheets or databases, staff can use interactive filters and visualizations to find matches in seconds, view geographic distribution, and track preferences. This increases operational efficiency, reduces response time in emergencies, and ultimately helps more animals and people in need.

---

*CS 340 Project Two artifacts included in this repository:*
- Project Two Dashboard code
- CRUD Python module (from Project One)
- Project Two README (Word document)
