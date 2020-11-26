# reservations_api

Your challenge is the following:
Create a backend/API for the generic table reservation service.

The API should consist of the following endpoints:</br>
* Table list. Returns the list of “table” objects, so that client applications can render/list the tables schema
* Tables availability for a given date. Expects a required `date` parameter and returns the information on which tables are reserved on specific date
* Table reservation action. Expects the required parameters for specifying the date and specific table reference to make a reservation. Validation should be applied to prevent the reservation for the table that is already taken for a given date</br>

There should also be an interface for “moderator users”, who should have the following functionality available:
* Set up the “tables schema” by creating separate table instances with the following information:
    *  table description (short text field)
table capacity (the number of people allowed)
    * See the list of the tables already created
    * In a separate section see the list of reservations
    * Be able to switch to the details view for specific reservation
