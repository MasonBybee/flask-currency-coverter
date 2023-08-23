### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  Python is primarly server side and javascript is primarly front end.
  While the python and js syntax are simlar python is more readable
  Javascript can handle Dom manipulation whiel python cannot

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.
  using get() method
  using try and except

- What is a unit test?
  A unit test test a specific portion of code to make sure it works

- What is an integration test?
  An integration test tests to see if multiple pieces of code work together

- What is the role of web application framework, like Flask?
  Provides a good foundation for developing web applications making tasks like routing and session management easy.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  using the parameter in a route url is more for essential parts of an applications data structure using query params is better for sorting

- How do you collect data from a URL placeholder parameter using Flask?
  in the route you have a /<variable> and then pass that variable in the def function like this def example_function(variable_name):

- How do you collect data from the query string using Flask?
  query_value = request.args.get('query_param_name', default_value)

- How do you collect data from the body of the request using Flask?
  value = request.form['field_name']

- What is a cookie and what kinds of things are they commonly used for?
  A cookie is a small piece of data stored on the user's browser by a website. They're commonly used for session management, personalization, tracking user behavior, and enhancing security.

- What is the session object in Flask?
  A session opject is similar to local storage in the sense that it stores data in your browser as key value pairs, however it stores it in an encrypted string.

- What does Flask's `jsonify()` do?
  converts Python data structures, like dictionaries or lists, into JSON format and returns it as a response with a content-type of application/json, making it suitable for building APIs.
