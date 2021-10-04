(WIP)

This is a data pipeline to monitor live tweets about software jobs opportunities via twitter's streaming API.

The components' execution stages as :

---Data Pipeline---

- Set rules to filter realtime tweets
- Run zookeeper and kafka
- Create a kafka topic
- Producer to send tweet as a message to kafka broker
- Consumer to extract data from this message and store to PstgresSQL database
- PostgreSQL database with tables to store the filtered tweets data
- Exploratory data analysis and visualization

---WebApp---

-Web application to get the realtime notifications as soon as filtered tweets stream data gets into the database